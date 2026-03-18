# Daily Papers — 2026-03-18 (Wednesday)

## 1. Diffusion Language Models Are Natively Length-Aware
- **Date:** 2026-03-06 | **arXiv:** [2603.06123](https://arxiv.org/abs/2603.06123)
- **Authors:** Vittorio Rossi et al.
- **Key idea:** DLM 的 latent prompt representation 本身包含输出长度信息；提出 zero-shot 动态裁剪 context window 机制，在生成前估计所需长度，减少 diffusion steps
- **Results:** GSM8K/HumanEval/IfEval/LongFormQA 四个 benchmark 上 FLOPs 显著降低，2/4 任务性能反而提升
- **Relevance:** ⭐⭐⭐ DLM 推理效率的实用改进，揭示了 prompt embedding 中隐含长度信号的有趣现象

## 2. The Diffusion Duality, Chapter II: Ψ-Samplers and Efficient Curriculum
- **Date:** 2026-02-24 | **arXiv:** [2602.21185](https://arxiv.org/abs/2602.21185) | **Venue:** ICLR 2026
- **Authors:** Justin Deschenaux et al.
- **Key idea:** 为 discrete diffusion 提出通用 Predictor-Corrector 采样器族（Ψ-samplers），适用于任意 noise process；配合 uniform-state diffusion 持续随步数提升质量（ancestral sampling 会饱和）
- **Results:** OWT 上更低 perplexity，CIFAR10 更好 FID/IS；训练阶段 memory 减 33%，时间减 25%
- **Relevance:** ⭐⭐⭐ 挑战"masked diffusion 必然主导"的假设，uniform-state + PC sampler 是竞争力十足的替代路线

## 3. dLLM: Simple Diffusion Language Modeling
- **Date:** 2026-02-26 | **arXiv:** [2602.22661](https://arxiv.org/abs/2602.22661)
- **Authors:** Zhanhui Zhou, Lingjie Chen, Hanghang Tong, Dawn Song
- **Key idea:** 统一 DLM 开发框架，标准化训练/推理/评估管线；支持 LLaDA、Dream 等模型的复现、微调、部署
- **Features:** 可将 BERT-style encoder 或 AR LM 转换为 DLM；minimal recipes for small DLMs from scratch
- **Relevance:** ⭐⭐ 工程框架而非方法创新，但对 dLLM 实验复现非常实用

---

> 今日新论文 3 篇，均为 dLLM/discrete diffusion 方向的近期工作。
