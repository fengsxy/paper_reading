# Daily Paper Review — 2026-04-02

**Paper**: Why Gaussian Diffusion Models Fail on Discrete Data?
**arXiv ID**: 2604.02028v1
**Date**: 2026-04-02
**Tag**: dLLM / Theory / Discrete Data

---

## 1. Task

**问题形式化**：

Gaussian diffusion models 在连续域（图像、音频）取得了巨大成功，但直接应用于离散数据时效果很差。

论文用一个 **Random Hierarchy Model** 的 toy case，系统性地分析为什么 DDPM solver 在离散数据上失效。

**目标**：揭示 Gaussian diffusion 在离散数据上的根本性失败机制。

---

## 2. Challenge

| 方法 | 困境 |
|------|------|
| 直接在离散数据上用 Gaussian diffusion | 连续噪声在离散空间中没有意义 |
| Discrete diffusion（absorbing state 等） | 有效但收敛慢 |
| 替代的 noise 策略 | 缺乏理论解释 |

**根本问题**：Gaussian noise 对离散数据来说"不是自然的"——它假设数据可以被理解为连续空间中的一个点加上高斯扰动，但离散 token 没有这种连续结构。

---

## 3. Insight & Novelty

**核心发现**：Gaussian diffusion 在离散数据上的失败来自两个根本原因。

**Reason 1**：Mode collapse in the score function
> 离散数据在连续空间中被表示为 mixture of delta distributions（如 one-hot vectors）。在这些 delta 位置之间，score function（梯度）是未定义的或不稳定的。
>
> 当 DDPM 的 solver 尝试在这些"空隙"中采样时，没有正确的 score signal 来引导方向。

**Reason 2**：The diffusion-sampling mismatch
> Forward process 添加 Gaussian noise，把 discrete tokens 变成连续的"模糊"分布。
> 但 denoising solver 假设数据可以用连续分布很好地近似。
>
> 当 noise level 降低时，离散数据的 delta 性质重新出现，但 solver 仍在用连续近似，导致 mismatch。

**创新点 1**：Random Hierarchy Model 作为一个最小化测试床
- **解决的问题**：如何系统性地分析离散 diffusion 的失败
- **受启发于**：Toy model 可以控制变量，揭示本质机制
- **具体设计**：层级结构的离散数据，模拟真实语言的 token 依赖

**创新点 2**：Mode collapse 的正式证明
- **解决的问题**：为什么 score function 在离散数据上失效
- **受启发于**：Delta distribution 的数学性质 → score 不连续
- **具体设计**：证明当数据是 mixture of deltas 时，最优 score 是 0 或无穷大（无中间值）

---

## 4. Potential Flaw

### 4.1 情境局限

- **Toy model 过于简化**：真实语言的 token 结构比 Random Hierarchy Model 复杂得多
- **只在 DDPM solver 上验证**：其他 solver（如 SDE）可能有不同的行为

### 4.2 数据问题

- **替代的 noise 策略（如 discrete noise）**：虽然暗示了有其他选择，但没有充分探索
- **实际有效的 discrete diffusion 方法**：没有解释为什么 absorbing state 或 uniform noise 的方法有效

### 4.3 值得挖掘的方向

**最值得做的**：为什么某些 discrete diffusion 变体（如 absorbing state、uniform noise）work。

> 论文揭示了 Gaussian diffusion 在离散数据上的失败，但没有充分解释"什么替代方案 work，以及为什么"。
>
> 核心问题：从信息论角度，离散数据的"自然"噪声是什么？答案可能是：**任何 preserve 离散结构的噪声**——即 noise that respects the discrete topology of the data manifold。

---

## 5. Motivation

**General idea 推导路径**（第一性原理）：

> Gaussian diffusion 的核心假设：**数据在连续空间中有良好的定义，可以用高斯扰动来建模不确定性**。
>
> 这个假设在图像上成立——像素值是 0-255 的连续值，加高斯噪声是有物理意义的。
>
> 但 token 是离散的——"猫"和"狗"之间的距离是什么？没有自然定义。
>
> 当你在离散 token 上加 Gaussian noise 时，你实际上在做一件事：**把离散数据 embedding 到连续空间，然后加噪声**。
>
> 但 embedding 本身是任意的——"猫" embedding 成 [0.1, 0.3, ...] 只是方便计算，不代表"猫"的语义连续性。
>
> 这就是根本问题：**Gaussian diffusion 依赖连续空间的几何结构，但离散 token 没有这种结构。**