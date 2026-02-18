# Information-Estimation Metric (IEM): 用 Denoising 定义距离

**论文:** Learning a distance measure from the information-estimation geometry of data  
**arXiv:** 2510.02514  
**发表:** ICLR 2026  
**关键词:** Information theory, Estimation theory, Perceptual distance, Diffusion models

---

## 1. 问题背景：什么是"好"的距离度量？

在机器学习中，我们经常需要衡量两个样本之间的"距离"：

- 图像相似度
- 文本语义距离
- 生成质量评估

### 1.1 传统方法的问题

**L2 距离（像素级）：**
```python
d(x, y) = ||x - y||²
```
问题：对人类感知不敏感。一个像素的微小偏移可能导致巨大的 L2 距离，但人眼几乎看不出区别。

**Learned Perceptual Distance (LPIPS)：**
```python
d(x, y) = ||f(x) - f(y)||²  # f 是预训练网络的特征
```
问题：依赖于特定的预训练网络，缺乏理论基础。

**核心问题：** 能否从 **第一性原理** 推导出一个有意义的距离度量？

---

## 2. 核心思想：Information-Estimation Duality

### 2.1 信息论与估计论的联系

这篇论文的出发点是信息论和估计论之间的深刻联系：

> **De Bruijn's Identity:** 信息量的变化率 = 估计误差

具体来说，对于加了 Gaussian noise 的信号：

$$\frac{d}{d\sigma²} H(X + \sigma Z) = \frac{1}{2} \text{MMSE}(\sigma²)$$

其中：
- $H$ 是 entropy
- $\text{MMSE}$ 是 minimum mean squared error（最优估计的误差）

**直觉：** 信息量的变化和估计难度直接相关。

### 2.2 从估计误差到距离

论文的核心洞察：

> **两个样本的"距离" = 它们在不同噪声水平下的估计误差差异**

形式化定义：

$$\text{IEM}(x, y) = \int_0^\infty \left| \text{MSE}_x(\sigma) - \text{MSE}_y(\sigma) \right| d\sigma$$

其中 $\text{MSE}_x(\sigma)$ 是对样本 $x$ 加噪声后的 denoising error。

---

## 3. 直觉理解

### 3.1 为什么 Denoising Error 能反映"距离"？

想象两张图片 x 和 y：

**Case 1: x 和 y 很相似**
- 加同样的噪声后，它们的 noisy versions 也相似
- Denoiser 对它们的处理方式相似
- Denoising error 的 pattern 相似

**Case 2: x 和 y 很不同**
- 加噪声后，它们的 noisy versions 差异大
- Denoiser 对它们的处理方式不同
- Denoising error 的 pattern 不同

### 3.2 多尺度分析

不同噪声水平 σ 对应不同的"尺度"：

| 噪声水平 | 对应尺度 | 捕捉的信息 |
|---------|---------|-----------|
| σ 小 | 细节 | 纹理、边缘 |
| σ 中 | 中等 | 物体形状 |
| σ 大 | 粗糙 | 全局结构 |

IEM 通过积分所有噪声水平，**综合考虑所有尺度的信息**。

### 3.3 与 Diffusion 的联系

Diffusion model 的训练过程就是学习在不同噪声水平下 denoise。

所以 **IEM 可以直接用训练好的 diffusion model 计算**！

```python
def compute_IEM(x, y, denoiser, sigma_levels):
    iem = 0
    for sigma in sigma_levels:
        # 加噪声
        x_noisy = x + sigma * torch.randn_like(x)
        y_noisy = y + sigma * torch.randn_like(y)
        
        # Denoise
        x_denoised = denoiser(x_noisy, sigma)
        y_denoised = denoiser(y_noisy, sigma)
        
        # 计算 MSE
        mse_x = ((x - x_denoised) ** 2).mean()
        mse_y = ((y - y_denoised) ** 2).mean()
        
        # 累加差异
        iem += abs(mse_x - mse_y)
    
    return iem
```

---

## 4. 理论分析

### 4.1 IEM 是有效的距离度量

论文证明 IEM 满足距离度量的公理：

1. **非负性:** $\text{IEM}(x, y) \geq 0$
2. **同一性:** $\text{IEM}(x, y) = 0 \Leftrightarrow x = y$
3. **对称性:** $\text{IEM}(x, y) = \text{IEM}(y, x)$
4. **三角不等式:** $\text{IEM}(x, z) \leq \text{IEM}(x, y) + \text{IEM}(y, z)$

### 4.2 局部 Riemannian Metric

在局部，IEM 可以近似为一个 **Riemannian metric**：

$$\text{IEM}(x, x + \epsilon) \approx \epsilon^T G(x) \epsilon$$

其中 $G(x)$ 是 **metric tensor**，取决于数据流形的局部几何。

**意义：** IEM 不仅是全局距离，还诱导了数据空间上的几何结构。

### 4.3 特殊情况：Gaussian 分布

对于 Gaussian 分布 $\mathcal{N}(\mu, \Sigma)$：

$$\text{IEM}(x, y) = (x - y)^T \Sigma^{-1} (x - y) = \text{Mahalanobis distance}$$

这说明 IEM 在简单情况下退化为经典的统计距离。

---

## 5. 实验结果

### 5.1 人类感知判断

任务：预测人类对图像相似度的判断

| Method | Agreement with Human ↑ |
|--------|----------------------|
| L2 | 0.45 |
| SSIM | 0.52 |
| LPIPS (VGG) | 0.71 |
| LPIPS (Alex) | 0.73 |
| **IEM** | **0.72** |

IEM 与 LPIPS 竞争力相当，但 **不需要专门训练**，只需要一个 diffusion model。

### 5.2 图像检索

任务：给定 query 图像，找最相似的图像

| Method | Recall@10 ↑ |
|--------|------------|
| L2 | 0.31 |
| LPIPS | 0.58 |
| **IEM** | **0.61** |

### 5.3 生成质量评估

任务：评估生成图像的质量

IEM 可以用来定义新的生成质量指标：

$$\text{IEM-FID} = \text{IEM}(\mu_{real}, \mu_{gen})$$

实验表明 IEM-FID 与人类评估的相关性高于传统 FID。

---

## 6. 深度分析

### 6.1 为什么 IEM 能捕捉感知相似度？

**假设：** 人类视觉系统也在做某种 "denoising"。

神经科学研究表明，视觉皮层的一个重要功能是 **去除噪声、提取信号**。

如果人脑的 denoising 机制和 diffusion model 类似，那么 IEM 自然能预测人类感知。

### 6.2 与 Score Function 的关系

Diffusion model 学习的是 **score function**：

$$s(x, \sigma) = \nabla_x \log p_\sigma(x)$$

Denoising 和 score 的关系：

$$\hat{x} = x_{noisy} + \sigma² s(x_{noisy}, \sigma)$$

所以 IEM 本质上是在比较两个样本的 **score function 差异**。

### 6.3 信息几何视角

IEM 可以理解为数据流形上的 **测地距离**（geodesic distance）。

在信息几何中，概率分布空间有自然的 Riemannian 结构（Fisher information metric）。

IEM 是这种结构在样本空间的投影。

---

## 7. 对 dLLM 研究的启发

### 7.1 Token Difficulty Metric

IEM 的核心思想可以迁移到 dLLM：

> **Token 的 "difficulty" = 它的 denoising error**

定义：

$$D_i(x) = \mathbb{E}_{\sigma}[\text{MSE}(x_i, \hat{x}_i | x_{masked})]$$

其中 $\hat{x}_i$ 是 dLLM 对 position $i$ 的预测。

### 7.2 Difficulty-Based Ordering

有了 token difficulty metric，可以定义 ordering 策略：

```python
def difficulty_based_ordering(x_masked, dllm):
    difficulties = []
    for i in range(seq_len):
        # 计算 position i 的 difficulty
        d_i = compute_token_difficulty(x_masked, i, dllm)
        difficulties.append(d_i)
    
    # 按 difficulty 从低到高排序
    # 先生成 "容易" 的 token，再生成 "难" 的
    order = sorted(range(seq_len), key=lambda i: difficulties[i])
    return order
```

**直觉：** 先确定容易的 token（作为 anchor），再根据 context 生成难的 token。

### 7.3 与 Latent Forcing 的联系

Latent Forcing 的发现：DINO latents 应该先 denoise，pixels 后 denoise。

用 IEM 的视角理解：
- DINO latents 的 denoising error 小 → difficulty 低 → 先生成
- Pixels 的 denoising error 大 → difficulty 高 → 后生成

**这给了 Latent Forcing 一个理论解释！**

### 7.4 具体研究方向

**Idea 1: Token-Level IEM**

定义 token 之间的 IEM：

$$\text{IEM}(t_1, t_2) = \int_0^1 |\text{MSE}_{t_1}(m) - \text{MSE}_{t_2}(m)| dm$$

其中 $m$ 是 mask ratio。

**Idea 2: Difficulty Prediction Network**

训练一个网络预测 token difficulty：

$$d_i = f_\theta(x_{context}, i)$$

然后用 difficulty 指导 generation order。

**Idea 3: Adaptive Denoising**

根据 difficulty 调整 denoising 策略：
- Low difficulty tokens: 少步数，aggressive denoising
- High difficulty tokens: 多步数，careful denoising

---

## 8. 代码实现

论文提供了开源代码：https://github.com/ohayonguy/information-estimation-metric

核心实现：

```python
class IEM:
    def __init__(self, denoiser, sigma_levels):
        self.denoiser = denoiser
        self.sigma_levels = sigma_levels
    
    def compute_mse_curve(self, x):
        """计算样本 x 在不同噪声水平下的 MSE"""
        mse_curve = []
        for sigma in self.sigma_levels:
            x_noisy = x + sigma * torch.randn_like(x)
            x_denoised = self.denoiser(x_noisy, sigma)
            mse = ((x - x_denoised) ** 2).mean()
            mse_curve.append(mse)
        return torch.tensor(mse_curve)
    
    def distance(self, x, y):
        """计算 IEM 距离"""
        mse_x = self.compute_mse_curve(x)
        mse_y = self.compute_mse_curve(y)
        return (mse_x - mse_y).abs().sum()
```

---

## 9. 局限性

### 9.1 计算成本

计算 IEM 需要多次 forward pass（每个噪声水平一次），比 L2 或 LPIPS 慢。

### 9.2 依赖 Denoiser 质量

IEM 的质量取决于 denoiser 的质量。如果 denoiser 不好，IEM 也不准。

### 9.3 离散数据的挑战

原始 IEM 是为连续数据设计的。对于离散数据（文本），需要修改定义。

---

## 10. 总结

Information-Estimation Metric 的贡献：

1. **理论基础**: 从 information-estimation duality 推导距离度量
2. **实用性**: 可以直接用 diffusion model 计算
3. **性能**: 在感知相似度任务上与 SOTA 竞争

**对 dLLM 最重要的启发：**

> Denoising error 可以作为 "difficulty" 的度量。
> 
> 这为 optimal ordering 提供了一个 principled 的定义：
> **先生成 low-difficulty tokens，后生成 high-difficulty tokens。**

---

## 参考

- arXiv:2510.02514
- De Bruijn's Identity (Stam, 1959)
- LPIPS (Zhang et al., 2018)
- Score-based generative models (Song et al., 2021)
