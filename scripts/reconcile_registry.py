#!/usr/bin/env python3
"""
reconcile_registry.py — Reconcile registry.json with actual file system state.

Scans each BV's actual file existence and fixes registry pipeline status.
File system is the source of truth.

Usage:
    python scripts/reconcile_registry.py --dry-run
    python scripts/reconcile_registry.py --apply
    python scripts/reconcile_registry.py BV1VczqBREQ8 --apply
"""
import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.config import project_root

ROOT = project_root()
REGISTRY_PATH = ROOT / "sources" / "registry.json"

OPS_OUTPUTS = {
    "practice_task": ROOT / "practice" / "tasks",
    "prompts": ROOT / "assets" / "prompts",
    "sop": ROOT / "assets" / "sops",
    "checklist": ROOT / "assets" / "checklists",
    "eval_report": ROOT / "evals" / "reports",
}

OPS_SUFFIXES = {
    "practice_task": "-task.md",
    "prompts": "-prompts.md",
    "sop": "-sop.md",
    "checklist": "-checklist.md",
    "eval_report": "-operationalize.md",
}

TUTORIAL_DIR = ROOT / "wiki" / "tutorials"
RAW_RESPONSE_DIR = ROOT / "evals" / "raw_responses"


def check_ops_files(bv: str) -> tuple[dict, list[str], list[str]]:
    """Check which operationalize output files exist for a BV.
    Returns (existing_paths, missing_keys, all_relative_paths).
    """
    existing = {}
    missing = []
    for key, dir_path in OPS_OUTPUTS.items():
        suffix = OPS_SUFFIXES[key]
        fpath = dir_path / f"{bv}{suffix}"
        if fpath.exists():
            existing[key] = str(fpath.relative_to(ROOT)).replace("\\", "/")
        else:
            missing.append(key)
    return existing, missing


def infer_status(bv: str, existing: dict, missing: list[str], registry_status: str | None) -> tuple[str, dict]:
    """Infer operationalize_status from file system state."""
    has_tutorial = any(TUTORIAL_DIR.glob(f"{bv}-*.md")) if TUTORIAL_DIR.exists() else False
    has_raw_response = any(RAW_RESPONSE_DIR.glob(f"{bv}-*")) if RAW_RESPONSE_DIR.exists() else False

    if len(existing) == 5:
        # All files present
        return "done", {"operationalize_status": "done", "operationalize_outputs": existing, "missing_outputs": []}
    elif len(existing) > 0:
        # Some files present
        return "partial", {"operationalize_status": "partial", "operationalize_outputs": existing, "missing_outputs": missing}
    elif registry_status == "done" and len(existing) < 5:
        # Registry says done but files missing
        return "inconsistent", {"operationalize_status": "inconsistent", "operationalize_outputs": existing, "missing_outputs": missing}
    elif has_raw_response:
        return "failed", {"operationalize_status": "failed", "operationalize_outputs": existing, "missing_outputs": missing}
    elif has_tutorial:
        return "pending", {"operationalize_status": "pending", "operationalize_outputs": existing, "missing_outputs": []}
    else:
        return "no_tutorial", {"operationalize_outputs": existing, "missing_outputs": []}


def reconcile(dry_run: bool = True, target_bv: str | None = None) -> list[dict]:
    """Reconcile registry with file system. Returns list of changes."""
    data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    changes = []

    for video in data.get("videos", []):
        bv = video.get("bv", "")
        if target_bv and bv != target_bv:
            continue

        existing, missing = check_ops_files(bv)
        current_status = video.get("operationalize_status")
        inferred_status, updates = infer_status(bv, existing, missing, current_status)

        needs_update = False
        reason = ""

        if current_status != inferred_status and inferred_status != "no_tutorial":
            needs_update = True
            reason = f"status: {current_status or 'missing'} → {inferred_status}"
        elif current_status == "done" and not video.get("operationalize_outputs"):
            needs_update = True
            reason = "status=done but missing operationalize_outputs"
        elif inferred_status == "done" and current_status != "done":
            needs_update = True
            reason = f"5 files exist but status={current_status}"

        if needs_update:
            change = {
                "bv": bv,
                "title": video.get("title", ""),
                "current_status": current_status,
                "inferred_status": inferred_status,
                "reason": reason,
                "updates": updates,
                "existing_files": len(existing),
                "missing_keys": missing,
            }
            changes.append(change)

            if not dry_run:
                video.update(updates)
                video["reconciled_at"] = datetime.now().isoformat()

    if not dry_run and changes:
        REGISTRY_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    return changes


def main():
    parser = argparse.ArgumentParser(description="Reconcile registry with file system state")
    parser.add_argument("--dry-run", action="store_true", help="Only show what would change")
    parser.add_argument("--apply", action="store_true", help="Actually apply changes")
    parser.add_argument("bv", nargs="?", help="Specific BV to reconcile")
    args = parser.parse_args()

    dry_run = not args.apply
    changes = reconcile(dry_run=dry_run, target_bv=args.bv)

    if not changes:
        print("Registry is consistent. No changes needed.")
        return

    action = "Would update" if dry_run else "Updated"
    print(f"{action} {len(changes)} entries:\n")
    for c in changes:
        print(f"  {c['bv']} — {c['title']}")
        print(f"    {c['reason']}")
        print(f"    Files: {c['existing_files']}/5 | Missing: {c['missing_keys'] or 'none'}")
        print()

    if dry_run:
        print("Run with --apply to write changes.")


if __name__ == "__main__":
    main()
