#!/usr/bin/env python3
"""
frontmatter_migrate.py — Add missing frontmatter fields to old operationalize output files.

Scans practice/tasks, assets/prompts, assets/sops, assets/checklists, evals/reports
and supplements missing fields (source_type, source_tutorial, capability, secondary_capability, status)
using registry.json as the source of truth.

Usage:
    python scripts/frontmatter_migrate.py --dry-run
    python scripts/frontmatter_migrate.py --apply
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.config import project_root

ROOT = project_root()

REGISTRY_PATH = ROOT / "sources" / "registry.json"

SCAN_DIRS = {
    "practice_task": ROOT / "practice" / "tasks",
    "prompts": ROOT / "assets" / "prompts",
    "sops": ROOT / "assets" / "sops",
    "checklists": ROOT / "assets" / "checklists",
    "eval_report": ROOT / "evals" / "reports",
}

REQUIRED_FIELDS = ["source_type", "source_tutorial", "capability", "secondary_capability", "status"]

# Map from directory type to source_type value
SOURCE_TYPE_MAP = {
    "practice_task": "tutorial_operationalize",
    "prompts": "tutorial_operationalize",
    "sops": "tutorial_operationalize",
    "checklists": "tutorial_operationalize",
    "eval_report": "tutorial_operationalize",
}

# Map from directory type to status default
DEFAULT_STATUS_MAP = {
    "practice_task": "todo",
    "prompts": "active",
    "sops": "active",
    "checklists": "active",
    "eval_report": "final",
}


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Parse YAML frontmatter, return (meta_dict, body)."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", text, re.DOTALL)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            val = v.strip().strip('"').strip("'")
            meta[k.strip()] = val
    return meta, m.group(2)


def build_frontmatter(meta: dict) -> str:
    """Reconstruct YAML frontmatter from dict."""
    lines = ["---"]
    for k, v in meta.items():
        if isinstance(v, list):
            lines.append(f"{k}: [{', '.join(v)}]")
        else:
            lines.append(f'{k}: "{v}"' if " " in str(v) or ":" in str(v) else f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines)


def load_registry() -> dict:
    """Load registry.json, return {bv: video_info}."""
    if not REGISTRY_PATH.exists():
        return {}
    data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    return {v["bv"]: v for v in data.get("videos", [])}


def extract_bv(filename: str) -> str | None:
    """Extract BV number from filename like BV1xxx-task.md."""
    m = re.match(r"(BV\w+)", filename)
    return m.group(1) if m else None


def scan_and_migrate(dry_run: bool = True) -> list[dict]:
    """Scan all directories and report/fix missing frontmatter fields."""
    registry = load_registry()
    results = []

    for dir_type, dir_path in SCAN_DIRS.items():
        if not dir_path.exists():
            continue
        for f in sorted(dir_path.glob("*.md")):
            bv = extract_bv(f.name)
            if not bv:
                continue

            text = f.read_text(encoding="utf-8")
            meta, body = parse_frontmatter(text)
            missing = [field for field in REQUIRED_FIELDS if field not in meta or not meta[field]]

            if not missing:
                continue

            # Resolve values from registry
            video_info = registry.get(bv, {})
            ops_outputs = video_info.get("operationalize_outputs", {})

            new_fields = {}
            for field in missing:
                if field == "source_type":
                    new_fields[field] = SOURCE_TYPE_MAP.get(dir_type, "unknown")
                elif field == "source_tutorial":
                    # Find tutorial filename
                    tutorial_dir = ROOT / "wiki" / "tutorials"
                    matches = list(tutorial_dir.glob(f"{bv}-*.md")) if tutorial_dir.exists() else []
                    new_fields[field] = f"wiki/tutorials/{matches[0].name}" if matches else ""
                elif field == "capability":
                    new_fields[field] = meta.get("capability", "")
                elif field == "secondary_capability":
                    new_fields[field] = meta.get("secondary_capability", "")
                elif field == "status":
                    new_fields[field] = DEFAULT_STATUS_MAP.get(dir_type, "unknown")

            entry = {
                "file": str(f.relative_to(ROOT)),
                "bv": bv,
                "dir_type": dir_type,
                "missing": missing,
                "new_fields": new_fields,
            }
            results.append(entry)

            if not dry_run:
                meta.update(new_fields)
                new_text = build_frontmatter(meta) + "\n" + body
                f.write_text(new_text, encoding="utf-8")

    return results


def main():
    parser = argparse.ArgumentParser(description="Migrate frontmatter in old operationalize files")
    parser.add_argument("--dry-run", action="store_true", help="Only show what would be changed")
    parser.add_argument("--apply", action="store_true", help="Actually apply changes")
    args = parser.parse_args()

    dry_run = not args.apply
    results = scan_and_migrate(dry_run=dry_run)

    if not results:
        print("All files have complete frontmatter. Nothing to migrate.")
        return

    action = "Would migrate" if dry_run else "Migrated"
    print(f"{action} {len(results)} files:\n")
    for r in results:
        print(f"  {r['file']}")
        print(f"    Missing: {', '.join(r['missing'])}")
        print(f"    New values: {r['new_fields']}")
        print()

    if dry_run:
        print("Run with --apply to actually write changes.")


if __name__ == "__main__":
    main()
