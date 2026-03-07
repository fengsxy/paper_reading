---
title: "2026-03-07-daily-papers"
---

# 2026-03-07 每日论文精选

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

### 4. Free Lunch for Pass@k? Low Cost Diverse Sampling for Diffusion Language Models
- **arXiv:** [2603.04893](https://arxiv.org/abs/2603.04893)
- **作者:** Sean Lamont et al.
- **核心问题:** 文本生成的多样性对于复杂推理任务（如代码生成、数学问题求解）中的有效探索至关重要。传统采样方法经常在重复失败模式上浪费计算资源。
- **解决方案:** 提出无需训练、低成本的干预方法，增强扩散语言模型的生成多样性。
- **实验结果:** 在 HumanEval 和 GSM8K 基准上使用 LLaDA-8B-Instruct 评估，方法在多种温度设置下显著提升多样性和 Pass@k 性能。
- **意义:** 为当前和未来扩散语言模型提供简单、低成本的改进，特别适用于受益于多样解搜索的任务。

### 5. Diffusion LLMs can think EoS-by-EoS
- **arXiv:** [2603.05197](https://arxiv.org/abs/2603.05197)
- **作者:** Zhengbo Luo et al.
- **核心发现:** 扩散 LLM 在需要相互依赖子目标的复杂推理任务上作为自回归 LLM 的替代方案表现出色。值得注意的是，如果生成长度设置为远大于正确答案所需的值，且模型用 EoS 令牌填充答案时，性能更好。
- **假设:** 扩散模型 EoS-by-EoS 思考，即它们使用 EoS 令牌的表示作为隐藏草稿纸，这使它们能解决更难的推理问题。
- **实验:** 在 LLaDA1.5、LLaDA2.0-mini 和 Dream-v0 上测试 Addition、Entity Tracking 和 Sudoku 任务。
- **意义:** 提供对扩散模型推理能力的新解释，暗示扩散模型可能利用 EoS 令牌作为内部推理空间。

### 6. Reasoning or Rationalization? The Role of Justifications in Masked Diffusion Models for Fact Verification
- **arXiv:** [2603.01190](https://arxiv.org/abs/2603.01190)
- **作者:** Jacob Devasier et al.
- **核心问题:** 与自回归模型不同，掩码扩散语言模型（MDLMs）同时细化所有序列位置，引发这些模型如何处理需要合理裁决的任务的问题。
- **发现:** MDLM 通常在扩散过程早期收敛于裁决，将其作为全局锚。关键的是，通过延迟裁决解掩码强制推理优先会主动损害性能（准确率从 86.2% 降至 71.9%）。干预实验揭示模型在 56% 的案例中对被迫的错误裁决进行合理化，且裁决强烈依赖于理由质量（理由损坏时 57.3% 准确率 vs. 完整理由时更高）。
- **意义:** 揭示扩散模型在事实验证任务中的推理机制，挑战"扩散模型需要显式推理链"的假设。

### 7. Generalized Discrete Diffusion with Self-Correction
- **arXiv:** [2603.02230](https://arxiv.org/abs/2603.02230)
- **作者:** Linxuan Wang et al. (Purdue, Google Research)
- **核心问题:** 自校正是在保持并行采样的同时最小化性能退化的有效技术。先前方法受限于有限的泛化能力，可能损害推理性能。
- **解决方案:** 提出自校正离散扩散（SCDD）模型，将预训练的自校正重新表述为具有显式状态转换的形式，直接在离散时间中学习，避免先前方法的连续插值管道问题。
- **意义:** 为离散扩散模型提供更通用的自校正框架，改善推理表现。

### 8. Diffusion-MPC in Discrete Domains: Feasibility Constraints, Horizon Effects, and Critic Alignment
- **arXiv:** [2603.02348](https://arxiv.org/abs/2603.02348)
- **作者:** Haochuan Kevin Wang (UT Austin)
- **应用领域:** 基于扩散的模型预测控制（Diffusion-MPC）在离散组合域（以 Tetris 为例）。
- **方法:** 使用 MaskGIT 风格的离散去噪器采样候选放置序列，通过重新排序选择动作。分析三个关键因素：可行性约束采样、重新排序策略、计算缩放。
- **发现:** 计算选择（K, H）决定主导失败模式：小 K 限制候选质量，大 H 放大错误排名和模型失配。
- **意义:** 提供扩散规划器在离散环境中结构挑战的诊断和实用指导。

## 信息论与表示学习

### 9. An Information-Theoretic Framework For Optimizing Experimental Design To Distinguish Probabilistic Neural Codes
- **arXiv:** [2603.01387](https://arxiv.org/abs/2603.01387)
- **作者:** Po-Chen Kuo et al.
- **研究背景:** 贝叶斯大脑假说是理解不确定性下感知决策的主流理论，但神经群体如何编码不确定性信息仍不清楚。
- **贡献:** 提出信息论框架，优化实验设计以区分概率神经编码（likelihood coding vs. posterior coding）。通过最大化信息差距，得到最优刺激分布，以最大判别力区分不同的概率编码假说。
- **意义:** 为神经科学实验设计提供原则性、理论驱动的方法，推进对神经群体如何表示和处理感知不确定性的理解。

### 10. Bi-TEAM: A Unified Cross-Scale Representation Learning Framework for Chemically Modified Biomolecules
- **arXiv:** [2603.01873](https://arxiv.org/abs/2603.01873)
- **作者:** Chunbin Gu et al. (北大等)
- **核心挑战:** 蛋白质语言模型擅长捕捉长程生物语义但缺失细粒度化学细节；化学语言模型编码原子信息但缺乏更广泛的序列上下文。
- **方法:** Bi-TEAM 统一生物语义和化学精度，提供跨尺度表示学习框架，用于化学修饰的生物分子（如肽和蛋白质）。
- **意义:** 为机器学习驱动的肽和蛋白质生化空间探索提供通用基础。

## 其他值得关注的研究

### 11. D3LM: A Discrete DNA Diffusion Language Model
- **arXiv:** [2603.01780](https://arxiv.org/abs/2603.01780)
- **作者:** Zhao Yang et al.
- **应用领域:** DNA 基础模型。早期 DNA 模型采用 BERT 风格训练（理解任务强但缺乏生成能力），自回归模型支持生成但左到右因果建模不适合 DNA 的双向调控关系。
- **方法:** D3LM 采用 Nucleotide Transformer v2 架构，但将训练目标重新表述为离散 DNA 空间中的掩码扩散，在单一模型中实现双向理解和生成能力。
- **结果:** 在调控元件生成任务上，D3LM 的 SFID 为 10.92，接近真实 DNA 序列（7.85），大幅优于自回归模型的 29.16。
- **意义:** 证明扩散语言模型是统一 DNA 基础模型的有前途范式。

### 12. Efficient Self-Evaluation for Diffusion Language Models via Sequence Regeneration
- **arXiv:** [2603.02760](https://arxiv.org/abs/2603.02760)
- **作者:** Linhao Zhong et al. (大疆、港中文等)
- **核心问题:** 扩散大语言模型（dLLMs）因其多样性、可控性和并行性能力而受关注。但其非顺序、双向掩码的生成方式使质量评估困难，突显有效自评估的需求。
- **方法:** 提出基于序列再生的高效自评估方法。
- **意义:** 为 dLLMs 提供实用的质量评估机制，推动扩散模型在实践中的应用。

---

## 今日观察

今日论文聚焦离散扩散语言模型的最新进展：

1. **记忆与推理机制**：MetaState 引入跨步持久化记忆，EoS-by-EoS 研究暗示扩散模型可能利用 EoS 令牌作为隐藏草稿纸，这些都指向扩散模型内部推理能力的探索。

2. **架构创新**：CoDAR 解决连续扩散的 token rounding 瓶颈，SCDD 改进自校正的泛化能力，代表 dLLM 架构持续优化。

3. **多样性、评估与可控性**：Free Lunch 提出低成本多样性采样方法；Self-Evaluation 为解决 dLLM 质量评估难题提供途径；Fact Verification 研究揭示扩散模型在推理任务中的独特行为。

4. **跨领域应用**：DNA 基础模型（D3LM）显示扩散范式的跨领域潜力；Diffusion-MPC 探索离散组合优化。

5. **可信 AI**：记忆化分析（Characterizing Memorization）为扩散模型的隐私和版权风险评估提供理论基础。

当前最活跃的研究方向包括：dLLM 的记忆机制、多样性采样、自我评估方法、以及扩散模型在更广泛任务类型中的应用探索。
