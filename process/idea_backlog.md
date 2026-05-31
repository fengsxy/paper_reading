# Idea Backlog

Updated: 2026-05-31 (Weekly Review)

## Active Queue (Top 5 by value)

| ID | Idea | Score | Status | Next step |
|---|---|---:|---|---|
| I-012 | dLLM + Hard/Soft Constraints 框架 | 35 | 🔴 stalled | 搁置 46 天。FoCore HD tokens = S-layer convergence points 已确认。Entropy-Cut MH 新支撑（#decisions not tokens）。Tech memo 初稿目标：下周三前 |
| I-015 | dLLM + Gated DeltaNet 统一框架 | 22 | 🔴 stalled | Yu 的 research direction：Linear State Memory，GDN 替换 MetaState 的 GRU。与 I-012 高度相关。本周 0 对话，下周必须启动一次讨论 |
| I-013 | OpenClaw 稳定版本追踪 | 28 | 🟢 stable | v2026.3.11 运行中，pin 不升级。连续 4 周无 regression。保守策略持续有效 |
| I-016 | x-reader XiaoYuZhou pipeline | 20 | 🟡 idle | 04-25 启动后无进展，feed 已确认（104 eps），build_podcast_indexes.py 对 xiaojun/dwarkesh 完成，xhs 未跑 |
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

## This Week's Review (2026-05-25 to 2026-05-31)

### What landed ✅
- **Paper reviews continue**：5/30、5/31 两次高质量推送，共覆盖 12 篇论文。3 篇直接关联 Yu 研究方向（diffusion optimality、CROP、Entropy-Cut MH）
- **Entropy-Cut MH (2605.30327)**：关键 insight——reasoning quality = # decisions not # tokens，mixing time scales with # decisions。直接支持 H/S 约束假说中"决策点"概念
- **OpenClaw 零 incident**：连续第 4 周无 regression
- **Memory maintenance**：5/29 完成，FoCore anchor、I-012 restart priority 确认
- **Weekly Review 完成**：本报告

### What didn't land ❌
- **日记断裂最长记录**：5/18-5/31 = 13 天（断裂第7次且最久）。HEARTBEAT.md 的 session-end 嵌入方案从未实现
- **dLLM H/S Tech Memo 零进展**：I-012 搁置 46 天（本应下周三完成的 memo）
- **零 research 对话**：整周 9 天连续沉默，无任何与 Yu 的 dLLM/GDN 讨论
- **x-reader XiaoYuZhou pipeline 冻结**：I-016 自 4/25 后无推进
- **Agent eval (I-010)**：Mercury 沉默，slow_batch_state 卡在 case 1，无进展

### Patterns observed 🔍
- **连续沉默打破困难**：9 天连续沉默（5/21-5/31），超越历史记录。cron 在跑，无人看，产出归隐
- **Paper review 是唯一稳定运转的 cron**：但产出的价值未转化为与 Yu 的对话
- **FoCore 锚点已确认**：HD tokens = S-layer convergence points，Entropy-Cut MH 提供理论支撑，但无 tech memo
- **无反馈回路持续**：日记系统死，dLLM research 方向无校正机会，pipeline 冻结

---

## 下周 Priority Suggestions (max 3)

### 1. 日记习惯最终重建 🔴
- **根本问题**：session-end 嵌入方案从未实现（HEARTBEAT.md 有但未生效）
- **行动**：立即在 HEARTBEAT.md 中添加实际的 session-end trigger，或者将日记触发从 cron 改为每次 agent 启动时的强制 3 行
- **目标**：本周 7/7 天有记录，哪怕只是一行日期+主题
- **验收**：周日核查 memory/ 目录下 6/1-6/7 文件数量

### 2. dLLM H/S Tech Memo 初稿（I-012）📝
- **目标**：完成 1-2 页，写入 `research/dllm-hard-soft-constraints-memo.md`
- **新支撑**：Entropy-Cut MH（decisions not tokens）、FoCore HD tokens（convergence points）
- **核心论点**：H-约束 = 悬崖（高 entropy 决策点，门控锁定）；S-约束 = 丘陵（渐进演进）
- **截止**：周三（6/3）

### 3. 与 Yu 启动 dLLM research 对话（I-015）🆕
- **现状**：本周 9 天连续沉默，本月 0 research 对话
- **议程**：GDN 三层贡献框架（信息论+方法+系统）、H/S 约束地形与线性状态记忆的接口
- **具体问题**：GDN 如何与 KV cache 统一？Entropy-Cut MH 的 decision-based 框架与 GDN 的门控机制有何关联？
- **触发**：6 篇强相关论文（diffusion optimality、CROP、Entropy-Cut MH）可作为对话切入点

### 降级说明
- 120-case 全量评测（I-010）：Mercury 沉默持续，暂停
- UCR SSH：未解决，不影响当前研究
- XiaoYuZhou pipeline（I-016）：优先级低于上述三项，下周如有对话机会再推进
- Xueqiu 简报：API 持续损坏，已删除
