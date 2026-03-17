# Daily Papers — 2026-03-17 (Tuesday)

> 今日搜索未发现显著新论文（相比昨日 3/16 批次）。以下为近日更新但此前未收录的补充：

## 1. Soft-Masked Diffusion Language Models
- **Updated:** 2026-03 (arXiv preprint)
- **arXiv:** [2510.17206](https://arxiv.org/abs/2510.17206)
- **Key idea:** 用连续 soft mask（而非 hard absorbing mask）做 discrete diffusion，保留更多 token 级信息；在 language modeling + coding 任务上超越 MDLM
- **Relevance:** dLLM 核心改进方向，与 LLaDA/MDLM 系列直接对比
- **Note:** 已在 3/16 batch 涉及相关工作，此处补充完整条目

## 2. One-step Language Modeling via Continuous Denoising
- **Date:** 2026-02-18 | **arXiv:** [2602.16813](https://arxiv.org/abs/2602.16813)
- **Key idea:** 将离散 token 映射为 one-hot 连续表示，用 flow matching 实现 1-step 生成；提出基于 decoding error rate 的时间重参数化
- **Relevance:** 极端少步生成的 diffusion LM，连续 vs 离散表示的 trade-off 探索

## 3. Generalization of Diffusion Models Arises with a Balanced Representation Space
- **Updated:** 2026-02-10 | **arXiv:** [2512.20963](https://arxiv.org/abs/2512.20963)
- **Key idea:** 从表示学习视角分析 diffusion model 的泛化 vs 记忆：balanced representation space 是泛化的关键
- **Relevance:** diffusion + representation learning 理论交叉，直接相关

---

> 总体评估：今日无重大新发论文，上述为近期遗漏的补充收录。
