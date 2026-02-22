# Idea Backlog

Updated: 2026-02-22 (Weekly Review)

## Active Queue (Top 5 by value)

| ID | Idea | Score | Status | Next step |
|---|---|---:|---|---|
| I-002 | Auto queue-derived episode target expansion | 24 | done ✅ | Stable; queue-driven watchdog works for Dwarkesh/Xiaojun |
| I-006 | Xiaoyuzhou RSS pipeline (LinkStart 104 eps) | 24 | in_progress | Feed URL confirmed; need to build index + queue + timeline |
| I-004 | Transcript formatter: per-paragraph timestamp + `.raw.md` backup | 23 | partially done | Dwarkesh subtitle→markdown works; Whisper pipeline needs chunking polish |
| I-007 | Bilibili ingestion pipeline with whisper-subtitles reference | 23 | planned | Study `JimLiu/whisper-subtitles`, create minimal adapter |
| I-001 | Unified task board in markdown (A/B/C tasks + ETA) | 22 | partially done | `process/task_board.md` exists but stale; needs auto-update wiring |

## Graduated to Done
- I-002: Queue-driven episode expansion — deployed, stable, powers Dwarkesh/Xiaojun watchdogs
- I-003: Podcast index auto-refresh — indexes built for xiaojun(151)/dwarkesh(185)/crossroad(23); cron not yet wired for diff-only commits
- YouTube auto-captions pipeline (not in original backlog) — massive win, 100x faster than Whisper for English content

## This Week's Review

### What landed
- Dwarkesh pipeline essentially complete (180 transcripts, 153/180 real analyses)
- YouTube subtitle approach was the single biggest unlock — turned days of work into minutes
- Xiaojun grew from 12→69 transcripts via Whisper batch pipeline
- Self-evolution proposal system created (5 proposals logged, none executed yet)
- Cron cleanup: removed 4 low-value jobs, kept 7 focused ones

### What didn't land
- Xiaoyuzhou/Crossroad: zero transcripts produced despite being "in_progress" since Feb 18
- Bilibili pipeline: no progress (still planned)
- Task board auto-update (I-001): file exists but never got wired to hourly updates
- MEMORY.md: proposed (Proposal #2) but never created

### Blockers encountered
- API daily limits ($200-400/day) repeatedly killed batch subagent runs mid-flight
- YouTube cookies expiration + PO Token issues (solved with --js-runtimes node)
- Jekyll build failures from bad YAML front matter (multiple rounds of fixes)
- Disk full (100%) from audio files — cleaned 9.3GB

## Next Week Priority Suggestions (max 3)

1. **Finish Dwarkesh 27 TBD analyses** — lowest effort, highest visible completion. Just 27 files to fill. Can batch via subagents in one session.

2. **Xiaoyuzhou LinkStart pipeline** (I-006) — feed URL is confirmed, 104 episodes ready. Build index → queue → start transcription. This has been "in_progress" for 5 days with zero output.

3. **Create MEMORY.md** (Self-Evolution Proposal #2) — 10+ daily files with 1000+ lines of context but no long-term memory. Every main session starts blind. Quick win, zero risk.
