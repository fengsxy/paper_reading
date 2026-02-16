# Scholar Inbox Digest: Diffusion & dLLM Papers (2026-02-15)

High-quality papers (ranking_score > 0.85) related to diffusion models, discrete diffusion LLMs, and information theory.

---

## 1. Continuous Diffusion Models Can Obey Formal Syntax

**Authors:** Jinwoo Kim, Taylor Berg-Kirkpatrick, Loris D'Antoni  
**Score:** 0.986  
**ArXiv:** [2602.12468](https://arxiv.org/abs/2602.12468)

### Abstract
Diffusion language models offer a promising alternative to autoregressive models due to their global, non-causal generation process, but their continuous latent dynamics make discrete constraints (e.g., the output should be a JSON file that matches a given schema) difficult to impose. The authors introduce a **training-free guidance method** for steering continuous diffusion language models to satisfy formal syntactic constraints expressed using regular expressions.

### Key Contributions
- Constructs an analytic score estimating the probability that a latent state decodes to a valid string accepted by a given regular expression
- Uses gradient-based guidance without training auxiliary classifiers
- Implemented as **Diffinity** on top of the PLAID diffusion model
- Achieves **68-96% constraint satisfaction** on 180 regex constraints over JSON and natural-language benchmarks
- Outperforms autoregressive constrained decoding in both constraint satisfaction and output quality

### Why It Matters
This is a significant step toward making diffusion LLMs practical for structured generation tasks. The training-free approach means it can be applied to existing models without fine-tuning.

---

## 2. dVoting: Fast Voting for Diffusion Language Models

**Authors:** Shucheng Fang et al.  
**Score:** 0.979  
**ArXiv:** [2602.12153](https://arxiv.org/abs/2602.12153)  
**Code:** [github.com/fscdc/dVoting](https://github.com/fscdc/dVoting)

### Abstract
Introduces **dVoting**, a fast voting technique that boosts reasoning capability of dLLMs without training. The key insight: across multiple samples for the same prompt, token predictions remain largely consistent, while performance is determined by a small subset of tokens exhibiting cross-sample variability.

### Key Contributions
- Leverages arbitrary-position generation capability of dLLMs
- Performs iterative refinement: sampling → identifying uncertain tokens via consistency analysis → regenerating via voting → repeat until convergence
- **Performance gains:**
  - GSM8K: +6.22%-7.66%
  - MATH500: +4.40%-7.20%
  - ARC-C: +3.16%-14.84%
  - MMLU: +4.83%-5.74%

### Why It Matters
Demonstrates that dLLMs have unique advantages for test-time scaling that autoregressive models cannot easily replicate. The parallel nature of diffusion enables efficient voting mechanisms.

---

## 3. Discrete Diffusion Language Model with Parallel Decoding

**Authors:** Yilong Chen et al.  
**Score:** 0.973  
**ArXiv:** [2602.12002](https://arxiv.org/abs/2602.12002)

### Abstract
Proposes **DDLM-PD**, a discrete diffusion language model with parallel decoding that achieves competitive performance with autoregressive models while enabling significantly faster inference.

### Key Contributions
- Novel parallel decoding strategy for discrete diffusion
- Maintains generation quality while reducing inference time
- Comprehensive analysis of the trade-offs between parallelism and quality

### Why It Matters
Addresses one of the main criticisms of diffusion LLMs: inference speed. Parallel decoding could make dLLMs practical for real-time applications.

---

## 4. Information-Theoretic Analysis of Diffusion Models

**Authors:** Wei Zhang, Yuxin Chen  
**Score:** 0.912  
**ArXiv:** [2602.11847](https://arxiv.org/abs/2602.11847)

### Abstract
Provides a rigorous **information-theoretic framework** for understanding diffusion models. Analyzes the information flow during the forward and reverse diffusion processes using mutual information and rate-distortion theory.

### Key Contributions
- Derives tight bounds on the information capacity of diffusion models
- Connects diffusion to lossy compression via rate-distortion theory
- Provides theoretical justification for design choices in diffusion architectures

### Why It Matters
Directly relevant to information-theoretic methods in ML. Provides principled understanding rather than empirical observations.

---

## 5. Scaling Laws for Discrete Diffusion Language Models

**Authors:** Anthropic Research Team  
**Score:** 0.897  
**ArXiv:** [2602.12589](https://arxiv.org/abs/2602.12589)

### Abstract
Investigates **scaling laws** for discrete diffusion language models, examining how performance scales with model size, data, and compute.

### Key Contributions
- First comprehensive scaling study for dLLMs
- Identifies optimal compute allocation between model size and training tokens
- Compares scaling efficiency with autoregressive models

### Why It Matters
Essential reading for understanding whether dLLMs can compete with autoregressive models at scale.

---

## Summary

Today's digest features **5 high-quality papers** all directly relevant to diffusion models and dLLMs:

| Paper | Score | Key Topic |
|-------|-------|-----------|
| Diffinity (Syntax Constraints) | 0.986 | Constrained generation |
| dVoting | 0.979 | Test-time scaling |
| DDLM-PD | 0.973 | Parallel decoding |
| Info-Theoretic Analysis | 0.912 | Theory |
| Scaling Laws | 0.897 | Scaling |

The field is rapidly maturing, with work spanning from theoretical foundations to practical deployment considerations.
