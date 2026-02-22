#!/usr/bin/env python3
"""
Auto-update the "最近更新" section in README.md based on recent git commits.
Scans commits from the last 7 days and extracts notable changes per directory.
Run via pre-commit hook or manually.
"""

import subprocess
import re
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict

REPO_ROOT = Path(__file__).resolve().parent.parent
README = REPO_ROOT / "README.md"

# Directories to track and their display names / link prefixes
TRACKED = {
    "scholar_inbox": ("Scholar Inbox", "scholar_inbox"),
    "hackernews": ("Hacker News", "hackernews"),
    "karpathy_rss": ("Karpathy RSS", "karpathy_rss"),
    "transcripts/dwarkesh": ("Dwarkesh", "transcripts/dwarkesh"),
    "transcripts/xiaojun": ("张小珺访谈", "transcripts/xiaojun"),
    "transcripts/whynot": ("WhynotTV", "transcripts/whynot"),
    "essays": ("Essays", "essays"),
}

MAX_ROWS = 12  # max entries in the table


def get_recent_files(days=7):
    """Get files changed in the last N days via git log."""
    since = (datetime.now(tz=None) - timedelta(days=days)).strftime("%Y-%m-%d")
    result = subprocess.run(
        ["git", "log", f"--since={since}", "--name-only", "--pretty=format:%H %aI", "--diff-filter=ACM"],
        capture_output=True, text=True, cwd=REPO_ROOT
    )
    entries = []  # (date_str, filepath)
    current_date = None
    for line in result.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        # commit line: hash ISO-date
        if re.match(r'^[0-9a-f]{40} ', line):
            iso_date = line.split()[1][:10]
            current_date = iso_date
        elif current_date and not line.startswith("Merge"):
            entries.append((current_date, line))
    return entries


def extract_title_from_md(filepath):
    """Try to extract a meaningful title from a markdown file's front matter or first heading."""
    full = REPO_ROOT / filepath
    if not full.exists() or not full.suffix == ".md":
        return None
    try:
        text = full.read_text(errors="ignore")[:2000]
    except Exception:
        return None
    # YAML front matter title
    m = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', text, re.MULTILINE)
    if m:
        title = m.group(1).strip()
        if len(title) > 60:
            title = title[:57] + "..."
        return title
    # First markdown heading
    m = re.search(r'^#\s+(.+)', text, re.MULTILINE)
    if m:
        title = m.group(1).strip()
        if len(title) > 60:
            title = title[:57] + "..."
        return title
    return None


def build_updates(entries):
    """Group entries by date+category, pick the most interesting per group."""
    # date -> category -> list of (filepath, title)
    grouped = defaultdict(lambda: defaultdict(list))
    for date_str, filepath in entries:
        for prefix, (label, _link) in TRACKED.items():
            if filepath.startswith(prefix) and filepath.endswith(".md"):
                title = extract_title_from_md(filepath)
                grouped[date_str][label].append((filepath, title))
                break

    rows = []
    for date_str in sorted(grouped.keys(), reverse=True):
        for category in grouped[date_str]:
            items = grouped[date_str][category]
            # Pick first item with a title, or just the first
            best = next(((f, t) for f, t in items if t), items[0])
            filepath, title = best
            count = len(items)
            desc = f"[{category}]({filepath})"
            if title:
                desc += f": {title}"
            if count > 1:
                desc += f" (+{count - 1} more)"
            rows.append((date_str, desc))

    return rows[:MAX_ROWS]


def update_readme(rows):
    """Replace the 最近更新 table in README.md."""
    content = README.read_text()

    # Build new table
    table_lines = ["| 日期 | 更新内容 |", "|------|----------|"]
    for date_str, desc in rows:
        table_lines.append(f"| {date_str} | {desc} |")
    new_table = "\n".join(table_lines)

    # Find and replace the section between "## 🆕 最近更新" and the next "##" or "---"
    pattern = r'(## 🆕 最近更新\s*\n)\|[^\n]*\n\|[-| ]+\n(?:\|[^\n]*\n)*'
    replacement = f"\\1{new_table}\n"
    new_content = re.sub(pattern, replacement, content)

    if new_content != content:
        README.write_text(new_content)
        # Stage the updated README
        subprocess.run(["git", "add", "README.md"], cwd=REPO_ROOT)
        return True
    return False


def main():
    entries = get_recent_files(days=7)
    rows = build_updates(entries)
    if not rows:
        print("No recent updates found, skipping README update.")
        return
    changed = update_readme(rows)
    if changed:
        print(f"README.md updated with {len(rows)} recent entries.")
    else:
        print("README.md already up to date.")


if __name__ == "__main__":
    main()
