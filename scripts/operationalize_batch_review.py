#!/usr/bin/env python3
"""
operationalize_batch_review.py — Review operationalize status for multiple BV numbers.
Outputs a markdown summary of which BVs have all 5 output files and their current status.

Usage:
    python scripts/operationalize_batch_review.py BV1VczqBREQ8 BV15mndznEkS
    python scripts/operationalize_batch_review.py --all
    python scripts/operationalize_batch_review.py --all --limit 10
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.config import project_root

ROOT = project_root()

REGISTRY_PATH = ROOT / "sources" / "registry.json"

OUTPUT_DIRS = {
    "practice_task": ROOT / "practice" / "tasks",
    "prompts": ROOT / "assets" / "prompts",
    "sop": ROOT / "assets" / "sops",
    "checklist": ROOT / "assets" / "checklists",
    "eval_report": ROOT / "evals" / "reports",
}

OUTPUT_SUFFIXES = {
    "practice_task": "-task.md",
    "prompts": "-prompts.md",
    "sop": "-sop.md",
    "checklist": "-checklist.md",
    "eval_report": "-operationalize.md",
}


def load_registry() -> list[dict]:
    if not REGISTRY_PATH.exists():
        return []
    data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    return data.get("videos", [])


def check_outputs(bv: str) -> dict:
    """Check which output files exist for a BV number."""
    results = {}
    for key, dir_path in OUTPUT_DIRS.items():
        suffix = OUTPUT_SUFFIXES[key]
        pattern = f"{bv}{suffix}"
        exists = (dir_path / pattern).exists() if dir_path.exists() else False
        results[key] = exists
    results["all_present"] = all(results.values())
    return results


def review_bvs(bv_list: list[str], videos: list[dict]) -> str:
    """Build review markdown for a list of BV numbers."""
    bv_map = {v["bv"]: v for v in videos}
    lines = ["# Operationalize Batch Review", ""]

    summary = {"done": 0, "failed": 0, "skipped": 0, "no_status": 0, "all_files_present": 0, "missing_files": 0}

    for bv in bv_list:
        info = bv_map.get(bv, {})
        title = info.get("title", "Unknown")
        ops_status = info.get("operationalize_status", "none")
        outputs = check_outputs(bv)
        capability = info.get("capability", info.get("tags", [""])[0] if info.get("tags") else "")

        status_emoji = {"done": "✅", "failed": "❌", "skipped": "⏭️"}.get(ops_status, "⬜")
        files_emoji = "✅" if outputs["all_present"] else "⚠️"

        lines.append(f"## {bv} — {title}")
        lines.append("")
        lines.append(f"- **状态**: {status_emoji} {ops_status}")
        lines.append(f"- **能力**: {capability}")
        lines.append(f"- **5文件完整**: {files_emoji}")
        lines.append("")
        lines.append("| 输出 | 存在 | 路径 |")
        lines.append("|------|------|------|")
        for key in OUTPUT_DIRS:
            exists = "✅" if outputs[key] else "❌"
            suffix = OUTPUT_SUFFIXES[key]
            rel = f"{OUTPUT_DIRS[key].relative_to(ROOT)}/{bv}{suffix}" if outputs[key] else f"(缺失) {bv}{suffix}"
            lines.append(f"| {key} | {exists} | `{rel}` |")

        # Check eval status
        evals = info.get("evals", {})
        eval_status = evals.get("task_quality", {}).get("status", "none") if evals else "none"
        lines.append("")
        lines.append(f"- **Task Quality Eval**: {eval_status}")
        lines.append("")

        # Count for summary
        if ops_status == "done":
            summary["done"] += 1
        elif ops_status == "failed":
            summary["failed"] += 1
        elif ops_status == "skipped":
            summary["skipped"] += 1
        else:
            summary["no_status"] += 1
        if outputs["all_present"]:
            summary["all_files_present"] += 1
        else:
            summary["missing_files"] += 1

    # Summary
    lines.insert(2, f"**汇总**: {len(bv_list)} 个视频 | ✅ Done: {summary['done']} | ❌ Failed: {summary['failed']} | ⏭️ Skipped: {summary['skipped']} | ⬜ 无状态: {summary['no_status']} | 5文件完整: {summary['all_files_present']} | 缺文件: {summary['missing_files']}")
    lines.insert(3, "")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Batch review operationalize status")
    parser.add_argument("bvs", nargs="*", help="BV numbers to review")
    parser.add_argument("--all", action="store_true", help="Review all videos in registry")
    parser.add_argument("--limit", type=int, help="Limit number of videos when using --all")
    parser.add_argument("--status", choices=["done", "failed", "skipped", "none"],
                        help="Filter by operationalize status")
    args = parser.parse_args()

    videos = load_registry()

    if args.all:
        bv_list = [v["bv"] for v in videos]
        if args.status:
            bv_list = [v["bv"] for v in videos if v.get("operationalize_status", "none") == args.status]
        if args.limit:
            bv_list = bv_list[:args.limit]
    else:
        bv_list = args.bvs

    if not bv_list:
        print("No BV numbers specified. Use positional args or --all.")
        sys.exit(1)

    report = review_bvs(bv_list, videos)
    print(report)


if __name__ == "__main__":
    main()
