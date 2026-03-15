# dLLM 专用蒸馏与加速方法调研（补充报告）

**作者：Claw | 日期：2026-03-15 | 为 Yu 准备**
**新增 3 篇 dLLM 专用蒸馏论文精读，累计 22 篇**

---

## 一、为什么需要单独讨论 dLLM 蒸馏？

前两份报告覆盖了通用 LLM 蒸馏（MiniLLM、GKD、EOPD、Reopold）和 dLLM 的 consistency distillation（CDLM）。但 discrete diffusion 的蒸馏有**独特挑战**：

1. **离散采样不可微** → continuous diffusion 的 DDIM、Progressive Distillation 不能直接搬
2. **Token 间独立性假设** → 少步采样时 token 间相关性丢失
3. **"Repeated Prefill" 计算模式** → 每步重算全序列，不像 AR 有天然 KV cache

---

## 二、新增论文列表（3篇）

| # | 论文 | 来源 | 核心方法 |
|---|------|------|----------|
| 20 | **SDTT** (Self-Distillation Through Time) | EPFL, ICLR 2025 | 迭代自蒸馏，KLD loss |
| 21 | **Di4C** (Dimensional Correlations) | Sony, ICML 2025 | Mixture model 捕捉维度相关性 |
| 22 | **DyLLM** (Dynamic LLM Inference) | SNU, arXiv 2026.03 | Saliency-based token selection |

---

## 三、各方案详细分析

### SDTT — Self-Distillation Through Time (EPFL, ICLR 2025)

**核心方法**：迭代自蒸馏，每轮步数减半。

Teacher 和 student 是**同一个模型**——不需要外部大模型。区别只在采样步数。

**Target 构建（Algorithm 1，核心创新）**：
- 对每个 masked token，记录它在 teacher trajectory 中**被揭示时刻**的 log-probability
- 而非用统一的某一步——每个 token 的 target 来自 trajectory 中最相关的那一步
- 这解决了 discrete diffusion 中"不同 token 在不同时刻被揭示"的异步性问题

**蒸馏 Loss 对比**：
- L2: 在 discrete space 效果差（logit 空间的 L2 ≠ 概率空间的相似性）
- TV (Total Variation): 中等
- **KLD: 最好——student 甚至在 LAMBADA 上超越了 teacher！**

Student 超越 teacher 的原因：KLD 蒸馏有**正则化效果**——迫使 student 的分布更 smooth，减少了过拟合。

**结果**：
- 7 轮迭代：1024→16 步（64× reduction）
- 860M 参数（当时最大开源 discrete DLM）
- 比 AR+KV cache 快 8×，perplexity 几乎无损

**好在哪**：最简单的 dLLM 蒸馏方案，self-distillation 不需要额外模型

**不足**：7 轮迭代 = 7 次完整训练，累计成本不低

---

### Di4C — Distillation through Dimensional Correlations (Sony, ICML 2025)

**核心洞察**：步数减少的本质代价 = **失去了隐式建模 token 间相关性的能力**。

标准 discrete diffusion 假设 token 间独立预测。多步采样时这个假设 OK——多步迭代隐式地建模了相关性。但少步采样时，token 间的联合分布无法被独立分布很好近似。

**解决方案**：用 **mixture distribution** 替代 element-wise independent distribution：
- Mixture 可以捕捉维度间相关性，同时保持可扩展性
- 本质上是在 student 中增加表达能力来补偿步数减少
- 理论证明：many-step independent model 可以被蒸馏到 few-step mixture model

**在 image 和 language 领域都有效**

**好在哪**：唯一从理论上分析了"为什么步数减少会降低质量"的工作

**与你的 linear state 的直接关系**：
- Di4C 用 mixture model 增加每步的表达能力 → 补偿步数减少
- Linear state 用跨步记忆增加每步的信息输入 → 也是补偿步数减少
- 两者思路互补：Di4C 增加 output 表达力，linear state 增加 input 信息量
- **可以组合：linear state 提供更好的输入 + mixture 提供更 expressive 的输出**

---

### DyLLM — Dynamic LLM Inference (SNU, arXiv 2026.03)

**核心观察**：dLLM 每步对所有 token 重算是巨大浪费——大多数 token 在相邻步骤间表示几乎不变。

**方法**：
1. 测量 cosine similarity：只有少量 "salient tokens" 发生有意义的变化
2. 每层独立判断 saliency（Layer-Adaptive）
3. 只对 salient tokens 重算 attention+FFN，non-salient tokens 复用 cache
4. Training-free

**结果**：
- LLaDA 8B: **7.6× throughput**
- Dream 7B: **9.6× throughput**
- 精度几乎无损

**好在哪**：当前 training-free 加速的最佳方案，比 Elastic-Cache 更精细

**与 linear state 的关系**：互补——DyLLM 减少不必要计算（skip 稳定 tokens），linear state 增加有效信息（保持跨步记忆）。两者组合 = 更少计算 + 更好信息保持。

---

## 四、dLLM 蒸馏方法全景对比

| 方案 | 类型 | 需要训练? | 减少步数 | 核心思路 | 好在哪 |
|------|------|-----------|----------|----------|--------|
| **SDTT** | Step distill | ✅ 迭代训练 | 64× (1024→16) | 自蒸馏，每轮 halving | 最简单，KLD student 超越 teacher |
| **CDLM** | Consistency | ✅ 8-16h | 3.4-7.9× | Consistency + distill + DLM 三 loss | 效率最高（8h），bidir→block-causal |
| **Di4C** | Step distill | ✅ 训练 mixture | 理论级 | Mixture model 建模维度相关性 | 唯一的理论分析 |
| **DyLLM** | Token pruning | ❌ Training-free | N/A (减少每步计算) | Saliency-based token selection | 9.6× throughput，最精细的 cache 方案 |
| **Elastic-Cache** | KV cache | ❌ Training-free | N/A (减少每步计算) | Attention-aware drift test | 45× 加速（长序列） |
| **dKV-Cache** | KV cache | ❌ Training-free | N/A (减少每步计算) | 延迟缓存策略 | Cache 反而提升质量 |
| **MetaState** | 跨步记忆 | ✅ 轻量训练 | N/A (减少所需步数) | GRU persistent memory | 首个跨步记忆方案 |

---

## 五、关键洞察

### 洞察1：dLLM 蒸馏有两条路线，应该组合

**路线 A：减少每步计算量**（DyLLM、Elastic-Cache、dKV-Cache）
- Training-free
- 每步还是做同样的事，只是跳过不必要的计算
- 不改变生成质量

**路线 B：减少总步数**（SDTT、CDLM、Di4C）
- 需要训练
- 每步做更多的事（跳多步）
- 可能降低质量，需要更 expressive 的模型补偿

**你的 linear state 属于路线 C：增加每步信息量**
- 不减少计算，不减少步数
- 而是让每步的输入更好（跨步记忆）
- 间接效果：更少步就能达到相同质量

**三条路线可以叠加**：linear state（更好输入）+ CDLM（跳步）+ DyLLM（跳 token）

### 洞察2：KLD > L2 在 discrete 蒸馏中

SDTT 发现 KLD 远优于 L2——甚至 student 超越了 teacher。这对你的实验设计有直接影响：如果做 linear state 的蒸馏训练，应该用 KLD loss（概率空间）而非 L2 loss（logit 空间）。

### 洞察3：维度相关性是步数减少的核心代价

Di4C 的理论分析说明：步数减少 = 失去隐式维度相关性建模。你的 linear state 可以从另一个角度弥补——跨步记忆保持了 token 间的依赖信息，使得即使少步也不丢失相关性。

---

## 六、参考文献

20. Deschenaux & Gulcehre. "Beyond Autoregression: Fast LLMs via Self-Distillation Through Time." ICLR 2025. arXiv:2410.21035.
21. Hayakawa et al. "Distillation of Discrete Diffusion through Dimensional Correlations." ICML 2025. arXiv:2410.08709.
22. Lee et al. "DyLLM: Efficient Diffusion LLM Inference via Saliency-based Token Selection." arXiv:2603.08026, 2026.
