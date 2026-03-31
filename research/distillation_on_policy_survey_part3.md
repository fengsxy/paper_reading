### 类别③：Step Distillation（减少 diffusion 步数）

#### Progressive Distillation (Salimans & Ho, ICLR 2022) — 经典方法

**核心方法**：
1. Teacher 用 N 步生成 → 训练 student 用 N/2 步匹配 teacher 的两步输出
2. Student 成为新 teacher → 再训 N/4 步的 student
3. 迭代直到 1-4 步

**关键设计**：student 的一步 = teacher 的两步。每次迭代减半步数。

**在 dLLM 中的应用**：
- 直接类比：teacher 用 T 步 denoise → student 用 T/2 步
- 但 discrete diffusion 比 continuous 更难蒸馏：离散采样不可微，无法直接用 L2 loss
- CDLM（Paper 9）是这个思路在 discrete diffusion 上的实现

---

#### Consistency Models (Song et al., ICML 2023) — 经典方法

**核心思想**：定义 consistency function f(x_t, t) → x_0：同一 trajectory 上的任意中间状态都映射到**同一个** x_0。

**两种训练方式**：
1. **Consistency Distillation (CD)**：从预训练 diffusion model 蒸馏。用 teacher 的 ODE trajectory 做训练信号。
2. **Consistency Training (CT)**：直接训练，不需要 teacher。用 adjacent states 的一致性约束。

**与 dLLM 的关系**：
- CDLM（Paper 9）直接搬了 CD 到 discrete diffusion
- CT 方向在 dLLM 中**还未被探索**——潜在研究机会
- Discrete space 中 "self-consistency" 需要重新定义（离散 token 没有连续 ODE trajectory）

---

#### CDLM — Consistency DLM（Paper 9，前报告已详述）

三个 loss 联合训练：Distillation + Consistency + DLM
- 8-16h 训练 → 3.6-14.5× latency reduction
- Bidir teacher → block-causal student（蒸馏 + 转换一步完成）
- 当前 dLLM 加速的最高效方案

---

### 类别④：Self-Distillation

#### OPSD — Self-Distilled Reasoner (CMU, arXiv 2026.01)

**核心创新：不需要外部 teacher**

**方法**：
1. Model 自己生成 solution
2. 用 privileged info（ground truth answer）筛选正确 solution
3. 在正确 solution 上做 on-policy self-distillation（自己的正确输出作为 teacher signal）
4. 迭代 self-improvement

**结果**：4-5× inference speedup on parallel-structured reasoning tasks

**与 dLLM 的关系**：
- dLLM 天然支持 self-distillation：多步 denoise（完整 trajectory）→ 少步 denoise（student）
- 不需要外部 AR teacher
- 利用 dLLM 自己的 iterative refinement 能力做 self-improvement
