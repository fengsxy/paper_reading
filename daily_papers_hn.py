#!/usr/bin/env python3
"""
每日论文+HN更新任务
搜索AI/ML论文并抓取Hacker News，筛选高质量内容
"""

import os
import sys
import json
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

# 添加workspace到路径
workspace = Path("/home/ubuntu/.openclaw/workspace")
sys.path.insert(0, str(workspace))

# 环境变量
os.chdir(workspace)
ydc_key = Path("/home/ubuntu/.openclaw/secrets/ydc_api_key").read_text().strip()
os.environ["YDC_API_KEY"] = ydc_key

# 输出路径
date_str = datetime.utcnow().strftime("%Y-%m-%d")
papers_file = workspace / "scholar_inbox" / f"{date_str}-daily-papers.md"
hn_file = workspace / "hackernews" / f"{date_str}.md"

def search_papers():
    """用YDC API搜索最近AI/ML论文"""
    import urllib.request
    import urllib.parse
    
    # 搜索查询：关注扩散模型、LLM、信息论、表示学习
    queries = [
        "diffusion models representation learning",
        "large language models information theory",
        "representation learning deep learning",
        "diffusion probabilistic models"
    ]
    
    papers = []
    seen_titles = set()
    
    for query in queries:
        url = f"https://ydc-index.io/v1/search?{urllib.parse.urlencode({
            'query': query,
            'count': 10,
            'language': 'EN'
        })}"
        
        req = urllib.request.Request(
            url,
            headers={
                "Accept": "application/json",
                "X-API-KEY": ydc_key
            }
        )
        
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode())
                
                # YDC API 返回结构: {"results": {"scholar": [...], "web": [...]}}
                # scholar 通常为空，改用 web 结果筛选
                web_results = data.get("results", {}).get("web", [])
                
                for item in web_results:
                    title = item.get("title", "").strip()
                    if not title or title in seen_titles:
                        continue
                    seen_titles.add(title)
                    
                    # web结果只有url字段，检查是否是PDF或学术站点
                    url = item.get("url", "")
                    is_paper = any(domain in url.lower() for domain in [
                        "arxiv.org", "pdf", "acm.org", "ieee.org", 
                        "openreview.net", "papers.nips.cc", "neurips.cc"
                    ])
                    if not is_paper:
                        continue
                    
                    papers.append({
                        "title": title,
                        "authors": "",  # web结果无作者信息
                        "venue": "",
                        "year": "",
                        "pdf": url,
                        "abstract": item.get("description", "")[:200]
                    })
        except Exception as e:
            print(f"搜索查询失败 '{query}': {e}", file=sys.stderr)
    
    # 去重并限制数量
    unique_papers = []
    for p in papers:
        if not any(p["title"].lower() == up["title"].lower() for up in unique_papers):
            unique_papers.append(p)
    
    return unique_papers[:8]  # 最多8篇

def fetch_hn():
    """抓取Hacker News首页并筛选AI/ML内容"""
    import urllib.request
    import re
    
    hn_items = []
    
    try:
        # 使用HN官方API获取最新30条
        url = "https://hacker-news.firebaseio.com/v0/topstories.json"
        with urllib.request.urlopen(url, timeout=10) as resp:
            story_ids = json.loads(resp.read().decode())[:30]
        
        # 并发获取stories
        import threading
        results = []
        lock = threading.Lock()
        
        def fetch_story(story_id):
            try:
                story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
                with urllib.request.urlopen(story_url, timeout=8) as resp:
                    story = json.loads(resp.read().decode())
                    if story and story.get("type") == "story":
                        title = story.get("title", "").lower()
                        url = story.get("url", "")
                        # 筛选AI/ML相关
                        ai_keywords = ["ai", "machine learning", "deep learning", "llm", "gpt", "diffusion", "neural", "transformer", "gpu", "training", "inference", "openai", "anthropic", "meta ai", "google ai", "research", "paper", "model"]
                        if any(kw in title for kw in ai_keywords):
                            with lock:
                                results.append({
                                    "title": story.get("title", ""),
                                    "url": url or f"https://news.ycombinator.com/item?id={story_id}",
                                    "score": story.get("score", 0),
                                    "comments": story.get("descendants", 0)
                                })
            except:
                pass
        
        threads = []
        for sid in story_ids:
            t = threading.Thread(target=fetch_story, args=(sid,))
            t.start()
            threads.append(t)
            if len(threads) >= 10:
                for t in threads:
                    t.join(timeout=5)
                threads = []
        
        for t in threads:
            t.join(timeout=5)
        
        hn_items = sorted(results, key=lambda x: x["score"], reverse=True)[:15]
        
    except Exception as e:
        print(f"抓取HN失败: {e}", file=sys.stderr)
    
    return hn_items

def write_files(papers, hn_items):
    """写入结果到文件"""
    # 写入论文
    with open(papers_file, "w", encoding="utf-8") as f:
        f.write(f"# 每日论文 - {date_str}\n\n")
        if papers:
            f.write(f"找到 {len(papers)} 篇高质量论文：\n\n")
            for i, p in enumerate(papers, 1):
                f.write(f"## {i}. {p['title']}\n\n")
                f.write(f"- **作者**: {p['authors']}\n")
                f.write(f"- **会议/期刊**: {p['venue']} {p['year']}\n")
                f.write(f"- **PDF**: {p['pdf']}\n")
                if p.get('abstract'):
                    f.write(f"- **摘要**: {p['abstract']}...\n")
                f.write("\n")
        else:
            f.write("今日未找到符合条件的论文。\n\n")
    
    # 写入HN
    with open(hn_file, "w", encoding="utf-8") as f:
        f.write(f"# Hacker News AI/ML讨论 - {date_str}\n\n")
        if hn_items:
            f.write(f"找到 {len(hn_items)} 条相关讨论：\n\n")
            for i, item in enumerate(hn_items, 1):
                f.write(f"## {i}. {item['title']}\n\n")
                f.write(f"- **链接**: {item['url']}\n")
                f.write(f"- **分数**: {item['score']} | **评论数**: {item['comments']}\n\n")
        else:
            f.write("今日HN未找到AI/ML相关内容。\n\n")

def generate_summary(papers, hn_items):
    """生成极简摘要（不超过200字）"""
    if len(papers) < 3 or len(hn_items) < 3:
        return None
    
    summary = []
    
    # 提取论文亮点
    if papers:
        paper_titles = [p['title'].split(':')[0].strip() for p in papers[:2]]
        summary.append(f"论文亮点：{'；'.join(paper_titles)}")
    
    # 提取HN热点
    if hn_items:
        hn_titles = [item['title'][:50] + ('...' if len(item['title']) > 50 else '') for item in hn_items[:2]]
        summary.append(f"HN热点：{'；'.join(hn_titles)}")
    
    full_summary = " | ".join(summary)
    return full_summary[:200]  # 硬限制200字

def main():
    print("开始执行每日论文+HN更新...")
    
    # 1. 搜索论文
    print("搜索AI/ML论文...")
    papers = search_papers()
    print(f"找到 {len(papers)} 篇论文")
    
    # 2. 抓取HN
    print("抓取Hacker News...")
    hn_items = fetch_hn()
    print(f"找到 {len(hn_items)} 条HN讨论")
    
    # 3. 写入文件
    print("写入文件...")
    write_files(papers, hn_items)
    
    # 4. Git提交
    print("Git提交...")
    subprocess.run(["git", "add", "scholar_inbox", "hackernews"], check=False)
    commit_msg = f"chore: daily papers+hn {date_str}"
    subprocess.run(["git", "commit", "-m", commit_msg], check=False)
    subprocess.run(["git", "push"], check=False)
    
    # 5. 生成摘要（如果需要）
    summary = generate_summary(papers, hn_items)
    if summary:
        print(f"[\"摘要\"]: {summary}")
        print(f"SUMMARY: {summary}")
        return summary
    else:
        print("今日新内容不足，已归档。")
        return "今日新内容不足，已归档。"

if __name__ == "__main__":
    try:
        result = main()
        # 极简总结（<50字）
        if result and result != "今日新内容不足，已归档。":
            brief = result.split("|")[0].strip()[:45] + ("..." if len(result) > 45 else "")
            print(brief)
        else:
            print("内容不足，已归档。")
    except Exception as e:
        print(f"任务执行失败: {e}", file=sys.stderr)
        sys.exit(1)
