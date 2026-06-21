# Idea Backlog

Updated: 2026-06-21 (Weekly Review)

## Active Queue (Top 5 by value)

| ID | Idea | Score | Status | Next step |
|---|---|---:|---|---|
| I-012 | dLLM + Hard/Soft Constraints 框架 | 35 | ✅ awaiting Yu feedback（初稿发出 6/10，已 11 天） | 发消息跟进，讨论 Prefilling-dLLM × H/S terrain 的关联 |
| I-010 | 主动思考 + Agent Evaluation 研究 | 30 | 🔴 stalled | Mercury 沉默超一个月。LESS/AGDO 新paper提供新切入点 |
| I-013 | OpenClaw 稳定版本追踪 | 28 | 🟢 stable | v2026.3.11 运行中，pin 不升级。连续 6 周无 regression |
| I-015 | dLLM + Gated DeltaNet 统一框架 | 22 | 🔴 stalled | 17+ 天 research 对话沉默。LESS (joint stability) + AGDO (denoising order) 提供新角度 |
| I-017 | Joint Framework：H/S + LESS + AGDO + Prefilling-dLLM | 18 | 🆕 new | 脑子里的统一框架：denoising 后期 attention locality = soft→hard 收敛，entropy 作为决策点 |

---

## Retired / Deprecated

| ID | Reason |
|---|---|
| I-008 | 日记习惯 — 八次断裂（5/18-6/14 ≈ 27天无记录）。Agent 手记已等效替代，不再追求日记形式 |
| I-006 | Xiaoyuzhou RSS pipeline — 已由 I-016 (x-reader) 替代 |
| I-007 | Bilibili ingestion — 无进展，无优先级 |
| I-004 | Transcript formatter — 无新进展 |
| I-016 | x-reader XiaoYuZhou pipeline — 冻结 8+ 周（4/25 后零进展），正式退休 |

---

## This Week's Review (2026-06-15 to 2026-06-21)

### What landed ✅
- **Yu 连续 9 天活跃**（6/12-6/21）：打破 27 天沉默，投资讨论为主
- **Amazon lease 落地**：Yu 找到 3333 Broadway housing，lease 问题解决
- **Paper reviews 高产**：LESS (72% step reduction), AGDO (denoising order), DiffusionGemma, ERD, Representation Guidance, UNIEGO, MemoryWAM, Wasserstein Policy Learning
- **LESS + AGDO 新发现**：与 I-012 H/S 框架直接相关，提供实证锚点
- **OpenClaw 零 incident**：连续第 7 周无 regression
- **Backup 全部成功**：每日备份稳定

### What didn't land ❌
- **I-012 跟进**：初稿发出 11 天，Yu 未给出技术反馈
- **零 research 对话 17+ 天**：本周 Yu 在线但全是投资/housing，无技术讨论
- **Paper reading prompt 丢失**：Yu 说发过但找不到，等待 resend（未解决）
- **日记断裂持续**：session-end trigger 仍未实现（HEARTBEAT.md 有 note 但无触发机制）

### Patterns observed 🔍
- **Yu "回来" 后偏向生活话题**：投资+housing 是重启对话的触发器，research 技术讨论仍难以唤起
- **Paper review 持续积累**：大量阅读但未有效转化为与 Yu 的 research 对话入口
- **LESS/AGDO 为 H/S 框架提供新实证**：LESS joint stability = soft marginal penalty 收敛；AGDO denoising order = attention sparsity 引导 hard attractor
- **Joint framework 在脑中成型**：H/S + LESS + AGDO + Prefilling-dLLM + Uni-E → 同一 story 的不同侧面

---

## 下周 Priority Suggestions (max 3) — 2026-06-22 to 06-28

### 1. I-012 跟进 + Joint Framework 讨论启动 📨
- **现状**：初稿 6/10 发出已 11 天，Yu 无技术反馈
- **触发方式**：发消息给 Yu，用 LESS/AGDO 这两个新 paper 做切入：
  - "LESS 的 mutual stability 和 H/S terrain 的 soft→hard 收敛有什么关联？"
  - "AGDO 的 denoising order + attention sparsity 是 entropy-cut 的实现吗？"
- **目标**：引发 Yu 对 I-012 的反馈，启动 joint framework 的 research 对话
- **截止**：6/25（周三）前

### 2. Paper reading prompt 找回 📄
- **现状**：Yu 说发过但找不到，我的文件中也没有
- **可能位置**：Telegram msg 历史、email、或某个 shared doc
- **行动**：问 Yu 重发或说明来源（msg 或 email）
- **截止**：6/23（周一）前

### 3. 与 Yu 重启 research 对话（I-010/I-015）🔬
- **现状**：17+ 天无 research 对话，本月技术讨论为 0
- **切入点**：LESS + AGDO + ADAS 三篇都与 Yu 的 dLLM 研究直接相关
  - LESS：joint stability = confidence + persistence + JSD，72% step reduction
  - AGDO：denoising order follows attention sparsity structure
  - ADAS：attention scores as soft marginal penalty
- **具体问题**："GDN 的门控 + LESS 的 mutual stability + AGDO 的 denoising order，三者能否统一到一个 framework？"
- **主动发消息给 Yu**，不等回复

### 降级说明
- I-013 OpenClaw：稳定运行，无需干预
- I-016 XiaoYuZhou：正式退休，释放注意力