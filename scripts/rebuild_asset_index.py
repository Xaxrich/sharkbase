#!/usr/bin/env python3
"""
rebuild_asset_index.py — Scan asset directories and regenerate assets/asset_index.md.

Usage:
    python scripts/rebuild_asset_index.py
    python scripts/rebuild_asset_index.py --dry-run
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.config import project_root

ROOT = project_root()

ASSET_DIRS = {
    "prompts": ROOT / "assets" / "prompts",
    "sops": ROOT / "assets" / "sops",
    "checklists": ROOT / "assets" / "checklists",
    "templates": ROOT / "assets" / "templates",
    "skills": ROOT / "assets" / "skills",
}

INDEX_PATH = ROOT / "assets" / "asset_index.md"


def extract_frontmatter(text: str) -> dict:
    """Parse YAML frontmatter from markdown text."""
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta


def scan_category(name: str, dir_path: Path) -> list[dict]:
    """Scan a directory for .md files and extract metadata."""
    entries = []
    if not dir_path.exists():
        return entries
    for f in sorted(dir_path.glob("*.md")):
        text = f.read_text(encoding="utf-8")
        meta = extract_frontmatter(text)
        # First heading as title
        hm = re.search(r"^#\s+(.+)", text, re.MULTILINE)
        title = meta.get("title", hm.group(1).strip() if hm else f.stem)
        source = meta.get("source", meta.get("source_tutorial", ""))
        capability = meta.get("capability", "")
        entries.append({
            "filename": f.name,
            "title": title,
            "source": source,
            "capability": capability,
        })
    return entries


def build_index(entries_by_category: dict[str, list[dict]]) -> str:
    """Build the asset_index.md content."""
    lines = ["# 资产索引", ""]
    lines.append(f"> 自动生成 by rebuild_asset_index.py | 资产总数: "
                 f"{sum(len(v) for v in entries_by_category.values())}")
    lines.append("")

    category_labels = {
        "prompts": "## Prompts",
        "sops": "## SOPs",
        "skills": "## Skills",
        "templates": "## Templates",
        "checklists": "## Checklists",
    }

    for cat in ["prompts", "sops", "skills", "templates", "checklists"]:
        entries = entries_by_category.get(cat, [])
        lines.append(category_labels[cat])
        lines.append("")
        if not entries:
            lines.append("| 资产 | 来源 | 用途 |")
            lines.append("|------|------|------|")
            lines.append("| (暂无) | | |")
        else:
            lines.append("| 资产 | 来源 | 能力 |")
            lines.append("|------|------|------|")
            for e in entries:
                src = e["source"] or (e["filename"].split("-")[0] if "-" in e["filename"] else "")
                lines.append(f"| [[{e['filename'].replace('.md','')}]] | {src} | {e['capability']} |")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Rebuild assets/asset_index.md")
    parser.add_argument("--dry-run", action="store_true", help="Print to stdout instead of writing file")
    args = parser.parse_args()

    entries_by_category = {}
    for cat, dir_path in ASSET_DIRS.items():
        entries_by_category[cat] = scan_category(cat, dir_path)

    content = build_index(entries_by_category)

    if args.dry_run:
        print(content)
    else:
        INDEX_PATH.write_text(content, encoding="utf-8")
        total = sum(len(v) for v in entries_by_category.values())
        print(f"Rebuilt asset_index.md with {total} assets")


if __name__ == "__main__":
    main()
