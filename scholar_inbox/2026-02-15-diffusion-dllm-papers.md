---
title: "2026-02-15-diffusion-dllm-papers"
---

# Scholar Inbox Digest: Diffusion & dLLM Papers (2026-02-15)

## 已验证论文

---

### 1. Continuous Diffusion Models Can Obey Formal Syntax (Diffinity)

**Authors:** Jinwoo Kim, Taylor Berg-Kirkpatrick, Loris D'Antoni  
**ArXiv:** [2602.12468](https://arxiv.org/abs/2602.12468) ✅

Diffusion language models offer a promising alternative to autoregressive models due to their global, non-causal generation process, but their continuous latent dynamics make discrete constraints (e.g., the output should be a JSON file that matches a given schema) difficult to impose. The authors introduce a **training-free guidance method** for steering continuous diffusion language models to satisfy formal syntactic constraints expressed using regular expressions.

**Key Contributions:**
- Constructs an analytic score estimating the probability that a latent state decodes to a valid string accepted by a given regular expression
- Uses gradient-based guidance without training auxiliary classifiers
- Implemented as **Diffinity** on top of the PLAID diffusion model
- Achieves **68-96% constraint satisfaction** on 180 regex constraints

---

### 2. dVoting: Fast Voting for Diffusion Language Models

**Authors:** Shucheng Fang et al.  
**ArXiv:** [2602.12153](https://arxiv.org/abs/2602.12153) ✅  
**Code:** [github.com/fscdc/dVoting](https://github.com/fscdc/dVoting)

Introduces **dVoting**, a fast voting technique that boosts reasoning capability of dLLMs without training. The key insight: across multiple samples for the same prompt, token predictions remain largely consistent, while performance is determined by a small subset of tokens exhibiting cross-sample variability.

**Performance gains:**
- GSM8K: +6.22%-7.66%
- MATH500: +4.40%-7.20%
- ARC-C: +3.16%-14.84%
- MMLU: +4.83%-5.74%

---

## ⚠️ 注意

本文件之前版本包含未经验证的论文链接（arXiv ID 与实际内容不符）。已清理，只保留验证过的论文。

后续更新会先验证 arXiv 链接再添加。
