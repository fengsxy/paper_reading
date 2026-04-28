# Daily Paper Review — 2026-04-04

**Paper**: Unlocking Prompt Infilling Capability for Diffusion Language Models
**arXiv ID**: 2604.03677v1
**Date**: 2026-04-04
**Tag**: dLLM / Prompt Infilling / Training

---

## 1. Task

**问题形式化**：

Masked Diffusion Language Model（dLM）通过 bidirectional denoising 生成文本，但**这个能力在 infilling prompts 时被锁住了**。

论文认为这不是 architecture 的限制，而是 **SFT（Supervised Fine-Tuning）的 convention 问题**——当前 SFT 只对 response 做 masking，不对 prompt 做 masking。

结果：模型学会了"给定 prompt，生成完整 response"，但没有学会"给定 partial prompt+response，填充中间部分"。

---

## 2. Challenge

| 方法 | 困境 |
|------|------|
| Response-only masking | 模型没有学过 infilling，prompt+response 的联合 masking 场景从未训练 |
| Architecture change | 认为这是 architectural limitation，需要改变模型结构 |
| 在 prompt 上加噪声 | 没有从 training 层面解决问题 |

**根本问题**：这是一个 training problem，不是 architecture problem。

---

## 3. Insight & Novelty

### 3.1 Insight

**核心发现**：当前 SFT 的 masking convention 是人为的 artifact。

> Masked dLM 的 architecture 天然支持 prompt infilling——bidirectional attention 可以同时看到 prompt 和 response，masking mechanism 可以只 mask 中间部分。
>
> 但训练时从未这样用过——所以模型没有这个能力。
>
> 这意味着：**我们只需要改变训练方式，不需要改变架构。**

**关键发现**：Full-sequence masking 在 SFT 时同时 mask prompt 和 response jointedly，可以让模型解锁 infilling 能力——且学到的 infilling template 可以迁移到不同模型。

### 3.2 Novelty

**创新点 1**：Full-sequence masking during SFT
- **解决的问题**：如何让模型学会 infilling
- **受启发于**：prompt infilling 的能力未被训练 → 提出 joint prompt+response masking
- **具体设计**：在 SFT 时同时 mask prompt 和 response，模型学会基于 few-shot examples 填充 masked 部分

**创新点 2**：Model-infilled prompts 的效果
- **解决的问题**：模型自设计的 infilling template 是否有效
- **受启发于**：模型有能力但没有被引导
- **具体设计**：一旦解锁，模型自动生成的 infilling template 可以 match 或超越手工设计的 template

**创新点 3**：Cross-model transferability
- **解决的问题**：学到的 infilling 能力是否可以迁移
- **受启发于**：masking 的通用性
- **具体设计**：在一个模型上训练的 infilling skill 可以迁移到其他 dLM 模型

---

## 4. Potential Flaw

### 4.1 情境局限

- **Masked dLM only**：Block-wise dLLM 的 infilling 能力是否同样受限，未测试
- **Short prompts**：对极短 prompt 的 infilling 可能不需要 joint masking
- **不同 infilling 类型**：本文主要验证"中间段落填充"，"头部填充"和"尾部填充"可能需要不同处理

### 4.2 数据问题

- **需要 infilling-style 的训练数据**：现有的 SFT 数据集大多是对话/续写格式，不是 infilling 格式
- **Few-shot example 的选择**：infilling 效果依赖 few-shot examples 的质量

### 4.3 值得挖掘的方向

**最值得做的**：Block-wise dLLM 的 infilling 能力。

> Masked dLM 的 infilling 能力被 response-only masking 锁住了，block-wise dLLM 呢？
>
> 如果 block-wise dLLM 也有类似的 training artifact 问题，那用 full-sequence masking 的方法可能也能解锁 block-wise 的 infilling 能力。
>
> 这对于 code editing 和 structured editing 任务特别有价值。

---

## 5. Motivation

**General idea 推导路径**（第一性原理）：

> Masked dLM 的训练目标是：给定 masked sequence，恢复出完整 clean sequence。
>
> 但现有的 SFT 训练只 mask response，不 mask prompt。这意味着：
>
> 模型学到的是"P -> R"（prompt 到完整 response），而不是"P + R -> gap"（prompt + partial response 填充 gap）。
>
> **这是一个 training distribution 的问题，不是模型能力的问题。**
>
> 就像一个学生从来没练过"完形填空"，只练过"阅读理解"，考试时自然不会完形填空。
>
> 解法：让学生练习完形填空——在训练时 joint mask prompt 和 response，让模型学会在已知部分内容的情况下推断中间内容。
