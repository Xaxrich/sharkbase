#!/usr/bin/env python3
"""
eval_quality.py — Generate manual scoring templates and record human scores.

Does NOT call LLM. Generates templates for human scoring, and can read back
filled scores into registry.

Usage:
    python scripts/eval_quality.py tutorial BV1VczqBREQ8
    python scripts/eval_quality.py task BV1VczqBREQ8
    python scripts/eval_quality.py task BV1VczqBREQ8 --dry-run
    python scripts/eval_quality.py task BV1VczqBREQ8 --record
    python scripts/eval_quality.py task BV1VczqBREQ8 --record --dry-run
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.config import project_root

ROOT = project_root()

RUBRIC_DIR = ROOT / "evals" / "rubrics"
REPORT_DIR = ROOT / "evals" / "reports"
REGISTRY_PATH = ROOT / "sources" / "registry.json"

TARGET_PATHS = {
    "tutorial": ROOT / "wiki" / "tutorials",
    "task": ROOT / "practice" / "tasks",
    "asset": ROOT / "assets",
}

RUBRIC_FILES = {
    "tutorial": "tutorial_quality.md",
    "task": "task_quality.md",
    "asset": "task_quality.md",
}


def parse_rubric_table(text: str) -> list[dict]:
    """Extract rubric dimensions from markdown table."""
    dimensions = []
    for line in text.splitlines():
        if "|" in line and "---" not in line:
            cells = [c.strip() for c in line.split("|")[1:-1]]
            if cells and cells[0] not in ("维度", "Dimension"):
                dimensions.append({
                    "name": cells[0],
                    "low": cells[1] if len(cells) > 1 else "",
                    "mid": cells[2] if len(cells) > 2 else "",
                    "high": cells[-1] if len(cells) > 2 else cells[1],
                })
    return dimensions


def find_target_file(target_type: str, bv: str) -> Path | None:
    """Find the target file for a given type and BV number."""
    dir_path = TARGET_PATHS.get(target_type)
    if not dir_path or not dir_path.exists():
        return None

    if target_type == "asset":
        for subdir in ["prompts", "sops", "checklists", "templates", "skills"]:
            asset_dir = dir_path / subdir
            if asset_dir.exists():
                for f in asset_dir.glob(f"{bv}-*.md"):
                    return f
        return None

    pattern = f"{bv}-*.md" if target_type == "tutorial" else f"{bv}-task.md"
    matches = list(dir_path.glob(pattern))
    return matches[0] if matches else None


def load_rubric(target_type: str) -> list[dict]:
    """Load and parse rubric for the given target type."""
    rubric_file = RUBRIC_FILES.get(target_type, "task_quality.md")
    rubric_path = RUBRIC_DIR / rubric_file
    if not rubric_path.exists():
        return []
    text = rubric_path.read_text(encoding="utf-8")
    return parse_rubric_table(text)


def build_report(target_type: str, bv: str, target_file: Path | None, dimensions: list[dict]) -> str:
    """Build the evaluation report template."""
    lines = [
        "---",
        f"type: eval_report",
        f"target_type: {target_type}",
        f"source: {bv}",
        f"status: pending_manual_score",
        f"target_file: {str(target_file.relative_to(ROOT)).replace(chr(92), '/')}" if target_file else "target_file: unknown",
        "---",
        "",
        f"# {target_type.capitalize()} Quality Eval: {bv}",
        "",
        f"**目标文件**: `{str(target_file.relative_to(ROOT)).replace(chr(92), '/')}`" if target_file else "**目标文件**: 未找到",
        "",
        "**评分状态**: 待人工评分",
        "",
        "## 评分",
        "",
        "| 维度 | 1分 | 3分 | 5分 | 得分 | 评注 |",
        "|------|-----|-----|-----|------|------|",
    ]
    for d in dimensions:
        lines.append(f"| {d['name']} | {d['low']} | {d['mid']} | {d['high']} |  |  |")

    lines.extend([
        "",
        "## 评分结果",
        "",
        "| 维度 | 分数 | 证据 | 修改建议 |",
        "|------|------|------|----------|",
    ])
    for d in dimensions:
        lines.append(f"| {d['name']} |  |  |  |")

    lines.extend([
        "",
        "## 总分",
        "",
        "**得分**: / ",
        "",
        "## 是否通过",
        "",
        "",
        "## 通过判断",
        "",
        "- [ ] 总分达到通过标准",
        "- [ ] 关键维度达到最低要求",
        "",
        "## 总体评注",
        "",
        "## 建议动作",
        "",
        "- [ ] 通过 → 进入下一阶段",
        "- [ ] 需重写 → 标记并补充",
        "- [ ] 降级/删除 → 标记原因",
        "",
    ])
    return "\n".join(lines)


def update_registry(bv: str, target_type: str, report_path: str):
    """Update registry.json with eval report info."""
    if not REGISTRY_PATH.exists():
        return
    data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    for video in data.get("videos", []):
        if video.get("bv") == bv:
            evals = video.setdefault("evals", {})
            key = f"{target_type}_quality"
            evals[key] = {
                "status": "pending_manual_score",
                "report": report_path,
            }
            break
    REGISTRY_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def parse_scored_report(report_path: Path) -> dict | None:
    """Parse a filled evaluation report and extract scores."""
    if not report_path.exists():
        return None

    text = report_path.read_text(encoding="utf-8")

    # Extract total score
    total_match = re.search(r"\*\*得分\*\*[：:]\s*(\d+)", text)
    if not total_match:
        return None
    total_score = int(total_match.group(1))

    # Extract whether passed
    passed = False
    pass_match = re.search(r"## 是否通过\s*\n\s*(通过|pass|yes|true)", text, re.IGNORECASE)
    if pass_match:
        passed = True

    # Extract per-dimension scores from the 评分结果 table
    scores = {}
    in_results = False
    for line in text.splitlines():
        if "评分结果" in line:
            in_results = True
            continue
        if in_results and "|" in line and "---" not in line:
            cells = [c.strip() for c in line.split("|")[1:-1]]
            if len(cells) >= 2 and cells[0] and cells[1].isdigit():
                scores[cells[0]] = int(cells[1])

    return {
        "score": total_score,
        "passed": passed,
        "dimension_scores": scores,
    }


def record_score(target_type: str, bv: str, dry_run: bool = True) -> bool:
    """Read a filled eval report and write scores back to registry."""
    report_filename = f"{bv}-{target_type}-quality.md"
    report_path = REPORT_DIR / report_filename

    if not report_path.exists():
        print(f"Error: Report not found: {report_path}")
        print("Run without --record first to generate the template.")
        return False

    result = parse_scored_report(report_path)
    if not result:
        print(f"Error: Report has not been scored yet: {report_path}")
        print("Fill in the '总分' field and '评分结果' table, then re-run with --record.")
        return False

    rel_path = f"evals/reports/{report_filename}"
    registry_update = {
        "status": "scored",
        "score": result["score"],
        "passed": result["passed"],
        "report": rel_path,
    }

    if result["dimension_scores"]:
        registry_update["dimension_scores"] = result["dimension_scores"]

    if dry_run:
        print(f"Would update registry for {bv}:")
        print(f"  evals.{target_type}_quality:")
        for k, v in registry_update.items():
            print(f"    {k}: {v}")
        return True

    # Apply
    if not REGISTRY_PATH.exists():
        print("Error: registry.json not found")
        return False

    data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    for video in data.get("videos", []):
        if video.get("bv") == bv:
            evals = video.setdefault("evals", {})
            key = f"{target_type}_quality"
            evals[key] = registry_update
            # Update report status too
            break

    REGISTRY_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Recorded: {bv} {target_type}_quality score={result['score']} passed={result['passed']}")
    return True


def main():
    parser = argparse.ArgumentParser(description="Generate quality eval template or record scores")
    parser.add_argument("target_type", choices=["tutorial", "task", "asset"],
                        help="What to evaluate")
    parser.add_argument("bv", help="BV number of the video")
    parser.add_argument("--dry-run", action="store_true", help="Print to stdout instead of writing")
    parser.add_argument("--record", action="store_true",
                        help="Read scored report and write back to registry")
    args = parser.parse_args()

    if args.record:
        success = record_score(args.target_type, args.bv, dry_run=args.dry_run)
        sys.exit(0 if success else 1)

    # Generate mode
    target_file = find_target_file(args.target_type, args.bv)
    if not target_file:
        print(f"Warning: No {args.target_type} file found for {args.bv}", file=sys.stderr)

    dimensions = load_rubric(args.target_type)
    if not dimensions:
        print(f"Warning: No rubric found for {args.target_type}", file=sys.stderr)

    report = build_report(args.target_type, args.bv, target_file, dimensions)
    report_filename = f"{args.bv}-{args.target_type}-quality.md"
    report_path = REPORT_DIR / report_filename

    if args.dry_run:
        print(report)
    else:
        REPORT_DIR.mkdir(parents=True, exist_ok=True)
        report_path.write_text(report, encoding="utf-8")
        rel_path = f"evals/reports/{report_filename}"
        update_registry(args.bv, args.target_type, rel_path)
        print(f"Generated: {report_path}")
        print(f"Registry updated: evals.{args.target_type}_quality.status = pending_manual_score")


if __name__ == "__main__":
    main()
