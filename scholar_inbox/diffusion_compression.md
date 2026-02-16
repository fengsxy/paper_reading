# Diffusion for Compression: 用生成模型做压缩

**论文合集:**
- Lossy Compression with Pretrained Diffusion Models (arXiv:2501.09815)
- Turbo-DDCM (arXiv:2511.06424)
- Advances in Diffusion-Based Generative Compression (arXiv:2601.18932)
- Algorithms for the Communication of Samples (arXiv:2110.12805)

**关键词:** Lossy compression, Diffusion models, Rate-distortion, Channel simulation

---

## 1. 问题背景：为什么用 Diffusion 做压缩？

### 1.1 传统压缩的局限

传统图像压缩（JPEG, WebP, HEIC）的工作方式：

```
原图 → 变换（DCT/Wavelet）→ 量化 → 熵编码 → 压缩文件
```

问题：
- 低比特率时出现明显 artifacts（块效应、模糊）
- 无法利用图像的 **语义信息**

### 1.2 生成式压缩的思想

核心想法：

> **不存储像素，存储 "如何生成这张图"**

```
原图 → 编码为 latent code → 用生成模型重建
```

如果生成模型足够好，可以用很少的 bits 描述 latent code，然后高质量重建。

### 1.3 为什么是 Diffusion？

Diffusion models 的优势：
1. **高质量生成**: 当前最好的图像生成质量
2. **灵活的 conditioning**: 可以条件于各种信息
3. **理论基础**: 与 rate-distortion theory 有深刻联系

---

## 2. 理论基础：Rate-Distortion 与 Diffusion

### 2.1 Rate-Distortion Theory

Shannon 的 rate-distortion theory 告诉我们：

> 要以失真度 D 压缩数据，至少需要 R(D) bits。

$$R(D) = \min_{p(\hat{x}|x): \mathbb{E}[d(x,\hat{x})] \leq D} I(X; \hat{X})$$

其中 $I(X; \hat{X})$ 是互信息。

### 2.2 Diffusion 与 Rate-Distortion 的联系

一个深刻的观察（Ho et al., 2020）：

> **Diffusion 的 ELBO 可以分解为 rate-distortion 形式**

$$-\log p(x) \leq \underbrace{D_{KL}(q(x_T|x) || p(x_T))}_{\text{Rate}} + \underbrace{\sum_{t=1}^{T} \mathbb{E}[\|x - \hat{x}_t\|^2]}_{\text{Distortion}}$$

这意味着：**训练 diffusion model 本质上是在优化 rate-distortion tradeoff！**

### 2.3 DiffC 算法

DiffC（Theis et al., 2022）是第一个利用这个联系的压缩算法：

```
编码:
1. 对原图 x 运行 forward diffusion 得到 x_T
2. 用 reverse channel coding 编码 x_T
3. 存储编码后的 bits

解码:
1. 解码得到 x_T
2. 运行 reverse diffusion 得到重建图 x̂
```

---

## 3. 论文 1: Lossy Compression with Pretrained Diffusion Models

### 3.1 核心贡献

这篇论文首次 **完整实现** 了 DiffC 算法，并应用于 Stable Diffusion。

之前 DiffC 只是理论上可行，实际实现有很多挑战：
- Reverse channel coding 的数值问题
- 与预训练 diffusion model 的兼容性
- 计算效率

### 3.2 技术细节

**Reverse Channel Coding 的挑战：**

理论上，要编码 $x_T$，需要：
1. 发送方和接收方共享随机种子
2. 用 importance sampling 找到能重建 $x_T$ 的种子

问题：importance sampling 的 variance 很大，需要大量样本。

**本文的解决方案：**

1. **Truncated importance sampling**: 限制样本数量
2. **Adaptive precision**: 根据重要性调整精度
3. **Efficient implementation**: 优化 GPU 利用率

### 3.3 实验结果

| Method | BPP ↓ | LPIPS ↓ | 时间 |
|--------|-------|---------|------|
| JPEG | 0.5 | 0.35 | <1s |
| WebP | 0.5 | 0.28 | <1s |
| HiFiC | 0.5 | 0.15 | ~1s |
| **DiffC (SD 1.5)** | **0.5** | **0.12** | **~10s** |

在 ultra-low bitrate（0.1-0.5 BPP）下，DiffC 显著优于传统方法。

### 3.4 关键洞察

> **预训练的 diffusion model 已经是很好的压缩器，无需额外训练！**

这是因为 diffusion model 学习了数据的 **分布**，而好的压缩本质上就是利用分布的知识。

---

## 4. 论文 2: Turbo-DDCM

### 4.1 问题：DiffC 太慢

DiffC 需要多步 diffusion，每步都要 forward pass，导致压缩/解压很慢。

### 4.2 解决方案：DDCM

DDCM（Denoising Diffusion Codebook Models）的思想：

> **用 codebook 代替连续的 latent space**

```
传统 DiffC:
x → 连续 latent x_T → 编码 → bits

DDCM:
x → 离散 codebook index → 直接存储 index
```

### 4.3 Turbo-DDCM 的改进

1. **高效组合**: 每步组合大量 noise vectors，减少 denoising 次数
2. **Priority-aware**: 重要区域用更多 bits
3. **Distortion-controlled**: 可以指定目标失真度

### 4.4 结果

| Method | BPP | LPIPS | 时间 |
|--------|-----|-------|------|
| DiffC | 0.3 | 0.15 | 10s |
| **Turbo-DDCM** | **0.3** | **0.14** | **2s** |

5x 加速，质量相当。

---

## 5. 论文 3: Algorithms for the Communication of Samples

### 5.1 背景：Channel Simulation

这篇论文（ICML 2022）研究的是一个更基础的问题：

> **如何高效地 "传输" 一个从分布 p(x) 中采样的样本？**

这和压缩的联系：压缩可以看作是 "传输" 原图的一个近似样本。

### 5.2 Ordered Random Coding (ORC)

ORC 是一种 channel simulation 算法：

```
发送方:
1. 共享随机种子 seed
2. 用 seed 生成候选样本 {x_1, x_2, ..., x_K}
3. 找到最接近目标的 x_i
4. 发送 index i

接收方:
1. 用相同 seed 生成 {x_1, x_2, ..., x_K}
2. 根据 index i 选择 x_i
```

### 5.3 与 Importance Sampling 的联系

论文证明了 ORC 和 importance sampling 的等价性：

$$\text{ORC} \equiv \text{Importance Sampling with ordered proposals}$$

这个联系很重要，因为它允许我们用 importance sampling 的理论分析 ORC。

### 5.4 Poisson Functional Representation

论文还介绍了 Poisson functional representation：

> **任何分布都可以表示为 Poisson process 的函数**

这提供了另一种 channel simulation 的方法，可能比 ORC 更高效。

---

## 6. 综合分析：Diffusion Compression 的未来

### 6.1 当前状态

| 方面 | 状态 |
|------|------|
| 质量 | 在 ultra-low bitrate 下 SOTA |
| 速度 | 比传统方法慢 10-100x |
| 实用性 | 研究阶段，尚未大规模部署 |

### 6.2 主要挑战

1. **速度**: 需要更快的 diffusion 或更好的 channel coding
2. **可控性**: 如何精确控制 rate-distortion tradeoff
3. **标准化**: 需要统一的格式和协议

### 6.3 未来方向

1. **One-step diffusion compression**: 结合 Drifting Models 的思想
2. **Neural channel coding**: 用神经网络学习更好的 channel coding
3. **Semantic compression**: 只保留语义重要的信息

---

## 7. 对 dLLM 研究的启发

### 7.1 文本压缩的类比

Diffusion compression 的思想可以迁移到文本：

| 图像压缩 | 文本压缩 |
|---------|---------|
| 存储 latent code | 存储 "文本的本质" |
| 用 diffusion 重建像素 | 用 dLLM 重建 tokens |
| Rate-distortion tradeoff | 压缩率 vs 语义保真度 |

### 7.2 dLLM 作为压缩器？

一个有趣的问题：

> **dLLM 能否用于文本压缩？**

思路：
1. 将文本编码为 "语义 latent"
2. 用 dLLM 从 latent 重建文本
3. 只存储 latent（比原文本小）

### 7.3 Information-Theoretic 视角

Diffusion compression 的成功表明：

> **生成模型的质量 ≈ 压缩效率**

这给了评估 dLLM 一个新视角：

$$\text{dLLM 质量} \propto \text{文本压缩效率}$$

如果 dLLM 能高效压缩文本，说明它真正理解了文本的结构。

### 7.4 具体研究方向

**Idea 1: dLLM-based Text Compression**

```python
def compress_text(text, dllm):
    # 1. 编码为 latent
    latent = dllm.encode(text)  # 需要设计 encoder
    
    # 2. 量化 latent
    quantized = quantize(latent)
    
    # 3. 熵编码
    bits = entropy_encode(quantized)
    
    return bits

def decompress_text(bits, dllm):
    # 1. 熵解码
    quantized = entropy_decode(bits)
    
    # 2. 用 dLLM 重建
    text = dllm.generate(condition=quantized)
    
    return text
```

**Idea 2: Rate-Distortion Analysis of dLLM**

分析 dLLM 的 rate-distortion 性能：
- Rate: 生成所需的 "信息量"（bits）
- Distortion: 生成文本与目标的差异

**Idea 3: Compression-Guided Ordering**

用压缩效率指导 generation order：
- 先生成 "压缩效率高" 的 tokens（容易预测）
- 后生成 "压缩效率低" 的 tokens（难预测）

这和 IEM 的 difficulty-based ordering 思想一致！

---

## 8. 代码示例

### 8.1 简化的 DiffC 实现

```python
class DiffusionCompressor:
    def __init__(self, diffusion_model, num_steps=50):
        self.model = diffusion_model
        self.num_steps = num_steps
    
    def encode(self, image):
        """将图像编码为 latent"""
        # Forward diffusion
        x_t = image
        for t in range(self.num_steps):
            noise = torch.randn_like(x_t)
            x_t = self.add_noise(x_t, noise, t)
        
        # x_T 是最终的 latent
        return x_t
    
    def decode(self, latent):
        """从 latent 重建图像"""
        x_t = latent
        for t in reversed(range(self.num_steps)):
            # Reverse diffusion
            noise_pred = self.model(x_t, t)
            x_t = self.remove_noise(x_t, noise_pred, t)
        
        return x_t
    
    def compress(self, image):
        """压缩图像"""
        latent = self.encode(image)
        # 量化和熵编码
        bits = self.entropy_encode(self.quantize(latent))
        return bits
    
    def decompress(self, bits):
        """解压图像"""
        latent = self.dequantize(self.entropy_decode(bits))
        image = self.decode(latent)
        return image
```

### 8.2 Rate-Distortion 评估

```python
def evaluate_rate_distortion(compressor, images, target_bpp_list):
    results = []
    
    for target_bpp in target_bpp_list:
        compressor.set_target_bpp(target_bpp)
        
        total_bpp = 0
        total_distortion = 0
        
        for image in images:
            # 压缩
            bits = compressor.compress(image)
            actual_bpp = len(bits) / (image.shape[-1] * image.shape[-2])
            
            # 解压
            reconstructed = compressor.decompress(bits)
            
            # 计算失真
            distortion = compute_lpips(image, reconstructed)
            
            total_bpp += actual_bpp
            total_distortion += distortion
        
        results.append({
            'bpp': total_bpp / len(images),
            'distortion': total_distortion / len(images)
        })
    
    return results
```

---

## 9. 总结

Diffusion for Compression 的贡献：

1. **理论联系**: 揭示了 diffusion 和 rate-distortion theory 的深刻联系
2. **实际应用**: 在 ultra-low bitrate 下达到 SOTA 压缩质量
3. **新范式**: 用生成模型做压缩，而不是传统的变换编码

**对 dLLM 最重要的启发：**

> 生成模型的质量可以用压缩效率来衡量。
> 
> dLLM 可能可以用于文本压缩。
> 
> "容易压缩" 的 tokens 应该先生成（和 difficulty-based ordering 一致）。

---

## 参考

- arXiv:2501.09815 (Lossy Compression with Pretrained Diffusion Models)
- arXiv:2511.06424 (Turbo-DDCM)
- arXiv:2601.18932 (Advances in Diffusion-Based Generative Compression)
- arXiv:2110.12805 (Algorithms for the Communication of Samples)
- Rate-Distortion Theory (Shannon, 1959)
- DiffC (Theis et al., 2022)
