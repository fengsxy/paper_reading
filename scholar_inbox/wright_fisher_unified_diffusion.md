# Wright-Fisher Unified Diffusion: 从群体遗传学统一三种 Diffusion

**论文:** A Unification of Discrete, Gaussian, and Simplicial Diffusion  
**arXiv:** 2512.15923  
**关键词:** Wright-Fisher model, Population genetics, Unified diffusion theory

---

## 1. 问题背景：Diffusion 的三种形态

目前存在三种主要的 diffusion 方法：

### 1.1 Gaussian Diffusion
- 用于连续数据（图像）
- Forward: 加 Gaussian noise
- Backward: 预测并去除 noise
- 代表：DDPM, Score-based models

### 1.2 Discrete Diffusion
- 用于离散数据（文本）
- Forward: 随机 mask 或 corrupt tokens
- Backward: 预测原始 tokens
- 代表：D3PM, MDLM, LLaDA

### 1.3 Simplicial Diffusion
- 在 probability simplex 上操作
- 数据表示为 categorical distribution
- 代表：Dirichlet diffusion

**核心问题：** 这三种方法看起来很不同，但有没有统一的理论框架？

---

## 2. Wright-Fisher 模型：来自群体遗传学的灵感

### 2.1 什么是 Wright-Fisher 模型？

Wright-Fisher 模型是群体遗传学中描述 **等位基因频率演化** 的经典模型。

想象一个种群中有两种等位基因 A 和 a：
- 当前代：A 的频率是 p，a 的频率是 1-p
- 下一代：随机采样 N 个个体，A 的新频率是 p'

这个过程可以用 **binomial sampling** 描述：

$$p' \sim \frac{1}{N} \text{Binomial}(N, p)$$

### 2.2 连续时间极限

当种群大小 N → ∞，时间离散化 → 0，Wright-Fisher 过程收敛到一个 **SDE**：

$$dp = \sqrt{p(1-p)} \, dW$$

其中 dW 是 Wiener process（布朗运动）。

关键特性：
- 在 p=0 和 p=1 处有 **absorbing boundaries**
- 最终会 **fixate** 到某一个等位基因

### 2.3 多等位基因情况

如果有 K 个等位基因，频率向量 **p** = (p₁, ..., pₖ) 在 **simplex** 上：

$$\sum_{i=1}^{K} p_i = 1, \quad p_i \geq 0$$

Wright-Fisher SDE 变成：

$$dp_i = \sqrt{p_i(1 - p_i)} \, dW_i - \sum_{j \neq i} \sqrt{p_i p_j} \, dW_{ij}$$

这就是 **simplicial diffusion** 的理论基础！

---

## 3. 统一框架：三种 Diffusion 的联系

### 3.1 核心洞察

论文的核心发现：

> **Gaussian diffusion 和 Simplicial diffusion 都是 Wright-Fisher 模型的不同 large-population limits。**

具体来说：

| Diffusion 类型 | Wright-Fisher 极限 | 数学形式 |
|---------------|-------------------|---------|
| Discrete | 有限种群 | Multinomial sampling |
| Simplicial | 种群 → ∞，保持 simplex | Wright-Fisher SDE |
| Gaussian | 种群 → ∞，simplex → ℝⁿ | Ornstein-Uhlenbeck process |

### 3.2 从 Discrete 到 Simplicial

Discrete diffusion 可以看作是在 **有限种群** 上的 Wright-Fisher：

- Vocabulary size K = 种群中的等位基因数
- Token = 当前 "fixated" 的等位基因
- Masking = 让频率回到 uniform（所有等位基因等概率）

当我们把 one-hot token 表示 "软化" 为 probability distribution，就得到 simplicial diffusion。

### 3.3 从 Simplicial 到 Gaussian

Simplex 上的 Wright-Fisher SDE：

$$dp_i = \sqrt{p_i(1 - p_i)} \, dW_i - \sum_{j \neq i} \sqrt{p_i p_j} \, dW_{ij}$$

当 K → ∞ 且做适当的 rescaling，simplex "展平" 成 ℝⁿ，得到：

$$dx = -\frac{1}{2}x \, dt + dW$$

这就是 **Ornstein-Uhlenbeck process**，即 Gaussian diffusion 的 forward process！

---

## 4. 技术细节

### 4.1 Likelihood 的统一形式

三种 diffusion 的 likelihood 可以统一写成：

$$\log p(x_0 | x_T) = \mathbb{E}\left[ \int_0^T \mathcal{L}(x_t, s_\theta(x_t, t), t) \, dt \right]$$

其中 $\mathcal{L}$ 是 **local loss**，$s_\theta$ 是 **score function**。

不同 diffusion 类型对应不同的 $\mathcal{L}$：

| 类型 | Local Loss |
|-----|-----------|
| Gaussian | $\|s_\theta - \nabla \log p_t\|^2$ |
| Simplicial | KL divergence on simplex |
| Discrete | Cross-entropy |

### 4.2 数值稳定性问题

Simplicial diffusion 有一个实际问题：在 simplex 边界附近数值不稳定。

当 $p_i \to 0$ 时，$\sqrt{p_i}$ 的导数 → ∞，导致梯度爆炸。

论文提出的解决方案：
1. **Boundary regularization**: 在边界附近加 regularization
2. **Reparametrization**: 用 log-ratio 参数化代替直接参数化

### 4.3 跨域训练

统一框架的一个好处：可以训练 **单一模型** 处理多种数据类型。

实验设置：
- 同时在 continuous（图像）和 discrete（文本）数据上训练
- 测试时可以在任意 domain 做 diffusion

结果：跨域训练的模型与单域训练的模型性能相当！

---

## 5. 实验结果

### 5.1 DNA Sequence Generation

任务：生成符合特定 motif 的 DNA 序列

| Method | Motif Match ↑ | Diversity ↑ |
|--------|--------------|-------------|
| Discrete Diffusion | 0.72 | 0.65 |
| Dirichlet Diffusion | 0.68 | 0.71 |
| **Wright-Fisher Simplicial** | **0.81** | **0.73** |

Wright-Fisher simplicial diffusion 在 conditional generation 上显著优于之前方法。

### 5.2 Multi-Domain Training

| Training | Image FID ↓ | Text PPL ↓ |
|----------|-------------|------------|
| Image only | 3.2 | - |
| Text only | - | 12.5 |
| **Joint** | **3.4** | **12.8** |

联合训练只有轻微的性能下降，但获得了一个统一的模型。

---

## 6. 深度分析

### 6.1 为什么群体遗传学的模型适用于 ML？

表面上看，群体遗传学和机器学习是完全不同的领域。但深层的数学结构是相同的：

| 群体遗传学 | 机器学习 |
|-----------|---------|
| 等位基因频率 | Token probability |
| 种群演化 | Diffusion process |
| Fixation | Sampling a token |
| Selection | Conditioning |

这种 **跨领域的数学统一** 是非常有价值的，因为：
1. 可以借用群体遗传学的成熟理论
2. 提供了新的直觉和分析工具

### 6.2 Selection 的概念

在群体遗传学中，**selection** 描述某些等位基因比其他等位基因更有优势：

$$dp_i = s_i p_i(1 - p_i) \, dt + \text{noise}$$

其中 $s_i$ 是 **selection coefficient**。$s_i > 0$ 意味着等位基因 i 更容易 fixate。

**对 dLLM 的启发：**

> 能否定义 token 的 "selection coefficient"？
> 
> $s_i$ 大的 token 应该更早被确定（更容易 "fixate"）。
> 
> 这可能给出 optimal ordering 的理论基础！

### 6.3 Fixation Time

群体遗传学中有一个重要概念：**fixation time**——等位基因从初始频率到完全 fixate 需要多长时间。

对于 neutral evolution（无 selection）：

$$\mathbb{E}[T_{fix}] \propto N$$

对于有 selection 的情况：

$$\mathbb{E}[T_{fix}] \propto \frac{\log N}{s}$$

**对 dLLM 的启发：**

> Token 的 "fixation time" 可能对应于它应该在第几步被确定。
> 
> High selection coefficient → 短 fixation time → 早期确定
> Low selection coefficient → 长 fixation time → 后期确定

---

## 7. 对 dLLM 研究的启发

### 7.1 理论基础

这篇论文给 dLLM 提供了更深的理论基础：

- dLLM 的 forward process（masking）= Wright-Fisher 的 "回到 uniform"
- dLLM 的 backward process（unmasking）= Wright-Fisher 的 "fixation"

### 7.2 Optimal Ordering 的新视角

用 Wright-Fisher 框架思考 optimal ordering：

1. 每个 token position 有一个 "selection coefficient" $s_i$
2. $s_i$ 取决于：
   - Token 本身的 "difficulty"
   - 与其他 token 的依赖关系
   - 当前的 context

3. Optimal ordering = 按 expected fixation time 排序

### 7.3 具体研究方向

**Idea 1: Selection Coefficient Estimation**

训练一个模型预测每个 position 的 selection coefficient：

$$s_i = f_\theta(x_{masked}, i)$$

然后按 $s_i$ 从大到小的顺序生成。

**Idea 2: Adaptive Diffusion Schedule**

不同 token 用不同的 diffusion schedule：

- High $s_i$ tokens: 快速 denoise（少步数）
- Low $s_i$ tokens: 慢速 denoise（多步数）

**Idea 3: Theoretical Analysis**

用 Wright-Fisher 的数学工具分析 dLLM：

- Fixation probability
- Expected generation time
- Variance of output

---

## 8. 局限性

### 8.1 计算复杂度

Wright-Fisher SDE 的模拟比简单的 Gaussian diffusion 更复杂。

### 8.2 高维 Simplex

当 vocabulary size K 很大时（如 32K），simplex 是高维的，数值问题更严重。

### 8.3 理论 vs 实践

虽然理论上统一了三种 diffusion，但实践中 Gaussian diffusion 仍然是图像生成的首选。

---

## 9. 总结

Wright-Fisher Unified Diffusion 的贡献：

1. **理论统一**: 证明了 discrete、Gaussian、simplicial diffusion 都是 Wright-Fisher 模型的极限
2. **新工具**: 引入群体遗传学的概念（selection, fixation）到 diffusion
3. **实践改进**: Wright-Fisher simplicial diffusion 在 DNA generation 上达到 SOTA

**对 dLLM 最重要的启发：**

> Selection coefficient 可能是理解 optimal ordering 的关键。
> 
> 哪些 token 应该先生成？那些 "selection pressure" 大的——即对最终结果影响最大、最容易确定的 token。

---

## 参考

- arXiv:2512.15923
- Wright-Fisher model (Fisher, 1930; Wright, 1931)
- D3PM (Austin et al., 2021)
- Score-based generative models (Song et al., 2021)
