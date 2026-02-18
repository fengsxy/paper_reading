# Paper Reading Notes

Personal paper reading notes by [Longxuan Yu](https://fengsxy.github.io) @ UC Riverside

## 🧭 Timeline

- [张小珺访谈 Timeline](transcripts/xiaojun/)

## 🆕 最近更新

| 日期 | 更新内容 |
|------|----------|
| 2026-02-17 | [Karpathy RSS](karpathy_rss/2026-02-17-karpathy-rss-digest.md): Showboat 生态, 零工经济骗局, Claude Code 做研究 |
| 2026-02-17 | [Scholar Inbox](scholar_inbox/2026-02-16-diffusion-dllm.md): Diffinity, dVoting, Discrete Copula Diffusion 等 10 篇 |
| 2026-02-17 | [Hacker News](hackernews/2026-02-17.md): NanoClaw Docker, AI PR Review, Epstein 文件分析 |
| 2026-02-16 | [Karpathy RSS](karpathy_rss/2026-02-16-karpathy-rss-digest.md): AI Vampire, Deep Blue 焦虑, 社区三难困境 |
| 2026-02-16 | [Essay](essays/2026-02-16-openclaw-reflections-zh.md): 大年三十的 OpenClaw 思考 |

---

## 📚 Scholar Inbox

### Diffusion LLM (dLLM) - Core

| Paper | arXiv | Topic |
|-------|-------|-------|
| [McDiffuSE: MCTS for Ordering](scholar_inbox/mcdiffuse_mcts_ordering.md) | 2602.12586 | 用 MCTS 搜索最优生成顺序 |
| [dVoting: Fast Voting](scholar_inbox/dvoting.md) | 2602.12153 | 不需要训练的 voting 加速 |
| [DAWN: Dependency-Aware](scholar_inbox/dawn_dependency_aware.md) | 2602.06953 | 基于依赖图的快速推理 |
| [RCD: Residual Context](scholar_inbox/rcd_residual_context.md) | 2601.22954 | 回收被丢弃 token 的计算 |
| [LLaDA2.1: T2T + RL](scholar_inbox/llada21_t2t_rl.md) | 2602.08676 | Token 编辑 + 强化学习对齐 |
| [XDLM: Unified Framework](scholar_inbox/xdlm_unified.md) | 2602.01362 | 统一 MDLM 和 UDLM |

### dLLM - Decoding & Search

| Paper | arXiv | Topic |
|-------|-------|-------|
| [Self-Rewarding SMC](scholar_inbox/self_rewarding_smc.md) | 2602.01849 | SMC 提升采样质量和多样性 |
| [SOAR: Adaptive Search](scholar_inbox/soar_adaptive_search.md) | 2602.10953 | 低 confidence 搜索，高 confidence 加速 |
| [RDD: Reversible Decoding](scholar_inbox/rdd_reversible_decoding.md) | 2602.00150 | 可逆解码，从错误中恢复 |

### dLLM - Efficiency

| Paper | arXiv | Topic |
|-------|-------|-------|
| [SureLock: Early Stopping](scholar_inbox/surelock_early_stopping.md) | 2602.06412 | 跳过已收敛 token 的计算 (ICLR 2026) |
| [FOCUS: Dynamic Batching](scholar_inbox/focus_dynamic_batching.md) | 2601.23278 | 动态聚焦可解码 token |

### dLLM - Generation Quality

| Paper | arXiv | Topic |
|-------|-------|-------|
| [Positional Alignment + CTC](scholar_inbox/positional_alignment_ctc.md) | 2601.22947 | 用 CTC 解决位置对齐问题 |
| [LR-DLLM: Length Regularization](scholar_inbox/lr_dllm_length_regularization.md) | 2602.07546 | 解决变长生成的长度偏差 |
| [Diffinity: Constrained Gen](scholar_inbox/diffinity_constrained_generation.md) | 2602.12468 | 让 dLLM 遵守正则表达式约束 |

### Diffusion Theory & Methods

| Paper | arXiv | Topic |
|-------|-------|-------|
| [Drifting Models](scholar_inbox/drifting_models.md) | 2502.04770 | One-step generation 新范式 |
| [Wright-Fisher Unified Diffusion](scholar_inbox/wright_fisher_unified_diffusion.md) | 2512.15923 | 统一 discrete/Gaussian/simplicial diffusion |
| [Information-Estimation Metric](scholar_inbox/information_estimation_metric.md) | 2510.02514 | 用 denoising error 定义距离 |

### Other

| Paper | arXiv | Topic |
|-------|-------|-------|
| [Parallel Token Generation](scholar_inbox/parallel_token_generation.md) | - | Flow-based 并行生成 |
| [Hot Mess Theory](scholar_inbox/hot_mess_theory.md) | - | AI 失败的 bias-variance 分析 |
| [Diffusion for Compression](scholar_inbox/diffusion_compression.md) | - | 用 diffusion 做图像压缩 |

## 🔬 Research Notes

深度研究调研文档

| 文档 | 内容 |
|------|------|
| [Overnight Summary](research/overnight_summary.md) | 一夜研究总结：核心收获与下一步 |
| [Karpathy Insights](research/karpathy_insights.md) | Karpathy 最新项目分析 (nanochat, hn-time-capsule) |
| [Ordering Theory Draft](research/ordering_theory_draft.md) | dLLM Ordering 的信息论框架草稿 |
| [Answer-Anchored CoT Experiment](research/answer_anchored_cot_experiment.md) | 实验设计：先给答案再填 CoT |
| [dLLM Codebase Survey](research/dllm_codebase_survey.md) | 主流 dLLM 代码库评估 (LLaDA, Dream, MDLM...) |
| [Token Difficulty Related Work](research/token_difficulty_related_work.md) | Token Difficulty 相关工作调研 |
| [Ordering Paper Outline](research/ordering_paper_outline.md) | Ordering 论文大纲草稿 |

## 📡 Karpathy RSS Digest

Curated picks from [Andrej Karpathy's RSS feeds](https://youmind.com/rss/pack/andrej-karpathy-curated-rss) - 92 sources covering AI, tech, and independent blogs.

| Date | Highlights |
|------|------------|
| [2026-02-16](karpathy_rss/2026-02-16-karpathy-rss-digest.md) | AI Vampire (Yegge), Deep Blue 焦虑 (Willison), $20/月的投降 (Duggan), 社区三难困境 (Doctorow) |
| [2026-02-15](karpathy_rss/2026-02-15-karpathy-rss-digest.md) | microgpt 200行GPT (Karpathy), AI加剧工作 (HBR), Agent攻击维护者, 500个零日漏洞, 中级工程师危机 |
| [2026-02-08](karpathy_rss/2026-02-08-karpathy-rss-digest.md) | Dark Factory (StrongDM), AI采用之旅 (Hashimoto), 90%代码AI写 (Crawshaw), Vouch开源治理, 心理健康危机 |
| [2026-02-01](karpathy_rss/2026-02-01-karpathy-rss-digest.md) | Moltbook AI 社交网络 (Willison), Vibe-Knowing (Diallo), OpenClaw Docker, GPT-2 成本降 600x |

## 🔥 Hacker News

Daily AI/ML highlights from Hacker News

| Date | Highlights |
|------|------------|
| [2026-02-16](hackernews/2026-02-16.md) | DeepMind 数学研究, Audio AI 小团队, MicroGPT 可视化, AGI 讨论 |

## ✍️ Essays

| Date | Title |
|------|-------|
| [2026-02-16 (中文)](essays/2026-02-16-openclaw-reflections-zh.md) | 大年三十的 OpenClaw 思考 |
| [2026-02-16 (EN)](essays/2026-02-16-openclaw-reflections-en.md) | Reflections on OpenClaw: Chinese New Year's Eve Thoughts |

---

**Total: 20 papers + 7 research docs + 1 essay + 4 RSS digests**

Updated daily at 8:00 AM Pacific
