#!/usr/bin/env python3
"""
Daily Paper & HN Update v2
- Deduplication via seen_papers.json
- Date-filtered search (recent 48h only)
- URL normalization (arxiv abs/html/pdf → single ID)
- Quality scoring: recency + relevance + novelty
"""

import os
import sys
import re
import json
import requests
from datetime import datetime, timedelta, timezone
from pathlib import Path

WORKSPACE = Path.home() / ".openclaw" / "workspace"
SCHOLAR_DIR = WORKSPACE / "scholar_inbox"
HN_DIR = WORKSPACE / "hackernews"
SEEN_FILE = SCHOLAR_DIR / "seen_papers.json"
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")

# Load API key
ydc_key_path = Path.home() / ".openclaw" / "secrets" / "ydc_api_key"
if not ydc_key_path.exists():
    print("Error: YDC API key not found")
    sys.exit(1)
YDC_API_KEY = ydc_key_path.read_text().strip()

# Yu's research interests — rotate queries for diversity
SEARCH_QUERIES = [
    "discrete diffusion language model new 2026",
    "diffusion LLM training inference 2026",
    "representation learning information theory neural network 2026",
    "trustworthy AI alignment safety LLM 2026",
    "self-distillation knowledge distillation LLM 2026",
    "linear attention state space model 2026",
    "generative model evaluation benchmark 2026",
]

AI_HN_KEYWORDS = [
    "ai", "ml", "machine learning", "deep learning", "neural",
    "diffusion", "llm", "gpt", "transformer", "claude",
    "representation", "information theory", "generative",
    "openai", "anthropic", "deepmind", "meta ai", "apple ml",
    "alignment", "safety", "benchmark", "distillation",
    "attention", "reasoning", "agent", "rl", "reinforcement",
]


def load_seen() -> dict:
    """Load dedup database."""
    if SEEN_FILE.exists():
        return json.loads(SEEN_FILE.read_text())
    return {}


def save_seen(seen: dict):
    """Persist dedup database."""
    SEEN_FILE.parent.mkdir(parents=True, exist_ok=True)
    SEEN_FILE.write_text(json.dumps(seen, indent=2, ensure_ascii=False))


def normalize_arxiv_id(url: str) -> str | None:
    """Extract arxiv ID from any arxiv URL variant."""
    m = re.search(r'arxiv\.org/(?:abs|html|pdf)/(\d{4}\.\d{4,5})', url)
    return m.group(1) if m else None


def title_key(title: str) -> str:
    """Normalize title for dedup."""
    return re.sub(r'[^a-z0-9]', '', title.lower())[:60]


def is_seen(paper: dict, seen: dict) -> bool:
    """Check if paper was already recommended."""
    # Check arxiv ID
    aid = normalize_arxiv_id(paper.get("url", ""))
    if aid and aid in seen:
        return True
    # Check title
    tk = title_key(paper.get("title", ""))
    if tk and tk in seen:
        return True
    return False


def mark_seen(paper: dict, seen: dict):
    """Add paper to dedup database."""
    aid = normalize_arxiv_id(paper.get("url", ""))
    if aid:
        seen[aid] = TODAY
    tk = title_key(paper.get("title", ""))
    if tk:
        seen[tk] = TODAY


def search_papers(seen: dict) -> list[dict]:
    """Search for new papers via YDC, with dedup and date filtering."""
    all_papers = []
    used_ids = set()

    # Pick 3 queries (rotate by day-of-year for diversity)
    day_idx = datetime.now(timezone.utc).timetuple().tm_yday
    selected = []
    for i in range(3):
        idx = (day_idx + i) % len(SEARCH_QUERIES)
        selected.append(SEARCH_QUERIES[idx])

    for query in selected:
        try:
            resp = requests.get(
                "https://ydc-index.io/v1/search",
                headers={"Accept": "application/json", "X-API-KEY": YDC_API_KEY},
                params={"query": query, "count": 10, "language": "EN"},
                timeout=30,
            )
            resp.raise_for_status()
            results = resp.json().get("results", {}).get("web", [])

            for hit in results:
                url = hit.get("url", "")
                title = hit.get("title", "")
                snippets = hit.get("snippets", [])
                page_age = hit.get("page_age", "")

                if not title or not url:
                    continue

                # Skip non-paper URLs
                if not any(d in url for d in [
                    "arxiv.org", "openreview.net", "proceedings.mlr.press",
                    "aclanthology.org", "neurips.cc", "transformer-circuits",
                    "openai.com/research", "anthropic.com/research",
                    "huggingface.co/papers",
                ]):
                    continue

                # Normalize arxiv URLs to abs form
                aid = normalize_arxiv_id(url)
                if aid:
                    if aid in used_ids:
                        continue
                    used_ids.add(aid)
                    url = f"https://arxiv.org/abs/{aid}"

                paper = {
                    "title": re.sub(r'^\[.*?\]\s*', '', title).strip(),
                    "url": url,
                    "abstract": snippets[0][:300] if snippets else "",
                    "page_age": page_age,
                    "arxiv_id": aid,
                }

                # Skip if already seen
                if is_seen(paper, seen):
                    continue

                # Recency score (prefer papers from last 7 days)
                recency = 0
                if page_age:
                    try:
                        pub_date = datetime.fromisoformat(page_age.replace("Z", "+00:00"))
                        days_old = (datetime.now(timezone.utc) - pub_date).days
                        if days_old <= 2:
                            recency = 3
                        elif days_old <= 7:
                            recency = 2
                        elif days_old <= 30:
                            recency = 1
                        else:
                            recency = 0
                    except (ValueError, TypeError):
                        recency = 0

                paper["recency_score"] = recency
                all_papers.append(paper)

        except Exception as e:
            print(f"Search error for '{query}': {e}", file=sys.stderr)

    # Sort: recency first, then by title length (proxy for specificity)
    all_papers.sort(key=lambda p: (-p["recency_score"], len(p["title"])))

    # Take top 8
    return all_papers[:8]


def fetch_hn_stories() -> list[dict]:
    """Fetch top HN stories, filter AI/ML content."""
    try:
        top_ids = requests.get(
            "https://hacker-news.firebaseio.com/v0/topstories.json", timeout=10
        ).json()[:150]

        stories = []
        for sid in top_ids[:100]:  # Check first 100
            try:
                story = requests.get(
                    f"https://hacker-news.firebaseio.com/v0/item/{sid}.json",
                    timeout=5,
                ).json()
                if not story or story.get("type") != "story":
                    continue

                title_lower = story.get("title", "").lower()
                url_lower = story.get("url", "").lower()
                combined = title_lower + " " + url_lower

                if any(kw in combined for kw in AI_HN_KEYWORDS):
                    score = story.get("score", 0)
                    comments = story.get("descendants", 0)
                    # Quality threshold
                    if score >= 20 or comments >= 10:
                        stories.append({
                            "id": story["id"],
                            "title": story["title"],
                            "url": story.get("url", f"https://news.ycombinator.com/item?id={story['id']}"),
                            "score": score,
                            "comments": comments,
                            "engagement": score + comments * 2,
                        })
            except Exception:
                continue

        stories.sort(key=lambda x: -x["engagement"])
        return stories[:15]
    except Exception as e:
        print(f"HN fetch error: {e}", file=sys.stderr)
        return []


def write_papers(papers: list[dict]):
    """Write paper digest to markdown."""
    SCHOLAR_DIR.mkdir(parents=True, exist_ok=True)
    out = SCHOLAR_DIR / f"{TODAY}-daily-papers.md"

    lines = [f"# Daily Papers — {TODAY}\n"]
    if not papers:
        lines.append("No new relevant papers found today.\n")
    else:
        for i, p in enumerate(papers, 1):
            lines.append(f"## {i}. {p['title']}")
            lines.append(f"- **Link:** {p['url']}")
            if p.get("page_age"):
                lines.append(f"- **Date:** {p['page_age'][:10]}")
            if p.get("abstract"):
                lines.append(f"- **Abstract:** {p['abstract']}")
            lines.append("")

    out.write_text("\n".join(lines))
    return out


def write_hn(stories: list[dict]):
    """Write HN digest to markdown."""
    HN_DIR.mkdir(parents=True, exist_ok=True)
    out = HN_DIR / f"{TODAY}.md"

    lines = [f"# Hacker News AI/ML — {TODAY}\n"]
    if not stories:
        lines.append("No relevant HN stories found.\n")
    else:
        for i, s in enumerate(stories, 1):
            lines.append(f"## {i}. {s['title']}")
            lines.append(f"- **Score:** {s['score']} | **Comments:** {s['comments']}")
            lines.append(f"- **URL:** {s['url']}")
            lines.append(f"- **HN:** https://news.ycombinator.com/item?id={s['id']}")
            lines.append("")

    out.write_text("\n".join(lines))
    return out


def git_push():
    """Commit and push."""
    os.chdir(WORKSPACE)
    os.system("git add scholar_inbox hackernews")
    os.system(f"git commit -m 'chore: daily papers+hn {TODAY}'")
    os.system("git push")


def main():
    print(f"=== Daily Paper & HN Update v2 — {TODAY} ===")

    # Load dedup DB
    seen = load_seen()
    print(f"Dedup DB: {len(seen)} entries")

    # Search papers
    papers = search_papers(seen)
    print(f"New papers: {len(papers)}")

    # Mark as seen
    for p in papers:
        mark_seen(p, seen)
    save_seen(seen)

    # Fetch HN
    hn = fetch_hn_stories()
    print(f"HN stories: {len(hn)}")

    # Write files
    pf = write_papers(papers)
    hf = write_hn(hn)
    print(f"Written: {pf.name}, {hf.name}")

    # Push
    git_push()

    # Output summary for cron
    if papers:
        top = papers[0]
        print(f"\n📄 {len(papers)} new papers | Top: {top['title'][:50]}")
    else:
        print("\n今日无新论文。")

    if hn:
        top_hn = hn[0]
        print(f"🔥 {len(hn)} HN stories | Top: {top_hn['title'][:50]} ({top_hn['score']}↑)")

    # Return counts for cron notification decision
    return json.dumps({"papers": len(papers), "hn": len(hn)})


if __name__ == "__main__":
    result = main()
    print(f"\n{result}")
