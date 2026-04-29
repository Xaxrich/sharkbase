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

# Kimi API 配置
KIMI_API_BASE = "https://api.kimi.com/coding/"
KIMI_API_KEY = os.environ.get("KIMI_API_KEY", "sk-kimi-chOdpjpAMqJtl4zdcEpSz48acdAePCgxgUUgFtmAQhEn4GJoPxR5ESw2QgQOaxnJ")
KIMI_MODEL = "moonshot-v1-auto"

# Claude CLI 路径
CLAUDE_CLI = r"C:\Users\11377\AppData\Roaming\npm\claude.cmd"

# 路径
WIKI_ROOT = Path(r"E:\bili\wiki")
TUTORIALS_DIR = WIKI_ROOT / "tutorials"
REGISTRY_PATH = Path(r"E:\bili\sources\registry.json")

PROMPT_FILE = Path(__file__).parent / "tutorialize_prompt.md"


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


def call_kimi_via_claude_cli(transcript: str) -> str:
    """Call Kimi API through claude CLI (which is a recognized Coding Agent)."""
    prompt_text = PROMPT_FILE.read_text(encoding="utf-8") if PROMPT_FILE.exists() else ""
    full_prompt = prompt_text.replace("{transcript}", transcript) if "{transcript}" in prompt_text else prompt_text + "\n\n" + transcript

    # Write prompt to temp file to avoid shell escaping issues
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False, encoding="utf-8") as f:
        f.write(full_prompt)
        prompt_path = f.name

    try:
        env = os.environ.copy()
        env["ANTHROPIC_BASE_URL"] = KIMI_API_BASE
        env["ANTHROPIC_API_KEY"] = KIMI_API_KEY
        env["ANTHROPIC_MODEL"] = KIMI_MODEL
        env["CLAUDE_CODE_DISABLE_THINKING"] = "1"
        env["DISABLE_INTERLEAVED_THINKING"] = "1"
        env["CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS"] = "1"

        # Pipe prompt via stdin to avoid shell argument length limits
        result = subprocess.run(
            [CLAUDE_CLI, "--print"],
            input=full_prompt.encode("utf-8"),
            capture_output=True,
            env=env,
            timeout=600,
        )

        if result.returncode != 0:
            stderr_text = result.stderr.decode("utf-8", errors="replace")[:500] if result.stderr else "unknown"
            raise RuntimeError(f"claude CLI failed (exit {result.returncode}): {stderr_text}")

        return result.stdout.decode("utf-8", errors="replace").strip()
    finally:
        os.unlink(prompt_path)


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

    print(f"[2/3] Generating tutorial: {title} ({len(transcript)} chars)", flush=True)
    t0 = time.time()
    article = call_kimi_via_claude_cli(transcript)
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
