#!/usr/bin/env python3
"""
complete_practice_task.py — Move a practice task from P0/P1 to Done in queue,
and update registry with practice completion info.

Usage:
    python scripts/complete_practice_task.py BV1VczqBREQ8 --task "用 EARS 格式重写现有需求" --review practice/reviews/BV1VczqBREQ8-ears-review.md --output practice/outputs/BV1VczqBREQ8-ears-requirements.md --dry-run
    python scripts/complete_practice_task.py BV1VczqBREQ8 --task "用 EARS 格式重写现有需求" --review practice/reviews/BV1VczqBREQ8-ears-review.md --output practice/outputs/BV1VczqBREQ8-ears-requirements.md --apply
"""
import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.config import project_root

ROOT = project_root()
REGISTRY_PATH = ROOT / "sources" / "registry.json"
QUEUE_PATH = ROOT / "practice" / "queue.md"


def move_task_in_queue(bv: str, task_name: str, review_path: str, output_path: str, dry_run: bool = True) -> bool:
    """Move a task from P0/P1 to Done in queue.md."""
    if not QUEUE_PATH.exists():
        print("Error: practice/queue.md not found", file=sys.stderr)
        return False

    text = QUEUE_PATH.read_text(encoding="utf-8")
    lines = text.splitlines()

    # Find the task row in P0 or P1
    task_line_idx = None
    in_section = None
    task_line = None

    for i, line in enumerate(lines):
        if "## P0" in line:
            in_section = "P0"
        elif "## P1" in line:
            in_section = "P1"
        elif line.startswith("## "):
            in_section = None
        elif in_section and task_name in line and bv in line:
            task_line_idx = i
            task_line = line
            break

    if task_line_idx is None:
        print(f"Error: Task '{task_name}' for {bv} not found in P0/P1", file=sys.stderr)
        return False

    # Parse the task row
    cells = [c.strip() for c in task_line.split("|")[1:-1]]
    today = datetime.now().strftime("%Y-%m-%d")

    # Build Done row
    done_row = f"| {task_name} | {bv} | {cells[2] if len(cells) > 2 else ''} | {today} | {output_path} | [[{Path(review_path).stem}]] |"

    if dry_run:
        print(f"Would remove from {in_section}:")
        print(f"  {task_line.strip()}")
        print(f"Would add to Done:")
        print(f"  {done_row.strip()}")
        return True

    # Remove the task line and any empty line after the table header
    new_lines = []
    skip_next_separator = False
    for i, line in enumerate(lines):
        if i == task_line_idx:
            skip_next_separator = True
            continue
        if skip_next_separator and line.strip().startswith("|---"):
            continue
        if skip_next_separator and not line.strip().startswith("|"):
            skip_next_separator = False
            # Check if section is now empty
            continue
        skip_next_separator = False
        new_lines.append(line)

    # Find Done section and add the row
    done_idx = None
    for i, line in enumerate(new_lines):
        if "## Done" in line:
            done_idx = i
            break

    if done_idx is not None:
        # Find the first data row or the end of the table in Done
        insert_idx = done_idx + 1
        while insert_idx < len(new_lines) and (new_lines[insert_idx].strip().startswith("|---") or new_lines[insert_idx].strip().startswith("| (暂无)")):
            insert_idx += 1
        # Remove "(暂无)" placeholder if present
        for i in range(done_idx, min(done_idx + 5, len(new_lines))):
            if "(暂无)" in new_lines[i]:
                new_lines[i] = new_lines[i].replace("| (暂无) | | | | | |", "")

        new_lines.insert(insert_idx, done_row)

    QUEUE_PATH.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
    print(f"Moved '{task_name}' from {in_section} to Done in queue.md")
    return True


def update_registry(bv: str, task_name: str, output_path: str, review_path: str, dry_run: bool = True) -> bool:
    """Update registry.json with practice completion info."""
    if not REGISTRY_PATH.exists():
        print("Error: registry.json not found", file=sys.stderr)
        return False

    data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))

    for video in data.get("videos", []):
        if video.get("bv") == bv:
            practice = video.setdefault("practice", {})
            update = {
                "status": "done",
                "completed_task": task_name,
                "output": output_path.replace("\\", "/"),
                "review": review_path.replace("\\", "/"),
                "completed_at": datetime.now().isoformat(),
            }

            if dry_run:
                print(f"Would update registry for {bv}:")
                print(f"  practice: {json.dumps(update, ensure_ascii=False, indent=4)}")
                return True

            practice.update(update)
            break

    REGISTRY_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Updated registry for {bv}: practice.status = done")
    return True


def main():
    parser = argparse.ArgumentParser(description="Complete a practice task and move to Done")
    parser.add_argument("bv", help="BV number")
    parser.add_argument("--task", required=True, help="Task name as it appears in queue")
    parser.add_argument("--review", required=True, help="Path to practice review file")
    parser.add_argument("--output", required=True, help="Path to practice output file")
    parser.add_argument("--dry-run", action="store_true", help="Only show what would change")
    parser.add_argument("--apply", action="store_true", help="Actually apply changes")
    args = parser.parse_args()

    dry_run = not args.apply

    queue_ok = move_task_in_queue(args.bv, args.task, args.review, args.output, dry_run=dry_run)
    registry_ok = update_registry(args.bv, args.task, args.output, args.review, dry_run=dry_run)

    if dry_run and (queue_ok or registry_ok):
        print("\nRun with --apply to write changes.")

    sys.exit(0 if (queue_ok and registry_ok) else 1)


if __name__ == "__main__":
    main()
