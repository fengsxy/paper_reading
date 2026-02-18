# Idea Backlog

Updated: 2026-02-18

## Active Queue

| ID | Idea | Score | Status | Next step |
|---|---|---:|---|---|
| I-001 | Unified task board in markdown (A/B/C tasks + ETA) for duplex-like status reporting | 22 | planned | create `process/task_board.md` and wire hourly updates |
| I-002 | Auto queue-derived episode target expansion (already deployed) | 24 | done | observe 24h stability |
| I-003 | Podcast index auto-refresh cron (xiaojun/dwarkesh/crossroad) | 21 | planned | add daily cron + commit only on diff |
| I-004 | Transcript formatter: per-paragraph timestamp + `.raw.md` backup pipeline | 23 | planned | implement formatter script and test on 129-132 |
| I-005 | Pages link verifier for new posts (200 check + broken-link report) | 20 | planned | build `scripts/pages_verify.py` and run in cron |

## Done
- Dynamic queue-driven Xiaojun watchdog
- YDC-first search policy + key persistence
- Full podcast index for xiaojun/dwarkesh/crossroad
- Screen-managed long-running transcribe session
