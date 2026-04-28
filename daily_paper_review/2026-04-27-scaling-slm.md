# Daily Paper Review — 2026-04-27

**Paper**: Scaling Properties of Continuous Diffusion Spoken Language Models
**arXiv ID**: 2604.24416v1
**Date**: 2026-04-27
**Tag**: Continuous Diffusion / Speech / Scaling Laws

---

## 1. Task

**问题形式化**：

Speech-only Spoken Language Models（SLM）与 text-based 模型在性能上存在显著差距。离散 AR SLM 需要大量计算资源和数据才能匹配 text 模型性能。

核心瓶颈：**离散化本身**（discretizing continuous speech）会引入信息瓶颈，阻碍 AR 模型在 speech 上的表现。

论文探索：**Continuous Diffusion（CD）SLM 是否更可行？**

同时引入 **pJSD（phoneme Jensen-Shannon divergence）** 作为 SLM 语言质量的量化指标。

---

## 2. Challenge

| 方法 | 困境 |
|------|------|
| Discrete AR SLM | 离散化引入瓶颈，需要极大规模数据和计算才能匹配 text 模型 |
| Text-speech 混合模型 | 依赖 text 模态，丢失纯 speech 的优势 |
| 直接将 continuous speech 用于 AR | speech 的连续性和 AR 的离散 token 天然不匹配 |

**根本问题**：离散化 speech 的表示是否必要？continuous diffusion 是否能更好地保留 speech 的连续信息？

---

## 3. Insight & Novelty

### 3.1 Insight

**核心发现（scaling law）**：

> CD SLM 与 AR SLM 一样，validation loss 和 pJSD 都表现出 scaling law——模型变大、计算变多，性能单调提升。

**关键发现**：

> 随着计算规模增大，**optimal token-to-parameter ratio 下降**——这意味着 larger model 可以用相对更少的 tokens 达到最优性能。
>
> 但 loss 对数据和模型大小的选择变得不敏感（insensitive）——这暗示了 **fast inference 的潜力**：可以用更少的 token 生成达到接近最优的性能。

**与 H/S 假说的潜在关联**：

> 如果 coarse semantic 先收敛（对应 H/S 假说的 S 阶段），那 CD SLM 的 scaling law 可能也存在类似的两阶段收敛：low-level acoustic features 先稳定（S），high-level semantic content 后锁定（H）。

### 3.2 Novelty

**创新点 1**：提出 pJSD（phoneme JSD）作为 speech 语言质量的专用指标
- **解决的问题**：如何量化 SLM 的语言质量
- **受启发于**：speech 的离散 phoneme 结构 → 用 Jensen-Shannon divergence 衡量 phoneme 分布的预测质量
- **具体设计**：在 phoneme 级别计算预测分布与真实分布的 JSD

**创新点 2**：CD SLM 的 scaling law 实证
- **解决的问题**：CD SLM 是否随规模表现出可预测的性能提升
- **受启发于**：AR 和 text 模型有 scaling law → CD SLM 是否也有
- **具体设计**：在 16B 参数、tens of millions of hours 的对话数据上验证 scaling behavior

**创新点 3**：发现 token-to-parameter ratio 随规模下降
- **解决的问题**：如何高效部署 large CD SLM
- **受启发于**：loss 对数据/模型大小变得不敏感 → 可以用更少 tokens 快速推理
- **具体设计**：验证不同规模下的 optimal token-to-parameter ratio

---

## 4. Potential Flaw

### 4.1 情境局限

- **Speech-only**：未探索与 text 的联合建模
- **Long-form coherence 仍是挑战**：虽然能生成 emotive、prosodic、multi-speaker speech，但长文本一致性未解决
- **仅验证了 scaling law，未深入机制解释**

### 4.2 数据问题

- **数据质量敏感性**：scaling law 依赖数据质量，低质量 speech data 可能破坏 optimal ratio
- **多语言场景**：不同语言的 phoneme 分布差异大，pJSD 的通用性未充分验证

### 4.3 值得挖掘的方向

**最值得做的**：CD SLM 的 denoising trajectory 分析——既然 CD SLM 也有明确的去噪过程，那 temporal emergence（2604.23235）的方法是否可以直接迁移到 speech domain？如果 acoustic features 的收敛和 semantic content 的收敛也遵循类似的粗细分离规律，这对 speech synthesis 的 early-exit 推理有直接价值。

---

## 5. Motivation

**General idea 推导路径**（第一性原理）：

> Speech 是 continuous signal。AR 模型是 discrete by nature。
>
> 把 continuous speech 离散化为 discrete tokens，本身就是在人为降维——必然丢失信息。
>
> **那为什么要离散化？**
>
> 因为 AR 模型需要 discrete tokens 作为输入。这是 AR 模型 architecture 的限制，不是 speech 本身的性质。
>
> **如果用 continuous diffusion 呢？**
>
> Continuous diffusion 可以在 continuous space 中去噪，不需要离散化 speech。
>
> 那关键是：这样做能保留更多 speech 的原始信息吗？scaling law 还成立吗？
>
> 论文证明了：**是的，scaling law 成立，且 optimal token-to-parameter ratio 随规模下降**——这暗示了 CD SLM 在 efficient inference 上的潜力。
