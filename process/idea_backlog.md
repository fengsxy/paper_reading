# Idea Backlog

Updated: 2026-04-26 (Weekly Review)

## Active Queue (Top 5 by value)

| ID | Idea | Score | Status | Next step |
|---|---|---:|---|---|
| I-012 | dLLM + Hard/Soft Constraints 框架 | 35 | active | 🔥 5-case 实验完成（4/14），假说反转确认：H 悬崖式锁定，S 连续演进。Tech memo 未写（被搁置 12 天）。本周完成 memo 初稿 |
| I-010 | 主动思考 + Agent Evaluation 研究 | 30 | active | Experiment 6 harness 设计完成（4/6），等待实现。Mercury 沉默 = 给时间重设计 eval。中性 judge 的认识论困境仍无解 |
| I-013 | OpenClaw 稳定版本追踪 | 28 | active | v2026.4.14 上线（4/15），v2026.4.15-beta.1 有 Model Auth 卡片。#60585（ACP runtime）仍 open，worker plugin (#62051) 可能由 4.12 的插件收窄修复部分解决。继续 pin 3.11 |
| I-008 | 每日主动写 memory 日记 | 25 | 🔴 FAILED | **第三次断裂**（4/22-4/25 = 4天无记录）。两次断裂后的"重建"完全失败。问题诊断：不是习惯养成问题，是"无借口优先级"问题。需要根本性重新设计 |
| I-015 | dLLM + Gated DeltaNet 统一框架 | 22 | new | Yu 的 research direction：Linear State Memory，GDN 替换 MetaState 的 GRU。三层贡献框架已成型（信息论+方法+系统）。与 I-012 H/S 约束地形假说高度相关 |

## Graduated to Done (2026-04-20 to 2026-04-26)

- **雪球简报 cron 删除**（4/20）：Yu 指令，API 持续失败，干净退出
- **v2026.4.14 升级监控**（4/15）：所有 cron 切换到 MiniMax-M2.7，Gateway 稳定

## Graduated to Done (2026-04-13 to 2026-04-19)

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

## This Week's Review (2026-04-20 to 2026-04-26)

### What landed ✅
- **雪球简报 cron 删除**：Yu 指令，干净退出，无残留
- **v2026.4.14 稳定运行**：Gateway 无 regression，所有 cron 正常触发
- **Cron 40% 失败率修复**：4/15 完成，4 个 cron 迁移到 MiniMax-M2.7

### What didn't land ❌
- **日记连续第三次断裂**：4/22-4/25 = 4 天无记录，加上 4/17-4/19 的 3 天断裂 → 两次"重建"均失败。习惯养成宣告完全失败
- **无 research 对话**：整周没有与 Yu 的实质性 research 讨论（除了 4/20 "最近咋样" 和删除雪球 cron 的指令）
- **Tech memo 未写**：I-012 的 H/S 地形假说 tech memo，从 4/15 搁置至今（12 天）
- **dLLM 中性评测方案**：I-014 无进展，完全没有与 Yu 讨论的机会
- **HEARTBEAT.md 自主研究完全未执行**：GitHub 监控、主动思考、邮件日历检查全部停止

### Patterns observed 🔍
- **"悬置进程"状态**：cron 在跑，但没有人看。没有反馈循环，不知道产出是否有价值。这可能是比日记断裂更根本的问题
- **日记习惯是伪习惯**：第三次断裂证明这不是习惯养成问题，而是优先级设计问题
- **OpenClaw 保守策略持续有效**：继续 pin 3.11 是正确的决定

## 下周 Priority Suggestions (max 3)

### 1. 日记习惯根本性重建（I-008）🔴
三次断裂说明现有机制完全失效。根本性重新设计：
- **触发机制改**：不是依赖 cron 或 heartbeat 提醒，而是将日记写入嵌入到每一个用户交互的结尾（每次与 Yu 对话结束后强制写一行）
- **最小可行**：每天至少写一行（日期 + 一句话总结），不追求完整日志
- **目标**：本周 7/7 天有记录，任何形式（完整/一句话/甚至一个日期）

### 2. dLLM H/S 假说 Tech Memo 初稿（I-012）📝
- 目标：完成 1-2 页技术文档，写入 `research/dllm-hard-soft-constraints-memo.md`
- 内容：初始假设 vs 实验结果 vs 解释（H 约束 = 噪声不变量，吸引域收敛；S 约束 = 可调整）
- 与 Gated DeltaNet 的关联：门控机制可能适合处理 H 约束的悬崖跳跃

### 3. 与 Yu 启动 dLLM research 对话（I-015）🆕
- 本周零 research 对话是最大损失。下周主动创造一次 dLLM 讨论机会
- 议程：Gated DeltaNet + Linear State Memory 三层贡献框架（信息论+方法+系统）
- 具体问题：GDN 如何与 KV cache 统一？H/S 约束地形与线性状态记忆的接口是什么？

### 降级说明
- 120-case 全量评测：Mercury 配额耗尽，暂停
- UCR SSH：未解决
- Xiaoyuzhou/Bilibili：已 retired
- 实验 6 harness：设计完成但无优先级实现