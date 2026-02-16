# Drifting Models: One-Step Generation 的新范式

**论文:** Generative Modeling via Drifting  
**arXiv:** 2602.04770  
**关键词:** One-step generation, Equilibrium-based training, ImageNet SOTA

---

## 1. 问题背景：为什么我们需要 One-Step Generation？

Diffusion models 已经统治了图像生成领域，但有一个根本问题：**推理太慢**。

典型的 diffusion model 需要 50-1000 步 denoising 才能生成一张图。虽然有各种加速方法（DDIM, DPM-Solver, Consistency Models），但本质上都是在 **近似** 原始的多步过程。

**核心问题：** 能不能从根本上改变范式，让模型 **天然支持** one-step generation？

---

## 2. 传统 Diffusion 的工作方式

先回顾一下传统 diffusion 是怎么工作的：

### 训练阶段
```
Clean image x₀ → 加噪声 → Noisy image xₜ → 模型预测噪声 → Loss
```

模型学习的是：给定任意噪声水平 t 的图像，预测加的噪声是什么。

### 推理阶段
```
Pure noise xₜ → Denoise → xₜ₋₁ → Denoise → ... → x₀ (Clean image)
```

必须一步步 denoise，因为模型只学会了 "去掉一点点噪声"，不会 "一步到位"。

**问题的根源：** 训练和推理的 **不对称性**。训练时只看单步，推理时要多步。

---

## 3. Drifting Models 的核心思想

Drifting Models 提出了一个完全不同的思路：

> **训练时就让分布演化到目标分布，推理时自然只需要 one step。**

### 3.1 什么是 "Drifting"？

想象一群粒子（samples）在空间中移动：

```
初始分布 p₀ (e.g., Gaussian noise)
    ↓ 粒子移动
    ↓ 
    ↓ 
目标分布 p_data (e.g., ImageNet images)
```

每个粒子的移动由一个 **drifting field** v(x, t) 控制：

$$\frac{dx}{dt} = v(x, t)$$

当系统达到 **平衡** 时，粒子的分布就是目标分布。

### 3.2 与 Diffusion 的关键区别

| | Diffusion | Drifting |
|---|---|---|
| 训练目标 | 学习 score function ∇log p(x) | 学习 drifting field v(x, t) |
| 训练过程 | 单步 denoising | 分布演化到平衡 |
| 推理过程 | 多步迭代 | One step |
| 理论基础 | SDE/ODE | 动力系统平衡 |

### 3.3 为什么能 One-Step？

关键洞察：**训练时模型已经学会了从任意初始点到目标分布的映射**。

传统 diffusion 训练时只学 "局部" 的 denoising，所以推理时要一步步走。

Drifting 训练时学的是 "全局" 的 drifting field，所以推理时可以直接跳到终点。

---

## 4. 技术细节

### 4.1 Drifting Field 的定义

给定初始分布 p₀ 和目标分布 p_data，drifting field 满足：

$$\frac{\partial p(x, t)}{\partial t} + \nabla \cdot (p(x, t) v(x, t)) = 0$$

这是 **连续性方程**（continuity equation），描述概率质量如何随时间流动。

### 4.2 训练目标

模型 v_θ(x, t) 学习 drifting field，训练目标是让演化后的分布匹配目标分布：

$$\mathcal{L} = D_{KL}(p_T || p_{data})$$

其中 p_T 是从 p₀ 经过 drifting 演化 T 时间后的分布。

### 4.3 平衡条件

当系统达到平衡时：

$$\nabla \cdot (p_{eq}(x) v(x)) = 0$$

此时分布不再变化，p_eq = p_data。

---

## 5. 实验结果

### 5.1 ImageNet 256×256

| Method | FID ↓ | Steps |
|--------|-------|-------|
| ADM | 10.94 | 250 |
| LDM | 3.60 | 250 |
| DiT-XL | 2.27 | 250 |
| **Drifting (Latent)** | **1.54** | **1** |
| **Drifting (Pixel)** | **1.61** | **1** |

**One-step generation 达到了 SOTA！**

### 5.2 与其他 One-Step 方法对比

| Method | FID ↓ | 训练成本 |
|--------|-------|---------|
| Consistency Models | 3.55 | 需要预训练 diffusion |
| Progressive Distillation | 2.57 | 需要多阶段蒸馏 |
| **Drifting** | **1.54** | 从头训练 |

Drifting 不需要预训练的 teacher model，直接从头训练就能达到最好效果。

---

## 6. 深度分析：为什么这个方法 Work？

### 6.1 信息论视角

传统 diffusion 的问题：每一步只传递 **有限的信息**。

从 xₜ 到 xₜ₋₁，模型只能 "看到" 当前噪声水平的信息，无法利用全局结构。

Drifting 的优势：drifting field 编码了 **全局的流形结构**。

模型学会了整个数据流形的 "地图"，所以可以一步到位。

### 6.2 动力系统视角

Drifting 本质上是在学习一个 **吸引子**（attractor）。

目标分布 p_data 是系统的稳定平衡点，任何初始点都会被 "吸引" 到这个平衡点。

这和物理中的 **梯度流**（gradient flow）类似：

$$\frac{dx}{dt} = -\nabla E(x)$$

其中 E(x) 是某种 "能量函数"，系统自然演化到能量最低点。

### 6.3 与 Flow Matching 的关系

Drifting 和 Flow Matching 有相似之处，都是学习一个 vector field。

但关键区别：
- Flow Matching：学习从 noise 到 data 的 **确定性路径**
- Drifting：学习让分布 **演化到平衡** 的 field

Drifting 更强调 "平衡" 的概念，而不是 "路径"。

---

## 7. 局限性和开放问题

### 7.1 训练稳定性

让分布演化到平衡需要仔细的训练策略，否则可能不收敛。

### 7.2 理论理解

为什么 drifting field 能被神经网络有效学习？理论上还不完全清楚。

### 7.3 扩展到其他模态

目前只在图像上验证，能否扩展到文本、音频？

**特别是：能否用 Drifting 的思想改进 dLLM？**

---

## 8. 对 dLLM 研究的启发

### 8.1 One-Step dLLM？

当前 dLLM 也需要多步 denoising。能否借鉴 Drifting 的思想，训练一个 one-step 的 dLLM？

挑战：文本是 discrete 的，drifting field 的定义需要修改。

### 8.2 平衡的概念

Drifting 的 "平衡" 概念很有意思。对于 dLLM：

> 什么时候生成过程达到 "平衡"？能否定义一个 principled 的 stopping criterion？

当前 dLLM 通常用固定步数或 confidence threshold，但这些都是 heuristic。

### 8.3 全局 vs 局部

Drifting 成功的关键是学习 **全局** 的 drifting field。

对于 dLLM，当前的 denoising 也是 "局部" 的（每步只看当前 mask 状态）。

能否设计一个 "全局" 的 denoising 策略？

---

## 9. 总结

Drifting Models 提出了一个优雅的新范式：

1. **训练时让分布演化到平衡**
2. **推理时自然支持 one-step generation**
3. **达到了 ImageNet one-step SOTA**

这可能是 diffusion 之后的下一个重要范式。

**关键 takeaway：** 与其在推理时加速多步过程，不如从训练时就设计成 one-step。

---

## 参考

- arXiv:2602.04770
- Flow Matching (Lipman et al., 2022)
- Consistency Models (Song et al., 2023)
