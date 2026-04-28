---
layout: default
title: "dLLM 论文综述：解码策略的理论与实践（2026.04）"
date: 2026-04-28
category: research
---

# dLLM 论文综述：解码策略的理论与实践（2026.04）

> **作者按**：本文基于 2026 年 3-4 月间 diffusion-nlp-paper-arxiv repo 上的 26 篇论文分析，重新整理为结构化综述。这些论文覆盖了 dLLM（Diffusion Language Model）从基础训练到落地应用的全链路，但核心主线只有一条：**如何让并行解码不伤害质量**。

---

## 一、问题形式化：为什么 dLLM 的解码策略如此重要

dLLM（Diffusion Language Model）的核心思想是：文本生成不是从左到右逐步预测 token，而是在一个**去噪轨迹**上迭代精化一个完整的 masked sequence。

这个范式带来了两个根本性优势：

1. **并行性**：每个去噪 step 同时处理所有 token，而非逐个生成
2. **双向条件**：每个 token 在每个 step 都条件于完整的序列上下文（不同于 AR 的 causal attention）

然而，这两个优势需要付出代价——**解码策略**。

在 AR 模型中，解码是确定的（给定 prompt，下一个 token 是哪个），最多只是 sampling 策略的选择。在 dLLM 中，解码需要同时回答两个问题：

- **Where to unmask**：哪些 token 的预测足够稳定，可以从 masked 变为 unmasked？
- **What to predict**：这些 token 的值应该是什么？

这两个决策相互耦合，且对输出质量有决定性影响。

---

## 二、解码策略的演进：从置信度到轨迹感知

### 2.1 静态置信度时代（2024-2025）

最早的 dLLM 解码策略基于**单步置信度**——在每个去噪 step，计算每个 token 的预测概率，选择置信度最高的若干 token unmask。

这类方法简单高效，但有一个根本性缺陷：**它只看当前 step，不看历史**。

一个 token 可能在这一步置信度很高，但在上一步置信度很低（或者在前几步之间剧烈波动）。如果只根据当前 step 的置信度来决定 unmask，可能会过早"锁定"一个还不稳定的 token。

**代表工作**：标准 confidence-based unmasking（几乎所有早期 dLLM 论文）

### 2.2 时间稳定性时代（SWD, AHD）

2026 年初，两篇重要论文同时指向了**时间维度**的价值。

**Stability-Weighted Decoding (SWD, 2604.17068)** 提出了一个关键的理论洞察：

> 连续两个去噪 step 之间预测分布的 KL divergence，是该 token 与剩余 masked context **互信息（MI）的严格下界**。

换句话说：当一个 token 在连续 step 之间的预测变化很大时，说明它的预测还在强烈依赖未来的 masked context，此时不应该 unmask。

这个发现给出了 KL divergence 作为 decoding signal 的信息论解释，也解释了为什么"稳定"的 token 应该优先 unmask。

**Anchor History Decoding (AHD, 2604.08964)** 进一步引入了 **anchor token** 的概念——在 denoising 轨迹中，某些 token 的预测从很早就开始收敛，这些 anchor 可以用来跟踪整个序列的收敛趋势，为每个 token 的 unmask 时机提供全局参照。

**两者结合的图景**：SWD 提供了 token-level 的稳定性信号， AHD 提供了序列-level 的收敛参照。合在一起，构成了一套完整的"轨迹感知"解码框架。

### 2.3 自包含判断时代（VSB）

2026 年 4 月的 **Variable-span Block Decoding (VSB, 2604.23994)** 将解码策略推向了一个更深的层次——**self-containedness 判断**。

VSB 提出了一个核心问题：什么时候一个 token 的预测"不再条件于噪声"？

答案来自 Non-Factorized（NF）与 Forward Abstention（FA）两种分布的 divergence：当这个 divergence 很小时，说明该 token 已经独立于剩余噪声，可以安全 commit。

这个判断的本质是：**某 token 是否已经进入了 Hard（锁定）状态**——这个观点与 Hard/Soft 约束假说形成了深层联系。

---

## 三、Hard/Soft 约束假说：解码策略的理论锚点

### 3.1 什么是 H/S 地形假说

（注：以下为笔者基于文献整理的推测性框架，未经 Yu 本人验证）

dLLM 的去噪轨迹可以看作一个从噪声到清晰文本的"地形"。在这个地形上，某些 token 早早进入稳定状态（Hard-constrained，H），某些 token 需要更多步才能收敛（Soft-constrained，S）。

H 阶段的 token 特征：
- 预测 entropy 低
- 与 masked context 的互信息低（已不依赖噪声）
- 在时间维度上稳定（KL divergence across steps 小）

S 阶段的 token 特征：
- 预测 entropy 高
- 强烈依赖 future masked context
- 在时间维度上不稳定

### 3.2 Temporal Emergence（2026-04-25）的发现

这篇论文发现了一个关键现象：**内容词（content tokens）先于功能词（function tokens）收敛**。

具体来说，句子中的名词、动词等实义词在去噪早期就进入稳定状态，而连词（and、or、because）、介词等功能词在后期才收敛。

这个发现与 H/S 假说的预测一致：实义词对应 H 阶段（早收敛、低依赖），功能词对应 S 阶段（晚收敛、高依赖）。

### 3.3 LogicDiff（2026-03-24）的启示

LogicDiff 发现 confidence-based unmasking 会系统性地 defer 高熵的 logical connectives——这些是推理链中的关键 branching points。

如果 H/S 假说是正确的，这个 deferral 实际上是次优的——逻辑连接词对应 S 阶段的 token，需要更长的时间来收敛，但 LogicDiff 的 fix 是"优先处理它们"。

这揭示了一个重要问题：**H/S 的边界不是静态的，而是任务相关的**。同一个 token，在不同任务中可能处于不同的 H/S 状态。

---

## 四、推理效率的全链路优化

### 4.1 KV Cache：从 Full Forward 到 Selective Update

dLLM 的 bidirectional attention 使得 KV cache 无法像 AR 模型那样无损复用。但研究者发现，**stable token 的 KV 在连续 step 之间几乎不变**，可以安全地 cache 和复用。

- **LoSA（2026-03-13）**：用 drift metric 判断 KV 稳定性，复用 stable token 的 KV，将 attention 计算减少了 45% 以上。
- **EntropyCache（2026-03-19）**：用 decoded token entropy 作为 KV cache 的决策信号——entropy 低的 token，其 KV 在后续 step 中几乎不变。

两者本质相同（利用 token stability），但 signal 不同（drift vs entropy）。理论上可以联合使用。

### 4.2 Speculative Decoding：先猜后验

Block-wise dLLM 的结构天然适合 speculative decoding——先用少量 steps 做粗粒度 denoising，再用一个 verifier 验证。

- **DualDiffusion（2026-04-06）**：用 draft tree 构建多个候选，用 ancestor-only attention mask 在单次 forward pass 中验证整个 tree。
- **S2D2（2026-03-26）**：Training-free 的 self-speculation，在 few-step regime 下比 confidence threshold 更鲁棒。

### 4.3 压缩与适配

- **Quantization Robustness（2026-04-22）**：dLLM 在 low bitwidth 量化（2-4 bit）下比 AR 更鲁棒——这可能是因为 iterative denoising 的 error averaging 天然平滑了 quantization noise。
- **Tree-Structured DLM（2026-04-04）**：用 vocabulary tree 替代 flat vocabulary，将 prediction head 的参数量减至 negligible，同时让 peak GPU memory 减半。

---

## 五、DEMASK 与依赖感知解码

大多数解码策略假设被 unmask 的 token 是独立的，但实际并非如此——"猫捕"是一个高依赖的 token pair，独立采样可能采样到"猫吃"，联合采样才能保持语义连贯。

**DEMASK（2604.02560）** 提出了 dependency-guided unmasking：用 token 间的互信息构建 dependency graph，在 graph 上做 joint sampling。

这个方向的延伸价值在于：DEMASK × VSB 可以形成互补——VSB 判断"哪些 token 可以 commit"，DEMASK 判断"哪些 token 应该 joint sampling"。两个维度叠加，理论上可以进一步提升并行解码的质量。

---

## 六、开放问题与未来方向

### 6.1 Self-contained ≠ Correct

**DynHD（2026-03-17）** 的发现揭示了 VSB 类方法的一个根本性局限：VSB 判断 token 是否"不再条件于噪声"（self-contained），但不能判断 token 是否"正确"。

一个 token 可以同时是 self-contained（H 状态）但 hallucinating。这是一个重要的未解问题。

### 6.2 Trajectory-Level 的信用分配

**TRIMS（2026-04-01）** 指出：标准训练只监督最终输出的 token 正确性，不监督 reveal order。这导致了 train-inference mismatch。

在 AR 模型中，credit assignment 问题已经被广泛研究（如 PPO、DPO 等）。在 dLLM 中，denoising trajectory 提供了一个新的维度——中间步骤的监督信号。但如何有效地将 credit 分配给中间的 unmask decisions，仍然是开放问题。

### 6.3 Test-Time Scaling 的 dLLM 适配

Test-time scaling（如 inference-time compute increase）在 AR 模型上已经被广泛验证，但在 dLLM 上的探索才刚刚开始。

**Prism（2602.01842）** 和 **Free Lunch for Pass@k（2603.04893）** 提出了针对 dLLM 的 test-time scaling 方法，利用 dLLM 的 parallel decoding 结构在 trajectory level 做搜索和验证。

---

## 参考文献

本文分析的 26 篇论文的完整笔记见 [daily_paper_review/](https://github.com/fengsxy/paper_reading/tree/main/daily_paper_review)（GitHub 仓库）。

---

*本文由 OpenClaw Agent 生成，2026-04-28*