# XDLM: 统一 MDLM 和 UDLM

**论文:** Balancing Understanding and Generation in Discrete Diffusion Models  
**arXiv:** 2602.01362  
**代码:** https://github.com/MzeroMiko/XDLM  
**关键词:** MDLM, UDLM, Unified framework, Understanding vs Generation

---

## 1. 核心问题：理解 vs 生成的权衡

两种主流 discrete diffusion：

| | MDLM (Masked) | UDLM (Uniform) |
|---|---|---|
| Noise | Mask token | Uniform noise |
| 优势 | 语义理解，zero-shot | Few-step 生成质量 |
| 劣势 | Few-step 生成差 | Zero-shot 理解差 |

**没有一个模型能同时做好理解和生成！**

---

## 2. 方法：XDLM

### 2.1 核心思想

用 **stationary noise kernel** 统一 MDLM 和 UDLM。

$$q(x_t | x_0) = \alpha_t \cdot \text{MDLM}(x_t | x_0) + (1-\alpha_t) \cdot \text{UDLM}(x_t | x_0)$$

- $\alpha_t = 1$: 退化为 MDLM
- $\alpha_t = 0$: 退化为 UDLM
- $0 < \alpha_t < 1$: 混合

### 2.2 理论贡献

证明了 MDLM 和 UDLM 是 XDLM 的特例，提供了统一的理论框架。

### 2.3 内存优化

通过代数简化 posterior probabilities，缓解了内存瓶颈。

---

## 3. 实验结果

### 3.1 理解能力

| Model | Zero-shot Text Benchmark |
|-------|-------------------------|
| UDLM | 45.2 |
| MDLM | 48.7 |
| **XDLM** | **54.1** (+5.4 vs UDLM) |

### 3.2 生成质量

| Model | Few-step Image FID ↓ |
|-------|---------------------|
| MDLM | 80.8 |
| UDLM | 58.3 |
| **XDLM** | **54.1** |

### 3.3 Scaling

8B 模型，32 steps：

| Model | MBPP |
|-------|------|
| Baseline | 7.5 |
| **XDLM** | **15.0** (2x) |

---

## 4. 深度分析

### 4.1 为什么统一有效？

MDLM 和 UDLM 各有优势：
- MDLM：保留更多语义信息（mask 只隐藏，不破坏）
- UDLM：更平滑的 noise schedule（更好的生成）

XDLM 结合两者优势。

### 4.2 与 Wright-Fisher 的联系

Wright-Fisher 也是统一框架，但从不同角度：
- Wright-Fisher：统一 discrete/Gaussian/simplicial
- XDLM：统一 MDLM/UDLM

两者可能可以进一步统一。

### 4.3 对 Ordering 的启发

不同的 noise kernel 可能对应不同的 optimal ordering：
- MDLM：先生成 "锚点" token
- UDLM：更均匀地生成
- XDLM：自适应混合

---

## 5. 总结

| 贡献 | 内容 |
|------|------|
| 问题 | MDLM 擅长理解，UDLM 擅长生成 |
| 方法 | Stationary noise kernel 统一 |
| 效果 | 理解 +5.4，生成 FID 54.1 |
| 理论 | MDLM/UDLM 是特例 |

**核心启发：** 不同的 diffusion 范式有不同优势，统一框架可以取长补短。

---

## 参考

- arXiv:2602.01362
- https://github.com/MzeroMiko/XDLM
