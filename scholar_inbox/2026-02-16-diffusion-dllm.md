# Scholar Inbox 精选 - 2026-02-16

## Diffusion / dLLM / Information Theory 相关高分论文

---

### 1. Continuous Diffusion Models Can Obey Formal Syntax
**Authors:** Jinwoo Kim, Taylor Berg-Kirkpatrick, Loris D'Antoni  
**Score:** 0.986  
**ArXiv:** [2602.12468](https://arxiv.org/abs/2602.12468)

**摘要：** 提出了一种无需训练的引导方法，使连续扩散语言模型能够满足用正则表达式表达的形式语法约束。通过构建分析性得分来估计潜在状态解码为给定正则表达式接受的有效字符串的概率，并使用其梯度来引导采样。在 PLAID 扩散模型上实现的 Diffinity 系统在 180 个正则表达式约束上达到 68-96% 的约束满足率，同时保持较低的困惑度代价。

**亮点：** 首次实现连续扩散语言模型的形式语法约束，对 JSON schema 等结构化输出生成有重要意义。

---

### 2. dVoting: Fast Voting for Diffusion Language Models
**Authors:** Shucheng Fang et al.  
**Score:** 0.979  
**ArXiv:** [2602.12153](https://arxiv.org/abs/2602.12153)  
**Code:** https://github.com/fscdc/dVoting

**摘要：** 提出 dVoting，一种无需训练的快速投票技术，利用 dLLM 的任意位置生成能力进行迭代优化。通过一致性分析识别不确定 token 并重新生成。在 GSM8K 上提升 6.22%-7.66%，MATH500 上提升 4.40%-7.20%，ARC-C 上提升 3.16%-14.84%。

**亮点：** 利用 dLLM 并行生成特性实现高效的 test-time scaling，开辟了 dLLM 推理增强的新方向。

---

### 3. Discrete Copula Diffusion
**Authors:** Anji Liu, Guy Van den Broeck  
**Score:** 0.970  
**ArXiv:** [2602.12924](https://arxiv.org/abs/2602.12924)

**摘要：** 提出离散 Copula 扩散模型，将联合分布分解为边缘分布和 copula 分布。通过分别建模边缘和依赖结构，实现更灵活的离散数据生成。在图像和文本生成任务上展示了优越性能。

**亮点：** 将 copula 理论引入离散扩散，为理解和改进离散扩散模型提供了新的理论视角。

---

### 4. Masked Diffusion Models are Secret Reasoners
**Authors:** Jiawei Liu et al.  
**Score:** 0.963  
**ArXiv:** [2602.12566](https://arxiv.org/abs/2602.12566)

**摘要：** 揭示了 masked diffusion language models (MDLMs) 的隐藏推理能力。通过分析发现 MDLMs 在去噪过程中隐式执行多步推理，并提出方法显式激活这种能力，在数学推理任务上取得显著提升。

**亮点：** 首次系统研究 MDLM 的推理机制，为 dLLM 的可解释性和能力提升提供了重要洞见。

---

### 5. Simple Guidance Mechanisms for Discrete Diffusion Models
**Authors:** Yair Schiff et al.  
**Score:** 0.958  
**ArXiv:** [2602.12634](https://arxiv.org/abs/2602.12634)

**摘要：** 提出简单有效的离散扩散模型引导机制，包括基于分类器和无分类器的方法。在条件生成任务上实现了与连续扩散模型相当的引导效果，同时保持计算效率。

**亮点：** 填补了离散扩散模型引导方法的空白，使条件生成更加可控。

---

### 6. Scaling Laws for Diffusion Language Models
**Authors:** Yuntao Bai et al.  
**Score:** 0.952  
**ArXiv:** [2602.12889](https://arxiv.org/abs/2602.12889)

**摘要：** 首次系统研究扩散语言模型的 scaling laws。发现 dLLM 遵循与自回归模型类似但不同的幂律关系，并确定了最优的模型大小-计算量权衡。为 dLLM 的大规模训练提供了理论指导。

**亮点：** 为 dLLM 的工业级部署提供了关键的 scaling 指导。

---

### 7. Information-Theoretic Analysis of Diffusion Processes
**Authors:** Chen Wei, Stefano Ermon  
**Score:** 0.948  
**ArXiv:** [2602.13102](https://arxiv.org/abs/2602.13102)

**摘要：** 从信息论角度分析扩散过程，建立了扩散模型与率失真理论的联系。证明了最优扩散过程对应于信息瓶颈的解，并据此提出改进的噪声调度策略。

**亮点：** 将信息论与扩散模型深度结合，为理解和优化扩散过程提供了新的理论框架。

---

### 8. Latent Consistency Distillation for Diffusion Transformers
**Authors:** Simian Luo et al.  
**Score:** 0.941  
**ArXiv:** [2602.12445](https://arxiv.org/abs/2602.12445)

**摘要：** 将 Latent Consistency Models 扩展到 Diffusion Transformers (DiT)，实现 1-4 步高质量图像生成。在 ImageNet 256x256 上达到 FID 2.1，同时推理速度提升 10-50 倍。

**亮点：** 为大规模 DiT 模型的高效部署提供了实用方案。

---

### 9. Flow Matching Meets Information Geometry
**Authors:** Yaron Lipman et al.  
**Score:** 0.932  
**ArXiv:** [2602.12778](https://arxiv.org/abs/2602.12778)

**摘要：** 从信息几何角度重新审视 flow matching，证明最优传输路径对应于统计流形上的测地线。提出基于 Fisher 信息度量的改进 flow matching 方法，在图像和分子生成上取得 SOTA。

**亮点：** 将信息几何与生成模型优雅结合，开辟了新的理论和方法论方向。

---

### 10. Mutual Information Estimation in High Dimensions via Diffusion
**Authors:** Greg Ver Steeg et al.  
**Score:** 0.928  
**ArXiv:** [2602.13245](https://arxiv.org/abs/2602.13245)

**摘要：** 提出基于扩散模型的高维互信息估计方法。利用 score function 与互信息梯度的关系，实现了比传统方法更准确的估计。在表示学习和特征选择任务上展示了应用价值。

**亮点：** 将扩散模型应用于信息论基础问题，为高维统计推断提供了新工具。

---

## 统计
- 总论文数: 10 篇 (ranking_score > 0.85 且相关)
- 日期: 2026-02-16
- 主题分布: dLLM (4), Diffusion Theory (3), Information Theory (3)
