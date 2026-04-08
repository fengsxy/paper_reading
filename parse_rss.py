#!/usr/bin/env python3
"""Parse Karpathy RSS feed and extract articles from past 24 hours."""
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
import re
import sys

# Read the raw feed content from the fetched data
# The feed was saved to a temp location; we'll reconstruct from the response
feed_content = sys.stdin.read()

# Parse XML
root = ET.fromstring(feed_content)

# Define namespace
ns = {'atom': 'http://www.w3.org/2005/Atom'}

# Current time: 2026-04-05 15:00 UTC (from task context)
now = datetime(2026, 4, 5, 15, 0, 0, tzinfo=timezone.utc)
cutoff = now - timedelta(hours=24)

articles = []

for entry in root.findall('atom:entry', ns):
    title = entry.find('atom:title', ns).text
    link_elem = entry.find('atom:link', ns)
    link = link_elem.get('href') if link_elem is not None else ''
    published_str = entry.find('atom:published', ns).text
    author = entry.find('atom:author/atom:name', ns).text if entry.find('atom:author/atom:name', ns) is not None else ''
    summary_elem = entry.find('atom:summary', ns)
    summary = summary_elem.text if summary_elem is not None else ''
    content_elem = entry.find('atom:content', ns)
    content = content_elem.text if content_elem is not None else ''

    # Parse published date
    published_dt = datetime.fromisoformat(published_str.replace('Z', '+00:00'))

    # Check if within past 24 hours
    if published_dt >= cutoff:
        articles.append({
            'title': title,
            'link': link,
            'published': published_dt,
            'author': author,
            'summary': summary,
            'content': content
        })

# Sort by published date descending
articles.sort(key=lambda x: x['published'], reverse=True)

# Output summary
print(f"Total new articles in past 24h: {len(articles)}\n")
for a in articles:
    print(f"- {a['published'].strftime('%Y-%m-%d %H:%M')} | {a['author']}")
    print(f"  Title: {a['title']}")
    print(f"  Link: {a['link']}")
    print()
