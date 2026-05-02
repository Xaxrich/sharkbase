#!/usr/bin/env python3
"""
rebuild_revision_log.py — Scan assets and practice/tasks for revision_source
frontmatter and auto-generate assets/revision_log.md.

Usage:
    python scripts/rebuild_revision_log.py --dry-run
    python scripts/rebuild_revision_log.py
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.config import project_root

ROOT = project_root()
SCAN_DIRS = [
    ROOT / "practice" / "tasks",
    ROOT / "assets" / "prompts",
    ROOT / "assets" / "sops",
    ROOT / "assets" / "checklists",
    ROOT / "assets" / "templates",
    ROOT / "assets" / "skills",
]
OUTPUT_PATH = ROOT / "assets" / "revision_log.md"


def parse_frontmatter(text: str) -> dict:
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta


def scan_revisions() -> list[dict]:
    """Scan all asset directories for files with revision_source frontmatter."""
    entries = []
    for dir_path in SCAN_DIRS:
        if not dir_path.exists():
            continue
        for f in sorted(dir_path.glob("*.md")):
            text = f.read_text(encoding="utf-8")
            meta = parse_frontmatter(text)
            if meta.get("revision_source"):
                entries.append({
                    "date": meta.get("revision_date", ""),
                    "source": meta.get("revision_source", ""),
                    "file": str(f.relative_to(ROOT)).replace("\\", "/"),
                    "status": meta.get("revision_status", ""),
                    "summary": "",  # not extractable from frontmatter alone
                })
    return entries


def build_log(entries: list[dict]) -> str:
    """Build revision_log.md content."""
    lines = [
        "# Asset Revision Log",
        "",
        "> 记录实践复盘中产生的资产修正。每次实践 review 后，相关 task/SOP/checklist/prompt 的修改都登记在此。",
        "",
        "| 日期 | 来源 Review | 被修改资产 | 修改状态 | 修改摘要 |",
        "|---|---|---|---|---|",
    ]
    for e in entries:
        lines.append(f"| {e['date']} | {e['source']} | {e['file']} | {e['status']} | |")
    if not entries:
        lines.append("| (暂无) | | | | |")
    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Rebuild assets/revision_log.md from frontmatter")
    parser.add_argument("--dry-run", action="store_true", help="Print to stdout instead of writing")
    args = parser.parse_args()

    entries = scan_revisions()
    content = build_log(entries)

    if args.dry_run:
        print(content)
    else:
        OUTPUT_PATH.write_text(content, encoding="utf-8")
        print(f"Rebuilt revision_log.md with {len(entries)} revisions")


if __name__ == "__main__":
    main()
