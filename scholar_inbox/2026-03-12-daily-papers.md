# Daily Papers - 2026-03-12

## Diffusion Models & Representation Learning

### 1. ReFusion: A Diffusion Large Language Model with Parallel Autoregressive Decoding
- **arXiv:** 2512.13586 (updated 2026-03-05)
- **Key insight:** Hybrid diffusion-autoregressive approach that enables KV cache reuse while maintaining parallel generation
- **Method:** Slot-level diffusion + intra-slot autoregressive infilling, reducing learning complexity from token combinations to slot permutations
- **Impact:** Addresses critical drawbacks of masked diffusion models (MDMs) - high computational overhead and incoherent generation

### 2. Quantum Diffusion Models: Score Reversal Is Not Free in Gaussian Dynamics
- **arXiv:** 2603.06488 (2026-03-06)
- **Key insight:** Complete positivity couples drift and diffusion at generator level in quantum-limited systems
- **Finding:** Wigner-score reverse drift violates complete positivity (CP) for certain squeezing parameters; any Gaussian CP repair requires extra diffusion
- **Relevance:** Theoretical foundations for diffusion models in quantum continuous-variable systems

### 3. Generalization of Diffusion Models Arises with a Balanced Representation Space
- **arXiv:** 2512.20963 (updated 2026-02-10)
- **Core thesis:** Memorization vs generalization determined by representation balance
- **Findings:** (i) memorization stores raw samples in weights → spiky activations; (ii) generalization learns data statistics → balanced semantic codes; (iii) real models show hybrid regime due to data imbalance
- **Tools:** Representation-based memorization detection + training-free editing via representation steering

### 4. A Closer Look at Model Collapse: From Generalization to Memorization
- **arXiv:** 2509.16499v1
- **Focus:** Model collapse in iterative training on synthetic data
- **Key finding:** Transition from generalization to memorization driven by declining entropy of synthetic training data
- **Practical concern:** As AI-generated content proliferates, next-gen models trained on mixed real/synthetic data face degradation risk

## Related Work

### 5. Beyond Autoregression: An Empirical Study of Diffusion LLMs for Code Generation
- **arXiv:** 2509.11252v2
- **Scope:** Diffusion models for code generation (sub-10B parameters)
- **Techniques:** Coupled GRPO for RL, edit-based corruption

---

**Search notes:** YDC API returned mostly older survey papers (2209.00796 from 2022) and general ML listings. Recent high-quality papers (ReFusion, Quantum Diffusion, Generalization study) found via secondary search. Limited fresh content in target areas today.
