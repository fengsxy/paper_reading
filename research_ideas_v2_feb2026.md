# dLLM Research Ideas v2 - 更深的第一性原理

*2026-02-16 更新*

---

## 🔬 更深层的反问

### 反问 1: dLLM 和 AR 的本质差异到底是什么？

之前说的 "bidirectional vs causal" 太表面了。让我们更深入：

**AR 模型的本质：**
- 学习 P(x_t | x_{<t}) — 条件概率
- 训练目标：最大化 log P(x_t | x_{<t})
- 信息流：单向，从左到右
- **隐含假设：语言是因果生成的**

**dLLM 的本质：**
- 学习 P(x_0 | x_t, t) — 去噪
- 训练目标：最小化 ||x_0 - f(x_t, t)||
- 信息流：双向，全局
- **隐含假设：语言是可以从噪声中恢复的**

**关键 insight：**
> AR 假设语言有因果结构，dLLM 假设语言有全局结构。
> 这两个假设哪个更符合人类语言的本质？

**反问：** 人类写作是 "从左到右" 还是 "先有大纲再填充"？
- 写代码：先写函数签名，再填充实现 → 更像 dLLM
- 写论文：先写 outline，再写细节 → 更像 dLLM
- 日常对话：确实是 sequential → 更像 AR

**结论：** dLLM 可能更适合 **结构化任务**（代码、数学、逻辑），AR 更适合 **流式任务**（对话、叙事）。

---

### 反问 2: 为什么 dLLM 在 reasoning 上好？

现有解释（latent tokens, bidirectional attention）都是 **描述性的**，不是 **解释性的**。

**更深的问题：**
- Reasoning 需要什么能力？
- dLLM 的哪个特性提供了这个能力？

**Reasoning 的本质：**
1. **约束满足** — 多个条件同时成立
2. **全局一致性** — 答案要和所有前提一致
3. **回溯** — 发现错误时能修正

**AR 的问题：**
- 单向生成，无法回溯
- 每个 token 只看到前面的，无法保证全局一致
- 一旦犯错，错误会 cascade

**dLLM 的优势：**
- 双向 attention 允许 "看到未来"
- 迭代 refinement 允许修正错误
- Joint prediction 强制全局一致

**关键 insight：**
> dLLM 的优势不是 "更多信息"，而是 "更好的约束传播"。
> Reasoning 本质上是约束满足问题，dLLM 的架构天然适合这个。

---

### 反问 3: 现有的 dLLM 论文到底在解决什么问题？

让我重新审视 66 篇论文：

| 问题类型 | 论文数 | 本质 |
|----------|--------|------|
| 太慢 | 53 | 工程问题，不是科学问题 |
| 生成质量差 | 8 | 可能是真问题，但解决方案都是 heuristics |
| 不理解为什么 work | 3 | 真正的科学问题，但没人深入 |
| 新应用 | 2 | 套用，不是创新 |

**结论：** 整个领域都在做 **工程优化**，没人在做 **科学理解**。

---

## 💡 新的 Idea（基于更深的思考）

### Idea 5: dLLM 作为约束满足器

**核心假设：** dLLM 的优势来自于它是一个 **implicit constraint solver**。

**理论框架：**
```
Reasoning problem: Find x such that C1(x), C2(x), ..., Cn(x) all hold

AR approach: 
- Generate x sequentially
- Hope constraints are satisfied
- No mechanism to enforce global consistency

dLLM approach:
- Start with random x
- Iteratively refine to satisfy constraints
- Bidirectional attention propagates constraint information
```

**实验设计：**
```
1. 设计 constraint satisfaction benchmarks:
   - Sudoku (hard constraints)
   - Logic puzzles (soft constraints)
   - Math word problems (mixed constraints)

2. 分析 dLLM 的 denoising 过程:
   - 每一步 constraint satisfaction 程度如何变化？
   - 哪些 constraints 先被满足？
   - Attention pattern 如何反映 constraint propagation？

3. 对比 AR + CoT vs dLLM:
   - AR 需要 explicit reasoning (CoT)
   - dLLM 是否有 implicit reasoning？
```

**预期贡献：**
- 提出 "dLLM as constraint solver" 的理论框架
- 解释为什么 dLLM 在 reasoning 上好
- 可能启发新的 dLLM 设计

**Baseline 代码：**
- LLaDA: 已有
- Constraint satisfaction metrics: 需要自己设计
- Attention analysis: TransformerLens

**评分：Novelty 10/10, Feasibility 7/10, Match 9/10**

---

### Idea 6: dLLM 的 "思考" 在哪里发生？

**核心问题：** AR 模型的 reasoning 发生在 CoT tokens 里。dLLM 的 reasoning 发生在哪里？

**假设：**
- AR: reasoning in token space (explicit)
- dLLM: reasoning in latent space (implicit)

**实验设计：**
```
1. 对比有无 CoT 的 dLLM:
   - dLLM + CoT vs dLLM without CoT
   - 如果 dLLM without CoT 也能 reason，说明 reasoning 在 latent space

2. 分析 hidden states 的演化:
   - 在 denoising 过程中，hidden states 如何变化？
   - 是否能观察到 "reasoning trajectory"？

3. Intervention 实验:
   - 在特定 timestep 干预 hidden states
   - 观察对 reasoning 结果的影响
```

**预期贡献：**
- 揭示 dLLM 的 implicit reasoning mechanism
- 与 "latent tokens" 论文形成对话
- 可能发现新的 reasoning 范式

**评分：Novelty 9/10, Feasibility 6/10, Match 10/10**

---

### Idea 7: Total Correlation 视角

**Greg 的 expertise：** Total Correlation, CorEx, information decomposition

**核心问题：** dLLM 的 representation 是否有更低的 Total Correlation？

**理论背景：**
```
Total Correlation: TC(X1, ..., Xn) = sum(H(Xi)) - H(X1, ..., Xn)
- 衡量变量之间的 redundancy
- TC = 0 意味着变量独立
- 高 TC 意味着高 redundancy
```

**假设：**
- AR 模型的 representation 可能有高 TC（因为每个 token 都要 encode 前面的信息）
- dLLM 的 representation 可能有低 TC（因为信息可以分布在不同 tokens）

**实验设计：**
```
1. 用 CorEx 估计 LLaDA vs LLaMA 的 TC
2. 分析 TC 与 task performance 的关系
3. 研究 TC 在不同 layers 的变化
```

**预期贡献：**
- 用 Greg 的 TC 框架分析 dLLM
- 可能发现 dLLM 的 information-theoretic 优势
- 与导师的 research 高度相关

**Baseline 代码：**
- CorEx: https://github.com/gregversteeg/CorEx
- Greg 的其他 TC 相关代码

**评分：Novelty 8/10, Feasibility 8/10, Match 10/10**

---

## 🎯 更新后的推荐

### 最佳组合策略

**Phase 1 (Month 1-2): 探索性实验**
- Idea 2 (Probing) + Idea 7 (TC analysis)
- 目标：理解 dLLM representation 的特性
- 产出：Initial findings, 与 Greg 讨论

**Phase 2 (Month 2-4): 深入理论**
- Idea 5 (Constraint solver) 或 Idea 6 (Implicit reasoning)
- 目标：建立理论框架
- 产出：Workshop paper

**Phase 3 (Month 4-6): 完整论文**
- 整合 Phase 1 和 Phase 2 的发现
- 目标：Top venue submission
- 产出：NeurIPS/ICML/ICLR paper

---

## 🔥 最推荐的单一 Idea

如果只能选一个，我推荐 **Idea 7 (Total Correlation)**：

**理由：**
1. **与 Greg 的 expertise 完美匹配** — 他是 TC/CorEx 的专家
2. **有成熟的工具** — CorEx 代码已经存在
3. **Novelty 高** — 没人用 TC 分析过 dLLM
4. **Feasibility 高** — 不需要训练模型
5. **可以扩展** — 如果发现有趣结果，可以深入到 Idea 5/6

**具体 action plan：**
```
Week 1: 
- 阅读 Greg 的 TC/CorEx papers
- 下载 LLaDA-8B, LLaMA-8B
- 设置 CorEx 环境

Week 2:
- 提取两个模型的 hidden states
- 计算 TC

Week 3:
- 分析结果
- 与 Greg 讨论

Week 4:
- 根据讨论决定下一步
```

---

## 📚 必读论文（更新）

### Greg Ver Steeg 的论文
1. **Discovering Structure in High-Dimensional Data Through Correlation Explanation** (CorEx)
2. **Maximally Informative Hierarchical Representations of High-Dimensional Data** (CorEx++)
3. **The Information Sieve** 
4. **Unsupervised Learning via Total Correlation Explanation**

### dLLM 理论相关
1. **Reasoning with Latent Tokens** (2602.03769) — latent reasoning
2. **XDLM** (2602.01362) — understanding vs generation trade-off
3. **Attention Floating** (2601.07894) — attention mechanism analysis

---

*Updated: 2026-02-16*
*Key insight: 用 Greg 的 TC 框架分析 dLLM 是最佳切入点*
