# Task Board (Live)

Updated: 2026-02-18 18:26 UTC

Priority order confirmed by Yu: `Xiaojun -> Dwarkesh -> WhynotTV -> Xiaoyuzhou`

| Task | Owner | Status | ETA | Notes |
|---|---|---|---|---|
| Xiaojun transcription pipeline | screen:xiaojun_transcribe | running | rolling hourly | queue-driven watchdog enabled |
| EP analysis TBD cleanup | watchdog | running | rolling hourly | auto-fix on detection |
| Podcast full indexes | build_podcast_indexes.py | done | n/a | xiaojun/dwarkesh/crossroad built |
| OpenClaw best-practice scan | cron | running hourly | next hour | YDC-only policy |
| Daily new idea delivery | cron | scheduled | daily 09:00 PT | fixed output template |
| WhynotTV #4 transcript completion | manual+watchdog | todo | next 24h | fill transcript body for `I0DrcsDf3Os`, then remove TBD |
| WhynotTV #4 analysis completion | manual+watchdog | todo | after transcript | complete analysis and keep `(ref: [mm:ss])` trace style |
| Xiaoyuzhou LinkStart ingestion (`63ff0da51b1faf8a0b70b337`) | research+pipeline | in_progress | this week | Apple Podcasts feed confirmed: `https://feed.xyzfm.space/q9a6lueucj6a` (104 eps); next: build full index + queue + timeline |
| Bilibili pipeline bootstrap | research+pipeline | todo | next | evaluate `JimLiu/whisper-subtitles` and adapt to repo transcript+analysis workflow; first test target: `https://space.bilibili.com/1140304215?spm_id_from=333.337.0.0` |
