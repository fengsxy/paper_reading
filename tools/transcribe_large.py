#!/usr/bin/env python3
"""
大文件音频转录 - 自动分段处理
"""

import os
import sys
import subprocess
import tempfile
from pathlib import Path

def split_audio(input_path, segment_minutes=20, output_dir=None):
    """将音频分割成多个片段"""
    if output_dir is None:
        output_dir = tempfile.mkdtemp()
    
    output_pattern = os.path.join(output_dir, "segment_%03d.mp3")
    
    cmd = [
        "ffmpeg", "-i", input_path,
        "-f", "segment",
        "-segment_time", str(segment_minutes * 60),
        "-c:a", "libmp3lame", "-q:a", "4",
        output_pattern,
        "-y"
    ]
    
    subprocess.run(cmd, capture_output=True)
    
    segments = sorted(Path(output_dir).glob("segment_*.mp3"))
    return [str(s) for s in segments]

def transcribe_segment(audio_path, language=None):
    """转录单个片段"""
    from groq import Groq
    
    api_key = os.environ.get("GROQ_API_KEY")
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
    }

def transcribe_large_file(input_path, language=None, output_path=None):
    """转录大文件"""
    print(f"处理: {input_path}")
    
    # 检查文件大小
    file_size = os.path.getsize(input_path) / (1024 * 1024)  # MB
    print(f"文件大小: {file_size:.1f} MB")
    
    if file_size > 20:
        print("文件较大，分段处理...")
        segments = split_audio(input_path)
        print(f"分割成 {len(segments)} 个片段")
    else:
        segments = [input_path]
    
    all_text = []
    all_segments = []
    time_offset = 0
    
    for i, seg_path in enumerate(segments):
        print(f"转录片段 {i+1}/{len(segments)}...")
        try:
            result = transcribe_segment(seg_path, language)
            all_text.append(result["text"])
            
            # 调整时间戳
            for seg in result.get("segments", []):
                seg["start"] = seg.get("start", 0) + time_offset
                seg["end"] = seg.get("end", 0) + time_offset
                all_segments.append(seg)
            
            # 更新时间偏移（假设每段 20 分钟）
            time_offset += 20 * 60
            
        except Exception as e:
            print(f"片段 {i+1} 转录失败: {e}")
            continue
    
    full_text = "\n".join(all_text)
    
    # 生成 markdown 输出
    output = f"# 转录结果\n\n{full_text}\n"
    
    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"已保存: {output_path}")
    else:
        print("\n" + "="*50)
        print(full_text[:2000] + "..." if len(full_text) > 2000 else full_text)
    
    return full_text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python transcribe_large.py <audio_file> [-o output.md] [-l zh]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = None
    language = "zh"
    
    if "-o" in sys.argv:
        idx = sys.argv.index("-o")
        output_file = sys.argv[idx + 1]
    
    if "-l" in sys.argv:
        idx = sys.argv.index("-l")
        language = sys.argv[idx + 1]
    
    transcribe_large_file(input_file, language, output_file)
