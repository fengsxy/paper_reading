#!/usr/bin/env bash
set -euo pipefail

QUEUE_FILE="${1:-scripts/xiaojun_queue.jsonl}"
OUT_DIR="${2:-data/audio/xiaojun}"
COOKIES_FILE="${COOKIES_FILE:-$HOME/.openclaw/secrets/youtube_cookies.txt}"

mkdir -p "$OUT_DIR"

if ! command -v yt-dlp >/dev/null 2>&1; then
  echo "yt-dlp not found. Install: pip install yt-dlp" >&2
  exit 1
fi

while IFS= read -r line; do
  [ -z "$line" ] && continue
  EP=$(python3 -c 'import json,sys; print(json.loads(sys.stdin.read()).get("episode"))' <<<"$line")
  SLUG=$(python3 -c 'import json,sys; print(json.loads(sys.stdin.read()).get("slug"))' <<<"$line")
  URL=$(python3 -c 'import json,sys; print(json.loads(sys.stdin.read()).get("url"))' <<<"$line")

  OUT="$OUT_DIR/${SLUG}.%(ext)s"
  echo "[download] EP${EP} $URL"
  yt-dlp -f bestaudio --cookies "$COOKIES_FILE" -o "$OUT" "$URL"

done < "$QUEUE_FILE"

echo "done: $OUT_DIR"
