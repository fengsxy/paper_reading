# Parallel Token Generation: Flow-Based 并行生成

**论文:** Parallel Token Generation for Language Models  
**OpenReview:** AGJomYSrUG  
**作者:** Mandt Lab (UCI)  
**关键词:** Multi-token prediction, Normalizing flows, Parallel generation

---

## 1. 问题背景：AR 的速度瓶颈

Autoregressive (AR) language models 是当前 LLM 的主流：

```
生成过程：
Token 1 → Token 2 → Token 3 → ... → Token N
   ↓         ↓         ↓              ↓
Forward   Forward   Forward       Forward
```

**问题：** 每个 token 需要一次 forward pass，生成 N 个 token 需要 N 次。

**目标：** 能否一次 forward pass 生成多个 token？

---

## 2. 之前的尝试及其问题

### 2.1 Speculative Decoding

思路：用小模型 draft 多个 token，大模型 verify。

```
小模型: 生成 [t1, t2, t3, t4, t5]
大模型: 验证，接受 [t1, t2, t3]，拒绝 [t4, t5]
```

问题：
- 需要两个模型
- Accept rate 不稳定
- 本质上还是 AR

### 2.2 Non-Autoregressive Models (NAR)

思路：一次性预测所有 token。

```
Input → Model → [t1, t2, t3, ..., tN]
```

问题：**条件独立假设**

$$p(t_1, ..., t_N | x) = \prod_i p(t_i | x)$$

这假设 tokens 之间相互独立，丢失了 token 间的依赖关系，导致质量下降。

### 2.3 Diffusion LLM (dLLM)

思路：用 diffusion 迭代 refine。

```
Noise → Denoise → Denoise → ... → Clean tokens
```

问题：
- 仍需多步迭代
- 每步的条件独立假设

---

## 3. 本文方法：Flow-Based Parallel Generation

### 3.1 核心思想

> **用 Normalizing Flow 的思想，把随机变量确定性地转换为 token 序列。**

关键洞察：AR 模型的 sampling 过程可以看作一个 **确定性变换**：

```
随机数 z = [z1, z2, ..., zN] → Tokens [t1, t2, ..., tN]
```

如果我们能学会这个变换，就可以一次性生成所有 token！

### 3.2 Inverse Autoregressive Flow (IAF)

回顾 Normalizing Flow：

$$x = f(z), \quad z \sim p(z)$$

$$p(x) = p(z) \cdot |\det \frac{\partial f^{-1}}{\partial x}|$$

**Inverse Autoregressive Flow** 的特点：
- Forward（z → x）是并行的
- Inverse（x → z）是 autoregressive 的

这正好符合我们的需求：
- 训练时：用 AR 的方式计算 likelihood（inverse）
- 推理时：并行生成（forward）

### 3.3 具体架构

```
输入: 随机向量 z = [z1, z2, ..., zN]
      Context c

模型: Transformer f_θ

输出: Token logits [l1, l2, ..., lN]

采样: ti = argmax(li) 或 ti ~ Categorical(softmax(li))
```

关键设计：

1. **Coupling layers**: 每层只更新部分位置
2. **Autoregressive structure in reverse**: 保证 likelihood 可计算
3. **Shared Transformer backbone**: 效率高

---

## 4. 训练方法

### 4.1 从头训练

目标函数：最大化 log-likelihood

$$\mathcal{L} = \mathbb{E}_{x \sim p_{data}} [\log p_\theta(x)]$$

其中 $p_\theta(x)$ 通过 change of variables 计算：

$$\log p_\theta(x) = \log p(z) + \log |\det J|$$

### 4.2 从 AR 模型蒸馏

更实用的方法：从预训练的 AR 模型蒸馏。

```
Teacher: AR model (e.g., GPT)
Student: Flow-based parallel model

Loss: KL(p_teacher || p_student)
```

蒸馏的好处：
- 利用 AR 模型的知识
- 训练更稳定
- 不需要大量数据

---

## 5. 实验结果

### 5.1 Toy Data

任务：生成符合特定 pattern 的序列

| Method | Match Rate ↑ | Tokens/Forward |
|--------|-------------|----------------|
| AR | 100% | 1 |
| NAR (independent) | 45% | N |
| **Flow-based** | **98%** | **~50** |

Flow-based 方法在单次 forward pass 中平均匹配 ~50 个 token！

### 5.2 Code Generation

任务：代码补全

| Method | Exact Match ↑ | Tokens/Forward |
|--------|--------------|----------------|
| AR | 100% | 1 |
| Speculative (k=4) | 100% | ~2.5 |
| **Flow-based** | **95%** | **~5** |

在代码数据上，单次 forward 匹配 ~5 个 token，且保持高质量。

### 5.3 Speedup

| Method | Tokens/Second ↑ |
|--------|----------------|
| AR | 50 |
| Speculative | 85 |
| **Flow-based** | **180** |

约 3.6x 加速。

---

## 6. 技术细节

### 6.1 为什么不假设独立也能并行？

关键在于 **flow 的结构**。

传统 NAR 假设：
$$p(t_1, ..., t_N) = \prod_i p(t_i)$$

Flow-based 方法：
$$p(t_1, ..., t_N) = p(z_1, ..., z_N) \cdot |\det J|^{-1}$$

虽然 $z_i$ 是独立的，但通过 flow 的变换，$t_i$ 之间有复杂的依赖关系。

**Jacobian $J$ 编码了 token 之间的依赖！**

### 6.2 Jacobian 的计算

对于一般的 flow，Jacobian 计算是 O(N³) 的。

本文使用 **triangular Jacobian** 结构：

$$J = \begin{pmatrix}
\frac{\partial t_1}{\partial z_1} & 0 & \cdots & 0 \\
\frac{\partial t_2}{\partial z_1} & \frac{\partial t_2}{\partial z_2} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial t_N}{\partial z_1} & \frac{\partial t_N}{\partial z_2} & \cdots & \frac{\partial t_N}{\partial z_N}
\end{pmatrix}$$

这样 $\det J = \prod_i \frac{\partial t_i}{\partial z_i}$，计算是 O(N) 的。

### 6.3 与 AR 的关系

有趣的是，AR 模型可以看作 flow 的特例：

AR sampling:
```python
for i in range(N):
    logits_i = model(t[:i])
    z_i = uniform(0, 1)
    t_i = inverse_cdf(logits_i, z_i)
```

这就是一个 **autoregressive flow**！

本文的贡献是把这个过程 "反过来"，变成 **inverse autoregressive flow**，从而实现并行。

---

## 7. 深度分析

### 7.1 与 dLLM 的对比

| | dLLM | Flow-based |
|---|---|---|
| 并行机制 | Diffusion (iterative) | Flow (one-shot) |
| 依赖建模 | 通常假设条件独立 | 通过 Jacobian 建模 |
| 训练 | Denoising objective | Likelihood + Jacobian |
| 推理步数 | 多步 | 单步 |
| 质量 | 略低于 AR | 接近 AR |

### 7.2 为什么 Flow 能保持质量？

关键：**Flow 保持了 AR 的表达能力**。

数学上，任何 AR 分布都可以用 flow 表示：

$$p_{AR}(t_1, ..., t_N) = \prod_i p(t_i | t_{<i})$$

Flow 通过 Jacobian 隐式地建模了 $p(t_i | t_{<i})$。

### 7.3 局限性

1. **训练复杂**: 需要计算 Jacobian，比 AR 训练更复杂
2. **蒸馏依赖**: 最好的结果需要从 AR 模型蒸馏
3. **长序列**: 对于很长的序列，单次 forward 可能不够

---

## 8. 对 dLLM 研究的启发

### 8.1 条件独立假设的问题

这篇论文指出了 dLLM 的一个核心问题：**条件独立假设**。

当前 dLLM 在每步 denoising 时：

$$p(x_1, ..., x_N | x_{masked}) = \prod_i p(x_i | x_{masked})$$

这丢失了 token 之间的依赖，导致 incoherence。

### 8.2 结合 Flow 和 Diffusion？

一个自然的想法：能否结合两者的优点？

**Idea: Flow-Enhanced Diffusion**

```
Diffusion: 多步 refine，逐渐提高质量
Flow: 每步内部用 flow 建模 token 依赖
```

具体来说：

```python
def flow_enhanced_diffusion_step(x_t, t):
    # 1. 预测每个位置的 logits（传统 dLLM）
    logits = model(x_t, t)
    
    # 2. 用 flow 建模 token 之间的依赖
    z = sample_base_distribution()
    x_t_minus_1 = flow_transform(z, logits)
    
    return x_t_minus_1
```

### 8.3 Jacobian 作为依赖度量

Flow 的 Jacobian 编码了 token 之间的依赖强度：

$$\frac{\partial t_i}{\partial z_j} \text{ 大} \Rightarrow t_i \text{ 强依赖于 } t_j$$

这可以用来：
1. **分析 token 依赖结构**
2. **指导 generation order**：先生成被依赖多的 token

### 8.4 具体研究方向

**Idea 1: Flow-Diffusion Hybrid**

结合 flow 的单步生成和 diffusion 的迭代 refine：

- 第一步：用 flow 生成初始序列（快但可能有错）
- 后续步：用 diffusion refine（修正错误）

**Idea 2: Dependency-Aware Ordering**

用 flow 的 Jacobian 分析 token 依赖，指导 dLLM 的 generation order：

```python
def compute_dependency(model, x):
    # 计算 Jacobian
    J = compute_jacobian(model, x)
    
    # 每个 token 被依赖的程度 = 对应列的 L1 norm
    dependency_score = J.abs().sum(dim=0)
    
    # 先生成被依赖多的 token
    order = dependency_score.argsort(descending=True)
    return order
```

**Idea 3: Theoretical Analysis**

用 flow 的理论工具分析 dLLM：

- dLLM 的条件独立假设损失了多少信息？
- 能否量化 "incoherence" 和 "independence assumption" 的关系？

---

## 9. 代码示例

### 9.1 简化的 Flow-Based Generation

```python
class FlowLM(nn.Module):
    def __init__(self, vocab_size, hidden_dim, num_layers):
        super().__init__()
        self.transformer = Transformer(hidden_dim, num_layers)
        self.to_logits = nn.Linear(hidden_dim, vocab_size)
        
    def forward(self, z, context):
        """
        z: [batch, seq_len, hidden_dim] - base distribution samples
        context: [batch, context_len] - conditioning context
        """
        # Transformer 处理
        h = self.transformer(z, context)
        
        # 输出 logits
        logits = self.to_logits(h)
        
        return logits
    
    def sample(self, context, seq_len):
        """并行生成"""
        batch_size = context.shape[0]
        
        # 采样 base distribution
        z = torch.randn(batch_size, seq_len, self.hidden_dim)
        
        # 一次 forward pass
        logits = self.forward(z, context)
        
        # 采样 tokens
        tokens = torch.argmax(logits, dim=-1)
        
        return tokens
```

### 9.2 蒸馏训练

```python
def distill_from_ar(flow_model, ar_model, data_loader):
    optimizer = Adam(flow_model.parameters())
    
    for batch in data_loader:
        context, target = batch
        
        # AR 模型的分布
        with torch.no_grad():
            ar_logits = ar_model(context, target)
            ar_probs = F.softmax(ar_logits, dim=-1)
        
        # Flow 模型的分布
        z = torch.randn_like(target_embedding)
        flow_logits = flow_model(z, context)
        flow_probs = F.softmax(flow_logits, dim=-1)
        
        # KL divergence loss
        loss = F.kl_div(flow_probs.log(), ar_probs, reduction='batchmean')
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
```

---

## 10. 总结

Parallel Token Generation 的贡献：

1. **新方法**: 用 normalizing flow 实现并行生成
2. **保持质量**: 不假设 token 独立，保持 AR 的表达能力
3. **实际加速**: 单次 forward 生成 ~5 tokens（代码数据）

**对 dLLM 最重要的启发：**

> 条件独立假设是 dLLM 质量下降的重要原因。
> 
> Flow 提供了一种建模 token 依赖的方法，可能可以和 diffusion 结合。
> 
> Jacobian 可以用来分析和利用 token 依赖结构。

---

## 参考

- OpenReview: AGJomYSrUG
- Normalizing Flows (Rezende & Mohamed, 2015)
- Inverse Autoregressive Flow (Kingma et al., 2016)
- Speculative Decoding (Leviathan et al., 2023)
