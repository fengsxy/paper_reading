# 2026-03-04 每日论文精选

## 扩散语言模型 (Diffusion Language Models)

### 1. Characterizing Memorization in Diffusion Language Models
**arXiv:** [2603.02333](https://arxiv.org/abs/2603.02333)  
**关键词:** Diffusion Language Models, Memorization, Privacy

**摘要：** 自回归语言模型（ARM）会记忆并逐字复现训练数据，引发隐私和版权问题。扩散语言模型（DLM）作为新兴替代方案，其记忆行为因生成动态的根本差异而未被充分研究。本文提出了一个广义概率提取框架，统一了前缀条件解码和基于扩散的生成，适用于任意掩码模式和随机采样轨迹。研究系统性地刻画了 DLM 中的记忆现象，为可信 AI 提供理论基础。

**意义：** 首次系统研究 DLM 的记忆行为，对隐私保护和可信生成模型有重要意义。

---

### 2. MetaState: Persistent Working Memory for Discrete Diffusion Language Models
**arXiv:** [2603.01331](https://arxiv.org/abs/2603.01331)  
**关键词:** Discrete Diffusion, Working Memory, dLLM

**摘要：** 离散扩散语言模型（dLLM）通过迭代去噪生成文本，支持并行解码和双向上下文。但标准 dLLM 每步仅依赖当前硬掩码序列，中间连续表示在采样和重新掩码后被丢弃。本文提出 **MetaState**，引入持久化跨步工作记忆机制，在保持主干冻结的情况下，仅增加极少可训练参数，在 LLaDA-8B 和 Dream-7B 上持续提升准确率。

**意义：** 为 dLLM 引入跨步记忆机制，改善生成质量，参数效率高。

---

### 3. CoDAR: Continuous Diffusion Language Models are More Powerful Than You Think
**arXiv:** [2603.02547](https://arxiv.org/abs/2603.02547)  
**关键词:** Continuous Diffusion, Token Rounding, Autoregressive Decoder

**摘要：** 连续扩散语言模型（DLM）尽管具有吸引力的连续生成动态，但性能落后于离散扩散方法。本文通过受控 token 恢复研究，识别出 **token rounding**（从去噪嵌入到 token 的最终投影）是主要瓶颈。提出 **CoDAR** 框架，保持扩散过程完全在嵌入空间连续进行，同时学习强大的上下文条件离散化器：一个自回归 Transformer 解码器，交叉注意去噪嵌入序列并执行上下文化的 token 舍入。

**意义：** 解决连续 DLM 的关键瓶颈，提出两阶段框架显著提升性能。

---

### 4. Reasoning or Rationalization? The Role of Justifications in Masked Diffusion Models
**arXiv:** [2603.01190](https://arxiv.org/abs/2603.01190)  
**关键词:** Masked Diffusion, Reasoning, Fact Verification

**摘要：** 与顺序生成的自回归模型不同，掩码扩散语言模型（MDLM）同时细化所有序列位置，引发对这些模型如何处理需要论证的任务的疑问。研究发现 MDLM 通常在扩散过程早期就收敛到判决（verdict），将其作为全局锚点，在论证完成前就已解决。强制推理优先约束（通过延迟判决解掩）实际上会降低性能，准确率从 86.2% 降至 71.9%，因为累积的论证 token 引入不一致性，覆盖了最初正确的预测。干预实验显示模型在 56% 的情况下会为错误的强制判决进行合理化。

**意义：** 揭示 MDLM 的推理机制与自回归模型根本不同，对可信 AI 和可解释性有重要启示。

---

## 表示学习与信息论

### 5. An Information-Theoretic Framework For Optimizing Experimental Design
**arXiv:** [2603.01387](https://arxiv.org/abs/2603.01387)  
**关键词:** Information Theory, Neural Coding, Bayesian Brain

**摘要：** 贝叶斯大脑假说是理解不确定性下感知决策的主导理论。尽管大量心理物理学证据支持大脑执行贝叶斯计算，但感觉神经群体如何编码不确定性信息仍不清楚。本文提出信息论框架，优化实验设计以区分概率神经编码假设（似然编码 vs 后验编码）。最大化信息差距可产生最优区分两种编码假设的刺激分布。

**意义：** 为神经科学实验设计提供信息论工具，推进对神经群体表示不确定性的理解。

---

### 6. Concept Heterogeneity-aware Representation Steering
**arXiv:** [2603.02237](https://arxiv.org/abs/2603.02237)  
**关键词:** Representation Steering, LLM Control, Concept Heterogeneity

**摘要：** 表示引导（representation steering）为在推理时通过干预内部激活来控制大型语言模型行为提供了轻量级机制。现有方法依赖单一全局引导方向，通常通过对比数据集的均值差获得。本文提出 **概念异质性感知表示引导**，考虑概念内部的多样性，提升控制精度和鲁棒性。

**意义：** 改进 LLM 可控性方法，考虑概念的内在异质性。

---

### 7. D3LM: A Discrete DNA Diffusion Language Model
**arXiv:** [2603.01780](https://arxiv.org/abs/2603.01780)  
**关键词:** DNA Foundation Model, Discrete Diffusion, Bidirectional Generation

**摘要：** 早期 DNA 基础模型采用 BERT 风格训练，在 DNA 理解任务上表现良好但缺乏生成能力。最近的自回归模型支持 DNA 生成，但采用从左到右的因果建模，对于调控关系本质上是双向的 DNA 来说并不理想。本文提出 **D3LM**（离散 DNA 扩散语言模型），通过离散 DNA 空间中的掩码扩散统一双向表示学习和 DNA 生成。在调控元件生成任务上，D3LM 达到 SFID 10.92，接近真实 DNA 序列（7.85），大幅优于自回归模型的 29.16。

**意义：** 扩散模型在生物序列建模中的成功应用，展示了统一理解和生成的潜力。

---

## 总结

本日论文聚焦于 **扩散语言模型的新进展**，特别是：
1. **可信性研究**：记忆行为、推理 vs 合理化
2. **架构创新**：持久化工作记忆、连续-离散混合框架
3. **跨领域应用**：DNA 序列生成
4. **表示学习**：信息论框架、概念异质性感知引导

扩散模型正在从图像生成向语言和生物序列建模扩展，同时研究者开始关注其可信性和可解释性问题。
