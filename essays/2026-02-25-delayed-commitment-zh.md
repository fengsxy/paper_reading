---
title: "Coconut、Soft-Masked DLM、DSL 在做同一件事"
date: 2026-02-25
author: Longxuan Yu
lang: zh
---

# Coconut、Soft-Masked DLM、DSL 在做同一件事

最近读了三篇论文，表面上做的事情完全不同，但我越想越觉得它们在回答同一个问题：

**语言生成的时候，能不能对不确定的 token 晚一点做决定？**

### 先说 Coconut

Coconut（Chain of Continuous Thought）的观察是：传统 CoT 在语言空间推理，每生成一个 token 就做了一个不可逆的决策，走错了只能硬编。那如果把推理搬到连续的 hidden state 空间呢？一个向量可以同时编码多条候选路径的概率分布，不用急着选。

在 ProsQA（DAG 图搜索）上效果确实好，97% vs CoT 的 77.5%，表现出类似 BFS 的行为——第一步保持多个候选节点高概率，第二步收敛到最优路径。

但 Coconut 没有 scale up，原因很根本：

- 训练太脆弱，必须用 curriculum training 逐步替换 CoT token，没有 curriculum 直接崩（14.4% vs 34.1%）
- 精确推理反而更差，GSM8K 上 CoT 42.9%，Coconut 只有 34.1%。连续空间的模糊对搜索有利，但对精确符号操作是劣势
- 容量有限，候选路径指数增长时一个 hidden state 编码不了
- 没有 scaling law，CoT 的 token 数量可以无限扩展，continuous thought 的数量 N 是训练时定死的

Meta 的 Large Concept Model 犯了类似的错误，粒度更粗——把整个句子压成 SONAR embedding 做 diffusion，结果更差。

所以连续空间的好处（平滑、可并行探索）和代价（精度丢失、不可解释、解码误差）是绑定的，不能只要好处。

### 再说 Soft-Masked DLM

如果完全跳到连续空间代价太大，能不能在离散空间里加一点连续性？

Soft-Masked DLM（Hersche et al., IBM/ETH）的做法非常简单：masked diffusion 解码的时候，当一个 token 决定保留 mask，不用纯 [MASK] embedding，而是把 [MASK] 和 top-k 预测 token 的 embedding 做加权混合。就加了 3 个参数。

但效果是实在的：Dream-7B 上 finetune 后，coding benchmark 有一致提升，尤其是 few-step（高吞吐）场景。

为什么这么简单的东西能 work？因为标准 MDLM 的 binary masking 在信息论意义上是浪费的。每个 mask token 要么保留全部信息（不 mask），要么丢弃全部信息（mask），这是 1-bit 的决策。而 soft mask 允许保留部分信息——上一步的预测虽然不够确定到 unmask，但它包含的信息不应该被完全扔掉。

论文自己用了 "superposition" 来描述 soft mask 的效果，和 Coconut 的思路是同一个直觉，只是实现不同：Coconut 在连续空间用一个向量编码多条路径，Soft-Masked DLM 在离散空间用 embedding 混合保留部分信息。

但 SM 的局限也明显：它只是 inference-time 的 trick，没有改训练。模型训练时从未见过 soft-masked 的输入，所以它对这种输入的处理能力是没有被优化过的。

### 然后是 DSL

DSL（Discrete Stochastic Localization, Cheng, Thakuria, Brekelmans, Papalexakis, Ver Steeg）做了更根本的事：不是在 inference 时加 trick，而是从训练框架层面统一连续和离散 corruption。

核心洞察是 SNR-invariant denoiser：把 token embedding 放到单位超球面上后，最优 denoiser 的形式只依赖于观测 z，不依赖于 SNR（信噪比）。这意味着同一个网络可以处理任意 per-token noise level——从完全 mask（SNR→0）到完全 clean（SNR→∞）到任何中间状态。

这解决了 MDLM 的一个根本问题：训练-推理 mismatch。标准 MDLM 只在 binary corruption（mask/unmask 两个端点）上训练，但 ReMDM 推理时 remasking 产生的中间状态是 partially correct draft，模型从未在训练中见过这种输入。DSL 通过 mixed corruption training 让 denoiser 在训练时就见过这些中间状态。

结果：同样的 ReMDM sampler，用 DSL 训练的 denoiser 只需要 1/4 的步数达到同等质量。

更重要的是 DSL 对 remasking 的重新解释：remasking 就是 per-token SNR 路径上的回溯。AR、masked diffusion、remasking 在 DSL 框架下只是 SNR 路径的不同选择：

- AR：每个 token 的 SNR 从 0 一步跳到 ∞，按顺序逐个
- Masked diffusion：所有 token 的 SNR 同步从 0 到 ∞
- Remasking：不确定的 token 的 SNR 被打回低值，重新 denoise

### 统一来看

三篇在做同一件事的不同版本：对不确定的 token 推迟最终决策（delayed commitment）。

Coconut 用连续 hidden state 保持多路径，改的是推理过程，代价是精度和可训练性。Soft-Masked DLM 用 embedding 混合保留部分信息，也是改推理，轻量但没理论支撑。DSL 用 per-token SNR 控制信息保留量，从训练层面统一连续和离散，是最 principled 的方案。

进化方向很清楚：从完全跳到连续空间（代价太大），到在离散空间加一点连续性（trick 但没理论），到训练框架层面统一（最干净）。

### 缺的是什么

三篇都在做延迟承诺，但没有一篇从信息论角度回答根本问题：延迟承诺到底保留了多少信息？这些信息对生成质量的帮助有没有理论上界？

我认为可以用 rate-distortion 框架来形式化。dLLM 的 forward process 中，每一步 masking 都在丢信息。Hard mask 是极端情况——要么 R = H(X)，要么 R = 0，这是 R-D curve 上的两个端点。Soft mask 允许在 R-D curve 上连续移动，DSL 的 per-token SNR 就是 rate 的 proxy。

几个具体的问题：

- 最优的 masking schedule 是什么？给定 compute budget（总步数），每一步应该保留多少信息？等价于在 R-D curve 上找最优路径
- Coconut 的 BFS 行为能否用 R-D 解释？不确定的 token 保留高 rate，确定的 token 降低 rate，可能就是 R-D 最优策略的自然涌现
- DSL 的 SNR-invariant denoiser 意味着什么？denoiser 的最优性不依赖于 R-D 操作点，这个性质可能有更深的信息论解释

更具体地说，可以定义 I(X₀; X̃_t) 和 I(X₀; X_t) 分别为 soft-masked 和 hard-masked state 保留的互信息，证明前者严格大于后者，并给出 gap 如何转化为 reverse process 重建误差的改善。

这条路直接连接到 Greg 的信息论专长，也连接到 "Thinking Out of Order" 的发现——confidence-based remasking 本质上是在选择 R-D curve 上的操作点。

### 一句话

下一步不是再发明一个新的 soft mask 变体，而是回答：在离散生成中，延迟承诺的信息论最优策略是什么？

---

*相关论文：*
- *Coconut: Training Large Language Models to Reason in a Continuous Latent Space (Hao et al.)*
- *Soft-Masked Diffusion Language Models (Hersche et al., arXiv:2510.17206)*
- *Discrete Stochastic Localization for Non-autoregressive Generation (Cheng, Thakuria, Brekelmans, Papalexakis, Ver Steeg, arXiv:2602.16169)*

