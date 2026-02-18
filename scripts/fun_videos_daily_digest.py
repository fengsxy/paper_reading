#!/usr/bin/env python3

import argparse
import datetime as dt
import email.utils
import json
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET


def _read_json(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _http_get(url: str, timeout: int = 30) -> bytes:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "paper_reading-fun_videos/1.0 (+https://github.com/fengsxy/paper_reading)"
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def _parse_atom(xml_bytes: bytes):
    # YouTube RSS is Atom.
    root = ET.fromstring(xml_bytes)

    ns = {
        "atom": "http://www.w3.org/2005/Atom",
        "yt": "http://www.youtube.com/xml/schemas/2015",
        "media": "http://search.yahoo.com/mrss/",
    }

    entries = []
    for e in root.findall("atom:entry", ns):
        title_el = e.find("atom:title", ns)
        link_el = e.find("atom:link", ns)
        published_el = e.find("atom:published", ns)
        updated_el = e.find("atom:updated", ns)

        title = (title_el.text or "").strip() if title_el is not None else ""
        link = link_el.get("href") if link_el is not None else None
        published_raw = (published_el.text or "").strip() if published_el is not None else ""
        updated_raw = (updated_el.text or "").strip() if updated_el is not None else ""

        when = None
        for raw in (published_raw, updated_raw):
            if not raw:
                continue
            try:
                when = dt.datetime.fromisoformat(raw.replace("Z", "+00:00"))
                break
            except Exception:
                continue

        if not link:
            continue

        entries.append(
            {
                "title": title,
                "url": link,
                "published_at": when,
            }
        )

    return entries


def _canonical_url(url: str) -> str:
    # Remove common tracking params.
    url = re.sub(r"[?&](si|feature|pp|t|list)=[^&#]+", "", url)
    url = url.replace("&&", "&").replace("?&", "?")
    url = url.rstrip("?&")
    return url


def _score(title: str) -> int:
    t = title.lower()
    plus = [
        "纪录",
        "访谈",
        "对话",
        "一口气",
        "完整",
        "深度",
        "解析",
        "讲清楚",
        "时间线",
        "背后",
        "为什么",
        "如何",
        "历史",
        "地缘",
        "经济",
        "投资",
        "科技",
        "工程",
        "社会",
        "人物",
        "故事",
        "冷知识",
        "反转",
    ]
    minus = [
        "带货",
        "广告",
        "抽奖",
        "直播",
    ]

    s = 0
    for k in plus:
        if k.lower() in t:
            s += 2
    for k in minus:
        if k.lower() in t:
            s -= 3
    return s


def _format_digest(date_str: str, items):
    lines = []
    lines.append("---")
    lines.append("layout: default")
    lines.append(f'title: "Fun Videos {date_str}"')
    lines.append(f"permalink: /fun_videos/{date_str}/")
    lines.append("---")
    lines.append("")
    lines.append(f"# Fun Videos | {date_str}")
    lines.append("")
    lines.append("> Picks meant for two people to watch together: high signal, story/insight-driven, and discussion-friendly.")
    lines.append("")

    if not items:
        lines.append("No new picks today.")
        lines.append("")
        return "\n".join(lines)

    for it in items:
        title = it["title"]
        url = it["url"]
        source = it.get("source", "")
        lines.append(f"## {title}")
        lines.append("")
        if source:
            lines.append(f"Source: {source}")
            lines.append("")
        lines.append(f"Link: {url}")
        lines.append("")
        lines.append("Couple angle: (auto) Talk about: what surprised you, what you'd do differently, and what you disagree on.")
        lines.append("")

    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sources", default="scripts/fun_videos_sources.json")
    ap.add_argument("--out-dir", default="fun_videos")
    ap.add_argument("--days", type=int, default=1)
    ap.add_argument("--max-items", type=int, default=10)
    ap.add_argument("--min-new", type=int, default=3)
    args = ap.parse_args()

    now = dt.datetime.now(dt.timezone.utc)
    start = now - dt.timedelta(days=args.days)

    sources = _read_json(args.sources)

    all_items = []
    for src in sources:
        cid = src.get("channel_id")
        name = src.get("name") or cid
        if not cid or cid.startswith("UCxxxxxxxx"):
            continue
        feed_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={cid}"
        try:
            xml_bytes = _http_get(feed_url)
            entries = _parse_atom(xml_bytes)
        except Exception as e:
            print(f"WARN: failed to fetch/parse {name}: {e}", file=sys.stderr)
            continue

        for ent in entries:
            when = ent.get("published_at")
            if when is None:
                continue
            if when < start:
                continue
            u = _canonical_url(ent["url"])
            all_items.append(
                {
                    "title": ent.get("title", "").strip(),
                    "url": u,
                    "published_at": when,
                    "source": f"YouTube: {name}",
                    "score": _score(ent.get("title", "")),
                }
            )

    # De-dupe by canonical url.
    seen = set()
    deduped = []
    for it in sorted(all_items, key=lambda x: (x["score"], x["published_at"]), reverse=True):
        if it["url"] in seen:
            continue
        seen.add(it["url"])
        deduped.append(it)

    picked = deduped[: args.max_items]

    date_str = now.date().isoformat()
    os.makedirs(args.out_dir, exist_ok=True)
    out_path = os.path.join(args.out_dir, f"{date_str}.md")

    # Only write when enough new items.
    if len(picked) < args.min_new:
        print(f"No write: only {len(picked)} new items (< min_new={args.min_new}).")
        return 0

    content = _format_digest(date_str, picked)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
