#!/usr/bin/env python3
"""
operationalize.py — Convert tutorial articles into practice tasks, prompts, SOPs, checklists, and eval reports.

Reads a wiki/tutorials/BVxxx-*.md file, sends it to Kimi API with the operationalize prompt,
parses the XML-like blocks from the response, and writes each block to the appropriate directory.

Usage:
    python scripts/operationalize.py BV1VczqBREQ8
    python scripts/operationalize.py BV1VczqBREQ8 --force
    python scripts/operationalize.py --all
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

# Add scripts/ to path for lib import
sys.path.insert(0, str(Path(__file__).parent))
from lib.config import get_path, get_value, kimi_api_key, project_root

# Paths from config
KIMI_API_BASE = get_value("models.kimi_api_base", "https://api.kimi.com/coding/")
KIMI_MODEL = get_value("models.kimi_model", "moonshot-v1-auto")
CLAUDE_CLI = str(get_path("workspace.claude_cli", "claude"))
KIMI_TIMEOUT = int(get_value("pipeline.kimi_timeout", "600"))

ROOT = project_root()
WIKI_ROOT = ROOT / "wiki"
TUTORIALS_DIR = WIKI_ROOT / "tutorials"
REGISTRY_PATH = ROOT / "sources" / "registry.json"
PRACTICE_TASKS_DIR = ROOT / "practice" / "tasks"
ASSETS_PROMPTS_DIR = ROOT / "assets" / "prompts"
ASSETS_SOPS_DIR = ROOT / "assets" / "sops"
ASSETS_CHECKLISTS_DIR = ROOT / "assets" / "checklists"
EVALS_REPORTS_DIR = ROOT / "evals" / "reports"

# Prompt from assets/prompts/ (the authoritative source)
PROMPT_FILE = ROOT / "assets" / "prompts" / "operationalize_prompt.md"

# Block definitions: (tag_name, output_dir, filename_suffix, frontmatter_type)
BLOCK_DEFS = [
    ("practice_task", PRACTICE_TASKS_DIR, "task", "practice_task"),
    ("prompts", ASSETS_PROMPTS_DIR, "prompts", "asset_prompts"),
    ("sop", ASSETS_SOPS_DIR, "sop", "asset_sop"),
    ("checklist", ASSETS_CHECKLISTS_DIR, "checklist", "asset_checklist"),
    ("eval_report", EVALS_REPORTS_DIR, "operationalize", "eval_report"),
]


def load_registry() -> dict:
    if REGISTRY_PATH.exists():
        return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    return {"version": 1, "videos": [], "stats": {}}


def save_registry(registry: dict):
    REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(REGISTRY_PATH, "w", encoding="utf-8") as f:
        json.dump(registry, f, ensure_ascii=False, indent=2)


def find_video_info(bv: str) -> dict:
    registry = load_registry()
    for video in registry.get("videos", []):
        if video["bv"] == bv:
            return video
    return {"bv": bv, "title": bv}


def find_tutorial(bv: str) -> Path | None:
    """Find tutorial file for a BV number."""
    matches = list(TUTORIALS_DIR.glob(f"{bv}-*.md"))
    if matches:
        return matches[0]
    return None


def find_existing_outputs(bv: str) -> dict[str, Path]:
    """Check which output files already exist for this BV."""
    existing = {}
    for tag, out_dir, suffix, _ in BLOCK_DEFS:
        pattern = f"{bv}-{suffix}.md"
        path = out_dir / pattern
        if path.exists():
            existing[tag] = path
    return existing


def call_kimi(prompt_text: str) -> str:
    """Call Kimi API through claude CLI."""
    api_key = kimi_api_key()  # Only checks at call time, not import time

    env = os.environ.copy()
    env["ANTHROPIC_BASE_URL"] = KIMI_API_BASE
    env["ANTHROPIC_API_KEY"] = api_key
    env["ANTHROPIC_MODEL"] = KIMI_MODEL
    env["CLAUDE_CODE_DISABLE_THINKING"] = "1"
    env["DISABLE_INTERLEAVED_THINKING"] = "1"
    env["CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS"] = "1"

    result = subprocess.run(
        [CLAUDE_CLI, "--print"],
        input=prompt_text.encode("utf-8"),
        capture_output=True,
        env=env,
        timeout=KIMI_TIMEOUT,
    )

    if result.returncode != 0:
        stderr_text = result.stderr.decode("utf-8", errors="replace")[:500] if result.stderr else "unknown"
        raise RuntimeError(f"claude CLI failed (exit {result.returncode}): {stderr_text}")

    return result.stdout.decode("utf-8", errors="replace").strip()


def parse_blocks(text: str) -> dict[str, str]:
    """Parse XML-like blocks from the Kimi response.

    Expected format:
        <practice_task>...</practice_task>
        <prompts>...</prompts>
        <sop>...</sop>
        <checklist>...</checklist>
        <eval_report>...</eval_report>

    Returns dict mapping tag names to their content.
    """
    blocks = {}
    tag_names = [d[0] for d in BLOCK_DEFS]
    for tag in tag_names:
        pattern = rf"<{tag}>(.*?)</{tag}>"
        match = re.search(pattern, text, re.DOTALL)
        if match:
            blocks[tag] = match.group(1).strip()
    return blocks


def write_output(bv: str, title: str, tag: str, content: str, out_dir: Path, suffix: str, fm_type: str) -> Path:
    """Write a parsed block to its output file with YAML frontmatter."""
    out_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{bv}-{suffix}.md"
    path = out_dir / filename

    frontmatter = f"""---
type: {fm_type}
bv: {bv}
title: "{title}"
generated_at: {time.strftime('%Y-%m-%dT%H:%M:%S')}
model: {KIMI_MODEL}
---

"""
    path.write_text(frontmatter + content + "\n", encoding="utf-8")
    return path


def update_registry(bv: str, output_paths: dict[str, Path]):
    """Update registry with operationalize output paths and timestamp."""
    registry = load_registry()
    for video in registry.get("videos", []):
        if video["bv"] == bv:
            video["operationalized_at"] = time.strftime('%Y-%m-%dT%H:%M:%S')
            video["operationalize_outputs"] = {
                "task": str(output_paths.get("practice_task", "")),
                "prompts": str(output_paths.get("prompts", "")),
                "sop": str(output_paths.get("sop", "")),
                "checklist": str(output_paths.get("checklist", "")),
                "eval_report": str(output_paths.get("eval_report", "")),
            }
            break
    save_registry(registry)


def operationalize(bv: str, force: bool = False) -> bool:
    """Process a single tutorial article into capability assets."""
    # Find tutorial
    tutorial_path = find_tutorial(bv)
    if not tutorial_path:
        print(f"ERROR: No tutorial found for {bv}")
        print("  Make sure the video has been tutorialized first (check wiki/tutorials/)")
        return False

    video_info = find_video_info(bv)
    title = video_info.get("title", bv)

    # Check existing outputs
    existing = find_existing_outputs(bv)
    if existing and not force:
        print(f"  Already operationalized: {len(existing)}/5 files exist (use --force to overwrite)")
        for tag, path in existing.items():
            print(f"    {tag}: {path.name}")
        return True

    # Read tutorial content (strip frontmatter)
    raw = tutorial_path.read_text(encoding="utf-8")
    # Remove YAML frontmatter if present
    if raw.startswith("---"):
        parts = raw.split("---", 2)
        if len(parts) >= 3:
            tutorial_text = parts[2].strip()
        else:
            tutorial_text = raw
    else:
        tutorial_text = raw

    print(f"[1/3] Tutorial: {tutorial_path.name} ({len(tutorial_text)} chars)", flush=True)

    # Build prompt
    prompt_text = PROMPT_FILE.read_text(encoding="utf-8") if PROMPT_FILE.exists() else ""
    if "{tutorial}" in prompt_text:
        full_prompt = prompt_text.replace("{tutorial}", tutorial_text)
    else:
        full_prompt = prompt_text + "\n\n" + tutorial_text

    # Call Kimi
    print(f"[2/3] Calling Kimi API for: {title}", flush=True)
    t0 = time.time()
    response = call_kimi(full_prompt)
    elapsed = time.time() - t0
    print(f"  Done in {elapsed:.0f}s, response: {len(response)} chars", flush=True)

    # Parse blocks
    blocks = parse_blocks(response)
    if not blocks:
        print(f"  WARNING: No parseable blocks found in response")
        print(f"  Response preview: {response[:500]}")
        # Save raw response as eval report so nothing is lost
        blocks["eval_report"] = f"# Raw Response (parsing failed)\n\n{response}"

    print(f"  Parsed blocks: {list(blocks.keys())}", flush=True)

    # Write outputs
    print(f"[3/3] Writing output files...", flush=True)
    output_paths = {}
    for tag, out_dir, suffix, fm_type in BLOCK_DEFS:
        content = blocks.get(tag)
        if content:
            path = write_output(bv, title, tag, content, out_dir, suffix, fm_type)
            output_paths[tag] = path
            print(f"  {tag}: {path.name}", flush=True)
        else:
            print(f"  {tag}: (missing in response)", flush=True)

    # Update registry
    update_registry(bv, output_paths)
    print(f"  Registry updated", flush=True)

    return True


def main():
    parser = argparse.ArgumentParser(
        description="Convert tutorial articles into practice tasks, prompts, SOPs, checklists, and eval reports"
    )
    parser.add_argument("bv", nargs="?", help="BV number of the video")
    parser.add_argument("--all", action="store_true", help="Process all tutorialized videos")
    parser.add_argument("--force", action="store_true", help="Overwrite existing outputs")
    args = parser.parse_args()

    if args.all:
        registry = load_registry()
        videos = [v for v in registry.get("videos", []) if v.get("status") == "ingested"]
        # Filter to videos that have tutorials
        eligible = []
        for v in videos:
            if find_tutorial(v["bv"]):
                eligible.append(v)
        print(f"Processing {len(eligible)} tutorialized videos...")
        for i, video in enumerate(eligible, 1):
            bv = video["bv"]
            print(f"\n--- [{i}/{len(eligible)}] {bv}: {video.get('title', '?')} ---")
            operationalize(bv, force=args.force)
        print(f"\nAll done!")
    elif args.bv:
        operationalize(args.bv, force=args.force)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
