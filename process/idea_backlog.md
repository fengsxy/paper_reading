# Idea Backlog

Updated: 2026-06-07 (Weekly Review)

## Active Queue (Top 5 by value)

| ID | Idea | Score | Status | Next step |
|---|---|---:|---|---|
| I-012 | dLLM + Hard/Soft Constraints 框架 | 35 | 🔴 stalled | 搁置 52+ 天。Entropy-Cut MH + FoCore HD tokens 理论支撑已齐，Tech memo 仍未动笔。目标 6/10 初稿 |
| I-015 | dLLM + Gated DeltaNet 统一框架 | 22 | 🔴 stalled | 17+ 天沉默，本月 0 research 对话。GDN+KV cache 统一问题待讨论。Entropy-Cut MH 接口待探索 |
| I-013 | OpenClaw 稳定版本追踪 | 28 | 🟢 stable | v2026.3.11 运行中，pin 不升级。连续 4 周无 regression。保守策略持续有效 |
| I-016 | x-reader XiaoYuZhou pipeline | 20 | 🔴 stalled | 自 4/25 后零进展，冻结 6+ 周。104 eps feed 已确认，podcast index 对 xiaojun/dwarkesh 完成，xhs 未跑 |
| I-010 | 主动思考 + Agent Evaluation 研究 | 30 | 🔴 stalled | Mercury 沉默超一个月。零进展。Entropy-Cut MH 提供新思路：entropy 作为 reasoning 决策点，无需 RL |

---

## Retired / Deprecated

| ID | Reason |
|---|---|
| I-008 | 日记习惯 — 八次断裂（5/18-5/31 = 13天无记录）。session-end 嵌入方案记在 HEARTBEAT.md 但未实现。宣告习惯养成失败 |
| I-006 | Xiaoyuzhou RSS pipeline — 已由 I-016 (x-reader) 替代 |
| I-007 | Bilibili ingestion — 无进展，无优先级 |
| I-004 | Transcript formatter — 无新进展 |

---

## This Week's Review (2026-06-01 to 2026-06-07)

### What landed ✅
- **Paper reviews**: 3 次高质量推送（6/1: 8 篇，6/6: 6 篇，6/7: 6 篇），共 20 篇。覆盖 ENBP、DoPr、Causal Atlases、CAPR、SAID、FRAP、ATWU 等，直接关联 Yu 研究方向（geometric representation、double preconditioning、entropy DAG）
- **OpenClaw 零 incident**：连续第 5 周无 regression
- **Memory maintenance**：6/1 完成
- **Weekly Idea Review**：6/5(Fri) 完成，6/7(Sun) 完成本报告
- **Backup 全部成功**：每日备份稳定

### What didn't land ❌
- **日记断裂第7次持续**：5/18-6/7 ≈ 20 天无日记。session-end trigger 从未实现（HEARTBEAT.md 有 note 但无实际触发机制）
- **dLLM H/S Tech Memo 零进展**：I-012 搁置 52+ 天
- **零 research 对话**：17+ 天连续沉默（6/1-6/7），本月 0 对话
- **XiaoYuZhou pipeline 冻结**：I-016 自 4/25 后无推进
- **断裂反思深化**：诚实性比规律性更重要，不再数字游戏——但实质无改变

### Patterns observed 🔍
- **沉默进入常态化**：17 天沉默已不再触发焦虑数字游戏，是进步也是问题
- **Paper review 是唯一稳定输出**：但产出始终未转化为与 Yu 的对话入口
- **研究文献快速积累无转化**：20 篇新论文覆盖 geometric/entropy/conformal/reasoning，无回路到 Yu
- **无外部触发条件**：日记需要 session-end，session 需要 Yu 在场，两个条件同时缺失

---

## 下周 Priority Suggestions (max 3) — 2026-06-08 to 06-14

### 1. 日记系统最小可用重建 🔴
- **根本问题**：session-end trigger 无法在 cron 中实现，需要实际 session 事件
- **最小行动**：在每次与 Yu 的 session 结束时（无论多短），立即写一行到 `memory/YYYY-MM-DD.md`（哪怕"与 Yu 讨论了 X"）——这是唯一真实触发路径
- **本周目标**：6/8-6/14 期间如有任一次 Yu 对话，确保写日记
- **如无对话**：考虑在每日 06:00 UTC agent notes cron 中嵌入一行日记（不依赖 session-end）

### 2. dLLM H/S Tech Memo 初稿（I-012）📝
- **目标**：完成 1-2 页初稿，写入 `research/dllm-hard-soft-constraints-memo.md`
- **理论支撑已齐**：Entropy-Cut MH（decisions not tokens）、FoCore HD tokens（convergence points）、H locks FIRST（reversal confirmed）
- **核心论点**：Hard constraints = 高 entropy 决策点（门控锁定，悬崖）；Soft constraints = 渐进丘陵
- **Entropy-Cut MH 接口**：GDN 的门控 ≈ decision-based reasoning 中的选择性 commit
- **截止**：6/10（周三）

### 3. 触发一次与 Yu 的 research 对话（I-015）🆕
- **现状**：17+ 天沉默，本月 0 research 对话
- **切入点**：6 篇强相关论文可作为 conversation starter：
  - **ENBP**（SE(3)-equivariant factor graphs）：geometric representation learning，100× faster than diffusion
  - **DoPr**（double preconditioning）：validation loss ≠ downstream success，重要反直觉发现
  - **Causal Atlases**：maximum entropy DAG ensemble，信息瓶颈理论连接
- **具体问题**：GDN 的线性状态记忆如何与 KV cache 架构统一？DoPr 的 train/test mismatch 结论对 diffusion-based LLM 意味着什么？
- **触发方式**：主动发一条消息给 Yu，不等

### 降级说明
- 120-case 全量评测（I-010）：Mercury 沉默持续，暂停
- XiaoYuZhou pipeline（I-016）：冻结超过 6 周，优先级低于上述三项
- Amazon housing lease：Yu 的 action item，不在我控制范围内
