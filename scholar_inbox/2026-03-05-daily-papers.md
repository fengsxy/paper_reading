# 2026-03-05 每日论文精选

## 离散扩散语言模型（Discrete Diffusion Language Models）

### 1. MetaState: Persistent Working Memory for Discrete Diffusion Language Models
- **arXiv:** [2603.01331](https://arxiv.org/abs/2603.01331)
- **作者:** Kejing Xia et al. (Georgia Tech, UMass Amherst, Harvard)
- **核心创新:** 提出 MetaState 机制，为离散扩散语言模型（dLLMs）引入跨步持久化工作记忆。标准 dLLMs 在每个去噪步骤后会丢弃中间连续表示，MetaState 保留这些表示作为"记忆"，桥接不同去噪步骤。
- **实验结果:** 在 LLaDA-8B 和 Dream-7B 上，MetaState 引入的可训练参数极少（保持主干冻结），但持续提升生成质量。
- **意义:** 证明持久化跨步记忆是改进离散扩散语言模型生成质量的有效机制。

### 2. CoDAR: Continuous Diffusion Language Models are More Powerful Than You Think
- **arXiv:** [2603.02547](https://arxiv.org/abs/2603.02547)
- **作者:** Junzhe Shen et al.
- **核心问题:** 连续扩散语言模型（Continuous DLMs）一直落后于离散扩散方法。通过受控的 token 恢复实验，发现 **token rounding**（从去噪嵌入到 token 的最终投影）是主要瓶颈。
- **解决方案:** 提出 CoDAR 框架，保持扩散过程完全在嵌入空间连续进行，同时学习一个强大的上下文条件离散化器：自回归 Transformer 解码器，通过交叉注意力机制对去噪嵌入序列进行上下文化的 token 舍入。
- **意义:** 为连续扩散语言模型提供新的架构思路，突破性能瓶颈。

### 3. Characterizing Memorization in Diffusion Language Models
- **arXiv:** [2603.02333](https://arxiv.org/abs/2603.02333)
- **作者:** Xiaoyu Luo et al.
- **研究问题:** 自回归语言模型的记忆化（memorization）问题已被广泛研究，但扩散语言模型的记忆化行为因生成动态的根本差异而未被充分探索。
- **贡献:** 提出统一的概率提取框架，将前缀条件解码和基于扩散的生成统一在任意掩码模式和随机采样轨迹下，系统性地理论和实证刻画 DLMs 的记忆化行为。
- **意义:** 填补扩散模型隐私和版权风险评估的空白，为可信 AI 提供理论基础。

### 4. D3LM: A Discrete DNA Diffusion Language Model
- **arXiv:** [2603.01780](https://arxiv.org/abs/2603.01780)
- **作者:** Zhao Yang et al.
- **应用领域:** DNA 基础模型。早期 DNA 模型采用 BERT 风格训练（理解任务强但缺乏生成能力），自回归模型支持生成但左到右因果建模不适合 DNA 的双向调控关系。
- **方法:** D3LM 采用 Nucleotide Transformer v2 架构，但将训练目标重新表述为离散 DNA 空间中的掩码扩散，在单一模型中实现双向理解和生成能力。
- **结果:** 在调控元件生成任务上，D3LM 的 SFID 为 10.92，接近真实 DNA 序列（7.85），大幅优于自回归模型的 29.16。
- **意义:** 证明扩散语言模型是统一 DNA 基础模型的有前景范式。

## 信息论与表示学习

### 5. An Information-Theoretic Framework For Optimizing Experimental Design
- **arXiv:** [2603.01387](https://arxiv.org/abs/2603.01387)
- **作者:** Po-Chen Kuo et al.
- **研究背景:** 贝叶斯大脑假说是理解不确定性下感知决策的主流理论，但神经群体如何编码不确定性信息仍不清楚。
- **贡献:** 提出信息论框架，优化实验设计以区分概率神经编码（likelihood coding vs. posterior coding）。通过最大化信息差距，得到最优刺激分布，以最大判别力区分不同的概率编码假说。
- **意义:** 为神经科学实验设计提供原则性、理论驱动的方法，推进对神经群体如何表示和处理感知不确定性的理解。

### 6. Energy-Efficient Information Representation in MNIST Classification
- **arXiv:** [2603.00588](https://arxiv.org/abs/2603.00588)
- **作者:** Patrick Stricker et al.
- **核心问题:** 人工神经网络常忽视高效表示学习，导致过参数化（最多 13 倍），增加冗余和能耗。
- **方法:** 采用生物启发的学习方法，优化信息存储和分类的效率。
- **意义:** 推进可扩展、节能的 AI，提供类脑模型框架，优化资源分配和适应性。大脑能为新记忆"预留空间"，这种机制值得 AI 借鉴。

## 其他值得关注

### 7. Bi-TEAM: Unified Cross-Scale Representation Learning for Chemically Modified Biomolecules
- **arXiv:** [2603.01873](https://arxiv.org/abs/2603.01873)
- **核心挑战:** 蛋白质语言模型擅长捕捉长程生物语义但缺失细粒度化学细节；化学语言模型编码原子信息但缺乏更广泛的序列上下文。
- **方法:** Bi-TEAM 统一生物语义和化学精度，提供跨尺度表示学习框架，用于化学修饰的生物分子（如肽和蛋白质）。
- **意义:** 为机器学习驱动的肽和蛋白质生化空间探索提供通用基础。
