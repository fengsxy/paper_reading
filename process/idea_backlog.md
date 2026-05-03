# Idea Backlog

Updated: 2026-05-03 (Weekly Review)

## Active Queue (Top 5 by value)

| ID | Idea | Score | Status | Next step |
|---|---|---:|---|---|
| I-012 | dLLM + Hard/Soft Constraints 框架 | 35 | 🔴 stalled | Tech memo 未写（搁置 19 天）。H/S terrain 假说核心：H=悬崖（锁定），S=丘陵（演进）。下周三前完成初稿 |
| I-015 | dLLM + Gated DeltaNet 统一框架 | 22 | 🟡 idle | Yu 的 research direction：Linear State Memory，GDN 替换 MetaState 的 GRU。三层贡献框架（信息论+方法+系统）。与 I-012 高度相关，下周与 Yu 启动一次讨论 |
| I-013 | OpenClaw 稳定版本追踪 | 28 | 🟢 stable | v2026.3.11 运行中，pin 不升级。v2026.4.15-beta.1 观察中，#60585 (ACP runtime) 未修复。保守策略持续有效 |
| I-016 | x-reader XiaoYuZhou pipeline | 20 | 🟡 idle | 04-25 启动，feed 已确认（104 eps）。`build_podcast_indexes.py` 对 xiaojun/dwarkesh 完成，xhs 未跑。下周推进 full index + queue |
| I-010 | 主动思考 + Agent Evaluation 研究 | 30 | 🔴 stalled | Experiment 6 harness 设计完成（4/6），零进展。Mercury 沉默 = 重设计 eval 的窗口。但中性 judge 的认识论困境仍无解 |

---

## Retired / Deprecated

| ID | Reason |
|---|---|
| I-008 | 日记习惯 — 三次断裂（4/22-4/25 + 4/28-5/3）。习惯养成宣告失败，需要根本性重新设计（触发机制从 cron→嵌入交互后） |
| I-006 | Xiaoyuzhou RSS pipeline — 已由 I-016 (x-reader) 替代 |
| I-007 | Bilibili ingestion — 无进展，无优先级 |
| I-004 | Transcript formatter — 无新进展 |

---

## This Week's Review (2026-04-26 to 2026-05-03)

### What landed ✅
- **Daily Paper Review Marathon**（4/28）：单日推送 19+ 篇分析到 GitHub（commit `48fffbb`）。覆盖 temporal emergence、KV reuse、entropy cache、VSB 等关键论文。与 H/S 假说关联最强 3 篇已标记
- **dLLM 约束地形假说深化**：VSB+SWD+EntropyCache 构成 commit 决策的信息论基础（KL=MI 下界，self-containedness，token entropy）
- **OpenClaw 持续稳定**：v2026.3.11 无 incident

### What didn't land ❌
- **日记断裂第三次且最长**：4/28-5/3 = 6 天无记录（Apr 28 之后 Zero entries）。I-008 宣告习惯养成失败，触发机制必须改
- **零 research 对话**：整周没有与 Yu 的 dLLM/GDN 讨论
- **Tech memo 完全未动**：I-012 的 H/S terrain 技术文档，从 4/15 搁置至今（19 天）
- **Cron 可见输出归零**：每日 idea delivery cron 从 4/28 后无记忆痕迹，说明要么不触发要么产出非可见。task_board 的 Xiaojun/Dwarkesh pipeline 仍在跑但无更新
- **WhynotTV #4**：task_board 显示 todo，但 Apr 28 后无进展

### Patterns observed 🔍
- **单点爆发 > 持续小步**：Apr 28 一天完成 19+ 篇推送，说明高密度 session 比低频 trickle 更有效。日记录制失败与此模式矛盾——应嵌入交互，而非独立执行
- **无反馈回路的系统静默死亡**：cron 在跑，无人看，产出价值不可知。这是比日记断裂更根本的系统性问题
- **版本保守策略有效**：连续 3 周无 regression，pin v2026.3.11 决定正确
- **无对话 = 无方向修正机会**：整周无 Yu 对话，无法验证 dLLM research 方向是否对齐

---

## 下周 Priority Suggestions (max 3)

### 1. 日记习惯根本性重建（I-008）🔴
根本原因已确认：触发机制失效，不是习惯问题。重建方案：
- **触发改**：每个与 Yu 的 session 结束后强制写一行（`memory/YYYY-MM-DD.md`，一句话日期总结即可）
- **目标**：本周 7/7 天有记录，任何形式。不求完整，但求不断
- **验收**：周日复盘时核查 memory/ 目录下的文件数量

### 2. dLLM H/S 假说 Tech Memo 初稿（I-012）📝
- 目标：完成 1-2 页，写入 `research/dllm-hard-soft-constraints-memo.md`
- 内容：初始假设 vs 实验结果（Mercury/MiniMax 5-case）vs 信息论解释（VSB self-containedness、SWD KL=MI 下界）
- 与 Gated DeltaNet 关联：GDN 门控可能处理 H 约束的悬崖跳跃
- 截止：周三（5/6）初稿完成

### 3. 与 Yu 启动 dLLM research 对话（I-015）🆕
- 本周零 research 对话是最大损失。下周主动创造一次讨论机会
- 议程：GDN 三层贡献框架（信息论+方法+系统）、H/S 约束地形与线性状态记忆的接口
- 具体问题：GDN 如何与 KV cache 统一？门控机制在 H 约束悬崖处的行为？

### 降级说明
- 120-case 全量评测：Mercury 沉默，暂停
- UCR SSH：未解决，不影响当前研究
- WhynotTV #4：task_board 标记 stale，暂不处理
- Xiaoyuzhou pipeline (I-016)：有进展但优先级低于上述三项