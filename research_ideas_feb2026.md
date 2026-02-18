# dLLM Research Ideas - First Principles Thinking

*Yu's research interests: Diffusion models, Representation learning, Information-theoretic methods, Trustworthy AI*
*Advisor: Greg Ver Steeg (information theory expert)*

---

## 第一性原理反问

### Q1: dLLM 的本质是什么？

**AR 模型:** P(x) = ∏ P(x_i | x_{<i}) — 因果分解，单向信息流
**dLLM:** P(x) = ∫ P(x|z) P(z) dz — 通过 latent 变量建模联合分布

**核心区别：** dLLM 不强制因果结构，允许 token 之间双向信息交换。

**反问：这个双向信息交换到底带来了什么？**
- 更好的 global coherence？（empirically yes）
- 更高的 mutual information？（没人验证过）
- 更好的 representations？（没人研究过）

---

### Q2: 当前哪些工作是 incremental 的？

**明显 incremental 的方向：**

1. **Inference Acceleration (53/66 papers)**
   - FOCUS, DAWN, FlashBlock, SureLock...
   - 本质都是 engineering tricks：caching, speculative decoding, parallel sampling
   - 没有新的理论 insight
   - **结论：不要做这个方向**

2. **Architecture tweaks**
   - 换个 attention pattern, 换个 noise schedule
   - 没有回答 "why" 的问题
   - **结论：不要做这个方向**

3. **Application papers**
   - dLLM for code, dLLM for speech...
   - 只是把 dLLM 套到新任务上
   - **结论：除非有独特 insight，否则不要做**

**非 incremental 的方向（但可能很难）：**

1. **理论理解** — 为什么 dLLM 在 reasoning 上好？
2. **Representation 分析** — dLLM 学到了什么？
3. **Privacy/Safety** — 完全空白
4. **Information-theoretic 分析** — 几乎没人做

---

### Q3: 什么是 "好的 idea"？

**好 idea 的标准：**
1. ✅ 非 incremental — 有新的 insight 或开辟新方向
2. ✅ 好验证 — 有清晰的实验设计，结果可预期
3. ✅ 有成熟 baseline — 不需要从头造轮子
4. ✅ 与 Yu 的 expertise 匹配 — information theory, representation learning

**反问：什么样的 contribution 是有价值的？**
- 发现一个新现象（empirical）
- 解释一个已知现象（theoretical）
- 提出一个新问题（problem formulation）
- 解决一个已知问题（method）

---

## Idea 筛选

### ❌ 不做的方向

| 方向 | 原因 |
|------|------|
| Inference acceleration | 太 incremental，竞争激烈 |
| Architecture design | 没有理论 motivation |
| Multimodal dLLM | 工程量大，不适合 PhD 初期 |
| Long context | 需要大量计算资源 |

### ✅ 值得考虑的方向

---

## Idea 1: Information Flow in dLLM vs AR

**核心问题：** dLLM 的 bidirectional attention 到底带来了多少 information gain？

**第一性原理：**
- AR: I(X_i; X_j) 只能通过 X_{<i} 传递（间接）
- dLLM: I(X_i; X_j) 可以直接传递（bidirectional attention）
- 假设：dLLM 的 token-wise MI 应该更高

**实验设计：**
```
1. 用 MINE/InfoNCE 估计 I(X_i; X_j | prompt)
2. 比较 LLaDA vs LLaMA (same size, same data)
3. 在不同任务上分析：
   - Reasoning tasks: 预期 dLLM MI 更高
   - Simple generation: 可能差不多
4. 分析 MI 与 task performance 的相关性
```

**Baseline 代码：**
- LLaDA: https://github.com/ML-GSAI/LLaDA (official)
- LLaMA: HuggingFace
- MI estimation: https://github.com/gtegner/mine-pytorch

**预期贡献：**
- 首次量化 dLLM vs AR 的 information flow 差异
- 解释为什么 dLLM 在 reasoning 上好
- 与 Greg 的 information theory expertise 完美匹配

**风险：**
- MI estimation 在高维空间可能不准
- 需要控制好实验变量

**评分：Novelty 9/10, Feasibility 7/10, Match 10/10**

---

## Idea 2: Probing dLLM Representations

**核心问题：** dLLM 学到的 representations 有什么独特性？

**第一性原理：**
- AR 模型的 representation 是 "predictive" — 预测下一个 token
- dLLM 的 representation 是 "reconstructive" — 重建 masked tokens
- 假设：dLLM representations 应该 encode 更多 global/semantic 信息

**实验设计：**
```
1. 提取 LLaDA vs LLaMA 的 hidden states
2. Probing tasks:
   - Syntactic: POS, dependency
   - Semantic: NER, SRL, coreference
   - Reasoning: simple logic, arithmetic
3. 特别分析 masked positions 的 representations
4. Layer-wise analysis: 哪一层差异最大？
```

**Baseline 代码：**
- Probing: https://github.com/john-hewitt/structural-probes
- LLaDA/LLaMA: 同上

**预期贡献：**
- 首次系统分析 dLLM representations
- 发现 dLLM 的 unique properties
- 为后续 representation learning 改进提供 insight

**风险：**
- 可能发现差异不大（也是有价值的 negative result）
- 需要设计好 probing tasks

**评分：Novelty 8/10, Feasibility 9/10, Match 9/10**

---

## Idea 3: Privacy Leakage in dLLM

**核心问题：** dLLM 的 bidirectional attention 是否更容易 memorize training data？

**第一性原理：**
- AR 模型只能 "向前看"，memorization 是 sequential 的
- dLLM 可以 "全局看"，可能更容易 memorize global patterns
- 假设：dLLM 可能有不同的 privacy-utility trade-off

**实验设计：**
```
1. 在 canary dataset 上训练 LLaDA vs LLaMA
2. Membership Inference Attack (MIA):
   - Loss-based MIA
   - Reference-based MIA
3. 比较 privacy leakage at same utility level
4. 分析 bidirectional attention 与 memorization 的关系
```

**Baseline 代码：**
- MIA: https://github.com/privacytrustlab/ml_privacy_meter
- DP training: Opacus (PyTorch)

**预期贡献：**
- 首次研究 dLLM 的 privacy properties
- 可能发现 dLLM 有 privacy 优势或劣势
- 对 trustworthy AI 有实际意义

**风险：**
- 需要训练模型（计算资源）
- 可能需要 smaller scale 实验

**评分：Novelty 10/10, Feasibility 6/10, Match 8/10**

---

## Idea 4: Information Bottleneck Perspective on dLLM

**核心问题：** 能否用 Information Bottleneck 理论解释 dLLM？

**第一性原理：**
- IB: min I(X; Z) s.t. I(Z; Y) ≥ threshold
- dLLM 的 diffusion process 可以看作 progressive compression
- 假设：dLLM 自然实现了某种 IB trade-off

**实验设计：**
```
1. 分析 dLLM 不同 timestep 的 I(X; Z_t) 和 I(Z_t; X_0)
2. 画出 information plane trajectory
3. 与 AR 模型的 layer-wise information 对比
4. 研究 noise schedule 对 IB trade-off 的影响
```

**Baseline 代码：**
- Information plane: https://github.com/ravidziv/IDNNs
- Greg 的 CorEx 相关代码

**预期贡献：**
- 用 IB 理论统一理解 dLLM
- 解释 XDLM 的 sweet spot (k=0.1)
- 理论贡献大，与 Greg 的 research 高度相关

**风险：**
- 理论性强，需要数学功底
- MI estimation 在 diffusion 过程中可能有挑战

**评分：Novelty 9/10, Feasibility 5/10, Match 10/10**

---

## 综合推荐

### 🥇 首选：Idea 2 (Probing dLLM Representations)

**理由：**
- Feasibility 最高，1-2 周可以出初步结果
- 不需要训练模型，只需要 inference
- 结果无论正负都有价值
- 为后续 Idea 1, 4 打基础

**具体 action plan：**
1. Week 1: 下载 LLaDA-8B, LLaMA-8B，设置 probing pipeline
2. Week 2: 跑 syntactic probing (POS, dependency)
3. Week 3: 跑 semantic probing (NER, SRL)
4. Week 4: 分析结果，写 initial findings

### 🥈 次选：Idea 1 (Information Flow Analysis)

**理由：**
- 与 Greg 的 expertise 完美匹配
- 理论贡献大
- 但 MI estimation 有技术挑战

**建议：** 在 Idea 2 有初步结果后，再开始 Idea 1

### 🥉 备选：Idea 3 (Privacy)

**理由：**
- 完全空白的方向，novelty 最高
- 但需要训练模型，资源要求高
- 可以先做 smaller scale pilot study

---

## 下一步

1. **立即开始 Idea 2** — 下载模型，设置环境
2. **同时阅读** — Greg 的 information theory papers，理解他的 approach
3. **2 周后 checkpoint** — 根据 Idea 2 的结果决定是否 pivot

---

## 自我 Challenge：这些 idea 真的好吗？

### Challenge 1: Probing 是不是太 incremental 了？

**反驳：**
- Probing AR models 已经做烂了（BERTology 那一套）
- 但 dLLM probing 真的没人做过
- 关键是要有 **新发现**，不是简单套用

**如何避免 incremental：**
- 不只是 "dLLM 也能做 probing"
- 要回答 "dLLM 的 representation 有什么 **独特** 的"
- 特别关注 **masked positions** 的 representation — 这是 dLLM 独有的

### Challenge 2: MI estimation 真的可行吗？

**问题：**
- 高维 MI estimation 是 notoriously hard
- MINE 在 >100 维时 variance 很大
- LLM hidden states 是 4096 维

**解决方案：**
- 用 PCA 降维后再估计
- 或者用 CKA (Centered Kernel Alignment) 作为 proxy
- 或者只估计 specific token pairs 的 MI

### Challenge 3: Privacy 实验需要多少资源？

**估算：**
- 训练 1B 模型：~100 GPU hours
- 训练 8B 模型：~1000 GPU hours
- MIA 实验本身不需要太多资源

**可行方案：**
- 用 smaller models (125M, 350M) 做 pilot
- 或者用 fine-tuning 而不是 from-scratch training
- 或者分析 existing checkpoints 的 memorization

---

## 更深层的思考：什么是真正的 contribution？

### 学术贡献的层次

1. **最低层：** 在新数据/任务上跑已有方法 → 不要做
2. **中间层：** 提出新方法解决已知问题 → 可以做，但要有 insight
3. **较高层：** 发现新现象/提出新问题 → 值得做
4. **最高层：** 建立新理论/统一已有理解 → 最值得做，但最难

### 这些 idea 在哪个层次？

| Idea | 层次 | 说明 |
|------|------|------|
| Probing | 2-3 | 如果只是跑 probing → 层次 2；如果发现新现象 → 层次 3 |
| MI Analysis | 3-4 | 发现 MI 差异 → 层次 3；建立理论解释 → 层次 4 |
| Privacy | 3 | 发现 dLLM 的 privacy 特性 → 新现象 |
| IB Theory | 4 | 用 IB 统一理解 dLLM → 理论贡献 |

### 结论

**最有价值的路径：**
1. 从 Probing (层次 2-3) 开始，积累对 dLLM 的理解
2. 发现有趣现象后，用 MI/IB 理论解释 (层次 3-4)
3. 最终目标是 **理论贡献**，不是 empirical tricks

---

## Final Recommendation

**短期 (1-2 months):** Probing + 初步 MI analysis
- 目标：发现 dLLM representation 的独特性
- 产出：Workshop paper 或 technical report

**中期 (3-6 months):** 深入 MI/IB 理论分析
- 目标：用 information theory 解释发现的现象
- 产出：Top venue paper (NeurIPS/ICML/ICLR)

**长期 (6-12 months):** Privacy 或 Causal 方向
- 目标：开辟新的研究方向
- 产出：有影响力的工作

---

*Generated: 2026-02-16*
*For: Yu (Ted) - PhD @ UCR with Greg Ver Steeg*
