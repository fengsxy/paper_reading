# 论文调研报告 (2026-02-16)

来源：Greg Ver Steeg 推荐的论文列表

---

## 1. Drifting Models (arXiv:2602.04770) ⭐ Hype Paper

**标题:** Generative Modeling via Drifting

**核心创新:**
- 提出 "Drifting Models" 新范式
- 训练时演化 pushforward 分布，推理时自然支持 **one-step generation**
- 引入 "drifting field" 控制样本移动，达到平衡时分布匹配

**关键结果:**
- ImageNet 256×256 one-step generation SOTA
- Latent space FID: **1.54**
- Pixel space FID: **1.61**

**与 Diffusion 的区别:**
- Diffusion: 推理时迭代 denoise
- Drifting: 训练时演化分布，推理只需 one step

**意义:** 可能是 diffusion 之后的下一个范式，值得关注。

---

## 2. Wright-Fisher Unified Diffusion (arXiv:2512.15923)

**标题:** A Unification of Discrete, Gaussian, and Simplicial Diffusion

**核心创新:**
- 统一三种 diffusion 方法：discrete、Gaussian、simplicial
- 理论基础：Wright-Fisher 群体遗传学模型
- Simplicial 和 Gaussian diffusion 是两种 large-population limits

**关键贡献:**
- 形式化连接三种方法的 likelihood 和超参数
- 解决 simplicial diffusion 的数值不稳定问题
- 可以训练单一模型，测试时在任意 domain 做 diffusion

**实验:**
- Wright-Fisher simplicial diffusion 在 conditional DNA generation 上优于之前方法
- 多 domain 训练的模型与单 domain 训练竞争力相当

**Greg 的评论:** "Maybe I should have tried to publish this idea two years ago :)"

---

## 3. Information-Estimation Metric (arXiv:2510.02514) - ICLR 2026

**标题:** Learning a distance measure from the information-estimation geometry of data

**作者:** Guy Ohayon, Florentin Guth 等 (Greg 在 NeurIPS 见过的人)

**核心创新:**
- 提出 Information-Estimation Metric (IEM)
- 基于 information theory 和 estimation theory 的基本关系
- 通过比较不同噪声水平下的 denoising error 来定义距离

**理论贡献:**
- 证明 IEM 是有效的全局距离度量
- 导出局部二阶近似的 Riemannian metric
- 对 Gaussian 分布，IEM = Mahalanobis distance
- 对复杂分布，自适应调整

**实践:**
- 可用 learned denoiser（类似 diffusion model）计算
- 在 ImageNet 上学习的 IEM 在预测人类感知判断上与 SOTA 竞争

**代码:** https://github.com/ohayonguy/information-estimation-metric

---

## 4. Diffusion for Compression (多篇论文)

### 4.1 Turbo-DDCM (arXiv:2511.06424)

**标题:** Turbo-DDCM: Fast and Flexible Zero-Shot Diffusion-Based Image Compression

**核心创新:**
- 基于 DDCM (Denoising Diffusion Codebook Models)
- 每步高效组合大量 noise vectors，减少 denoising 操作
- 支持 priority-aware 和 distortion-controlled 变体

### 4.2 Advances in Diffusion-Based Generative Compression (arXiv:2601.18932)

**标题:** Advances in Diffusion-Based Generative Compression

**内容:** 综述论文，统一回顾 diffusion-based lossy compression 方法

### 4.3 Lossy Compression with Pretrained Diffusion Models (arXiv:2501.09815)

**标题:** Lossy Compression with Pretrained Diffusion Models

**核心创新:**
- 将 DiffC 算法应用于 Stable Diffusion 1.5, 2.1, XL, Flux-dev
- 首次完整实现 DiffC
- 10 秒内完成压缩/解压
- 无需额外训练，在 ultra-low bitrates 上与 SOTA 竞争

**Greg 的评论:** 他想过用 "Poisson functional representation" 做 diffusion compression，但被这篇抢先了。

### 4.4 Algorithms for the Communication of Samples (arXiv:2110.12805) - ICML 2022

**标题:** Algorithms for the Communication of Samples

**内容:** 
- Ordered Random Coding (ORC)
- 揭示 importance sampling 和 Poisson functional representation 的联系

---

## 5. Parallel Token Generation (OpenReview: AGJomYSrUG)

**标题:** Parallel Token Generation for Language Models

**作者:** Mandt 和 Felix (UCI)

**核心创新:**
- 单次 transformer call 联合预测多个 token
- 不限制表达能力（不假设 token 独立）
- 灵感来自 inverse autoregressive normalizing flows
- 将 sampling 过程整合到训练模型中

**关键结果:**
- Distilled model 在 toy data 上平均匹配 teacher ~50 tokens
- 在 coding dataset 上匹配 ~5 tokens
- 全部在单次 forward pass 内完成

**与 dLLM 的关系:** 这是另一种并行生成方法，不是 diffusion-based，而是 flow-based。

---

## 6. Hot Mess Theory (OpenReview: sIBwirjYlY)

**标题:** The Hot Mess of AI: How Does Misalignment Scale With Model...

**作者:** Jascha Sohl-Dickstein 等 (Greg 在 NeurIPS 见过)

**核心问题:**
- AI 失败是因为系统性追求错误目标？还是因为 "hot mess"（混乱无序）？

**方法:**
- 用 bias-variance decomposition 分析 AI 错误
- **Incoherence** = variance 占 error 的比例

**关键发现:**
1. 模型 reasoning/action 时间越长，**越 incoherent**
2. Incoherence 随 scale 变化是 task-dependent 的
3. 在多个设置中，**更大更强的模型反而更 incoherent**
4. Scale alone 不太可能消除 incoherence

**结论:**
- 未来 AI 更可能造成 "工业事故"（不可预测的错误行为）
- 而不是持续追求 misaligned goal
- 这增加了 reward hacking / goal misspecification 研究的重要性

**Greg 的评论:** "I think 'hot mess' theory is a very interesting and creative idea"

---

## 总结：与 dLLM 研究的关联

| 论文 | 与 dLLM 的关联 | 潜在研究方向 |
|------|---------------|-------------|
| Drifting Models | One-step generation 思想可迁移 | dLLM 能否做 one-step？ |
| Wright-Fisher | 统一 discrete/continuous diffusion | dLLM 的理论基础 |
| IEM | Information-theoretic distance | 可用于分析 dLLM token difficulty |
| Parallel Token Gen | 另一种并行方法 | 与 dLLM 对比/结合 |
| Hot Mess | Incoherence 分析 | dLLM 的 incoherence 如何？ |

**最值得关注:**
1. **Drifting Models** - 可能是下一个范式
2. **Hot Mess Theory** - 对 AI 失败模式的深刻洞察
3. **IEM** - Information-theoretic 工具，可能对分析 dLLM 有用
