#!/usr/bin/env python3
import subprocess
import json
from datetime import datetime, timedelta

papers = []
start = datetime(2026, 2, 1)
end = datetime(2026, 2, 15)

current = start
while current <= end:
    date_str = current.strftime("%m-%d-%Y")
    print(f"Fetching {date_str}...", flush=True)
    try:
        result = subprocess.run(
            ["/home/ubuntu/.local/bin/scholarinboxcli", "digest", "--date", date_str, "--json"],
            capture_output=True, text=True, timeout=60
        )
        if result.returncode == 0:
            data = json.loads(result.stdout)
            day_papers = data.get("digest_df", [])
            for p in day_papers:
                papers.append({
                    "date": current.strftime("%Y-%m-%d"),
                    "title": p.get("title"),
                    "arxiv_id": p.get("arxiv_id"),
                    "authors": p.get("shortened_authors"),
                    "abstract": p.get("abstract"),
                    "category": p.get("category"),
                    "ranking_score": p.get("ranking_score"),
                    "url": p.get("url"),
                    "github_url": p.get("github_url"),
                    "project_link": p.get("project_link"),
                    "keywords": p.get("keywords_metadata", {}).get("keywords"),
                    "method": p.get("keywords_metadata", {}).get("method_shortname"),
                    "subfield": p.get("keywords_metadata", {}).get("sub_subfield"),
                })
            print(f"  -> {len(day_papers)} papers")
    except Exception as e:
        print(f"  -> Error: {e}")
    current += timedelta(days=1)

# Save
with open("/home/ubuntu/.openclaw/workspace/scholar_inbox_feb2026.json", "w") as f:
    json.dump(papers, f, indent=2, ensure_ascii=False)

print(f"\nTotal: {len(papers)} papers saved")
