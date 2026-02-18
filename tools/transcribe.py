#!/usr/bin/env python3
"""
音频/视频转文字工具
支持: MP3, WAV, M4A, MP4, YouTube URL

使用方法:
1. Groq API (推荐，免费):
   export GROQ_API_KEY=your_key
   python transcribe.py audio.mp3

2. OpenAI Whisper API:
   export OPENAI_API_KEY=your_key
   python transcribe.py audio.mp3 --provider openai

获取 Groq API Key: https://console.groq.com/keys (免费)
"""

import argparse
import os
import sys
import json
import subprocess
from pathlib import Path


def download_youtube(url, output_path="/tmp/yt_audio.mp3"):
    try:
        cmd = ["yt-dlp", "-x", "--audio-format", "mp3", "-o", output_path, url]
        subprocess.run(cmd, check=True)
        return output_path
    except FileNotFoundError:
        print("需要安装 yt-dlp: pip install yt-dlp")
        sys.exit(1)


def transcribe_groq(audio_path, language=None):
    from groq import Groq
    
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("需要设置 GROQ_API_KEY\n获取: https://console.groq.com/keys")
        sys.exit(1)
    
    client = Groq(api_key=api_key)
    
    with open(audio_path, "rb") as f:
        transcription = client.audio.transcriptions.create(
            file=(Path(audio_path).name, f.read()),
            model="whisper-large-v3",
            language=language,
            response_format="verbose_json",
        )
    
    return {
        "text": transcription.text,
        "segments": getattr(transcription, 'segments', []),
        "language": getattr(transcription, 'language', language),
    }


def transcribe_openai(audio_path, language=None):
    from openai import OpenAI
    
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("需要设置 OPENAI_API_KEY")
        sys.exit(1)
    
    client = OpenAI(api_key=api_key)
    
    with open(audio_path, "rb") as f:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=f,
            language=language,
            response_format="verbose_json",
        )
    
    return {
        "text": transcription.text,
        "segments": transcription.segments,
        "language": transcription.language,
    }


def format_time(seconds):
    m = int(seconds // 60)
    s = int(seconds % 60)
    return f"{m:02d}:{s:02d}"


def format_transcript(result, fmt="text"):
    # Handle both dict and Pydantic objects
    if hasattr(result, 'model_dump'):
        result = result.model_dump()
    elif hasattr(result, 'text') and not isinstance(result, dict):
        # Pydantic object without model_dump
        result = {"text": result.text, "segments": getattr(result, 'segments', []), "language": getattr(result, 'language', 'unknown')}
    
    if fmt == "text":
        return result.get("text", str(result)) if isinstance(result, dict) else result
    elif fmt == "json":
        return json.dumps(result, ensure_ascii=False, indent=2, default=str)
    elif fmt == "markdown":
        text = result.get("text", "") if isinstance(result, dict) else str(result)
        lang = result.get("language", "unknown") if isinstance(result, dict) else "unknown"
        segments = result.get("segments", []) if isinstance(result, dict) else []
        
        lines = [f"# Transcript\n\n**Language:** {lang}\n"]
        if segments:
            for seg in segments:
                if hasattr(seg, 'start'):
                    start = format_time(seg.start)
                    seg_text = seg.text.strip() if hasattr(seg, 'text') else str(seg)
                elif isinstance(seg, dict):
                    start = format_time(seg.get("start", 0))
                    seg_text = seg.get("text", "").strip()
                else:
                    continue
                lines.append(f"**[{start}]** {seg_text}\n")
        else:
            lines.append(text)
        return "\n".join(lines)
    return result.get("text", str(result)) if isinstance(result, dict) else str(result)


def main():
    parser = argparse.ArgumentParser(description="音频/视频转文字")
    parser.add_argument("input", help="音频文件路径或 YouTube URL")
    parser.add_argument("--provider", choices=["groq", "openai"], default="groq")
    parser.add_argument("--language", "-l", help="语言代码 (zh, en, ja)")
    parser.add_argument("--format", "-f", choices=["text", "json", "markdown"], default="text")
    parser.add_argument("--output", "-o", help="输出文件路径")
    
    args = parser.parse_args()
    
    input_path = args.input
    if "youtube.com" in input_path or "youtu.be" in input_path:
        print(f"下载 YouTube: {input_path}")
        input_path = download_youtube(input_path)
    
    if not os.path.exists(input_path):
        print(f"文件不存在: {input_path}")
        sys.exit(1)
    
    print(f"使用 {args.provider} 转录...")
    if args.provider == "groq":
        result = transcribe_groq(input_path, args.language)
    else:
        result = transcribe_openai(input_path, args.language)
    
    output = format_transcript(result, args.format)
    
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"已保存: {args.output}")
    else:
        print("\n" + "="*50)
        print(output)


if __name__ == "__main__":
    main()
