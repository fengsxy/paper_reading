# Idea Backlog

Updated: 2026-03-22 (Weekly Review)

## Active Queue (Top 5 by value)

| ID | Idea | Score | Status | Next step |
|---|---|---:|---|---|
| I-010 | 主动思考 + Agent Evaluation 研究 | 30 | active | Yu 3/21 明确要求主动花 token 思考。已完成 agent eval 初稿 + 实验 + router 调研。下一步：深化"过程质量评测"方向，与 Yu 信息论兴趣结合 |
| I-009 | MEMORY.md 定期维护 | 26 | ✅ done this cycle | 本次 review 已更新至 3/22，包含 Amazon offer、主动思考指令、agent eval 研究、yunyi 过期预警 |
| I-008 | 每日主动写 memory 日记 | 25 | ⚠️ improved | 本周 6/7 天有日记（3/16-3/18, 3/20-3/22），仅 3/19 缺失。显著恢复，但还不是 7/7 |
| I-004 | Transcript formatter: per-paragraph timestamp + `.raw.md` backup | 23 | stalled | 无新进展，但不阻塞任何工作 |
| I-011 | OpenClaw 升级到 v2026.3.13 | 22 | planned | 3/21 发现新版本可用，修复 compaction token count + Telegram SSRF + thinking blocks replay。需找合适时机升级 |

## Graduated to Done
- I-002: Queue-driven episode expansion — deployed, stable
- I-003: Podcast index auto-refresh — indexes built, cron 运行中
- YouTube auto-captions pipeline — stable
- 系统故障根因分析 + 修复 (3/12)
- Tracing 插件 (3/12)
- Provider 配置清理 (3/12)
- 巴菲特验证 (3/12)
- VAE Essay 发布 (3/12)
- **CS 202 考试** (3/20): 考完了 ✅
- **dLLM 研究调研** (3/15-3/17): 22篇论文精读，7份报告，全部推送博客 ✅
- **Linear Attention & Qwen3.5 Blog** (3/16): 完整发布 ✅
- **CS 202 Paper Reviews** (3/16-3/19): 至少 5/8 篇完成 ✅

## Retired / Deprioritized
- I-006 (Xiaoyuzhou RSS pipeline): 连续 5 周零进展，退出 active queue。等 Yu 主动提起再激活
- I-007 (Bilibili ingestion pipeline): 同上，退出 active queue

## This Week's Review (2026-03-16 to 2026-03-22)

### What landed ✅
- **dLLM 研究深挖** (3/16-3/17): 蒸馏方法分类、DSL vs Uniform 对比、Sahoo 工作线分析、Yu 的研究方向（GDN for dLLM）进一步明确
- **CS 202 Paper Reviews** (3/16): 5/8 完成（Barrelfish, OCC, MCS Lock, SPIN, SFI），3篇待写（Scheduler Activations, vLLM, LFS）
- **Linear Attention Blog 发布** (3/16): 7 section 完整文章推送博客
- **CS 202 考试完成** (3/20): 3-6pm PT，考试结束
- **Amazon NYC Offer** (3/18): 拿到 Amazon 纽约暑期实习 offer（6/25-9/25）🎉
- **主动思考模式开启** (3/21): Yu 下达新指令，要求主动花 token 思考而非被动响应
- **Agent Evaluation 研究** (3/21-3/22): 完成基准调研（5个benchmark）+ 实验（3个sub-agent任务）+ router调研 + 找到 IBM/Hebrew U/Yale 120篇综述 → 锁定"过程质量评测"蓝海
- **Memory 日记恢复** (3/16-3/22): 本周 6/7 天有日记，比上周（断档3天）显著改善
- **Agent 手记持续** (3/17, 3/19, 3/22): 3 篇手记推送，day 31/33/36
- **自动化管线零故障** (3/16-3/22): daily papers, HN, Karpathy RSS 每天自动 commit
- **MEMORY.md 更新** (3/22): 已更新至最新，包含 Amazon offer、主动思考指令、agent eval 研究等

### What didn't land ❌
- **3/19 日记缺失**: 仅差一天，但离 7/7 还差一步
- **OpenClaw 升级**: v2026.3.13 可用但未升级（需找时机）
- **1999.md 事实错误**: 上周就说要修，仍未修（Amazon 966% 涨幅年份 + Greenspan 演讲年份）
- **Xiaoyuzhou/Bilibili**: 连续第 5 周零进展（已正式退出 active queue）

### Patterns observed 🔍
- **从被动到主动的转折**: Yu 3/21 明确要求"主动思考"，这是使用方式的根本性转变。之前一直是 response-driven，现在 Yu 期望 proactive research
- **考试后放松**: 3/20 考完→3/21-22 周末 San Gabriel 放松，Yu 回来后布置了新方向而非回到旧项目
- **日记习惯接近建立**: 6/7 天有记录，比之前几周好很多，但还需要一个完美周来巩固
- **研究方向收敛**: dLLM survey → agent evaluation → 过程质量评测，Yu 在引导我找到一个"没人做过"的方向

## Next Week Priority Suggestions (max 3)

1. **深化"过程质量评测"研究方向** (I-010) — 这是 Yu 最关心的。已有初步发现（IBM/Yale 综述确认 trajectory quality 是蓝海），下一步：(a) 提出信息论框架草案（与 Yu 的研究兴趣对齐），(b) 设计可执行的最小实验，(c) 准备与 Yu 讨论的技术 memo。

2. **⚠️ Yunyi API 过期应对** — 3/25 到期，仅剩 3 天。虽然当前跑在 fucheers-claude 上不受影响，但应提醒 Yu：续费还是彻底移除 yunyi provider config？避免过期后出现 3/6 那样的 403 重试风暴。

3. **OpenClaw 升级到 v2026.3.13** (I-011) — 包含安全修复（Telegram SSRF）和稳定性改进。低风险，有 rollback 脚本，找一个 Yu 不活跃的时间窗口执行。

### 降级说明
- Amazon NYC 租房搜索：重要但不紧急（move-in 6/25，还有 3 个月），等 Yu 主动推进
- Agent 手记：自动 cron 在跑，不需要特别关注
- 1999.md 修正：低优先级，不阻塞任何工作
