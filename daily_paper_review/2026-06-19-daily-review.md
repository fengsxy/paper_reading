# Daily Paper Review — 2026-06-19 (Friday)

**Fetching**: arXiv 2026-06-12 ~ 2026-06-19 | 23 papers found | Focus: diffusion models, representation learning, info theory

---

## Paper 1 (Primary): LESS — Mutual-Stability Sampling for Diffusion Language Models

**arXiv**: 2606.16908 | **MBZUAI / École Polytechnique** | 2026-06-15

---

### 1. Task

dLLMs generate text by iteratively denoising masked sequences (parallel token updates, bidirectional conditioning), but standard samplers use a **fixed reverse-step budget** chosen before decoding. This wastes computation on positions whose predictions have already stabilized, while occasionally committing unstable tokens too early — because unmasking is irreversible, early errors can't be recovered.

**Goal**: Adaptive per-position unmasking — commit each token only when its predictive distribution has converged, reducing total reverse steps without quality loss.

---

### 2. Challenge

| Problem | Why it matters |
|---|---|
| Fixed budget wastes steps on stable positions | Most reverse steps recompute positions that won't change |
| Premature token commitment is irreversible | Once written, incorrect tokens propagate to later steps |
| Prior adaptive samplers use partial signals | Confidence alone doesn't track distributional drift; KL is unbounded & directional |

Prior work: confidence-based (unmask when top-1 prob is high), margin-based, KL-divergence-aware — but each is incomplete alone.

---

### 3. Insight & Novelty

**Core insight**: Adaptive unmasking = **per-position online stopping problem**. Each masked position has a trajectory of predictive distributions over reverse steps; the stopping decision should jointly consider *three* signals about that trajectory.

**Three-way joint stability rule** (all three must pass):

1. **Top-1 confidence**: `p_{t,i}(w_{t,i})` is high — current prediction is locally decisive
2. **Top-1 token persistence**: the predicted token hasn't changed over a window of recent steps — guards against just-changed predictions
3. **Top-K inter-step Jensen–Shannon divergence**: predictive distribution itself has stabilized — bounded [0,1], symmetric, captures redistribution among top-K alternatives that confidence + persistence miss

**Key methodological contribution**: Using JSD rather than KL as the inter-step stability measure. KL is unbounded and directional; JSD is bounded and symmetric — more appropriate for measuring convergence of distributions.

**Training-free, model-agnostic**: No fine-tuning needed. Works on Dream-7B, LLaDA-8B, LLaDA-1.5-8B. Orthogonal to training-time acceleration (distillation, flow matching) and systems methods (caching, speculative decoding).

---

### 4. Potential Flaw

**情境局限**:
- Evaluated only on math, code, general-knowledge benchmarks. Long-context or open-ended generation tasks untested.
- **Persistence window P and top-K are hyperparameters** — ablates are limited; scaling behavior unclear.
- Ablation shows confidence is the dominant signal; persistence + JSD are "complementary safeguards." This raises a question: is the three-way conjunction strictly better than confidence-only with a higher threshold?

**值得挖掘的方向**:
- **Combine with SimSD (2026-06-02 review)**: SimSD adds speculative verification to dLLM; LESS reduces steps. Joint application: fewer steps × speculative speedup could compound.
- **Connection to I-012 (dLLM hard/soft constraint separation)**: The entropy-cut MH sampler in I-012 also deals with position-wise uncertainty. LESS's JSD-based stability criterion might inform adaptive proposal distributions in the FoCore HD tokens framework.

---

### 5. Motivation (First Principles)

> dLLM denoises a fully-masked sequence over T steps. At each step t, the model produces per-position distributions `p_{t,i}`. Standard samplers unmask in batches at fixed steps — this is the equivalent of "guessing the whole sentence after N rounds of editing, where N is fixed in advance."
>
> The online stopping framing is natural: each position i has its own convergence time `τ_i`. Fixed-budget decoding uses `max_i τ_i` for all positions. LESS uses per-position adaptive stopping.
>
> The JSD criterion is elegant: it measures distributional similarity on a coarsened top-K vocabulary, avoiding the full-vocabulary KL's unboundedness and directionality. The coarsening means JSD is tractable to compute at each step.
>
> 72.1% fewer steps is a strong claim. But note: "fewer steps" → "fewer forward passes" only if the unmasking set `U_t` is a superset of the stability-eligible set. The paper assumes unmasking all eligible positions per step — this could still be a significant fraction of positions.

---

### 6. TL;DR

**One-liner**: Training-free adaptive sampler for dLLM that jointly gates token commitment on confidence + token persistence + inter-step JSD, achieving 72.1% step reduction without accuracy loss.

**Relevance to your work**: Directly relevant to dLLM inference efficiency. The JSD-based distributional stability criterion is a clean, information-theoretic signal that could generalize beyond unmasking decisions.

**ArXiv link**: https://arxiv.org/abs/2606.16908

---

## Paper 2 (Secondary): Wasserstein Policy Learning for Distributional Outcomes

**arXiv**: 2606.19117 | **COLT 2026** | Great Bay U / CityU / Shanghai UFE | 2026-06-17

---

### 1. Task

Standard offline policy learning: learn a policy `π: X → A` (covariates → treatment) to maximize welfare defined as mean of scalar potential outcomes. This paper extends to **distribution-valued outcomes** — each potential outcome is a probability measure on ℝ, and welfare is a utility functional applied to the **Wasserstein barycenter** of induced outcome distributions.

**Key difference from prior distributional policy learning**: prior work has scalar outcomes with distributional objectives (quantiles, CVaR). Here, the *outcome itself* is a probability measure — the data lives in Wasserstein space `(P₂(ℝ), W₂)`.

---

### 2. Challenge

| Challenge | Why hard |
|---|---|
| Wasserstein barycenter has no closed form | Unlike expectation, can't just integrate — it's an OT optimization problem |
| Policy induces entire quantile curve | Objective depends on the full quantile function, not just mean/variance |
| Product complexity: Π × [0,1] | Must uniformly control deviation over both the policy class AND the quantile index |
| Polyton's "linear averaging destroys geometry" | Naively averaging distributions yields meaningless bimodal artifacts |

---

### 3. Insight & Novelty

**Key methodological insight**: Quantile isometry — `(P₂(ℝ), W₂)` is isometric to `L₂([0,1])` via quantile functions. This reduces the Wasserstein barycenter problem to estimation of a policy-indexed mean quantile curve in L₂ — turning a metric-space problem into a functional estimation problem.

**Construct IPW and doubly robust (DR) estimators** for the policy value, with a monotone rearrangement step to enforce valid quantiles.

**Main theoretical result**: Finite-sample regret bound `O~(√(N-dim(Π)/N))` — **the leading rate is governed entirely by policy-class complexity**. The distributional outcome does NOT add a leading-order nonparametric penalty beyond the scalar case. Minimax lower bound confirms rate-sharpness.

---

### 4. Potential Flaw

- **1D only**: Results are in one-dimensional Wasserstein space. Extension to multi-dimensional distributions (e.g., image distributions) is non-trivial.
- **Assumes overlap/positivity**: No discussion of what happens when propensity scores are near zero.
- **Policy class must be combinatorial**: The `N-dim(Π)` complexity measure requires structured policy classes (e.g., decision trees). Smooth parametric policies may behave differently.

**值得挖掘的方向**: The quantile-isometry reduction is a general trick. Could it apply to **evaluating diffusion model quality**? Wasserstein distance between generated and real distributions could be decomposed into quantile-curve estimation — potentially useful for evaluating dLLM outputs without human ratings.

---

### 5. TL;DR

**One-liner**: Offline policy learning where outcomes are probability measures; quantile-isometry reduces the Wasserstein barycenter problem to L₂ quantile-curve estimation; leading regret rate depends only on policy-class complexity, not outcome-space dimension.

**Relevance to your work**: Information-theoretic framing; Wasserstein geometry is relevant if you ever evaluate distributional closeness of generated vs. real data.

**ArXiv link**: https://arxiv.org/abs/2606.19117

---

*Sources: scholar_inbox/2026-06-19-daily-papers.md | arXiv 2606.16908, 2606.19117, 2501.09876*
