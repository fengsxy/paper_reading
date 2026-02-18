#!/usr/bin/env python3

import argparse
import json
import pathlib
import re
import subprocess
from datetime import datetime, timezone


def slugify(text: str) -> str:
    t = text.lower().strip()
    t = re.sub(r"https?://", "", t)
    t = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "_", t)
    t = re.sub(r"_+", "_", t).strip("_")
    return t[:120]


def run_yt_dlp(url: str):
    cmd = [
        "yt-dlp",
        "--flat-playlist",
        "--print",
        "%(id)s\t%(title)s\t%(upload_date)s\t%(duration)s\t%(channel)s\t%(webpage_url)s",
        url,
    ]
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    if p.returncode != 0:
        raise RuntimeError(p.stderr.strip() or "yt-dlp failed")
    rows = []
    for line in p.stdout.splitlines():
        parts = line.split("\t")
        if len(parts) < 6:
            continue
        vid, title, upload_date, duration, channel, webpage_url = parts[:6]
        rows.append(
            {
                "video_id": vid.strip(),
                "title": title.strip(),
                "upload_date": upload_date.strip(),
                "duration": duration.strip(),
                "channel": channel.strip(),
                "url": webpage_url.strip() or f"https://www.youtube.com/watch?v={vid.strip()}",
            }
        )
    return rows


def build_series_index(series_cfg: dict, out_root: pathlib.Path):
    series = series_cfg["series"].strip()
    url = (series_cfg.get("url") or "").strip()
    out_dir = out_root / series
    out_dir.mkdir(parents=True, exist_ok=True)

    if not url:
        return {"series": series, "status": "skipped", "reason": "missing url", "count": 0}

    items = run_yt_dlp(url)

    normalized = []
    for i, it in enumerate(items, start=1):
        ep = i
        ep_match = re.match(r"^\s*(\d{1,4})[\.、\s_-]", it["title"])
        if ep_match:
            try:
                ep = int(ep_match.group(1))
            except Exception:
                pass
        normalized.append(
            {
                "episode": ep,
                "slug": f"{ep}_{slugify(it['title'])[:80]}",
                "title": it["title"],
                "date": it["upload_date"],
                "url": it["url"],
                "video_id": it["video_id"],
                "duration": it["duration"],
                "channel": it["channel"],
            }
        )

    normalized.sort(key=lambda x: (x.get("episode", 10**9), x.get("date", "")))

    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    json_path = out_dir / "index.json"
    md_path = out_dir / "index.md"

    json_path.write_text(json.dumps({"series": series, "generated_at": ts, "items": normalized}, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "---",
        "layout: default",
        f'title: "{series_cfg.get("name", series)} Index"',
        f"permalink: /podcast_index/{series}/",
        "---",
        "",
        f"# {series_cfg.get('name', series)} - Full Index",
        "",
        f"Generated at: `{ts}`",
        "",
        f"Total videos: **{len(normalized)}**",
        "",
        "| # | Date | Title | Link |",
        "|---:|:----:|---|---|",
    ]
    for it in normalized:
        d = it.get("date", "")
        lines.append(f"| {it['episode']} | {d} | {it['title'].replace('|','/')} | [YouTube]({it['url']}) |")
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    return {"series": series, "status": "ok", "count": len(normalized), "md": str(md_path), "json": str(json_path)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="scripts/podcast_channels.json")
    ap.add_argument("--out-dir", default="podcast_index")
    args = ap.parse_args()

    cfg = json.loads(pathlib.Path(args.config).read_text(encoding="utf-8"))
    out_root = pathlib.Path(args.out_dir)
    out_root.mkdir(parents=True, exist_ok=True)

    results = []
    for c in cfg:
        try:
            r = build_series_index(c, out_root)
        except Exception as e:
            r = {"series": c.get("series", "unknown"), "status": "error", "reason": str(e), "count": 0}
        results.append(r)

    (out_root / "index.json").write_text(json.dumps({"generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "results": results}, ensure_ascii=False, indent=2), encoding="utf-8")

    top = [
        "---",
        "layout: default",
        "title: \"Podcast Full Index\"",
        "permalink: /podcast_index/",
        "---",
        "",
        "# Podcast Full Index",
        "",
    ]
    for r in results:
        if r["status"] == "ok":
            top.append(f"- [{r['series']}](/podcast_index/{r['series']}/) ({r['count']} videos)")
        else:
            top.append(f"- {r['series']}: {r['status']} ({r.get('reason','')})")
    (out_root / "index.md").write_text("\n".join(top) + "\n", encoding="utf-8")

    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
