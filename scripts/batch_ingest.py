#!/usr/bin/env python3
"""
batch_ingest.py — Batch process a video series for the knowledge base.

Reads a series list file (from Bilibili UGC season), transcribes all videos,
classifies them into A/B/C tiers, then processes A and B tiers through
the full knowledge base pipeline.

Usage:
    python scripts/batch_ingest.py sources/series_ai_engineering.txt --transcribe
    python scripts/batch_ingest.py sources/series_ai_engineering.txt --classify
    python scripts/batch_ingest.py sources/series_ai_engineering.txt --ingest --tier A
    python scripts/batch_ingest.py sources/series_ai_engineering.txt --ingest --tier A B
    python scripts/batch_ingest.py sources/series_ai_engineering.txt --all
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

BILI_DIR = Path(r"E:\bili")
B2T_DIR = Path(r"E:\bili2text")
REGISTRY_PATH = BILI_DIR / "sources" / "registry.json"
FFMPEG = Path(
    r"C:\Users\11377\AppData\Local\Microsoft\WinGet\Packages"
    r"\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1-full_build\bin\ffmpeg.exe"
)
UV_PATH = Path(r"C:\Users\11377\.local\bin\uv.exe")
SENSEVOICE_MODEL = r"E:\bili2text\models\sensevoice-onnx\iic\SenseVoiceSmall-Onnx"
B2T_AUDIO_DIR = B2T_DIR / ".b2t" / "audio"
B2T_DOWNLOAD_DIR = B2T_DIR / ".b2t" / "downloads"
B2T_TRANSCRIPT_DIR = B2T_DIR / ".b2t" / "transcripts" / "original"
CHUNK_DIR = B2T_DIR / ".b2t" / "audio" / "chunks"
CHUNK_DURATION = 300  # 5 minutes per chunk
CLAUDE_CLI = Path(r"C:\Users\11377\AppData\Roaming\npm\claude.cmd")
KIMI_API_BASE = "https://api.kimi.com/coding/"
KIMI_API_KEY = os.environ.get("KIMI_API_KEY", "sk-kimi-chOdpjpAMqJtl4zdcEpSz48acdAePCgxgUUgFtmAQhEn4GJoPxR5ESw2QgQOaxnJ")
KIMI_MODEL = "moonshot-v1-auto"


def parse_series_file(path: Path) -> list[dict]:
    """Parse the series list file into a list of video dicts."""
    videos = []
    for line in path.read_text(encoding="utf-8").strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        # Format: "1. BV1xxx\t44min\tTitle"
        m = re.match(r"(\d+)\.\s+(BV\w+)\t(\d+)min\t(.+)", line)
        if m:
            videos.append({
                "index": int(m.group(1)),
                "bv": m.group(2),
                "duration_min": int(m.group(3)),
                "title": m.group(4),
            })
    return videos


def load_registry() -> dict:
    if REGISTRY_PATH.exists():
        return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    return {"version": 1, "videos": [], "stats": {}}


def save_registry(registry: dict):
    REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(REGISTRY_PATH, "w", encoding="utf-8") as f:
        json.dump(registry, f, ensure_ascii=False, indent=2)


def is_transcribed(bv: str) -> bool:
    """Check if a video already has a transcript file."""
    registry = load_registry()
    for v in registry.get("videos", []):
        if v.get("bv") == bv and v.get("status") in ("transcribed", "ingested"):
            tp = v.get("transcript_path", "")
            if tp and Path(tp).exists():
                return True
    return False


def find_transcript_for_bv(bv: str) -> Path | None:
    """Find transcript file for a BV number by checking registry then directory."""
    # Check registry first (most reliable)
    registry = load_registry()
    for v in registry.get("videos", []):
        if v.get("bv") == bv:
            tp = v.get("transcript_path", "")
            if tp and Path(tp).exists():
                return Path(tp)

    # Search transcript directory for files matching BV
    if B2T_TRANSCRIPT_DIR.exists():
        # Direct BV prefix match
        matches = list(B2T_TRANSCRIPT_DIR.glob(f"{bv}-*.txt"))
        if matches:
            return max(matches, key=lambda f: f.stat().st_mtime)

    return None


def download_video(bv: str) -> Path | None:
    """Download video and extract audio. Uses bili2text for download, then falls back to ffmpeg."""
    env = os.environ.copy()
    ffmpeg_dir = str(FFMPEG.parent)
    env["PATH"] = ffmpeg_dir + ";" + env.get("PATH", "")
    env["PYTHONIOENCODING"] = "utf-8"

    # Check if audio already exists for this BV
    existing_audio = find_audio_for_bv(bv)
    if existing_audio:
        print(f"  Audio already exists: {existing_audio.name}", flush=True)
        return existing_audio

    # Run bili2text tx - downloads video + extracts audio (SenseVoice may fail, that's ok)
    cmd = [
        str(UV_PATH), "run", "bili2text", "tx", bv,
        "--provider", "sensevoice", "--model", SENSEVOICE_MODEL,
    ]
    print(f"  Downloading via bili2text...", flush=True)
    try:
        subprocess.run(cmd, cwd=str(B2T_DIR), capture_output=True, env=env, timeout=600)
    except Exception as e:
        print(f"  Download error (continuing): {e}", flush=True)

    # Check again for audio
    existing_audio = find_audio_for_bv(bv)
    if existing_audio:
        return existing_audio

    # Fallback: extract audio from downloaded video
    dl_files = list(B2T_DOWNLOAD_DIR.glob(f"{bv}*.mp4"))
    if dl_files:
        video_path = dl_files[0]
        audio_path = B2T_AUDIO_DIR / f"{bv}.wav"
        print(f"  Extracting audio from {video_path.name}...", flush=True)
        extract_cmd = [
            str(FFMPEG), "-y", "-i", str(video_path),
            "-ar", "16000", "-ac", "1", "-acodec", "pcm_s16le",
            str(audio_path),
        ]
        try:
            subprocess.run(extract_cmd, capture_output=True, timeout=300)
            if audio_path.exists():
                return audio_path
        except Exception as e:
            print(f"  Audio extraction failed: {e}", flush=True)

    return None


def find_audio_for_bv(bv: str) -> Path | None:
    """Find existing audio file for a BV number."""
    # Check registry first (most reliable mapping)
    registry = load_registry()
    for v in registry.get("videos", []):
        if v.get("bv") == bv:
            tp = v.get("transcript_path", "")
            if tp and Path(tp).exists():
                return None  # Already transcribed, no need for audio
            # No transcript path mapping for audio, search by file

    # Search audio directory for files matching this BV
    # Audio files are named by video title, not BV, so we can't easily match
    # Instead, check downloads dir to map BV to title, then find audio
    dl_files = list(B2T_DOWNLOAD_DIR.glob(f"{bv}*.mp4"))
    if not dl_files:
        return None

    # Can't easily map, just return None and let download handle it
    return None


def transcribe_audio(audio_path: Path, bv: str) -> str | None:
    """Transcribe audio using chunk-based SenseVoice with GPU."""
    CHUNK_DIR.mkdir(parents=True, exist_ok=True)

    # Split audio into chunks
    print(f"  Splitting into {CHUNK_DURATION}s chunks...", flush=True)
    split_cmd = [
        str(FFMPEG), "-y", "-i", str(audio_path),
        "-f", "segment", "-segment_time", str(CHUNK_DURATION),
        "-ar", "16000", "-ac", "1", "-acodec", "pcm_s16le",
        str(CHUNK_DIR / "chunk_%03d.wav"),
    ]
    try:
        result = subprocess.run(split_cmd, capture_output=True, timeout=300)
        if result.returncode != 0:
            print(f"  Split failed: {result.stderr.decode('utf-8', errors='replace')[:300]}", flush=True)
            return None
    except Exception as e:
        print(f"  Split error: {e}", flush=True)
        return None

    chunks = sorted(CHUNK_DIR.glob("chunk_*.wav"))
    print(f"  {len(chunks)} chunks to transcribe", flush=True)
    if not chunks:
        return None

    # Import SenseVoice inside bili2text's venv
    all_texts = []
    try:
        # Use uv run python to get the right venv
        script = f"""
import sys
sys.path.insert(0, r"{B2T_DIR}")
from funasr_onnx import SenseVoiceSmall
from funasr_onnx.utils.postprocess_utils import rich_transcription_postprocess

model = SenseVoiceSmall(r"{SENSEVOICE_MODEL}", quantize=True, device_id=0)

import json
chunks = {json.dumps([str(c) for c in chunks])}
results = []
for i, chunk_path in enumerate(chunks):
    try:
        res = model([chunk_path], language="auto", use_itn=True)
        for item in res:
            text = rich_transcription_postprocess(
                str(item.get("text", "")) if isinstance(item, dict) else str(item)
            )
            if text.strip():
                results.append(text.strip())
        print(f"  Chunk {{i+1}}/{{len(chunks)}} done", flush=True)
    except Exception as e:
        print(f"  Chunk {{i+1}} error: {{e}}", flush=True)

print("RESULT_JSON:" + json.dumps(results, ensure_ascii=False))
"""
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"

        result = subprocess.run(
            [str(UV_PATH), "run", "python", "-c", script],
            cwd=str(B2T_DIR),
            capture_output=True,
            env=env,
            timeout=1800,
        )

        stdout = result.stdout.decode("utf-8", errors="replace")
        # Extract the JSON result
        marker = "RESULT_JSON:"
        if marker in stdout:
            json_str = stdout[stdout.index(marker) + len(marker):]
            all_texts = json.loads(json_str)
        else:
            # Fallback: try to read lines
            for line in stdout.splitlines():
                if "Chunk" in line and "done" in line:
                    pass  # progress line
            print(f"  No result marker found in output", flush=True)
            return None

    except subprocess.TimeoutExpired:
        print(f"  Transcription timeout", flush=True)
        return None
    except Exception as e:
        print(f"  Transcription error: {e}", flush=True)
        return None
    finally:
        # Clean up chunks
        for chunk in CHUNK_DIR.glob("chunk_*.wav"):
            try:
                chunk.unlink()
            except:
                pass

    if not all_texts:
        return None

    full_text = "\n".join(all_texts)

    # Save transcript
    safe_name = audio_path.stem.replace(" ", "-")[:60]
    output_path = B2T_TRANSCRIPT_DIR / f"{safe_name}-{time.strftime('%Y%m%d')}-chunked.txt"
    B2T_TRANSCRIPT_DIR.mkdir(parents=True, exist_ok=True)
    output_path.write_text(full_text + "\n", encoding="utf-8")
    print(f"  Saved: {output_path.name} ({len(full_text)} chars)", flush=True)

    return str(output_path)


def transcribe_video(bv: str) -> bool:
    """Download, extract audio, and transcribe a single video."""
    # Step 1: Find or download audio
    audio_path = download_video(bv)
    if not audio_path:
        print(f"  Could not get audio for {bv}", flush=True)
        return False

    print(f"  Audio: {audio_path.name} ({audio_path.stat().st_size / 1024 / 1024:.1f} MB)", flush=True)

    # Step 2: Transcribe using chunked approach
    transcript_path = transcribe_audio(audio_path, bv)
    if not transcript_path:
        return False

    return True


def update_registry_with_transcript(bv: str, title: str, duration_min: int):
    """Add or update a video record in registry after transcription."""
    registry = load_registry()
    # Check if already exists
    for v in registry.get("videos", []):
        if v.get("bv") == bv:
            return

    transcript_path = find_transcript_for_bv(bv)
    char_count = 0
    if transcript_path and transcript_path.exists():
        char_count = len(transcript_path.read_text(encoding="utf-8"))

    record = {
        "bv": bv,
        "url": f"https://www.bilibili.com/video/{bv}",
        "title": title,
        "uploader": "Easonlee的AI笔记",
        "transcript_path": str(transcript_path) if transcript_path else "",
        "metadata_path": "",
        "wiki_page": "",
        "ingested_at": datetime.now().isoformat(),
        "transcribe_engine": "sensevoice",
        "char_count": char_count,
        "tags": [],
        "status": "transcribed",
        "series": "AI工具实践",
        "duration_min": duration_min,
    }
    registry["videos"].append(record)
    registry["stats"]["total_videos"] = len(registry["videos"])
    registry["stats"]["total_chars"] = sum(v.get("char_count", 0) for v in registry["videos"])
    registry["stats"]["last_updated"] = datetime.now().isoformat()
    save_registry(registry)


def classify_tier(video: dict) -> str:
    """Classify a video into A/B/C tier based on duration and title."""
    dur = video["duration_min"]
    title = video["title"]

    # C tier: short reviews, rankings, quick demos
    c_keywords = ["测评", "评测", "排行", "推荐", "对比", "vs", "哪个", "最佳", "盘点"]
    if dur < 15:
        return "C"

    # Check for shallow review content
    is_review = any(kw in title for kw in c_keywords)
    if dur < 25 and is_review:
        return "C"

    # B tier: 15-30 min practical tutorials, medium depth
    if dur < 30:
        return "B" if not is_review else "C"

    # A tier: 30+ min deep technical/methodology content
    a_keywords = ["实战", "教程", "深度", "源码", "架构", "原理", "入门课", "大师课", "完整", "全解析"]
    is_deep = any(kw in title for kw in a_keywords)

    if dur >= 30 and (is_deep or dur >= 40):
        return "A"

    # 30-40 min non-deep content
    return "B"


def call_kimi(prompt: str) -> str:
    """Call Kimi API through claude CLI."""
    env = os.environ.copy()
    env["ANTHROPIC_BASE_URL"] = KIMI_API_BASE
    env["ANTHROPIC_API_KEY"] = KIMI_API_KEY
    env["ANTHROPIC_MODEL"] = KIMI_MODEL
    env["CLAUDE_CODE_DISABLE_THINKING"] = "1"
    env["DISABLE_INTERLEAVED_THINKING"] = "1"
    env["CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS"] = "1"

    result = subprocess.run(
        [str(CLAUDE_CLI), "--print"],
        input=prompt.encode("utf-8"),
        capture_output=True,
        env=env,
        timeout=600,
    )

    if result.returncode != 0:
        stderr = result.stderr.decode("utf-8", errors="replace")[:300]
        raise RuntimeError(f"claude CLI failed (exit {result.returncode}): {stderr}")

    return result.stdout.decode("utf-8", errors="replace").strip()


def generate_wiki_page(video: dict, transcript: str) -> str:
    """Generate a wiki video page using Kimi API."""
    prompt = f"""你是一名知识库编辑。请基于以下视频转录稿，生成一个 Obsidian 兼容的 Markdown 知识库页面。

视频信息：
- 标题：{video['title']}
- BV号：{video['bv']}
- UP主：Easonlee的AI笔记
- 时长：{video['duration_min']}分钟

请按以下模板生成页面（YAML frontmatter + 正文）：

---
type: video
bv: {video['bv']}
title: "{video['title']}"
uploader: Easonlee的AI笔记
url: https://www.bilibili.com/video/{video['bv']}
tags: [根据内容生成3-5个中文标签]
concepts: [提取2-4个核心概念]
---

# {video['title']}

## 一句话摘要
用一句话概括视频的核心价值。

## 核心观点
- 提取3-5个核心观点

## 详细笔记
按视频逻辑结构整理关键内容，不是逐字转录，是提炼和重组。使用二级和三级标题组织结构。

## 我的评注
对视频内容的批判性分析：
- 赞同什么
- 质疑什么
- 与AI工程实践的关联

## 待深入问题
- 还有哪些值得深入探索的问题

规则：
1. 语言清晰、直接、克制
2. 不要逐字复述，要提炼和重组
3. 不要编造视频里没有的内容
4. 标签使用中文
5. 直接输出 Markdown，不要输出废话

转录稿：

<<<
{transcript}
>>>
"""
    return call_kimi(prompt)


def generate_tutorial(video: dict, transcript: str) -> str:
    """Generate a tutorial article using Kimi API."""
    prompt_path = Path(__file__).parent / "tutorialize_prompt.md"
    prompt_text = prompt_path.read_text(encoding="utf-8") if prompt_path.exists() else ""
    full_prompt = prompt_text.replace("{transcript}", transcript) if "{transcript}" in prompt_text else prompt_text + "\n\n" + transcript
    return call_kimi(full_prompt)


def cmd_transcribe(args):
    """Batch transcribe all videos in the series."""
    videos = parse_series_file(Path(args.series_file))
    total = len(videos)
    already = sum(1 for v in videos if is_transcribed(v["bv"]))
    print(f"Total: {total} videos, already transcribed: {already}, to process: {total - already}")

    success, failed, skipped = 0, 0, 0
    for i, video in enumerate(videos, 1):
        bv = video["bv"]
        if is_transcribed(bv):
            skipped += 1
            continue

        print(f"\n[{i}/{total}] {bv}: {video['title']} ({video['duration_min']}min)", flush=True)
        t0 = time.time()

        ok = transcribe_video(bv)
        elapsed = time.time() - t0

        if ok:
            update_registry_with_transcript(bv, video["title"], video["duration_min"])
            success += 1
            print(f"  OK in {elapsed:.0f}s", flush=True)
        else:
            failed += 1
            print(f"  FAILED, skipping", flush=True)

    print(f"\n=== Transcription complete: {success} ok, {failed} failed, {skipped} skipped ===")


def cmd_classify(args):
    """Classify videos into A/B/C tiers."""
    videos = parse_series_file(Path(args.series_file))
    tiers = {"A": [], "B": [], "C": []}

    for v in videos:
        tier = classify_tier(v)
        v["tier"] = tier
        tiers[tier].append(v)

    # Save classification
    out_path = BILI_DIR / "sources" / "series_ai_engineering_classified.json"
    classified = {t: [{"bv": v["bv"], "title": v["title"], "duration_min": v["duration_min"], "index": v["index"]} for v in vs] for t, vs in tiers.items()}
    out_path.write_text(json.dumps(classified, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"A tier ({len(tiers['A'])} videos): deep technical/methodology content")
    for v in tiers["A"]:
        print(f"  {v['bv']} ({v['duration_min']}min) {v['title']}")
    print(f"\nB tier ({len(tiers['B'])} videos): practical tutorials, medium depth")
    for v in tiers["B"]:
        print(f"  {v['bv']} ({v['duration_min']}min) {v['title']}")
    print(f"\nC tier ({len(tiers['C'])} videos): short reviews, skipped")
    for v in tiers["C"]:
        print(f"  {v['bv']} ({v['duration_min']}min) {v['title']}")
    print(f"\nSaved to: {out_path}")


def cmd_ingest(args):
    """Ingest A/B tier videos: generate wiki pages and tutorials."""
    classified_path = BILI_DIR / "sources" / "series_ai_engineering_classified.json"
    if not classified_path.exists():
        print("ERROR: Run --classify first")
        return

    classified = json.loads(classified_path.read_text(encoding="utf-8"))
    tiers_to_process = args.tier or ["A", "B"]
    registry = load_registry()

    videos_to_process = []
    for tier in tiers_to_process:
        for v in classified.get(tier, []):
            videos_to_process.append({**v, "tier": tier})

    print(f"Processing {len(videos_to_process)} videos (tiers: {tiers_to_process})")

    wiki_dir = BILI_DIR / "wiki" / "videos"
    tutorial_dir = BILI_DIR / "wiki" / "tutorials"
    wiki_dir.mkdir(parents=True, exist_ok=True)
    tutorial_dir.mkdir(parents=True, exist_ok=True)

    for i, video in enumerate(videos_to_process, 1):
        bv = video["bv"]
        tier = video["tier"]
        title = video["title"]
        # Sanitize title for filename - keep only safe chars
        safe_title = re.sub(r'[^\w一-鿿\-.]', '-', title)[:60]
        wiki_path = wiki_dir / f"{bv}-{safe_title}.md"
        tutorial_path = tutorial_dir / f"{bv}-{safe_title}.md"

        # Check if any file with this BV prefix already exists (regardless of title)
        existing_wiki = list(wiki_dir.glob(f"{bv}-*.md"))
        existing_tutorial = list(tutorial_dir.glob(f"{bv}-*.md"))
        # Keep the largest existing file if duplicates exist
        if len(existing_wiki) > 1:
            largest = max(existing_wiki, key=lambda f: f.stat().st_size)
            for f in existing_wiki:
                if f != largest:
                    f.unlink()
            existing_wiki = [largest]
        if len(existing_tutorial) > 1:
            largest = max(existing_tutorial, key=lambda f: f.stat().st_size)
            for f in existing_tutorial:
                if f != largest:
                    f.unlink()
            existing_tutorial = [largest]

        # Find transcript
        transcript_path = find_transcript_for_bv(bv)

        if not transcript_path:
            print(f"[{i}/{len(videos_to_process)}] {bv}: No transcript found, skipping")
            continue

        transcript = transcript_path.read_text(encoding="utf-8").strip()
        if not transcript:
            print(f"[{i}/{len(videos_to_process)}] {bv}: Empty transcript, skipping")
            continue

        print(f"\n[{i}/{len(videos_to_process)}] {bv} ({tier}): {title} ({len(transcript)} chars)", flush=True)

        # Generate wiki page
        if existing_wiki and not args.force:
            print(f"  Wiki page exists, skipping (use --force to overwrite)")
        else:
            print(f"  Generating wiki page...", flush=True)
            t0 = time.time()
            try:
                wiki_content = generate_wiki_page(video, transcript)
                wiki_path.write_text(wiki_content + "\n", encoding="utf-8")
                print(f"  Wiki page done in {time.time()-t0:.0f}s ({len(wiki_content)} chars)", flush=True)
            except Exception as e:
                print(f"  Wiki page FAILED: {e}", flush=True)

        # Generate tutorial (A and B tiers)
        if tier in ("A", "B"):
            if existing_tutorial and not args.force:
                print(f"  Tutorial exists, skipping")
            else:
                print(f"  Generating tutorial...", flush=True)
                t0 = time.time()
                try:
                    tutorial_content = generate_tutorial(video, transcript)
                    frontmatter = f"""---
type: tutorial
bv: {bv}
title: "{title}"
generated_at: {time.strftime('%Y-%m-%dT%H:%M:%S')}
model: {KIMI_MODEL}
source_transcript: {transcript_path.name}
---

"""
                    tutorial_path.write_text(frontmatter + tutorial_content + "\n", encoding="utf-8")
                    print(f"  Tutorial done in {time.time()-t0:.0f}s ({len(tutorial_content)} chars)", flush=True)
                except Exception as e:
                    print(f"  Tutorial FAILED: {e}", flush=True)

        # Update registry
        for v in registry.get("videos", []):
            if v.get("bv") == bv:
                v["status"] = "ingested"
                v["wiki_page"] = f"wiki/videos/{wiki_path.name}"
                v["tier"] = tier
                break
        save_registry(registry)

    print(f"\n=== Ingest complete ===")


def cmd_all(args):
    """Run the full pipeline: transcribe → classify → ingest."""
    cmd_transcribe(args)
    cmd_classify(args)
    args.tier = ["A", "B"]
    args.force = False
    cmd_ingest(args)


def main():
    parser = argparse.ArgumentParser(description="Batch process a video series")
    parser.add_argument("series_file", help="Path to the series list file")
    parser.add_argument("--transcribe", action="store_true", help="Batch transcribe all videos")
    parser.add_argument("--classify", action="store_true", help="Classify videos into A/B/C tiers")
    parser.add_argument("--ingest", action="store_true", help="Ingest A/B tier videos")
    parser.add_argument("--all", action="store_true", help="Run full pipeline")
    parser.add_argument("--tier", nargs="+", default=["A", "B"], help="Tiers to process (default: A B)")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    if args.all:
        cmd_all(args)
    elif args.transcribe:
        cmd_transcribe(args)
    elif args.classify:
        cmd_classify(args)
    elif args.ingest:
        cmd_ingest(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
