# Daily Paper Review — 2026-04-06

**Paper**: DualDiffusion: A Speculative Decoding Strategy for Masked Diffusion Models
**arXiv ID**: 2604.05250v1
**Date**: 2026-04-06
**Tag**: dLLM / Speculative Decoding / Efficiency

---

## 1. Task

**问题形式化**：

Masked Diffusion Models（MDM）提供并行生成和双向注意力的优势，但推理速度受限于 **O(N^2) 计算量**（无法 cache KV pairs）和 **多步迭代**。

Speculative decoding 是一种加速方案：用 lightweight drafter 提出多个 token，target model 并行验证。但现有方法在 drafter 质量上有局限。

**目标**：结合 fast drafter（高效近似）和 slow verifier（精确），用少量 drafter steps + 1 个 verifier step 实现最优的 quality/efficiency trade-off。

---

## 2. Challenge

| 方法 | 困境 |
|------|------|
| FastDLLM / DkvCache | 加速但牺牲生成质量 |
| 单独使用 drafter | drafter 质量不够，end-to-end 质量下降 |
| 单独使用 verifier | 无加速 |

---

## 3. Insight & Novelty

**核心洞察**：Drafter 和 verifier 可以分别利用不同的近似优势。

> Drafter 的任务：生成多个候选，不需要每个都对
> Verifier 的任务：验证 drafter 的输出，确保质量
>
> 这种分离允许 drafter 用高效近似，verifier 用精确计算。

**创新点 1**：Drafter 的 multiple steps + Verifier 的 single step
- **解决的问题**：如何平衡 drafter 质量和 verifier 开销
- **具体设计**：运行 drafter 多个 steps（轻量近似），然后一个 verifier forward pass 验证所有输出

**创新点 2**：Draft tree 的树结构
- **解决的问题**：如何利用 drafter 的 per-position distributions
- **具体设计**：从 drafter 的每个位置分布构建 draft tree，用 best-first heap 选择最可能的 continuation

**创新点 3**：Ancestor-only attention mask
- **解决的问题**：如何高效验证 tree 结构
- **具体设计**：用一个 ancestor-only attention mask 在单次 forward pass 中验证整个 tree

---

## 4. Potential Flaw

- **Drafter 和 verifier 的选择**：需要分别训练两个模型，增加复杂度
- **与 VSB/AHD 等方法的结合未探索**：解码策略的联合优化可能带来更大收益
- **不同任务的加速比差异大**：MMLU 和 GSM8K 上的加速比可能不代表通用场景

---

## 5. Motivation

**General idea**：Speculative decoding 的本质是"用快但不太准的模型生成候选，用准但慢的模型验证"。这个思想在 AR 模型上已经 work 了，在 dLLM 上的关键是：如何让 drafter 也利用 dLLM 的 parallel generation 结构，而不是变成 AR 的 sequential draft。
