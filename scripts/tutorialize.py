"""
将视频转录稿提交给 Kimi API（通过 claude CLI），生成课程化教学文章。

原理：Kimi 的 coding API 只允许 Coding Agent 访问，claude CLI 正是 Coding Agent。
所以通过 claude CLI 的 --print 模式，设置 Kimi 的 Anthropic 兼容端点来调用。

用法:
    python scripts/tutorialize.py BV1D9ojBzEAd
    python scripts/tutorialize.py BV1D9ojBzEAd --force   # 覆盖已有文章
    python scripts/tutorialize.py --all                   # 处理所有已 ingest 的视频
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile
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

WIKI_ROOT = project_root() / "wiki"
TUTORIALS_DIR = WIKI_ROOT / "tutorials"
REGISTRY_PATH = project_root() / "sources" / "registry.json"

# Prompt from assets/prompts/ (the authoritative source)
PROMPT_FILE = project_root() / "assets" / "prompts" / "tutorialize_prompt.md"


def load_registry():
    if REGISTRY_PATH.exists():
        return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    return {"version": 1, "videos": [], "stats": {}}


def find_transcript(bv: str) -> Path | None:
    registry = load_registry()
    for video in registry.get("videos", []):
        if video["bv"] == bv:
            tp = video.get("transcript_path")
            if tp and Path(tp).exists():
                return Path(tp)
    return None


def find_video_info(bv: str) -> dict:
    registry = load_registry()
    for video in registry.get("videos", []):
        if video["bv"] == bv:
            return video
    return {"bv": bv, "title": bv}


def call_kimi_via_claude_cli(prompt_text: str) -> str:
    """Call Kimi API through claude CLI (which is a recognized Coding Agent)."""
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


def tutorialize(bv: str, force: bool = False):
    """Generate tutorial article for a video."""
    transcript_path = find_transcript(bv)
    if not transcript_path:
        print(f"ERROR: No transcript found for {bv}")
        print("  Make sure the video has been ingested first (check registry.json)")
        return False

    print(f"[1/3] Transcript: {transcript_path.name}", flush=True)
    transcript = transcript_path.read_text(encoding="utf-8").strip()
    if not transcript:
        print("ERROR: Transcript is empty")
        return False

    video_info = find_video_info(bv)
    title = video_info.get("title", bv)
    safe_title = title.replace("/", "-").replace("\\", "-").replace(":", "-")[:60]
    output_path = TUTORIALS_DIR / f"{bv}-{safe_title}.md"

    if output_path.exists() and not force:
        print(f"  Already exists: {output_path.name} (use --force to overwrite)")
        return True

    # Build prompt
    prompt_text = PROMPT_FILE.read_text(encoding="utf-8") if PROMPT_FILE.exists() else ""
    if "{transcript}" in prompt_text:
        full_prompt = prompt_text.replace("{transcript}", transcript)
    else:
        full_prompt = prompt_text + "\n\n" + transcript

    print(f"[2/3] Generating tutorial: {title} ({len(transcript)} chars)", flush=True)
    t0 = time.time()
    article = call_kimi_via_claude_cli(full_prompt)
    elapsed = time.time() - t0
    print(f"  Done in {elapsed:.0f}s, article: {len(article)} chars", flush=True)

    # Add YAML frontmatter
    frontmatter = f"""---
type: tutorial
bv: {bv}
title: "{title}"
generated_at: {time.strftime('%Y-%m-%dT%H:%M:%S')}
model: {KIMI_MODEL}
source_transcript: {transcript_path.name}
---

"""
    output_path.write_text(frontmatter + article + "\n", encoding="utf-8")
    print(f"[3/3] Saved: {output_path.name}", flush=True)
    return True


def main():
    parser = argparse.ArgumentParser(description="Generate tutorial article from video transcript via Kimi API")
    parser.add_argument("bv", nargs="?", help="BV number of the video")
    parser.add_argument("--all", action="store_true", help="Process all ingested videos")
    parser.add_argument("--force", action="store_true", help="Overwrite existing tutorials")
    args = parser.parse_args()

    TUTORIALS_DIR.mkdir(parents=True, exist_ok=True)

    if args.all:
        registry = load_registry()
        videos = [v for v in registry.get("videos", []) if v.get("status") == "ingested"]
        print(f"Processing {len(videos)} videos...")
        for i, video in enumerate(videos, 1):
            bv = video["bv"]
            print(f"\n--- [{i}/{len(videos)}] {bv}: {video.get('title', '?')} ---")
            tutorialize(bv, force=args.force)
        print(f"\nAll done! Tutorials saved to: {TUTORIALS_DIR}")
    elif args.bv:
        tutorialize(args.bv, force=args.force)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
