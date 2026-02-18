#!/usr/bin/env python3
"""Batch transcribe (OpenAI Whisper) for Xiaojun podcast.

- Reads a JSONL queue file: scripts/xiaojun_queue.jsonl
- Downloads audio (if missing) into data/audio/xiaojun/
- If audio is large/long, segments into 15min chunks and transcribes chunk-by-chunk
- Writes transcript to transcripts/xiaojun/<slug>.md
- Writes analysis template to transcripts/xiaojun/<slug>.analysis.md (if not exists)

Requires:
- yt-dlp
- ffmpeg
- python package: openai
- env: OPENAI_API_KEY
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_QUEUE = ROOT / "scripts" / "xiaojun_queue.jsonl"
DEFAULT_AUDIO_DIR = ROOT / "data" / "audio" / "xiaojun"
DEFAULT_OUT_DIR = ROOT / "transcripts" / "xiaojun"
DEFAULT_COOKIES = Path.home() / ".openclaw" / "secrets" / "youtube_cookies.txt"


@dataclass
class Item:
    episode: int
    slug: str
    guest: str
    title: str
    date: str
    url: str


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def run_retry(cmd: list[str], tries: int = 3, sleep_seconds: int = 10) -> None:
    last = None
    for i in range(tries):
        try:
            run(cmd)
            return
        except subprocess.CalledProcessError as e:
            last = e
            if i < tries - 1:
                print(f"[warn] command failed, retry {i+1}/{tries}: {' '.join(cmd)}")
                subprocess.run(["bash", "-lc", f"sleep {sleep_seconds}"], check=False)
    raise last  # type: ignore[misc]



def ensure_deps() -> None:
    for bin_name in ["yt-dlp", "ffmpeg", "ffprobe"]:
        if subprocess.call(["bash", "-lc", f"command -v {bin_name} >/dev/null 2>&1"]) != 0:
            raise SystemExit(f"missing dependency: {bin_name}")


def load_queue(path: Path) -> list[Item]:
    items: list[Item] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        d = json.loads(line)
        items.append(Item(
            episode=int(d["episode"]),
            slug=str(d["slug"]),
            guest=str(d.get("guest", "")),
            title=str(d.get("title", "")),
            date=str(d.get("date", "")),
            url=str(d["url"]),
        ))
    return items


def download_audio(item: Item, audio_dir: Path, cookies: Path) -> Path:
    audio_dir.mkdir(parents=True, exist_ok=True)
    # Prefer deterministic filename, but keep original container (webm/m4a)
    out_tmpl = str(audio_dir / f"{item.slug}.%(ext)s")
    cmd = [
        "yt-dlp",
        "-f",
        "bestaudio",
        "-o",
        out_tmpl,
        "--no-progress",
        "--retries",
        "10",
        "--fragment-retries",
        "10",
        "--retry-sleep",
        "5",
    ]
    if cookies.exists():
        cmd += ["--cookies", str(cookies)]
    cmd.append(item.url)

    run_retry(cmd, tries=3, sleep_seconds=15)

    # Find the downloaded file
    candidates = sorted(audio_dir.glob(f"{item.slug}.*"))
    if not candidates:
        raise RuntimeError(f"download failed: {item.slug}")
    # pick largest
    return max(candidates, key=lambda p: p.stat().st_size)


def audio_duration_seconds(path: Path) -> float:
    out = subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(path)
    ], text=True).strip()
    return float(out)


def to_mp3(src: Path, dst: Path) -> None:
    run(["ffmpeg", "-y", "-i", str(src), "-vn", "-acodec", "libmp3lame", "-q:a", "5", str(dst), "-loglevel", "error"])


def segment_mp3(src: Path, out_dir: Path, segment_seconds: int) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    out_tmpl = str(out_dir / "part_%03d.mp3")
    run(["ffmpeg", "-y", "-i", str(src), "-f", "segment", "-segment_time", str(segment_seconds), "-c", "copy", out_tmpl, "-loglevel", "error"])
    return sorted(out_dir.glob("part_*.mp3"))


def fmt_time(seconds: float) -> str:
    s = int(seconds)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    if h:
        return f"{h:02d}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"


def transcribe_chunk(path: Path, language: str | None) -> dict:
    from openai import OpenAI

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("missing env: OPENAI_API_KEY")

    client = OpenAI(api_key=api_key)
    with path.open("rb") as f:
        resp = client.audio.transcriptions.create(
            model="whisper-1",
            file=f,
            language=language,
            response_format="verbose_json",
            timestamp_granularities=["segment"],
        )

    # Convert to plain dict for stable handling
    segs = []
    for s in (resp.segments or []):
        segs.append({"start": float(s.start), "end": float(s.end), "text": str(s.text)})

    return {
        "text": resp.text,
        "language": resp.language,
        "duration": float(resp.duration),
        "segments": segs,
    }


def write_transcript(item: Item, merged: dict, out_path: Path) -> None:
    fm = {
        "type": "transcript",
        "series": "xiaojun",
        "episode": item.episode,
        "date": item.date,
        "guest": item.guest,
        "title": item.title,
        "source_url": item.url,
    }

    lines = [
        "---",
        *[f"{k}: {json.dumps(v, ensure_ascii=False) if isinstance(v, str) and (':' in v) else v}" for k, v in fm.items()],
        "---",
        "",
        f"# Transcript: EP{item.episode} {item.guest} - {item.title}",
        "",
        f"Source: {item.url}",
        "",
        "---",
        "",
    ]

    for seg in merged.get("segments", []):
        t = fmt_time(seg["start"])
        txt = seg["text"].strip()
        if txt:
            lines.append(f"**[{t}]** {txt}")

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def ensure_analysis_template(item: Item, out_path: Path) -> None:
    if out_path.exists():
        return

    content = f"""---
type: analysis
series: xiaojun
episode: {item.episode}
date: {item.date}
guest: {item.guest}
title: {item.title}
source_url: {item.url}
---

# Analysis: EP{item.episode} - {item.guest}

## 0. 3-5 句摘要

TBD

## 1. 反共识/非显然观点

TBD

## 2. 可学习的点（可迁移的方法论）

TBD

## 3. 提问技巧（采访方法）

TBD

## 4. 可进一步验证/挖坑

TBD
"""
    out_path.write_text(content, encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--queue", type=Path, default=DEFAULT_QUEUE)
    ap.add_argument("--audio-dir", type=Path, default=DEFAULT_AUDIO_DIR)
    ap.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    ap.add_argument("--cookies", type=Path, default=DEFAULT_COOKIES)
    ap.add_argument("--language", default="zh")
    ap.add_argument("--segment-seconds", type=int, default=900)
    ap.add_argument("--download-missing", action="store_true", help="if audio missing, download via yt-dlp")
    args = ap.parse_args()

    ensure_deps()

    items = load_queue(args.queue)
    args.out_dir.mkdir(parents=True, exist_ok=True)

    for item in items:
        transcript_path = args.out_dir / f"{item.slug}.md"
        analysis_path = args.out_dir / f"{item.slug}.analysis.md"

        if transcript_path.exists():
            print(f"[skip transcript exists] {transcript_path}")
            ensure_analysis_template(item, analysis_path)
            continue

        audio_file = None
        candidates = list(args.audio_dir.glob(f"{item.slug}.*"))
        if candidates:
            audio_file = max(candidates, key=lambda p: p.stat().st_size)
        else:
            if not args.download_missing:
                print(f"[skip missing audio] {item.slug} (pass --download-missing to auto-download)")
                continue
            try:
                audio_file = download_audio(item, args.audio_dir, args.cookies)
            except Exception as e:
                print(f"[error download] {item.slug}: {e}")
                continue

        with tempfile.TemporaryDirectory() as td:
            td_path = Path(td)
            mp3 = td_path / f"{item.slug}.mp3"
            to_mp3(audio_file, mp3)

            seg_dir = td_path / "chunks"
            chunks = segment_mp3(mp3, seg_dir, args.segment_seconds)

            merged = {"segments": []}
            offset = 0.0
            for idx, ch in enumerate(chunks):
                print(f"[transcribe] {item.slug} chunk {idx+1}/{len(chunks)}")
                data = transcribe_chunk(ch, args.language)
                for s in data.get("segments", []):
                    merged["segments"].append({
                        "start": float(s["start"]) + offset,
                        "end": float(s["end"]) + offset,
                        "text": s["text"],
                    })
                offset += float(data.get("duration", 0.0))

        merged["segments"].sort(key=lambda x: x["start"])
        write_transcript(item, merged, transcript_path)
        ensure_analysis_template(item, analysis_path)
        print(f"[ok] wrote {transcript_path}")


if __name__ == "__main__":
    main()
