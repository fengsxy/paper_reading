#!/usr/bin/env python3
"""
音频/视频转文字工具 (OpenAI Whisper)
支持: MP3, WAV, M4A, MP4, YouTube URL

使用方法:
  export OPENAI_API_KEY=your_key
  python transcribe.py audio.mp3 -l zh -f markdown -o output.md

参考: https://developers.openai.com/api/docs/guides/speech-to-text
"""

import argparse
import os
import sys
import json
import subprocess
from pathlib import Path


def download_youtube(url, output_path="/tmp/yt_audio.mp3", cookies_path=None):
    """下载 YouTube 音频"""
    try:
        cmd = ["yt-dlp", "-x", "--audio-format", "mp3", "-o", output_path]
        if cookies_path and os.path.exists(cookies_path):
            cmd.extend(["--cookies", cookies_path])
        cmd.append(url)
        subprocess.run(cmd, check=True)
        return output_path
    except FileNotFoundError:
        print("需要安装 yt-dlp: pip install yt-dlp")
        sys.exit(1)


def transcribe(audio_path, language=None):
    """使用 OpenAI Whisper API 转录"""
    from openai import OpenAI
    
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("需要设置 OPENAI_API_KEY")
        sys.exit(1)
    
    client = OpenAI(api_key=api_key)
    
    with open(audio_path, "rb") as f:
        response = client.audio.transcriptions.create(
            model="whisper-1",
            file=f,
            language=language,
            response_format="verbose_json",
            timestamp_granularities=["segment"]
        )
    
    return response


def format_time(seconds):
    """格式化时间戳"""
    m = int(seconds // 60)
    s = int(seconds % 60)
    return f"{m:02d}:{s:02d}"


def format_output(response, fmt="text"):
    """格式化输出"""
    if fmt == "text":
        return response.text
    
    elif fmt == "json":
        data = {
            "text": response.text,
            "language": response.language,
            "duration": response.duration,
            "segments": [
                {"start": s.start, "end": s.end, "text": s.text}
                for s in (response.segments or [])
            ]
        }
        return json.dumps(data, ensure_ascii=False, indent=2)
    
    elif fmt == "markdown":
        lines = [
            f"# Transcript\n",
            f"**Language:** {response.language}",
            f"**Duration:** {format_time(response.duration)}\n",
            "---\n"
        ]
        
        if response.segments:
            for seg in response.segments:
                start = format_time(seg.start)
                lines.append(f"**[{start}]** {seg.text.strip()}\n")
        else:
            lines.append(response.text)
        
        return "\n".join(lines)
    
    return response.text


def main():
    parser = argparse.ArgumentParser(
        description="音频/视频转文字 (OpenAI Whisper)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python transcribe.py audio.mp3
  python transcribe.py audio.mp3 -l zh -f markdown -o transcript.md
  python transcribe.py "https://youtube.com/watch?v=xxx" -l zh
        """
    )
    parser.add_argument("input", help="音频文件路径或 YouTube URL")
    parser.add_argument("-l", "--language", help="语言代码 (zh, en, ja, etc.)")
    parser.add_argument("-f", "--format", choices=["text", "json", "markdown"], 
                        default="text", help="输出格式")
    parser.add_argument("-o", "--output", help="输出文件路径")
    parser.add_argument("--cookies", default="~/.openclaw/secrets/youtube_cookies.txt",
                        help="YouTube cookies 文件路径")
    
    args = parser.parse_args()
    
    input_path = args.input
    
    # 处理 YouTube URL
    if "youtube.com" in input_path or "youtu.be" in input_path:
        cookies_path = os.path.expanduser(args.cookies)
        print(f"下载 YouTube 音频...")
        input_path = download_youtube(input_path, cookies_path=cookies_path)
    
    if not os.path.exists(input_path):
        print(f"文件不存在: {input_path}")
        sys.exit(1)
    
    print(f"转录中... ({os.path.basename(input_path)})")
    response = transcribe(input_path, args.language)
    
    output = format_output(response, args.format)
    
    if args.output:
        os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"已保存: {args.output}")
    else:
        print("\n" + "=" * 50)
        print(output)


if __name__ == "__main__":
    main()
