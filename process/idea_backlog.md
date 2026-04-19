# Idea Backlog

Updated: 2026-04-19 (Weekly Review)

## Active Queue (Top 5 by value)

| ID | Idea | Score | Status | Next step |
|---|---|---:|---|---|
| I-012 | dLLM + Hard/Soft Constraints 框架 | 35 | active | 🔥 突破：H/S 地形假说反转（H先锁定=悬崖，S连续=丘陵）。5-case Mercury vs MiniMax 实验完成，结论反直觉。核心问题：与 Yu 的 Gated DeltaNet 如何结合？最小可行实验设计 |
| I-010 | 主动思考 + Agent Evaluation 研究 | 30 | active | Experiment 6 harness 完成。Mercury 沉默 = 给时间重设计 eval。关键：中性 judge 的认识论困境（封闭系统无法自审）|
| I-013 | OpenClaw 稳定版本追踪 | 28 | active | v2026.4.14 上线，ACP runtime (#60585) 仍 open，worker plugin (#62051) 可能由 4.12 的插件收窄修复。4.15-beta.1 有 Model Auth 卡片。继续 pin 3.11 |
| I-008 | 每日主动写 memory 日记 | 25 | ⚠️ broken | 🔴 4/9-4/12 断 4 天 → 4/16 恢复 → **4/17-4/19 又断 3 天**。习惯两次断裂，说明自主性仍不足。本周再次重建 |
| I-014 | dLLM 中性评测方案设计 | 23 | new | Mercury 沉默后关键问题：封闭系统无法自审。需要外部 judge 或结构化评分协议。Yu 的 Gated DeltaNet 可能提供评测框架思路 |

## Graduated to Done (This Week 4/13-4/19)

- **dLLM DeepPlanning 5-case 实验** (4/14): Mercury vs MiniMax 对比，H/S 约束时间线分析。关键发现：假说反转（MiniMax 慢但质量高，Mercury 快但 H 约束无法满足）
- **dLLM 约束地形假说反转** (4/15): H 约束先锁定（悬崖地形），S 约束连续（丘陵地形）。与最初假设相反，值得深入写成技术文档
- **OpenClaw v2026.4.14 升级** (4/15): Gateway 稳定运行，所有 8 个 cron job 切换到 MiniMax-M2.7
- **Fucheers API 退出** (4/15): DNS fail 导致 provider 删除，Karpathy/Paper&HN cron 切换到 MiniMax
- **research docs 推送 GitHub**: dllm_long_horizon_agent.md, dllm_hard_soft_constraints_experiment.md → paper_reading repo
- **OpenClaw v2026.4.15-beta.1 监控** (4/15): Model Auth status card，context-window 修复 (#67277)
- **Cron job 超时优化**: Agent 手记 300s→600s（4/15）

## Graduated to Done (Previous Weeks)
- dLLM 研究调研：22篇论文精读 + 7份报告 → 博客发布 ✅
- MiniMax API 配置完成 ✅
- CS 202 Paper Reviews (5/8) ✅
- Amazon NYC Internship offer + housing decision ✅
- YouTube auto-captions pipeline ✅
- CS 202 考试 (A-) ✅

## Retired / Deprioritized
- I-006 (Xiaoyuzhou RSS pipeline): 5+ 周零进展，退出 active queue
- I-007 (Bilibili ingestion pipeline): 同上
- I-011 (OpenClaw 升级到 v2026.3.13+): 已合并到 I-013 版本追踪
- I-004 (Transcript formatter): 无新进展，不阻塞任何工作

## This Week's Review (2026-04-13 to 2026-04-19)

### What landed ✅
- **dLLM 实验突破**: 5-case Mercury vs MiniMax 完成，发现 H/S 地形假说反转（直觉反常识），这是本周最高价值产出
- **OpenClaw 4.14 升级成功**: Gateway 稳定，所有 cron 切换 MiniMax-M2.7，无 regression
- **约束地形反转写成文档**: "第五十二天"记录了关键洞察：H 约束悬崖式锁定，S 约束连续演进
- **Cron 超时优化**: Agent 手记从 300s→600s，避免慢性任务的 timeout 误报
- **Fucheers 干净退出**: DNS fail 导致删除，无残留，无浪费

### What didn't land ❌
- **日志连续断裂两次**: 4/9-4/12 断 4 天 → 4/16 短暂恢复 → 4/17-4/19 又断 3 天。这是本周期最严重的问题，说明自主维护机制完全失效
- **无新 daily question for Yu**: 本周没有任何给 Yu 的主动 research question
- **Mercury 配额耗尽**: 免费额度用尽，120-case 全量评测无限期暂停
- **无外部 neutral judge**: dLLM 中性评测问题悬而未决，封闭系统自审的认识论困境没有进展
- **4/17-4/19 完全无日志**: 连续 3 天没有任何 session 或 cron 日志记录（cron 可能仍在运行但无记录）

### Patterns observed 🔍
- **dLLM 研究进入"收获期"**: 框架假设被实验数据反直觉地修正——这是科学进步的正常路径。关键洞察：denoising 的分层假设在 H/S 约束上表现与预期相反
- **日志习惯是伪习惯**: 两次断裂（4 天 + 3 天）说明这不是真正的习惯养成。问题不在于提醒，而在于没有把它放在"无借口"的优先级
- **cron 在跑但没人看**: 4/17-4/19 无日志记录，cron 可能全部正常也可能部分失败。被动性是主要风险
- **OpenClaw 保守策略持续有效**: 4.14 无 regression，继续正确

## Next Week Priority Suggestions (max 3)

### 1. 日记习惯重建（I-008）🔴
两次断裂已证明这不是习惯。设置 HEARTBEAT.md 中强制检查项（每日第一次 heartbeat 必写日记），而非依赖 cron 或外部提醒。目标：本周 7/7 天有记录，连续 7 天后升级为"习惯"。

### 2. dLLM H/S 地形假说写成技术 memo（I-012）
将"假说反转"整理成 1-2 页技术 memo：
- 初始假设：soft 先收敛，hard 后锁定
- 实验结果：hard 在中后期悬崖式锁定（cliffs），soft 全程连续（hills）
- 解释：denoising 的顺序性与约束类型无关，与约束的"空间密度"相关
- 与 Gated DeltaNet 的关联：门控机制可能适合处理硬约束的悬崖跳跃

### 3. dLLM 中性评测方案设计（I-014）🆕
Mercury 沉默 + 封闭系统无法自审 = 核心瓶颈。与 Yu 讨论：是否可以用 Gated DeltaNet 的门控信号作为外部评分代理？或者设计一个基于约束满足率的半自动评测协议？

### 降级说明
- 120-case 全量评测：Mercury 配额耗尽，暂停
- UCR SSH：未解决
- Xiaoyuzhou/Bilibili：已 retired
