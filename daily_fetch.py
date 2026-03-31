#!/usr/bin/env python3
"""
Daily fetch of AI/ML papers from YDC (arXiv) and Hacker News highlights.
Writes markdown files to scholar_inbox/ and hackernews/.
Evaluates content volume and prints a concise summary to stdout (for cron notification).
"""

import os
import sys
import json
import re
import subprocess
import datetime
from pathlib import Path
from collections import OrderedDict

import requests

# Paths
workspace = Path('.')
scholar_dir = workspace / 'scholar_inbox'
hn_dir = workspace / 'hackernews'
scholar_dir.mkdir(exist_ok=True)
hn_dir.mkdir(exist_ok=True)

today = datetime.date.today()
today_str = today.strftime('%Y-%m-%d')
weekday = today.strftime('%A')
scholar_outfile = scholar_dir / f"{today_str}-daily-papers.md"
hn_outfile = hn_dir / f"{today_str}.md"

# YDC API setup
ydc_key_path = Path.home() / '.openclaw/secrets/ydc_api_key'
try:
    ydc_key = ydc_key_path.read_text().strip()
except Exception as e:
    print(f"Error reading YDC key: {e}", file=sys.stderr)
    sys.exit(1)

ydc_url = 'https://ydc-index.io/v1/search'
ydc_headers = {'Accept': 'application/json', 'X-API-KEY': ydc_key}

# Search queries: focus on diffusion, LLM, info theory, representation learning
queries = [
    '"diffusion model" site:arxiv.org',
    '"diffusion language model" site:arxiv.org',
    '("large language model" OR "LLM") site:arxiv.org',
    '"information theory" site:arxiv.org',
    '"representation learning" site:arxiv.org'
]

def fetch_papers():
    all_papers = []
    seen_urls = set()
    for q in queries:
        params = {'query': q, 'count': 10, 'freshness': 'week'}
        try:
            resp = requests.get(ydc_url, headers=ydc_headers, params=params, timeout=10)
            if resp.status_code != 200:
                print(f"YDC query failed: {q} -> {resp.status_code}", file=sys.stderr)
                continue
            data = resp.json()
            for item in data.get('results', {}).get('web', []):
                url = item.get('url')
                if url in seen_urls:
                    continue
                # Keep only arXiv links
                if 'arxiv.org/' in url and ('abs' in url or 'pdf' in url or 'html' in url):
                    # Extract arXiv ID
                    m = re.search(r'arxiv\.org/(abs|pdf|html)/([^\/]+)', url)
                    if not m:
                        continue
                    arxiv_id = m.group(2)
                    base_id = arxiv_id.split('v')[0]
                    title = item.get('title', '').strip()
                    # Remove leading [ID] if present
                    title = re.sub(r'^\[\w+\]\s*', '', title)
                    description = item.get('description', '')
                    page_age = item.get('page_age', '')
                    date_str = page_age.split('T')[0] if page_age else ''
                    paper = {
                        'title': title,
                        'url': url,
                        'abstract': description,
                        'date': date_str,
                        'id': base_id
                    }
                    all_papers.append(paper)
                    seen_urls.add(url)
        except requests.RequestException as e:
            print(f"Request error for query '{q}': {e}", file=sys.stderr)
        except json.JSONDecodeError as e:
            print(f"JSON decode error for query '{q}': {e}", file=sys.stderr)
    # Remove duplicates by arXiv ID (in case URLs differ)
    unique = {}
    for p in all_papers:
        unique[p['id']] = p
    papers = list(unique.values())
    # Sort by date descending, then by ID (newer IDs usually later)
    papers.sort(key=lambda p: (p['date'] or '', p['id']), reverse=True)
    return papers

def fetch_hn():
    # HN Algolia API: get stories from last 2 days with AI/ML keywords
    hn_url = 'https://hn.algolia.com/api/v1/search'
    two_days_ago = datetime.datetime.now() - datetime.timedelta(days=2)
    ts = int(two_days_ago.timestamp())
    params = {
        'query': 'AI',
        'tags': 'story',
        'numericFilters': f'created_at_i>{ts}',
        'hitsPerPage': 100
    }
    try:
        resp = requests.get(hn_url, params=params, timeout=10)
        if resp.status_code != 200:
            print(f"HN fetch failed: {resp.status_code}", file=sys.stderr)
            return []
        data = resp.json()
        hits = data.get('hits', [])
        relevant = []
        keywords = ['ai', 'llm', 'large language model', 'machine learning', 'diffusion',
                    'representation learning', 'information theory', 'ml', 'deep learning']
        for hit in hits:
            title = hit.get('title', '')
            url = hit.get('url')
            if not url:
                continue  # skip internal HN posts
            title_lower = title.lower()
            if not any(k in title_lower for k in keywords):
                continue
            relevant.append({
                'title': title,
                'url': url,
                'points': hit.get('points', 0),
                'comments': hit.get('num_comments', 0),
                'created_at': hit.get('created_at'),
                'objectID': hit.get('objectID')
            })
        # Sort by points descending
        relevant.sort(key=lambda x: x['points'], reverse=True)
        return relevant
    except requests.RequestException as e:
        print(f"Error fetching HN: {e}", file=sys.stderr)
        return []

# Main
papers = fetch_papers()
hn_stories = fetch_hn()

# Determine high-value HN (points>=10 or comments>=10)
hn_high_value = [s for s in hn_stories if s['points'] >= 10 or s['comments'] >= 10]
papers_count = len(papers)
hn_count = len(hn_high_value)

# Write scholar_inbox file
with open(scholar_outfile, 'w', encoding='utf-8') as f:
    f.write(f"# Daily Papers — {today_str} ({weekday})\n\n")
    if papers_count == 0:
        f.write("> 今日未检索到新论文。\n")
    elif papers_count < 3:
        f.write(f"> 今日新论文较少（{papers_count}篇），以下为近期值得关注但非今日新发的论文。\n")
    else:
        f.write(f"> 今日发现 {papers_count} 篇相关新论文（arXiv 一周内），重点关注以下精选：\n")
    f.write("\n")
    for i, p in enumerate(papers, 1):
        f.write(f"## {i}. {p['title']}\n")
        f.write(f"- **Date:** {p['date'] or 'N/A'}\n")
        f.write(f"- **arXiv:** [{p['id']}]({p['url']})\n")
        if p['abstract']:
            # Show first 200 chars of abstract/snippet
            snippet = p['abstract'][:200].strip()
            if len(p['abstract']) > 200:
                snippet += "..."
            f.write(f"- **Snippet:** {snippet}\n")
        f.write("\n")

# Write hackernews file
with open(hn_outfile, 'w', encoding='utf-8') as f:
    f.write(f"# Hacker News — {today_str}\n\n")
    if len(hn_stories) == 0:
        f.write("> 今日未检索到 AI/ML 相关讨论。\n")
    elif len(hn_stories) < 3:
        f.write(f"> 今日 AI/ML 讨论较少（{len(hn_stories)}条），以下为近期值得关注的内容。\n")
    else:
        f.write(f"## AI/ML 相关（共 {len(hn_stories)} 条，高价值（≥10分或≥10评论）{hn_count} 条）\n\n")
    # List all stories (high-value highlighted)
    for i, s in enumerate(hn_stories, 1):
        points = s['points']
        comments = s['comments']
        is_high = points >= 10 or comments >= 10
        prefix = "🔥 " if is_high else ""
        f.write(f"### {i}. {prefix}{s['title']}\n")
        f.write(f"- **Points:** {points} | **Comments:** {comments} | [HN讨论](https://news.ycombinator.com/item?id={s['objectID']})\n")
        if s['url']:
            f.write(f"- **Link:** {s['url']}\n")
        f.write("\n")

# Git add/commit/push
try:
    subprocess.run(['git', 'add', 'scholar_inbox', 'hackernews'], check=True, cwd=workspace)
    commit_msg = f"chore: daily papers+hn {today_str}"
    subprocess.run(['git', 'commit', '-m', commit_msg], check=True, cwd=workspace)
    subprocess.run(['git', 'push'], check=True, cwd=workspace)
    print("Git push completed.", file=sys.stderr)
except subprocess.CalledProcessError as e:
    print(f"Git operation failed: {e}", file=sys.stderr)
except FileNotFoundError:
    print("Git not found, skipping commit.", file=sys.stderr)

# Determine final summary for cron notification
if papers_count < 3 or hn_count < 3:
    final_summary = "今日新内容不足，已归档。"
else:
    # Extract top 1-2 insights: pick top paper and top HN high-value
    insight_parts = []
    if papers:
        # Take the newest paper's title or snippet? We'll shorten title to ~15 chars if possible.
        p_title = papers[0]['title']
        if len(p_title) > 15:
            p_title = p_title[:12] + "..."
        insight_parts.append(f"论文：{p_title}")
    if hn_high_value:
        h_title = hn_high_value[0]['title']
        if len(h_title) > 15:
            h_title = h_title[:12] + "..."
        insight_parts.append(f"HN：{h_title}")
    final_summary = " ".join(insight_parts) if insight_parts else "今日有料：关注扩散与LLM进展。"
    # Ensure not too long; aim <50 chars (Chinese counts each char, English words count as is)
    # We'll truncate if necessary
    if len(final_summary) > 50:
        final_summary = final_summary[:47] + "..."
# Print final_summary to stdout (this is the cron output)
print(final_summary)
