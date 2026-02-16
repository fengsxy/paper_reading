# Paper Draft Outline: Optimal Token Generation Order in Discrete Diffusion Language Models

## Title Options

1. **"Easy First, Hard Later: Optimal Token Generation Order in Discrete Diffusion Language Models"**
2. "Token Difficulty Determines Optimal Generation Order in Diffusion Language Models"
3. "From Easy to Hard: A Principled Approach to Token Ordering in dLLMs"

**Recommended:** Option 1 — catchy, captures the core insight, memorable.

---

## Abstract (~150 words)

Discrete diffusion language models (dLLMs) generate text by iteratively refining a sequence of masked tokens, but the order in which tokens are revealed significantly impacts generation quality. We investigate the fundamental question: *what is the optimal order to generate tokens?* Through theoretical analysis and extensive experiments, we establish a surprising connection between optimal generation order and token difficulty—measured by model uncertainty or entropy. We prove that under mild assumptions, the optimal strategy follows an "easy-first" principle: tokens with lower conditional entropy should be generated before harder ones. This ordering maximizes information gain at each step and reduces error propagation. We validate our theory on [benchmarks], showing that difficulty-aware ordering improves perplexity by X% and downstream task performance by Y% compared to random and confidence-based baselines. Our findings provide both theoretical foundations and practical guidelines for designing better dLLM decoding strategies.

---

## 1. Introduction (2-3 pages)

### Key Points:
- dLLMs as emerging paradigm: parallel generation, flexible ordering
- The ordering problem: unlike autoregressive models, dLLMs must *choose* which tokens to reveal
- Current approaches: confidence-based (reveal highest confidence first), random, learned policies
- **Gap:** No theoretical understanding of *why* certain orderings work better
- **Our contribution:** Formal connection between optimal ordering and token difficulty

### Opening Hook:
"When writing, humans often start with the words they're most certain about, filling in harder choices later. We show that diffusion language models should do the same—and prove why."

### Contributions (bullet points):
1. Theoretical framework connecting generation order to token difficulty
2. Proof that easy-first ordering is optimal under [assumptions]
3. Practical algorithm for difficulty-aware decoding
4. Empirical validation across multiple benchmarks

---

## 2. Background & Related Work (1.5-2 pages)

### 2.1 Discrete Diffusion Language Models
- Forward process: progressive masking
- Reverse process: iterative denoising
- Key models: D3PM, MDLM, SEDD, etc.
- The ordering degree of freedom

### 2.2 Token Generation Order in dLLMs
- Confidence-based decoding (reveal highest p(x) first)
- Random ordering
- Learned ordering policies
- Connection to non-autoregressive translation (NAT)

### 2.3 Token Difficulty & Uncertainty
- Entropy as difficulty measure
- Predictability in language
- Information-theoretic perspectives on generation

---

## 3. Problem Formulation (1-2 pages)

### 3.1 Setup
- Sequence $x = (x_1, ..., x_n)$
- Mask state $m_t$ at step $t$
- Generation order $\pi$: permutation determining reveal sequence
- Objective: find $\pi^*$ maximizing $p(x | \pi)$ or minimizing expected error

### 3.2 Defining Token Difficulty
- **Definition 1:** Conditional entropy $H(x_i | x_{\text{revealed}})$
- **Definition 2:** Model uncertainty $-\log p_\theta(x_i | \text{context})$
- Relationship between definitions

### 3.3 The Ordering Optimization Problem
- Formal statement: $\pi^* = \arg\max_\pi \mathbb{E}[\log p(x | \pi)]$
- Why this is non-trivial: combinatorial, context-dependent

---

## 4. Theoretical Analysis (3-4 pages) ⭐ Core Contribution

### 4.1 Warm-up: Two-Token Case
- Analytical solution for $n=2$
- Intuition: generating easy token first provides better context for hard token
- **Lemma 1:** For two tokens, easy-first is optimal when [condition]

### 4.2 General Case: Easy-First Principle
- **Theorem 1 (Main Result):** Under assumptions A1-A3, the optimal ordering $\pi^*$ satisfies:
  $$H(x_{\pi(i)} | x_{\pi(1)}, ..., x_{\pi(i-1)}) \leq H(x_{\pi(i+1)} | x_{\pi(1)}, ..., x_{\pi(i)})$$
  i.e., tokens are revealed in order of increasing conditional difficulty.

- **Assumptions:**
  - A1: Conditional independence structure (or bounded dependence)
  - A2: Monotonicity of difficulty reduction
  - A3: Model calibration

- **Proof sketch:** Information-theoretic argument via chain rule decomposition

### 4.3 Connection to Information Gain
- Each step should maximize information gain
- Easy tokens → high confidence → more informative context
- **Corollary 1:** Easy-first maximizes cumulative mutual information

### 4.4 When Does Easy-First Fail?
- Violations of assumptions
- Adversarial cases
- Practical implications

---

## 5. Method: Difficulty-Aware Decoding (1.5-2 pages)

### 5.1 Estimating Token Difficulty
- Use model's own entropy estimates
- Efficient computation via single forward pass
- Handling dynamic difficulty (re-estimate after each reveal)

### 5.2 Algorithm: Easy-First Decoding
```
Algorithm 1: Easy-First Decoding for dLLMs
Input: masked sequence, model θ, steps T
For t = 1 to T:
    1. Compute difficulty d_i = H_θ(x_i | revealed) for all masked i
    2. Select k tokens with lowest difficulty
    3. Sample and reveal these tokens
    4. Update context
Return: generated sequence
```

### 5.3 Practical Considerations
- Batch size $k$ per step (trade-off: speed vs. optimality)
- Temperature scaling
- Combining with other decoding strategies

---

## 6. Experiments (3-4 pages)

### 6.1 Experimental Setup
- **Models:** MDLM, SEDD, [others]
- **Datasets:** WikiText-103, OpenWebText, [domain-specific]
- **Baselines:**
  - Random ordering
  - Confidence-first (highest $p(x_i)$)
  - Learned ordering (if available)
  - Autoregressive (left-to-right)

### 6.2 Main Results

**Table 1: Perplexity Comparison**
| Method | WikiText-103 | OpenWebText | ... |
|--------|--------------|-------------|-----|
| Random | ... | ... | |
| Confidence-first | ... | ... | |
| **Easy-first (Ours)** | ... | ... | |

**Table 2: Downstream Tasks**
- Text completion
- Infilling
- Conditional generation

### 6.3 Analysis & Ablations
- Effect of difficulty estimation method
- Sensitivity to batch size $k$
- Computational overhead
- Correlation between predicted and true difficulty

### 6.4 Qualitative Examples
- Case studies showing ordering differences
- Failure cases and analysis

---

## 7. Discussion (1 page)

### 7.1 Implications for dLLM Design
- Training objectives that encourage easy-first structure
- Architecture modifications

### 7.2 Connections to Human Cognition
- Humans also generate easy-first in writing/speech
- Cognitive plausibility of our findings

### 7.3 Limitations
- Assumptions may not hold universally
- Computational cost of difficulty estimation
- Model-dependent results

---

## 8. Conclusion (0.5 page)

- Summary of contributions
- Broader impact: principled decoding for dLLMs
- Future work: learning to predict difficulty, joint training

---

## Key Figures

### Figure 1: Teaser/Overview (Page 1)
**Content:** Side-by-side comparison showing:
- Left: Random ordering → errors propagate
- Right: Easy-first ordering → stable generation
- Visual: Heatmap of token difficulty over generation steps

### Figure 2: Intuition Diagram (Section 4)
**Content:** Two-token example illustrating why easy-first works
- Information flow diagram
- Entropy reduction visualization

### Figure 3: Theoretical Framework (Section 4)
**Content:** 
- Chain rule decomposition
- Cumulative information gain curves for different orderings

### Figure 4: Algorithm Visualization (Section 5)
**Content:** Step-by-step generation showing:
- Difficulty scores at each step
- Which tokens get revealed
- How context improves predictions

### Figure 5: Main Results (Section 6)
**Content:** 
- Bar chart comparing methods on perplexity
- Line plot: performance vs. generation steps

### Figure 6: Difficulty Correlation (Section 6)
**Content:**
- Scatter plot: predicted difficulty vs. actual error rate
- Shows our difficulty measure is meaningful

### Figure 7: Qualitative Examples (Section 6)
**Content:**
- Example sentences with color-coded generation order
- Comparison of orderings and final outputs

---

## Appendix (Supplementary)

- A: Full proofs
- B: Additional experiments
- C: Hyperparameter sensitivity
- D: Computational cost analysis
- E: More qualitative examples

---

## Estimated Length
- Main paper: 8-9 pages (NeurIPS/ICML format)
- Appendix: 3-5 pages

## Target Venues
- NeurIPS 2026
- ICML 2026
- ICLR 2027

---

## Open Questions / TODOs

1. [ ] What exact assumptions do we need for Theorem 1?
2. [ ] How to handle ties in difficulty?
3. [ ] Can we learn difficulty predictors that are faster than entropy?
4. [ ] Connection to curriculum learning?
5. [ ] Multi-step lookahead vs. greedy easy-first?

---

*Draft created: 2026-02-16*
*Author: Yu (Ted)*
