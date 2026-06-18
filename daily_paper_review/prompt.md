请分析以下论文，严格按照以下 6 点格式输出 Markdown（不要引入任何 LaTeX 公式，用中文）：

## 1. Task
【请形式化描述这篇论文解决的问题】

## 2. Challenge  
【传统方法的困境是什么？】

## 3. Insight & Novelty
### 3.1 Insight
- 【作者的 Insight 是什么？被什么启发的？】

### 3.2 Novelty
【每个创新点的格式】：【解决的问题】→【受哪个 insight 启发】→【具体设计是什么】

## 4. Potential Flaw
### 4.1 情境局限
【当前方法的适用范围有什么局限？】

### 4.2 数据问题
【什么样的数据会让方法遇到困难？】

### 4.3 值得挖掘的方向
【哪个困难最值得写成一篇 paper？】

## 5. Motivation
【用第一性原理回答：这个 idea 是怎么想到的？用问句形式，如"之前的方法 xxx，那能不能尝试 xxx？】

---

## 论文信息

**标题**: Unknown
**arXiv ID**: 2606.12273
**日期**: 2026-06-10
**链接**: http://arxiv.org/abs/2606.12273v1

**摘要**:
Diffusion large language models (dLLMs) offer an efficient alternative to autoregressive models through parallel decoding, yet existing post-training methods largely rely on random masking strategies that overlook intrinsic token dependencies. In this work, we present an empirical analysis of attention in dLLMs and show that tokens attending more strongly to unmasked context exhibit greater generation stability and play a critical role in reasoning. Motivated by these findings, we propose AGDO, an attention-guided denoising and optimization framework that aligns both training and optimization with attention-derived dependencies. AGDO determines the denoising order based on attention structure and emphasizes attention-critical tokens during supervised fine-tuning and reinforcement learning.
