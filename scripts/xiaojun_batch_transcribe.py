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
from concurrent.futures import ThreadPoolExecutor, as_completed


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


def to_m4a(src: Path, dst: Path) -> None:
    # Avoid MP3 muxer DTS issues by using M4A (AAC). OpenAI supports m4a.
    run([
        "ffmpeg",
        "-y",
        "-fflags",
        "+genpts",
        "-i",
        str(src),
        "-vn",
        "-af",
        "aresample=async=1:first_pts=0",
        "-c:a",
        "aac",
        "-b:a",
        "96k",
        str(dst),
        "-loglevel",
        "error",
    ])


def chunk_audio(src: Path, out_dir: Path, segment_seconds: int) -> list[tuple[float, Path]]:
    """Chunk by re-encoding each segment with -ss/-t.

    Returns a list of (start_seconds, chunk_path).

    This avoids ffmpeg segment muxer timestamp pitfalls and makes it safe
    to transcribe chunks concurrently while preserving global timestamps.
    """
    out_dir.mkdir(parents=True, exist_ok=True)

    total = audio_duration_seconds(src)
    chunks: list[tuple[float, Path]] = []
    start = 0
    idx = 0
    while start < int(total) + 1:
        out = out_dir / f"part_{idx:03d}.m4a"
        run([
            "ffmpeg",
            "-y",
            "-fflags",
            "+genpts",
            "-ss",
            str(start),
            "-t",
            str(segment_seconds),
            "-i",
            str(src),
            "-vn",
            "-af",
            "aresample=async=1:first_pts=0",
            "-c:a",
            "aac",
            "-b:a",
            "96k",
            str(out),
            "-loglevel",
            "error",
        ])
        if out.exists() and out.stat().st_size > 0:
            chunks.append((float(start), out))
        start += segment_seconds
        idx += 1

    return chunks


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
    ap.add_argument("--segment-seconds", type=int, default=1800, help="chunk size in seconds; set to 0 to disable chunking")
    ap.add_argument("--max-workers", type=int, default=4, help="max concurrent Whisper requests per episode")
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
            m4a = td_path / f"{item.slug}.m4a"
            to_m4a(audio_file, m4a)

            merged = {"segments": []}

            # If segment_seconds is 0, do a single request for the whole file.
            # This can be faster but may be more failure-prone for long episodes.
            if int(args.segment_seconds) <= 0:
                print(f"[transcribe] {item.slug} single-shot")
                data = transcribe_chunk(m4a, args.language)
                for s in data.get("segments", []):
                    merged["segments"].append({
                        "start": float(s["start"]),
                        "end": float(s["end"]),
                        "text": s["text"],
                    })
            else:
                seg_dir = td_path / "chunks"
                chunks = chunk_audio(m4a, seg_dir, args.segment_seconds)

                def _work(i: int, start_s: float, ch_path: Path) -> tuple[int, float, dict]:
                    print(f"[transcribe] {item.slug} chunk {i+1}/{len(chunks)}")
                    data = transcribe_chunk(ch_path, args.language)
                    return (i, start_s, data)

                with ThreadPoolExecutor(max_workers=max(1, int(args.max_workers))) as ex:
                    futs = [ex.submit(_work, i, start_s, ch_path) for i, (start_s, ch_path) in enumerate(chunks)]
                    for fut in as_completed(futs):
                        i, start_s, data = fut.result()
                        for s in data.get("segments", []):
                            merged["segments"].append({
                                "start": float(s["start"]) + float(start_s),
                                "end": float(s["end"]) + float(start_s),
                                "text": s["text"],
                            })

        merged["segments"].sort(key=lambda x: x["start"])
        write_transcript(item, merged, transcript_path)
        ensure_analysis_template(item, analysis_path)
        print(f"[ok] wrote {transcript_path}")


if __name__ == "__main__":
    main()
