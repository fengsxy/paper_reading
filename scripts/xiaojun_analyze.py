#!/usr/bin/env python3
"""Generate an analysis draft for a Xiaojun transcript.

Input: transcripts/xiaojun/<slug>.md
Output: transcripts/xiaojun/<slug>.analysis.md (overwrite unless --no-overwrite)

Uses OpenAI text model (requires OPENAI_API_KEY).
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path


def load_transcript(path: Path, max_chars: int) -> str:
    text = path.read_text(encoding="utf-8")
    # Drop YAML front matter if present
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            text = parts[2]
    text = text.strip()

    if len(text) <= max_chars:
        return text

    head = text[: max_chars // 2]
    tail = text[-max_chars // 2 :]
    return head + "\n\n... [TRUNCATED] ...\n\n" + tail


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("transcript", type=Path)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--model", default="gpt-4o-mini")
    ap.add_argument("--max-chars", type=int, default=120_000)
    ap.add_argument("--no-overwrite", action="store_true")
    args = ap.parse_args()

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("missing env: OPENAI_API_KEY")

    transcript_path: Path = args.transcript
    if not transcript_path.exists():
        raise SystemExit(f"missing transcript: {transcript_path}")

    out = args.out
    if out is None:
        out = transcript_path.with_suffix(".analysis.md")

    if args.no_overwrite and out.exists():
        print(f"[skip exists] {out}")
        return

    transcript_text = load_transcript(transcript_path, args.max_chars)

    from openai import OpenAI

    client = OpenAI(api_key=api_key)

    prompt = f"""You are helping analyze a long-form Chinese interview transcript.

Write a Chinese analysis note in Markdown with these sections:

1) 3-5句摘要
2) 反共识/非显然观点（至少8条）
3) 可学习的点（至少8条，可迁移的方法论/框架/表达）
4) 提问技巧（至少10条，具体到问法/追问策略/结构）
5) 可进一步验证/挖坑（至少8条，可查证的claims/值得追问的问题）

Rules:
- Each bullet MUST cite at least one timestamp from the transcript, using the format (ref: HH:MM:SS) or (ref: MM:SS).
- Prefer actionable, specific points over generic advice.
- Keep it sharp and information-dense; avoid filler.

Transcript:
"""

    resp = client.responses.create(
        model=args.model,
        input=[
            {"role": "user", "content": prompt + transcript_text}
        ],
        temperature=0.2,
    )

    md = resp.output_text
    out.write_text(md.strip() + "\n", encoding="utf-8")
    print(f"wrote: {out}")


if __name__ == "__main__":
    main()
