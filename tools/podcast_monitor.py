#!/usr/bin/env python3
"""
播客监控工具 - 检查指定频道/关键词的新视频
"""

import json
import os
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

# 监控的搜索关键词（模拟频道监控）
MONITOR_SEARCHES = [
    "张小珺 访谈",
    "WhynotTV podcast",
    "罗永浩 十字路口",
]

# 已处理视频的记录文件
PROCESSED_FILE = Path("/home/ubuntu/.openclaw/workspace/tools/processed_videos.json")

def load_processed():
    if PROCESSED_FILE.exists():
        return json.loads(PROCESSED_FILE.read_text())
    return {"videos": [], "last_check": None}

def save_processed(data):
    data["last_check"] = datetime.now().isoformat()
    PROCESSED_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2))

def search_videos(query, limit=5):
    """搜索 YouTube 视频"""
    cmd = [
        "yt-dlp", f"ytsearch{limit}:{query}",
        "--flat-playlist",
        "--print", "%(id)s|%(title)s|%(duration_string)s|%(upload_date)s"
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        videos = []
        for line in result.stdout.strip().split("\n"):
            if "|" in line:
                parts = line.split("|")
                if len(parts) >= 4:
                    videos.append({
                        "id": parts[0],
                        "title": parts[1],
                        "duration": parts[2],
                        "upload_date": parts[3]
                    })
        return videos
    except Exception as e:
        print(f"搜索失败: {e}")
        return []

def check_new_videos():
    """检查所有监控源的新视频"""
    processed = load_processed()
    processed_ids = set(processed["videos"])
    new_videos = []
    
    for query in MONITOR_SEARCHES:
        print(f"检查: {query}")
        videos = search_videos(query)
        for v in videos:
            if v["id"] not in processed_ids:
                # 检查是否是最近 7 天内上传的
                if v["upload_date"]:
                    try:
                        upload = datetime.strptime(v["upload_date"], "%Y%m%d")
                        if datetime.now() - upload < timedelta(days=7):
                            new_videos.append({**v, "source": query})
                    except:
                        pass
    
    return new_videos

def mark_processed(video_ids):
    """标记视频为已处理"""
    processed = load_processed()
    processed["videos"].extend(video_ids)
    processed["videos"] = list(set(processed["videos"]))[-500:]  # 保留最近 500 个
    save_processed(processed)

def main():
    print("=== 播客监控 ===")
    print(f"时间: {datetime.now().isoformat()}")
    
    new_videos = check_new_videos()
    
    if new_videos:
        print(f"\n发现 {len(new_videos)} 个新视频:")
        for v in new_videos:
            print(f"  - [{v['source']}] {v['title']} ({v['duration']})")
            print(f"    https://youtube.com/watch?v={v['id']}")
        
        # 输出 JSON 供后续处理
        print("\n--- NEW_VIDEOS_JSON ---")
        print(json.dumps(new_videos, ensure_ascii=False))
    else:
        print("\n没有新视频")
    
    return new_videos

if __name__ == "__main__":
    main()
