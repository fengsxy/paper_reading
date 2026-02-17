# Scholar Inbox 精选 - 2026-02-16

## Diffusion / dLLM 相关论文（已验证）

---

### 1. Continuous Diffusion Models Can Obey Formal Syntax (Diffinity)
**Authors:** Jinwoo Kim, Taylor Berg-Kirkpatrick, Loris D'Antoni  
**ArXiv:** [2602.12468](https://arxiv.org/abs/2602.12468) ✅

**摘要：** 提出了一种无需训练的引导方法，使连续扩散语言模型能够满足用正则表达式表达的形式语法约束。通过构建分析性得分来估计潜在状态解码为给定正则表达式接受的有效字符串的概率，并使用其梯度来引导采样。在 PLAID 扩散模型上实现的 Diffinity 系统在 180 个正则表达式约束上达到 68-96% 的约束满足率。

**亮点：** 首次实现连续扩散语言模型的形式语法约束，对 JSON schema 等结构化输出生成有重要意义。

---

### 2. dVoting: Fast Voting for dLLMs
**Authors:** Shucheng Fang et al.  
**ArXiv:** [2602.12153](https://arxiv.org/abs/2602.12153) ✅  
**Code:** https://github.com/fscdc/dVoting

**摘要：** 提出 dVoting，一种无需训练的快速投票技术，利用 dLLM 的任意位置生成能力进行迭代优化。通过一致性分析识别不确定 token 并重新生成。在 GSM8K 上提升 6.22%-7.66%，MATH500 上提升 4.40%-7.20%，ARC-C 上提升 3.16%-14.84%。

**亮点：** 利用 dLLM 并行生成特性实现高效的 test-time scaling，开辟了 dLLM 推理增强的新方向。

---

## 说明

本文件只包含经过 arXiv 链接验证的论文。之前版本中的其他论文因链接错误已被移除。

如需更多 dLLM 相关论文，请参考：
- [T3D (2602.12262)](https://arxiv.org/abs/2602.12262) - 需验证
- [DiffuRank (2602.12528)](https://arxiv.org/abs/2602.12528) - 需验证
