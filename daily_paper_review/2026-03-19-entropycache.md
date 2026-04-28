# Daily Paper Review — 2026-03-19

**Paper**: EntropyCache: Decoded Token Entropy Guided KV Caching for Diffusion Language Models
**arXiv ID**: 2603.18489v1
**Date**: 2026-03-19
**Tag**: dLLM / KV Cache / Efficiency

---

## 1. Task

**问题形式化**：

Diffusion-based LLMs（dLLMs）依赖 bidirectional attention，无法像 AR 模型那样使用 lossless KV caching——每个 denoising step 都需要完整的 forward pass。

现有 approximate KV caching 方法通过选择性更新 cached states 来降低成本，但它们的 decision overhead 随 context length 或 model depth 增加。

**目标**：提出 EntropyCache——一种 training-free 的 KV caching 方法，用 decoded token entropy 作为决策信号。

---

## 2. Challenge

| 方法 | 困境 |
|------|------|
| Full forward pass each step | O(N) KV recomputation，无法利用 cache |
| 现有 approximate KV caching | Decision overhead 随 context length 增加 |
| Static KV cache | 对低熵和高熵 token 一刀切，无法区分 |

---

## 3. Insight & Novelty

**核心洞察**：Decoded token entropy 是一个 proxy——它衡量"这个 token 在当前 step 是否可能再改变"。

> 关键发现：当 token 的预测 entropy 很低时，这个 token 的 KV representations 在后续 steps 中几乎不会改变。
>
> 这意味着：低 entropy token 的 KV 可以安全地 cache 起来，无需在每个 step 重新计算。

**创新点 1**：Entropy-guided KV cache decision
- **解决的问题**：如何决定哪些 token 的 KV 应该 cache
- **受启发于**：Decoded token entropy → 直接衡量"稳定性"
- **具体设计**：当 token 的 entropy 低于阈值时，标记为 stable，cache 其 KV

**创新点 2**：Training-free + low overhead
- **解决的问题**：现有方法 decision overhead 太高
- **受启发于**：Entropy 计算本身就来自 model 的预测，不需要额外模型
- **具体设计**：只需在 forward pass 时计算 token entropy，entropy 低的 token cache 其 KV

**创新点 3**：与 LoSA（2026-03-13）形成对比
- **解决的问题**：LoSA 用"stable token 的 KV reuse"，EntropyCache 用 entropy 作为信号
- **具体设计**：两者机制类似（都是利用 token stability），但 signal 不同（LoSA 用 drift，EntropyCache 用 entropy）

---

## 4. Potential Flaw

### 4.1 情境局限

- **Entropy threshold 的选择**：不同模型、任务可能需要不同的阈值
- **极低 entropy 的假阳性**：某些 token 可能在某个 step entropy 低，但在后续 step 又变化（不稳定的低 entropy）

### 4.2 数据问题

- **不同任务的 entropy 分布不同**：Reasoning 任务的高熵 token 可能比 generation 任务更多
- **与其他 cache 策略的组合**：EntropyCache 与其他 KV caching 方法（如 sparse attention）的组合效果未知

### 4.3 值得挖掘的方向

**最值得做的**：EntropyCache × VSB 的联合设计。

> VSB 判断"哪些 token 已经 self-contained（不再需要条件于噪声）"
> EntropyCache 判断"哪些 token 的 KV 稳定，可以 cache"
>
> 两者结合：VSB commit 的 token 很可能 entropy 也低，但不完全一致——某些 token 虽然还不是 self-contained，但 entropy 已经很低（这些 token 适合 EntropyCache 但不适合 VSB commit）。

---

## 5. Motivation

**General idea 推导路径**（第一性原理）：

> KV cache 在 AR 模型中 work，因为 AR 的 token 是 sequential 生成的——一旦某个 token 被生成，它的 KV 在后续 step 中不会改变（因为它是 causal attention，不会看到未来的 token）。
>
> 但 dLLM 不同——每个 denoising step 都重新处理整个序列，因为 bidirectional attention 让每个 token 都条件于所有其他 token。
>
> **那问题变成：哪些 token 的 KV 在 denoising 过程中真的改变了？**
>
> 答案是：那些还在"变化"的 token。
>
> "还在变化"的衡量标准：entropy。当模型对某个 token 的预测 high entropy 时，意味着这个 token 的表示还不稳定，下一个 step 可能会改变。反之，当 entropy 低时，token 的表示已经稳定，不需要重新计算。
>
> EntropyCache 就是利用这个 insight——只对 high entropy 的 token 做 full forward pass，对 low entropy 的 token cache 起来。