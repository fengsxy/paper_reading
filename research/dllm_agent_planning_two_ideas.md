# dLLM for Planning: Two New Research Directions

*Date: 2026-04-07*
*Tags: dLLM, Diffusion Model, Planning, Agent*

---

今天和朋友（@fengsxy）聊了两个关于 **Diffusion Large Language Models (dLLM)** 在 Agent 规划方面的新想法。整理一下，看看有没有人感兴趣。

---

## Background

当前主流的 Agent 都是基于 **Autoregressive (AR) LLM** 构建的 — GPT 系列、Claude 系列都是 AR 模型。它们的特点是**逐 token 生成**，就像打字一样一个字一个字往外蹦。

但 dLLM（diffusion language model）完全不同 — 它的工作方式是**从噪声中逐步去噪**，类似于图像生成模型（如 Stable Diffusion）的工作方式。

> 核心问题：**如果用 dLLM 来做 Agent 规划，会有什么不同的特性？**

---

## Idea 1: Hard/Soft Constraints 分离 + 动态约束松弛

### 问题的核心矛盾

DeepPlanning 数据集（NeurIPS 2025）揭示了一个经典困境：

| 约束类型 | 特点 | 现有方法 |
|---------|------|---------|
| **Hard Constraints** | 可验证、必须满足 | Symbolic / PDDL |
| **Soft Constraints** | 模糊、无法编码 | LLM 学到的偏好 |

**问题**：如果约束太强，Symbolic 方法能解决但表达不了自然语言偏好；如果约束太弱，LLM 穷举太慢。

### 核心假设

> **dLLM 能够做到软约束 + 硬约束相互结合的 Plan。软约束不需要被显式编码 — dLLM 学会的是"推理模式"而非"具体 Plan"。**

LLM 在预训练中见过大量人类写的行程规划，所以它**已经知道**什么样的行程是"好的"。这不需要显式编码，是隐式的知识。

### 方法框架

```
Hard Constraints → Verifier (Symbolic) → 100% 保证满足
Soft Constraints → dLLM 推理能力 → 学到的偏好分布
```

### 约束松弛的创新

更进一步：**当 Hard Constraints 满足不了时，dLLM 自己决定如何松弛。**

```
原始约束: C = {c1, c2, ..., cn}
约束代价: cost(c_i) = 松弛 c_i 的"痛苦程度"

dLLM 决策:
  1. 尝试满足所有约束
  2. 如果失败 → dLLM 自己选择松弛哪条
  3. 选择总代价最小的松弛方案
```

这模拟了人类的真实决策过程："预算超一点，但去了更好的餐厅"。

### 为什么 dLLM 可能做到 AR 不能做到的？

AR LLM 做 selection 的本质问题是：**它没有验证机制**。它是在做"看起来不错"的判断，而不是系统性验证所有约束。

dLLM 的优势：
- **并行评估**：一次 denoise 可以同时生成多个候选plans
- **隐式约束传播**：去噪的每一步都隐式包含对全局约束的感知
- **软约束的 learned prior**：不需要编码，训练数据中已经包含了人类偏好的分布

### 相关工作参考

- **Planned Diffusion** (2025): AR + Diffusion 混合生成
- **Constrained Synthesis with Projected Diffusion** (NeurIPS 2024): 约束投影到满足空间
- **Constraints-Guided Diffusion Reasoner** (2025): PPO fine-tune 做逻辑约束
- **DeepPlanning** (NeurIPS 2025): 当前模型的 case accuracy 只有 ~35-60%

---

## Idea 2: dLLM-native Agent 架构

### AR Agent 的架构限制

```
User Query → Think → Act → Observe → Think → Act → ...
                      ↑
                 严格顺序执行
```

AR Agent 的问题：
- **一步等一步**：Tool calls 必须串行
- **Replanning 代价高**：发现错误就丢弃重来
- **错误累积**：早期决策影响后期

### dLLM Agent 的新范式

```
User Query → [Noise + Constraints] → Denoise → Candidate Plans → Verify → Refine → Final Plan
                                ↑
                      并行探索多个解的隐空间
```

### 核心特性

#### 1. Parallel Candidate Generation

AR 探索 5 个方案需要 5 次完整 forward。dLLM 一次 denoise 可以并行生成多个候选plans。

```
AR: 
  prompt → Plan A (可能不好) → 重新 prompt → Plan B ...
  
dLLM:
  x_T = noise
  denoise(x_T, constraints) → 同时生成 [Plan A, Plan B, Plan C]
  → 选择最好的
```

#### 2. Iterative Refinement 而非 Replanning

AR: 发现错误 → 丢弃重来（之前的计算浪费）
dLLM: 发现部分错误 → 在隐空间中修正（复用之前计算）

```
AR replanning:
  Plan A 在 step 3 失败 → 从头生成 Plan B (100% 重新计算)

dLLM refinement:
  Plan A 违反 budget → refine(Plan A, feedback) → Plan A'
  (保留了 step 1-2 的计算)
```

#### 3. 并行 Tool Use

AR 的工具调用是严格顺序的：
```
Step 1: call search_flights (等待)
Step 2: call search_hotels (必须等 Step 1 结果)
Step 3: ...
```

dLLM 可能实现真正的并行：
```
同时 call [search_flights, search_hotels, get_weather, get_reviews]
→ 一次性获取所有信息
→ 在完整信息下生成 plan
```

### 为什么 dLLM-native Agent 可能更好？

| 维度 | AR Agent | dLLM-native Agent |
|------|----------|-------------------|
| 生成方式 | Token-by-token | Parallel denoising |
| 多路径探索 | Beam search (昂贵) | 噪声本身提供多样性 |
| 错误处理 | Replanning (浪费) | Refinement (复用) |
| 全局一致性 | Error propagation | 全局调整 |
| 工具调用 | Sequential | Parallel |

---

## 实验设计建议

### Exp 1: Hard Constraint Satisfaction

使用 DeepPlanning 改造版：
- 添加"不可满足"的测试用例
- 测试 dLLM + Verifier 的约束满足率
- Baseline: AR LLM + Verifier

### Exp 2: Constraint Relaxation Decision

- 新增"约束冲突"场景
- 测试 dLLM 是否做出合理的 trade-off
- 评估：松弛决策的合理性、最小代价

### Exp 3: dLLM-native Agent vs AR Agent

- 在 DeepPlanning 上对比
- 指标：性能、效率（token 消耗）、多路径探索能力

---

## 待解决的问题

1. **Tool Use 模式**：dLLM 如何调用工具？并行还是顺序？
2. **Verifier Feedback**：如何设计 feedback 让 dLLM 能定位问题？
3. **1024-char 限制**：压缩表示是否会丢失关键信息？
4. **Evaluation**：如何公平对比 dLLM-native 和 AR agent？

---

## 结论

dLLM 在 Agent 规划方面有两个潜在的颠覆性方向：

1. **Hard/Soft 分离**：用 Symbolic 处理 hard constraints，用 dLLM 的 learned prior 处理 soft constraints，加上动态松弛决策
2. **dLLM-native 架构**：利用 diffusion 的并行生成和隐空间 refinement 特性，重新设计 Agent 的基本范式

如果这两个想法结合起来，可能会诞生一种**全新的 Agent 架构** — 不是"给 LLM 加上工具"，而是"为 dLLM 的生成特性量身定制的 Agent"。

---

*欢迎讨论！如果你有任何想法或建议，欢迎留言。*
