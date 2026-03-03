# 2026-03-03 每日论文精选

## 离散扩散语言模型

### 🔥 D3LM: A Discrete DNA Diffusion Language Model for Bidirectional DNA Understanding and Generation
**arXiv:2603.01780** | Zhao Yang et al.

早期 DNA 基础模型采用 BERT 风格训练，在理解任务上表现良好但缺乏生成能力。最近的自回归模型虽然能生成 DNA，但采用从左到右的因果建模，不适合 DNA 中固有的双向调控关系。

D3LM 通过 masked diffusion 统一了双向表示学习和 DNA 生成。直接采用 Nucleotide Transformer (NT) v2 架构，但将训练目标重新表述为离散 DNA 空间中的 masked diffusion，使单个模型同时具备双向理解和生成能力。

**关键结果：** 在调控元件生成任务上，D3LM 达到 SFID 10.92，接近真实 DNA 序列（7.85），大幅优于自回归模型的 29.16。这项工作表明扩散语言模型是统一 DNA 基础模型的有前景范式。

**相关性：** 离散扩散在生物序列建模中的应用，双向建模 vs 自回归的权衡。

---

### MetaState: Persistent Working Memory for Discrete Diffusion Language Models
**arXiv:2603.01331** | Kejing Xia et al. (Georgia Tech)

离散扩散语言模型（dLLMs）通过迭代去噪生成文本。与自回归模型相比，这种范式天然支持并行解码、双向上下文和灵活的生成模式。但标准 dLLMs 每个去噪步骤只依赖当前的硬掩码序列，中间连续表示在采样和重新掩码后被丢弃。

**MetaState** 引入持久的跨步工作记忆，保留和传播中间连续状态。在 LLaDA-8B 和 Dream-7B 上，MetaState 引入可忽略的可训练参数（保持主干冻结），持续改进准确率。

**意义：** 持久跨步记忆是连接去噪步骤、提高离散扩散语言模型生成质量的有效机制。

---

### Reasoning or Rationalization? The Role of Justifications in Masked Diffusion Models
**arXiv:2603.01190** | Jacob Devasier

与顺序生成 token 的自回归模型不同，Masked Diffusion Language Models (MDLMs) 同时细化所有序列位置，这引发了关于这些模型如何处理需要推理的任务的问题。

**关键发现：** MDLMs 通常在扩散过程早期就收敛到判断结果，将其作为全局锚点，在理由完成之前就已解决。强制推理优先（通过延迟判断解掩码）反而会降低性能，准确率从 86.2% 降至 71.9%，因为累积的理由 tokens 引入不一致性，覆盖了最初正确的预测。

干预实验表明，模型在 56% 的情况下会为错误的强制判断进行合理化，判断强烈依赖于理由质量（损坏理由时准确率 57.3%）。

**启示：** 扩散模型的并行细化特性可能不适合严格的推理链，更倾向于"合理化"而非"推理"。

---

## 表示学习与信息论

### Energy-Efficient Information Representation in MNIST Classification Using Biologically Inspired Learning
**arXiv:2603.00588** | Patrick Stricker et al.

高效的表示学习对于最优信息存储和分类至关重要，但在人工神经网络中经常被忽视。这种忽视导致网络过度参数化（最多 13 倍），增加冗余和能耗。

本文采用生物启发的学习方法，消除了网络架构预优化的需求，增强了适应性，反映了大脑为新记忆"预留空间"的能力。这种方法推进了可扩展和节能的 AI，为开发优化资源分配和适应性的类脑模型提供了有前景的框架。

**相关性：** 信息论视角下的表示学习效率，生物启发的神经网络设计。

---

### An Information-Theoretic Framework For Optimizing Experimental Design To Distinguish Probabilistic Neural Codes
**arXiv:2603.01387** | Po-Chen Kuo et al.

贝叶斯大脑假说一直是理解不确定性下感知决策的主导理论。虽然大量心理物理学证据支持大脑执行贝叶斯计算的观点，但感觉神经群体如何编码不确定性信息仍然难以捉摸。

本文提出信息论框架，通过最大化信息差距来优化实验设计，以区分似然编码和后验编码假说。这使得能够进行原则性的、理论驱动的实验设计，具有最大的判别能力来区分概率神经编码，推进我们对神经群体如何表示和处理感觉不确定性的理解。

**相关性：** 信息论在神经科学中的应用，概率编码的实验验证。

---

### Bi-TEAM: A Unified Cross-Scale Representation Learning Framework for Chemically Modified Biomolecules
**arXiv:2603.01873** | Chunbin Gu et al.

蛋白质生化空间的表示学习面临困难的权衡：蛋白质语言模型擅长捕获长程生物语义，但常常错过细粒度化学细节。相反，化学语言模型编码原子信息但缺乏更广泛的序列上下文。

Bi-TEAM 通过统一生物语义和化学精度，为机器学习驱动的肽和蛋白质生化空间探索提供了多功能基础。

**意义：** 跨尺度表示学习，生物序列和化学结构的联合建模。

---

## 其他

### DeepAFL: Deep Analytic Federated Learning
**arXiv:2603.00579** | Jianheng Tang et al.

联邦学习（FL）是打破数据孤岛的流行分布式学习范式。传统 FL 方法主要依赖基于梯度的更新，面临异质性、可扩展性、收敛性和开销等重大问题。

受 ResNet 在基于梯度学习中的巨大成功启发，本文在 DeepAFL 中设计了具有解析解的无梯度残差块。引入高效的逐层协议，通过最小二乘在 FL 中逐层训练深度解析模型。

**性能：** 在三个基准数据集上优于 SOTA 基线 5.68%-8.42%，具有异质性不变性和表示学习的双重优势。

**相关性：** 解析学习 vs 梯度学习，联邦学习中的表示学习。
