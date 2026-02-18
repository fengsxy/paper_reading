# 给 Greg 的邮件草稿

## 核心 Insight 提炼

你的思考里有几个很有价值的点，我来帮你梳理：

### Insight 1: Not all tokens are equal
- 模型一次前向传播获得的信息远超一个 token
- AR 架构的瓶颈：即使模型"已经知道答案"，也只能一个一个吐出来
- 这就是为什么 speculative decoding 和 dLLM 都在尝试突破这个限制

### Insight 2: dLLM 作为 difficulty-aware predictor
- dLLM 的 confidence 分布天然反映 token 难度
- 简单 token：高 confidence，可以激进地并行生成
- 难 token：低 confidence，需要更多 refinement 或 AR 指导
- **你的实验想法**：如果先给出答案（最难的部分），CoT 生成是否能大幅加速？

### Insight 3: 物理位置 vs 逻辑位置的解耦
- dLLM 的 KV Cache 问题本质是双向注意力与因果性的冲突
- WeDLM 的方案：解耦物理位置和逻辑位置
- 这可能是把 dLLM 用于 speculative decoding 的关键

### Insight 4: Soft remask > Hard mask
- 当前 dLLM 推理丢弃了太多信息（hard mask 一次性决定）
- Soft/progressive mask 保留更多中间信息
- 这与 speculative decoding 中复用 large model hidden states 的思路一致

---

## 邮件草稿（中文版）

**主题：** Research Thoughts on Bridging dLLM and Speculative Decoding

Hi Greg,

我最近在深入思考 diffusion language models (dLLM) 和 speculative decoding 之间的联系，想分享一些初步想法和相关论文。

**核心观察：Not all tokens are equal**

AR 模型的一个根本限制是：即使模型在第一层就"知道"了答案，架构也强制它一个 token 一个 token 地输出。这浪费了大量计算。Speculative decoding 和 dLLM 都在尝试突破这个限制，但方式不同：
- Speculative decoding：用小模型快速 draft，大模型验证
- dLLM：直接并行预测多个 token

我认为这两个方向可以互相启发。

**Idea 1: dLLM 作为 difficulty-aware predictor**

dLLM 的一个独特优势是它的 confidence 分布天然反映了 token 的难度。对于简单的 token，confidence 高，可以激进地并行生成；对于难的 token，confidence 低，可能需要 AR 模型来"锚定"。

我想做一个实验：对于 reasoning 任务，如果先给出最难的部分（比如最终答案），然后让 dLLM 生成 CoT，是否能大幅加速？这可以验证 dLLM 是否真的能利用"难 token 已知"的信息。

相关论文：[Thinking Out of Order](https://arxiv.org/abs/2601.22035) 分析了 dLLM 的生成顺序与 reasoning 顺序的关系。

**Idea 2: 解耦物理位置和逻辑位置**

dLLM 难以使用 KV Cache 的根本原因是双向注意力与因果性的冲突。[WeDLM](https://arxiv.org/abs/2512.22737) 提出了一个有趣的方案：解耦物理位置和逻辑位置，预测后重新排序以保证因果性。

我在想这个思路是否可以用于 speculative decoding：让 dLLM 作为 drafter，但通过位置解耦来兼容 AR verifier 的 KV Cache。

**Idea 3: Beyond hard mask**

当前 dLLM 的 hard mask 机制丢弃了太多信息。[Beyond Hard Masks](https://arxiv.org/abs/2601.07351) 和 [Residual Context Diffusion](https://arxiv.org/abs/2601.22954) 都在探索 soft/progressive masking。

这与 speculative decoding 中"复用 large model hidden states"的思路一致——不要丢弃中间信息。

**Open question**

为什么早期的 multi-token prediction (MTP) 不 work，但 dLLM 可以？我的理解是：
- MTP 的问题：并行预测的 token 之间有联合分布问题，预测数量受限
- dLLM 的优势：训练方式更激进（随机 mask），推理时可以 defer 不确定的 token

但我还没有完全想清楚这个问题。

---

如果你有时间，我很想讨论这些想法。特别是：
1. dLLM 作为 speculative decoding 的 drafter 是否可行？
2. 如何设计实验来验证 "difficulty-aware" 的假设？

Best,
Ted

---

## 英文版

**Subject:** Research Thoughts: Bridging Diffusion LLMs and Speculative Decoding

Hi Greg,

I've been thinking deeply about the connection between diffusion language models (dLLMs) and speculative decoding. I'd like to share some preliminary ideas and relevant papers.

**Core Observation: Not All Tokens Are Equal**

A fundamental limitation of AR models is that even if the model "knows" the answer at the first layer, the architecture forces it to output one token at a time. This wastes significant computation. Both speculative decoding and dLLMs attempt to break this limitation, but in different ways:
- Speculative decoding: draft quickly with a small model, verify with a large model
- dLLM: directly predict multiple tokens in parallel

I believe these two directions can inform each other.

**Idea 1: dLLM as a Difficulty-Aware Predictor**

A unique advantage of dLLMs is that their confidence distribution naturally reflects token difficulty. For easy tokens, confidence is high and we can aggressively parallelize; for hard tokens, confidence is low and we may need an AR model to "anchor" them.

I want to run an experiment: for reasoning tasks, if we first provide the hardest part (e.g., the final answer), can dLLM generate the CoT much faster? This would test whether dLLMs can truly leverage "hard tokens already known" information.

Related: [Thinking Out of Order](https://arxiv.org/abs/2601.22035) analyzes how dLLM generation order relates to reasoning order.

**Idea 2: Decoupling Physical and Logical Positions**

The fundamental reason dLLMs struggle with KV Cache is the conflict between bidirectional attention and causality. [WeDLM](https://arxiv.org/abs/2512.22737) proposes an interesting solution: decouple physical and logical positions, reorder after prediction to ensure causality.

I'm wondering if this idea could enable dLLM as a drafter in speculative decoding—using position decoupling to be compatible with the AR verifier's KV Cache.

**Idea 3: Beyond Hard Masks**

Current dLLM hard masking discards too much information. [Beyond Hard Masks](https://arxiv.org/abs/2601.07351) and [Residual Context Diffusion](https://arxiv.org/abs/2601.22954) explore soft/progressive masking.

This aligns with the idea in speculative decoding of "reusing large model hidden states"—don't discard intermediate information.

**Open Question**

Why did early multi-token prediction (MTP) fail while dLLMs work? My current understanding:
- MTP's problem: joint distribution issues between parallel tokens, limited prediction count
- dLLM's advantage: more aggressive training (random masking), can defer uncertain tokens during inference

But I haven't fully figured this out yet.

---

I'd love to discuss these ideas if you have time. Specifically:
1. Is dLLM as a speculative decoding drafter feasible?
2. How should we design experiments to test the "difficulty-aware" hypothesis?

Best,
Ted

---

## 附：推荐论文列表

| 论文 | 核心贡献 | 为什么重要 |
|------|----------|------------|
| [WeDLM](https://arxiv.org/abs/2512.22737) | 解耦物理/逻辑位置 | 可能是 dLLM + speculative decoding 的关键 |
| [Beyond Hard Masks](https://arxiv.org/abs/2601.07351) | Soft/progressive masking | 保留更多信息 |
| [Thinking Out of Order](https://arxiv.org/abs/2601.22035) | dLLM 生成顺序分析 | 理解 dLLM 的 reasoning 机制 |
| [Residual Context Diffusion](https://arxiv.org/abs/2601.22954) | 残差上下文 | 另一种保留信息的方式 |
| [d3LLM](https://arxiv.org/abs/2601.07568) | 训推对齐 | 解决 train-inference mismatch |
