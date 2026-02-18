#!/usr/bin/env python3
"""
小宇宙播客下载工具
"""

import re
import json
import subprocess
import sys
from pathlib import Path

def get_episode_audio(episode_url):
    """从小宇宙节目页面提取音频 URL"""
    import urllib.request
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
    req = urllib.request.Request(episode_url, headers=headers)
    
    with urllib.request.urlopen(req, timeout=30) as resp:
        html = resp.read().decode('utf-8')
    
    # 提取音频 URL
    audio_match = re.search(r'https://media\.xyzcdn\.net/[^"\']+\.m4a', html)
    if audio_match:
        return audio_match.group(0)
    
    # 尝试从 JSON 数据中提取
    json_match = re.search(r'"enclosure":\s*\{\s*"url":\s*"([^"]+)"', html)
    if json_match:
        return json_match.group(1)
    
    return None

def get_podcast_episodes(podcast_url, limit=10):
    """获取播客的节目列表"""
    import urllib.request
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
    req = urllib.request.Request(podcast_url, headers=headers)
    
    with urllib.request.urlopen(req, timeout=30) as resp:
        html = resp.read().decode('utf-8')
    
    # 提取节目链接
    episodes = re.findall(r'/episode/([a-f0-9]{24})', html)
    episodes = list(dict.fromkeys(episodes))[:limit]  # 去重并限制数量
    
    # 提取标题
    titles = re.findall(r'<div class="[^"]*title[^"]*">([^<]+)</div>', html)
    
    result = []
    for i, ep_id in enumerate(episodes):
        title = titles[i] if i < len(titles) else f"Episode {i+1}"
        result.append({
            "id": ep_id,
            "url": f"https://www.xiaoyuzhoufm.com/episode/{ep_id}",
            "title": title
        })
    
    return result

def download_audio(audio_url, output_path):
    """下载音频文件"""
    import urllib.request
    
    print(f"下载: {audio_url}")
    print(f"保存到: {output_path}")
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(audio_url, headers=headers)
    
    with urllib.request.urlopen(req, timeout=300) as resp:
        with open(output_path, 'wb') as f:
            while True:
                chunk = resp.read(8192)
                if not chunk:
                    break
                f.write(chunk)
    
    print(f"下载完成: {output_path}")
    return output_path

def main():
    if len(sys.argv) < 2:
        print("用法:")
        print("  python xiaoyuzhou.py <episode_url>  # 下载单个节目")
        print("  python xiaoyuzhou.py <podcast_url> --list  # 列出节目")
        sys.exit(1)
    
    url = sys.argv[1]
    
    if "--list" in sys.argv:
        # 列出播客节目
        episodes = get_podcast_episodes(url)
        print(f"找到 {len(episodes)} 个节目:")
        for ep in episodes:
            print(f"  - {ep['title']}")
            print(f"    {ep['url']}")
    else:
        # 下载单个节目
        audio_url = get_episode_audio(url)
        if audio_url:
            print(f"音频 URL: {audio_url}")
            # 生成输出文件名
            ep_id = re.search(r'/episode/([a-f0-9]+)', url)
            if ep_id:
                output = f"/tmp/{ep_id.group(1)}.m4a"
                download_audio(audio_url, output)
        else:
            print("未找到音频 URL")

if __name__ == "__main__":
    main()
