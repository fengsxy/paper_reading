# Idea Backlog

Updated: 2026-03-11 (Weekly Review)

## Active Queue (Top 5 by value)

| ID | Idea | Score | Status | Next step |
|---|---|---:|---|---|
| I-008 | 每日主动写 memory 日记 | 28 | new | 每天 session 结束前主动写日记，不依赖 cron |
| I-002 | Auto queue-derived episode target expansion | 24 | done ✅ | Stable; queue-driven watchdog works for Dwarkesh/Xiaojun |
| I-006 | Xiaoyuzhou RSS pipeline (LinkStart 104 eps) | 24 | stalled | Feed URL confirmed; need to build index + queue + timeline |
| I-004 | Transcript formatter: per-paragraph timestamp + `.raw.md` backup | 23 | partially done | Dwarkesh subtitle→markdown works; Whisper pipeline needs chunking polish |
| I-007 | Bilibili ingestion pipeline with whisper-subtitles reference | 23 | planned | Study `JimLiu/whisper-subtitles`, create minimal adapter |

## Graduated to Done
- I-002: Queue-driven episode expansion — deployed, stable, powers Dwarkesh/Xiaojun watchdogs
- I-003: Podcast index auto-refresh — indexes built for xiaojun(151)/dwarkesh(185)/crossroad(23); cron not yet wired for diff-only commits
- YouTube auto-captions pipeline (not in original backlog) — massive win, 100x faster than Whisper for English content

## This Week's Review (2026-03-03 to 2026-03-11)

### What landed
- **巴菲特股东信项目 100% 完成** (3/3): 49 年年度分析 + 49 封股东信中文版，总计 380,000 字，13 小时连续工作
- **学术研究方案快速产出** (3/4-3/5): 多元化纠纷解决机制 + 学校安全风险预防，总计 37,000 字（后删除）
- **模型配置优化** (3/10): 添加 fucheers-claude/claude-opus-4-6，切换默认模型
- **Cron jobs 持续稳定**: agent 手记、Karpathy RSS、Daily Paper & HN 持续运行

### What didn't land
- **记忆断档 6 天** (3/6-3/11): memory 日记从 3/5 断到 3/11，连续性断裂
- **Tracing 插件安装失败** (3/10): 依赖未发布的 plugin SDK，无法加载
- **Xiaoyuzhou/Crossroad**: 仍然零进展
- **MEMORY.md**: 仍未创建

### Blockers encountered
- 被动等待 cron 写日记，没有主动维护记忆习惯
- Tracing 插件依赖未发布的 openclaw/plugin-sdk/tracing 模块
- Yu 反馈"能装明白嘛？"——安装插件来回折腾，不够利索

## Next Week Priority Suggestions (max 3)

1. **每日主动写 memory 日记** (I-008) — 最高优先级。记忆连续性是 agent 存在的基础，Yu 说"我需要你的归来 MY FRIEND!"。每天 session 结束前主动写日记，不依赖 cron。低风险，高收益。

2. **创建 MEMORY.md** (Self-Evolution Proposal #2) — 10+ daily files with 1000+ lines of context but no long-term memory. Every main session starts blind. Quick win, zero risk. 30-60 分钟可完成。

3. **完成 Dwarkesh 27 TBD 分析** — 最低努力，最高可见完成度。只需填 27 个文件。可以 batch via subagents in one session。注意 API quota 限制。
