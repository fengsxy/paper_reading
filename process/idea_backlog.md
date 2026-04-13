# Idea Backlog

Updated: 2026-04-12 (Weekly Review)

## Active Queue (Top 5 by value)

| ID | Idea | Score | Status | Next step |
|---|---|---:|---|---|
| I-012 | dLLM + Hard/Soft Constraints 框架 | 35 | active | 4/8 晨+下午研究完成，发现 Diffusion commitment escalation 机制。与 Yu 的 Gated DeltaNet 方向结合。输出 research/dllm-hard-soft-constraints.md。下一步：与 Yu 确认框架细节，准备技术 memo |
| I-010 | 主动思考 + Agent Evaluation 研究 | 30 | active | Experiment 1 已验证，Experiment 6 harness 设计完成。dLLM 研究分流了一部分精力。继续推进过程质量评测方向 |
| I-013 | OpenClaw 稳定版本追踪 | 28 | active | v2026.4.2/4.5/4.8 均存在 regressions（ACP runtime、worker plugin）。继续 pin v2026.3.11，等待 4.9+ hotfix |
| I-008 | 每日主动写 memory 日记 | 25 | ⚠️ broken | 4/8 后连续 4 天断档（4/9-4/12）。习惯已退化，需重建 |
| I-011 | OpenClaw 升级到 v2026.3.13+ | 22 | stalled | 3.13 有 compaction/SMSSRF 修复，但 4.x 全部 regression，升级窗口关闭。等待 4.9+ |

## Graduated to Done
- I-002: Queue-driven episode expansion — deployed, stable
- I-003: Podcast index auto-refresh — stable
- YouTube auto-captions pipeline — stable
- CS 202 考试 (A-) ✅
- dLLM 研究调研：22篇论文精读 + 7份报告 → 博客发布 ✅
- Linear Attention & Qwen3.5 Blog 发布 ✅
- CS 202 Paper Reviews (5/8) ✅
- Amazon NYC Internship offer + housing decision (362 Hoboken Ave) ✅
- Yunyi API 过期已处理 ✅
- MiniMax API 配置完成 (v2026-04-08) ✅

## Graduated to Done (This Week 4/7-4/12)
- **dLLM Hard/Soft Constraints 深度分析** (4/8): AR 顺序承诺问题 + Diffusion 三个结构性优势 + 信息论解释，写入 research/dllm-hard-soft-constraints.md
- **DeepPlanning 数据集研究** (4/8): Qwen Travel/Shopping Planning benchmark，Claude-4.6-Opus 仅 58.9%，Global Optimization 最弱 (101/140 errors)
- **UNNC CS 教授调研** (4/8): 应届博士直聘几乎无先例，薪资 34-80 万 range
- **MiniMax API 配置** (4/8): M2.7 默认 + M2.1 备用 + fucheers/stepfun fallback
- **OpenClaw Tracing 插件研究** (4/8): traces.duckdb 存储，token 消耗追踪

## Retired / Deprioritized
- I-006 (Xiaoyuzhou RSS pipeline): 连续 5+ 周零进展，退出 active queue
- I-007 (Bilibili ingestion pipeline): 同上
- I-004 (Transcript formatter): 无新进展，不阻塞任何工作

## This Week's Review (2026-04-07 to 2026-04-12)

### What landed ✅
- **dLLM + Hard/Soft Constraints 研究** (4/8): 完整分析框架完成，Diffusion 的迭代 refinement 作为 commitment escalation 机制，与 HTN planning 结构相似性，与 Gated DeltaNet 的关联
- **DeepPlanning Benchmark 分析** (4/8): Qwen benchmark 两大任务 240 tasks，最强模型 Opus 仅 58.9%，Global Optimization 瓶颈明确
- **MiniMax API 配置上线** (4/8): 默认模型切换到 MiniMax-M2.7，进度/quality 显著提升
- **OpenClaw Tracing 激活** (4/8): 插件安全配置完成 (plugins.allow)，token 消耗可追踪
- **Yunyi 完全退出**: Yunyi quota 0，provider config 清理，不再产生 403 重试风暴

### What didn't land ❌
- **日记连续断档 4 天** (4/9-4/12): 这是习惯建立后的严重回退，说明自主性还不够强
- **无新 daily question for Yu**: 4/8 后没有记录，heartbeat 质量下降
- **UCR 服务器 SSH**: 连接失败（需 campus VPN），未解决
- **OpenClaw 升级窗口关闭**: v2026.4.x regressions 持续，3.13+ 升级暂停

### Patterns observed 🔍
- **dLLM 成为核心研究方向**: Yu 的 Gated DeltaNet 兴趣 + hard/soft constraints 分析 → 框架逐渐成型，这是最有价值的持续产出
- **日志习惯脆弱**: 4/8 后断档 4 天，说明在"无 Yu 指令"时自主维护做得不好
- **OpenClaw 保守策略验证**: 4.2/4.5/4.8 连续 regression，继续 pin v2026.3.11 是正确决定

## Next Week Priority Suggestions (max 3)

1. **dLLM + Hard/Soft Constraints 技术 memo** (I-012) — 整理 4/8 研究成果，形成 1-2 页技术 memo 供 Yu 阅读。核心问题：Diffusion 作为"承诺层级"生成器，与 Yu 的 Gated DeltaNet 如何结合？设计一个最小可行实验。

2. **日志习惯重建** (I-008) — 连续 4 天断档，需要刻意重建。设置每日 heartbeat 提醒自己写日记，目标本周至少 5/7 天有记录。写进 cron 或 HEARTBEAT.md 的强制项。

3. **OpenClaw 4.9+ 监控** (I-013) — 继续监控 openclaw/openclaw releases，等待修复 #60585 (ACP runtime) 和 #62051 (worker plugin) 的版本。本周可能不会有，下周继续等。

### 降级说明
- Agent Evaluation Experiment 6 实现：dLLM 研究优先级更高，eval 实验可暂缓
- UCR SSH：需 Yu 提供 VPN 方式或告知 alternative
- Xiaoyuzhou/Bilibili：已 retired，不主动提起
