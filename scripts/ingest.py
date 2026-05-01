#!/usr/bin/env python3
"""
ingest.py — Single video transcribe-and-ingest pipeline.

Bridges bili2text transcription output to the knowledge base system.
Handles the mechanical steps (transcription, file location, registry update),
leaving the intelligent steps (summarization, categorization, cross-referencing)
to Claude Code.

Usage:
    python scripts/ingest.py "BV1kfDTBXEfu"
    python scripts/ingest.py "https://www.bilibili.com/video/BV1kfDTBXEfu"
    python scripts/ingest.py "BV1kfDTBXEfu" --provider volcengine
    python scripts/ingest.py "BV1kfDTBXEfu" --provider whisper --model medium
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# --- Configuration ---
B2T_DIR = Path(r"E:\bili2text")
B2T_WORKSPACE = B2T_DIR / ".b2t"
BILI_DIR = Path(r"E:\bili")
REGISTRY_PATH = BILI_DIR / "sources" / "registry.json"
DEFAULT_PROVIDER = "sensevoice"
DEFAULT_MODEL = r"E:\bili2text\models\sensevoice-onnx\iic\SenseVoiceSmall-Onnx"


def find_uv() -> str:
    """Find uv executable."""
    candidates = [
        Path(r"C:\Users\11377\.local\bin\uv.exe"),
        Path.home() / ".local" / "bin" / "uv.exe",
    ]
    for p in candidates:
        if p.exists():
            return str(p)
    # Try PATH
    result = subprocess.run(["which", "uv"], capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout.strip()
    raise RuntimeError("uv not found. Install from https://docs.astral.sh/uv/")


def find_latest_file(directory: Path, pattern: str = "*.txt") -> Path | None:
    """Find the most recently modified file matching pattern in directory."""
    if not directory.exists():
        return None
    files = list(directory.glob(pattern))
    if not files:
        return None
    return max(files, key=lambda f: f.stat().st_mtime)


def find_transcript_and_metadata(bv_or_title: str) -> tuple[Path | None, Path | None]:
    """Locate transcript and metadata files for a given video."""
    transcript_dir = B2T_WORKSPACE / "transcripts" / "original"
    metadata_dir = B2T_WORKSPACE / "metadata"

    transcript = find_latest_file(transcript_dir, "*.txt")
    metadata = find_latest_file(metadata_dir, "*.json")

    return transcript, metadata


def load_registry() -> dict:
    """Load the video registry."""
    if REGISTRY_PATH.exists():
        with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"version": 1, "videos": [], "stats": {"total_videos": 0, "total_chars": 0, "last_updated": ""}}


def save_registry(registry: dict):
    """Save the video registry."""
    REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(REGISTRY_PATH, "w", encoding="utf-8") as f:
        json.dump(registry, f, ensure_ascii=False, indent=2)


def extract_bv(source: str) -> str | None:
    """Extract BV number from a URL or bare BV string."""
    match = re.search(r"(BV[\w]+)", source)
    return match.group(1) if match else None


FFMPEG_DIR = Path(
    r"C:\Users\11377\AppData\Local\Microsoft\WinGet\Packages"
    r"\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1-full_build\bin"
)


def _ensure_env() -> dict[str, str]:
    """Build environment with ffmpeg on PATH."""
    env = os.environ.copy()
    path_sep = ";" if os.name == "nt" else ":"
    if FFMPEG_DIR.exists():
        env["PATH"] = str(FFMPEG_DIR) + path_sep + env.get("PATH", "")
    env.setdefault("PYTHONIOENCODING", "utf-8")
    return env


def transcribe(source: str, provider: str, model: str | None = None) -> subprocess.CompletedProcess:
    """Run bili2text transcription."""
    uv = find_uv()
    cmd = [uv, "run", "bili2text", "tx", source, "--provider", provider]
    effective_model = model or DEFAULT_MODEL
    cmd.extend(["--model", str(effective_model)])

    print(f"[ingest] Running: {' '.join(cmd)}")
    print(f"[ingest] Working directory: {B2T_DIR}")

    result = subprocess.run(
        cmd,
        cwd=str(B2T_DIR),
        capture_output=True,
        text=True,
        timeout=1800,  # 30 minute timeout
        env=_ensure_env(),
    )
    return result


def main():
    parser = argparse.ArgumentParser(description="Transcribe a Bilibili video and prepare for ingestion")
    parser.add_argument("source", help="BV number, URL, or local file path")
    parser.add_argument("--provider", default=DEFAULT_PROVIDER, help="Transcription engine (default: volcengine)")
    parser.add_argument("--model", default=None, help="Model name (optional)")
    args = parser.parse_args()

    bv = extract_bv(args.source)
    if not bv:
        print(f"[ingest] Warning: Could not extract BV number from '{args.source}'")

    # Check if already processed
    registry = load_registry()
    if bv:
        for v in registry["videos"]:
            if v.get("bv") == bv and v.get("status") == "ingested":
                print(f"[ingest] Video {bv} already processed. Skipping transcription.")
                print(f"[ingest] Wiki page: {v.get('wiki_page', 'unknown')}")
                return

    # Run transcription
    result = transcribe(args.source, args.provider, args.model)
    if result.stdout:
        print(result.stdout)
    if result.returncode != 0:
        print(f"[ingest] Transcription failed (exit code {result.returncode})", file=sys.stderr)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        sys.exit(1)

    # Find output files
    transcript_path, metadata_path = find_transcript_and_metadata(bv or "")

    if not transcript_path:
        print("[ingest] Error: Could not find transcript output file", file=sys.stderr)
        sys.exit(1)

    # Read transcript
    with open(transcript_path, "r", encoding="utf-8") as f:
        transcript_text = f.read()

    # Read metadata if available
    metadata = {}
    if metadata_path and metadata_path.exists():
        with open(metadata_path, "r", encoding="utf-8") as f:
            metadata = json.load(f)

    # Update registry
    video_record = {
        "bv": bv or "",
        "url": args.source if args.source.startswith("http") else f"https://www.bilibili.com/video/{bv}",
        "title": metadata.get("download", {}).get("title", "unknown"),
        "uploader": metadata.get("download", {}).get("author", "unknown"),
        "transcript_path": str(transcript_path),
        "metadata_path": str(metadata_path) if metadata_path else "",
        "wiki_page": "",
        "ingested_at": datetime.now().isoformat(),
        "transcribe_engine": args.provider,
        "char_count": len(transcript_text),
        "tags": [],
        "status": "transcribed",
    }
    registry["videos"].append(video_record)
    registry["stats"]["total_videos"] = len(registry["videos"])
    registry["stats"]["total_chars"] = sum(v.get("char_count", 0) for v in registry["videos"])
    registry["stats"]["last_updated"] = datetime.now().isoformat()
    save_registry(registry)

    # Output summary for Claude Code to process
    print("\n" + "=" * 60)
    print("[ingest] Transcription complete. Summary for Claude Code:")
    print("=" * 60)
    print(f"  BV: {bv or 'N/A'}")
    print(f"  Title: {video_record['title']}")
    print(f"  Uploader: {video_record['uploader']}")
    print(f"  Engine: {args.provider}")
    print(f"  Transcript: {transcript_path}")
    print(f"  Metadata: {metadata_path or 'N/A'}")
    print(f"  Characters: {len(transcript_text)}")
    print(f"  Duration: {metadata.get('download', {}).get('duration', 'N/A')}")
    print("=" * 60)
    print("\nNext: Read the transcript and create wiki pages following CLAUDE.md rules.")


if __name__ == "__main__":
    main()
