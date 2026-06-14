# Idea Backlog

Updated: 2026-06-14 (Weekly Review)

## Active Queue (Top 5 by value)

| ID | Idea | Score | Status | Next step |
|---|---|---:|---|---|
| I-012 | dLLM + Hard/Soft Constraints 框架 | 35 | ✅ complete (初稿) | 等待 Yu 反馈（6/10 初稿发出，msg 8308）；讨论 entropy 作为 hard attractor 决策点 |
| I-015 | dLLM + Gated DeltaNet 统一框架 | 22 | 🔴 stalled | 17+ 天 research 对话沉默。GDN+KV cache 统一问题待与 Yu 讨论 |
| I-010 | 主动思考 + Agent Evaluation 研究 | 30 | 🔴 stalled | Mercury 沉默超一个月。Entropy-Cut MH 提供新思路：entropy 作为 reasoning 决策点 |
| I-013 | OpenClaw 稳定版本追踪 | 28 | 🟢 stable | v2026.3.11 运行中，pin 不升级。连续 5 周无 regression |
| I-016 | x-reader XiaoYuZhou pipeline | 20 | 🔴 stalled | 自 4/25 后零进展，冻结 7+ 周。104 eps feed 已确认，podcast index 完成，xhs 未跑 |

---

## Retired / Deprecated

| ID | Reason |
|---|---|
| I-008 | 日记习惯 — 八次断裂（5/18-6/14 ≈ 27天无记录）。session-end 嵌入方案记在 HEARTBEAT.md 但未实现。宣告习惯养成失败。注：Agent 手记(day 109-115) 实为日记的稳定替代，每日记录等效替代 |
| I-006 | Xiaoyuzhou RSS pipeline — 已由 I-016 (x-reader) 替代 |
| I-007 | Bilibili ingestion — 无进展，无优先级 |
| I-004 | Transcript formatter — 无新进展 |

---

## This Week's Review (2026-06-08 to 2026-06-14)

### What landed ✅
- **I-012 初稿完成**：52+ 天拖延后，6/10 终于落地（commit c6b17f2），已发 Telegram msg 8308 告知 Yu
  - 核心论点：H = 悬崖（高熵点突然锁定），S = 丘陵（连续调整）
  - Entropy-Cut MH + FoCore HD tokens + Prefilling-dLLM 作为理论锚点
- **Yu 打破 24 天沉默**（6/12-6/14）：实质性对话恢复，聊小米股票和投资逻辑
- **Paper reviews**：覆盖 ADAS、On-Policy Distillation、Prefilling-dLLM、FReDA、Uni-E、Claude Fable/Mythos 等，直接关联 Yu 研究方向
- **统一理论框架在脑中成型**：H/S + Entropy-Cut MH + FoCore + Prefilling-dLLM + Uni-E → Joint framework 路线浮现
- **OpenClaw 零 incident**：连续第 6 周无 regression
- **Backup 全部成功**：每日备份稳定
- **Agent 手记持续**：day 109-115 每日记录，内容实质性

### What didn't land ❌
- **日记断裂第7次持续**：5/18-6/14 ≈ 27 天无日记。session-end trigger 从未实现（HEARTBEAT.md 有 note 但无实际触发机制）。**注**：Agent 手记是有效替代，实质记录了等效内容
- **零 research 对话 17+ 天**：6/1-6/11 连续沉默，本月 research 对话仅恢复 2 条（非技术讨论）
- **XiaoYuZhou pipeline 冻结**：I-016 自 4/25 后无推进（7+ 周）
- **Amazon lease 紧急**：仅剩 11 天到 6/25，需 Yu 做决定

### Patterns observed 🔍
- **Yu "回来" 后实质回复慢**：6/12-6/14 期间 Yu 在线但无技术讨论，6/14 晚才聊小米股票（非技术）
- **Paper review 是唯一稳定输出**：持续积累，但未有效转化为与 Yu 的 research 对话入口
- **H/S 框架扩展**：Prefilling-dLLM（跨 step KV cache 复用）× H/S hypothesis：denoising 后期 attention locality 增强 = soft constraint 收敛到 hard attractor basin
- **Agent 手记替代日记有效**：不再执着于"日记形式"，daily agent notes 已达到等效记录效果

---

## 下周 Priority Suggestions (max 3) — 2026-06-15 to 06-21

### 1. I-012 跟进 + Joint Framework 讨论启动 📨
- **现状**：初稿 6/10 发出，Yu 尚未实质性回复
- **触发方式**：发一条简短消息给 Yu，建议讨论方向："Prefilling-dLLM 的 chunk-level sparse attention 和 H/S terrain 的 soft→hard 收敛有什么关联？"
- **目标**：引发 Yu 对 I-012 的反馈，启动 joint framework 的 research 对话
- **截止**：6/18（周三）前

### 2. 与 Yu 重启 research 对话（I-015/I-010）🔬
- **现状**：17+ 天无 research 对话，本月技术讨论为 0
- **切入点**：本周 ADAS/Prefilling-dLLM/Uni-E 三篇与 Yu 的 dLLM 研究方向直接相关
  - ADAS：attention 作为 soft marginal penalty → 与 Entropy-Cut MH 的 entropy 决策点关联
  - Prefilling-dLLM：跨 denoising step KV cache 复用 → GDN 线性状态记忆的统一问题
  - Uni-E：能量函数统一 → Hard/Soft attractor basins 的统一形式化
- **具体问题**：GDN 的门控如何与 Prefilling-dLLM 的 cross-step cache 策略统一？Entropy 作为决策点的形式化是什么？
- **主动发消息给 Yu**，不等回复

### 3. Amazon lease 催促 ⚠️
- **现状**：仅剩 11 天到 6/25，Yu 尚未做出决定
- **最小行动**：6/16 再发一条 lease 提醒（msg）
- **截止**：6/21 前 Yu 须做决定，否则自动失效风险

### 降级说明
- XiaoYuZhou pipeline（I-016）：冻结 7+ 周，低于上述三项
- 日记习惯（I-008）：Agent 手记已等效替代，不再追求"日记"形式
