#!/usr/bin/env python3
"""
backfill_capability.py — Fill missing capability frontmatter from content analysis.

Does NOT call LLM. Uses rule-based extraction from file content and capabilities/map.md.

Usage:
    python scripts/backfill_capability.py --dry-run
    python scripts/backfill_capability.py --apply
    python scripts/backfill_capability.py --target practice/tasks
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.config import project_root

ROOT = project_root()
CAPABILITY_MAP = ROOT / "capabilities" / "map.md"
REGISTRY_PATH = ROOT / "sources" / "registry.json"

SCAN_DIRS = [
    ROOT / "practice" / "tasks",
    ROOT / "assets" / "prompts",
    ROOT / "assets" / "sops",
    ROOT / "assets" / "checklists",
    ROOT / "evals" / "reports",
]

# Known capability names for fuzzy matching
CAPABILITY_NAMES = [
    "商业问题与机会判断",
    "知识输入与研究综合",
    "产品定义与规格设计",
    "AI辅助开发与Agent调度",
    "Agent架构与工作流设计",
    "评估体系与质量校准",
    "SOP与Prompt工程",
    "技术选型与工具链整合",
    "自我操作系统",
]

# Alias map: common variations → canonical name
CAPABILITY_ALIASES = {
    "产品定义": "产品定义与规格设计",
    "规格设计": "产品定义与规格设计",
    "AI辅助开发": "AI辅助开发与Agent调度",
    "Agent调度": "AI辅助开发与Agent调度",
    "Agent架构": "Agent架构与工作流设计",
    "工作流设计": "Agent架构与工作流设计",
    "评估体系": "评估体系与质量校准",
    "质量校准": "评估体系与质量校准",
    "SOP工程": "SOP与Prompt工程",
    "Prompt工程": "SOP与Prompt工程",
    "知识输入": "知识输入与研究综合",
    "研究综合": "知识输入与研究综合",
    "商业判断": "商业问题与机会判断",
    "技术选型": "技术选型与工具链整合",
    "工具链": "技术选型与工具链整合",
    "自我操作": "自我操作系统",
}


def parse_frontmatter(text: str) -> tuple[dict, str]:
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
    lines = ["---"]
    for k, v in meta.items():
        if isinstance(v, list):
            items = ", ".join(v)
            lines.append(f"{k}: [{items}]")
        elif " " in str(v) or ":" in str(v):
            lines.append(f'{k}: "{v}"')
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines)


def extract_capability_from_body(body: str) -> tuple[str | None, str | None]:
    """Extract primary and secondary capability from file body text."""
    primary = None
    secondary = None

    # Look for "主要能力" or "能力归位" patterns
    patterns = [
        r"\*\*主要能力\*\*[：:]\s*(.+)",
        r"\*\*能力归位\*\*[：:]\s*(.+)",
        r"主要能力[：:]\s*(.+)",
        r"能力归位[：:]\s*(.+)",
    ]
    for pat in patterns:
        m = re.search(pat, body)
        if m:
            text = m.group(1).strip()
            primary = match_capability(text)
            if primary:
                break

    # Look for secondary
    sec_patterns = [
        r"\*\*次要能力\*\*[：:]\s*(.+)",
        r"次要能力[：:]\s*(.+)",
    ]
    for pat in sec_patterns:
        m = re.search(pat, body)
        if m:
            text = m.group(1).strip()
            secondary = match_capability(text)
            if secondary:
                break

    return primary, secondary


def match_capability(text: str) -> str | None:
    """Match a text fragment to a known capability name."""
    text = text.strip()
    # Exact match
    if text in CAPABILITY_NAMES:
        return text
    # Alias match
    for alias, canonical in CAPABILITY_ALIASES.items():
        if alias in text:
            return canonical
    # Substring match
    for name in CAPABILITY_NAMES:
        if name in text or text in name:
            return name
    return None


def load_capability_map_bvs() -> dict[str, str]:
    """Load BV → capability mapping from capabilities/map.md."""
    bv_map = {}
    if not CAPABILITY_MAP.exists():
        return bv_map
    text = CAPABILITY_MAP.read_text(encoding="utf-8")
    # Find BV references near capability names
    for name in CAPABILITY_NAMES:
        # Find section for this capability
        section_match = re.search(rf"#+.*{re.escape(name)}.*?\n(.*?)(?=\n#|\Z)", text, re.DOTALL)
        if section_match:
            section = section_match.group(1)
            for bv_match in re.finditer(r"(BV\w+)", section):
                bv_map[bv_match.group(1)] = name
    return bv_map


def backfill(dry_run: bool = True, target_dir: str | None = None) -> list[dict]:
    """Scan files and backfill missing capability fields."""
    bv_map = load_capability_map_bvs()
    results = []

    for dir_path in SCAN_DIRS:
        if target_dir and target_dir not in str(dir_path):
            continue
        if not dir_path.exists():
            continue

        for f in sorted(dir_path.glob("*.md")):
            text = f.read_text(encoding="utf-8")
            meta, body = parse_frontmatter(text)

            has_capability = bool(meta.get("capability"))
            has_secondary = bool(meta.get("secondary_capability"))

            if has_capability and has_secondary:
                continue

            # Extract BV from filename
            bv_match = re.match(r"(BV\w+)", f.name)
            bv = bv_match.group(1) if bv_match else ""

            primary, secondary = extract_capability_from_body(body)

            # Fallback to capability map
            if not primary and bv in bv_map:
                primary = bv_map[bv]

            new_fields = {}
            if not has_capability and primary:
                new_fields["capability"] = primary
                new_fields["capability_status"] = "inferred"
                new_fields["capability_source"] = "body_primary_ability" if extract_capability_from_body(body)[0] else "capability_map"
            elif not has_capability and not primary:
                new_fields["capability"] = ""
                new_fields["capability_status"] = "needs_review"
                new_fields["capability_source"] = ""

            if not has_secondary and secondary:
                new_fields["secondary_capability"] = secondary

            if new_fields:
                entry = {
                    "file": str(f.relative_to(ROOT)).replace("\\", "/"),
                    "bv": bv,
                    "new_fields": new_fields,
                }
                results.append(entry)

                if not dry_run:
                    meta.update(new_fields)
                    new_text = build_frontmatter(meta) + "\n" + body
                    f.write_text(new_text, encoding="utf-8")

    return results


def main():
    parser = argparse.ArgumentParser(description="Backfill capability frontmatter")
    parser.add_argument("--dry-run", action="store_true", help="Only show what would change")
    parser.add_argument("--apply", action="store_true", help="Actually apply changes")
    parser.add_argument("--target", help="Only scan specific directory (e.g. practice/tasks)")
    args = parser.parse_args()

    dry_run = not args.apply
    results = backfill(dry_run=dry_run, target_dir=args.target)

    if not results:
        print("All files have capability fields. Nothing to backfill.")
        return

    action = "Would backfill" if dry_run else "Backfilled"
    print(f"{action} {len(results)} files:\n")
    for r in results:
        print(f"  {r['file']}")
        for k, v in r["new_fields"].items():
            print(f"    {k}: {v or '(empty)'}")
        print()

    if dry_run:
        print("Run with --apply to write changes.")


if __name__ == "__main__":
    main()
