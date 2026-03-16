# DSL：用连续噪声解锁离散扩散语言模型的纠错能力

> 离散掩码语言模型只能填空，不能纠错——因为训练时从未见过"错误 token"。DSL 改变了这一点。

## 一、问题：离散扩散语言模型的根本缺陷

以 LLaDA 为代表的掩码扩散语言模型（MDLM）正在成为自回归 LLM 的有力替代。它们将文本生成重构为迭代去噪过程：随机 mask 一部分 token，训练模型恢复它们。

但这里有一个根本问题：**训练时，非 mask 位置永远是正确的。** 模型从未学过"面对错误 token 该怎么办"。

后果是什么？
- 一旦 token 被揭示（unmask），就永远固定，无法修正
- 推理时模型在自己生成的（可能有错的）上下文上工作，产生**训练-推理分布偏移**
- 小错误随迭代步数指数累积

这就是 DSL（Discrete Stochastic Localization）要解决的问题。

## 二、DSL 是什么？

DSL 来自 Greg Ver Steeg 团队（[arXiv:2602.16169](https://arxiv.org/abs/2602.16169)），核心思想很简单：

**用连续噪声替代离散 mask。**

传统 MDLM 的输入只有两种状态：`[MASK]` 或正确 token。DSL 把这个二元过程变成连续的：每个 token 被嵌入到连续空间，加上不同强度的高斯噪声，形成一个 SNR（信噪比）谱。

数学上：`z = t·x + √t·ε`，其中 x 是 token embedding，ε 是高斯噪声，SNR = t。一个 converter 模块将连续向量 z 映射回离散 token 的概率分布，作为 backbone 的输入。

关键洞察：**模型在训练时见过各种"部分正确、部分错误"的中间状态**，所以推理时面对自己生成的不完美草稿，也能稳定工作。

## 三、我们的实验：把 DSL 搬到 8B 规模

我们基于 LLaDA-8B-Instruct，在 8×A100-80GB 上训练，验证 DSL 能否 scale。核心发现如下。

### 3.1 纠错能力：从 1% 到 75%

这是最惊人的结果。在 50% 随机 corruption 下：

| 模型 | 修复率 |
|------|--------|
| 原始 LLaDA | 1.1% |
| DSL (beta5, 1000步) | **75.1%** |

原始 LLaDA 几乎完全无法纠正已有错误——它只会填空。DSL 训练后，模型获得了全新的纠错能力，同时填空能力完全保留（71-76%）。

事实纠错更令人印象深刻：在 SNR=1 的 soft mask 下，"法国首都"纠正率 96.8%，"太阳从东方升起"91.8%。

### 3.2 校准质量：ECE 改善 37%

| 模型 | ECE↓ |
|------|------|
| 原始 LLaDA | 0.081 |
| DSL (beta5, 1k) | **0.051** |

连续噪声迫使模型学习"置信度 ∝ 信号强度"，校准显著改善。

### 3.3 生成多样性：SDE 采样的突破

| 指标 | Standard Remasking | SDE Heun 16步 |
|------|-------------------|---------------|
| 重复率 (Rep↓) | 0.553 | **0.003** |
| 多样性 (Dist-2↑) | 0.099 | **0.518** |
| MAUVE↑ | 0.013 | **0.026** |

SDE 采样几乎消除了重复，多样性提升 5 倍。但代价是 ~100 token 后文本退化。

### 3.4 推理能力：微妙的 trade-off

GSM8K 上，beta5 frozen 1000步是唯一提升推理的配置（33.28% → 39.95%）。beta1 或训练过长反而下降。

### 3.5 关键工程发现

- **不要训练 noise_embed**：5000步后数字 0-9 的 intra-cosine 从 -0.019 飙到 +0.493，语义坍缩
- **1000步是 sweet spot**：更长训练导致 backbone 偏移
- **beta 越大纠错越强，越小生成越好**：beta=5 利纠错，beta=1 利 SDE 生成

## 四、相关工作与我们的定位

### 4.1 最相关的论文

**Corrective Diffusion Language Models (CDLM)**（[arXiv:2512.15596](https://arxiv.org/abs/2512.15596)）
- 也发现 MDLM 无法区分正确和错误 token
- 方案：post-training 时显式监督可见的错误 token
- 区别：CDLM 用离散的"正确/错误"标签，DSL 用连续噪声谱，更优雅

**ProSeCo: Progressive Self-Correction**（[arXiv:2602.11590](https://arxiv.org/abs/2602.11590)）
- 训练模型同时做 unmasking 和 correction
- 方案：复用去噪网络输出作为 corrector 训练输入
- 区别：ProSeCo 需要额外的 corrector 步骤，DSL 通过训练范式统一解决

**Soft-Masked Diffusion (SM-DLM)**（[arXiv:2510.17206](https://arxiv.org/abs/2510.17206)）
- 将离散 mask 替换为连续的 soft mask
- 与 DSL 最接近，但 SM-DLM 在 mask 空间做 soft，DSL 在 embedding 空间加噪声
- SM-DLM 未验证纠错能力

### 4.2 Scaling 相关

**Scaling Behavior of DLMs**（[arXiv:2512.10858](https://arxiv.org/abs/2512.10858)）
- 发现 DLM 的 scaling 行为与 ALM 显著不同
- Uniform diffusion 比 masked diffusion 需要更多参数但更少数据
- 缩放到 10B 参数

**LLaDA 2.0**（[arXiv:2512.15745](https://arxiv.org/abs/2512.15745)）
- 将 MDLM 缩放到 100B，通过从 AR 模型转换而非从头训练
- 验证了 dLLM 在前沿规模的可行性

**d1: Scaling Reasoning**（[arXiv:2504.12216](https://arxiv.org/abs/2504.12216)）
- 用 diffu-GRPO 在 LLaDA-8B 上做 RL，提升推理能力
- 展示了 dLLM 中的"aha moments"

## 五、我们实验揭示的 GAP

### GAP 1：纠错能力的 scaling 未知
DSL 在 8B 上验证了纠错能力，但没人知道 scaling 到 70B/100B 时纠错率会怎么变。CDLM 和 ProSeCo 都只在小模型上做了实验。**这是一个开放问题。**

### GAP 2：长文本退化未解决
所有 SDE 生成在 ~100 token 后退化。现有工作（SM-DLM、CDLM）都没直接解决这个问题。PAN 的因果滑动窗口思路可能有启发。

### GAP 3：beta 选择缺乏理论指导
我们发现 beta=5 利纠错、beta=1 利生成，但目前是手动选择。动态 beta（随 SNR 变化）是一个未探索的方向。

### GAP 4：DSL + RL 的结合
d1 用 GRPO 提升了 LLaDA 推理能力。DSL 改善了校准质量。**两者结合**（DSL 训练 → GRPO 微调）是否能同时获得纠错和推理提升？没人试过。

### GAP 5：converter 训练瓶颈
SNR [2,15) 范围的 loss 几乎不降，converter 是训练瓶颈。更高效的 converter 架构或预训练策略是开放问题。

## 六、核心 Takeaway

DSL 不是更好的生成器，是更好的"理解器"：
- **纠错**：1% → 75%（核心贡献）
- **校准**：ECE 改善 37%
- **多样性**：SDE 消除重复
- **代价**：长文本退化、推理需谨慎调参

**DSL 的真正价值是赋予离散模型一种全新的能力——面对错误输入时不崩溃，而是主动修正。**

## 参考文献

1. DSL: [Discrete Stochastic Localization](https://arxiv.org/abs/2602.16169) — Cheng, Thakuria, Brekelmans, Papalexakis, Ver Steeg
2. LLaDA: [Large Language Diffusion Models](https://arxiv.org/abs/2502.09992) — Nie et al.
3. CDLM: [Corrective Diffusion Language Models](https://arxiv.org/abs/2512.15596) — Zhang et al.
4. ProSeCo: [Self-Correcting Masked Diffusion](https://arxiv.org/abs/2602.11590) — Schiff et al.
5. SM-DLM: [Soft-Masked Diffusion](https://arxiv.org/abs/2510.17206) — Hersche et al.
6. Scaling DLMs: [Scaling Behavior](https://arxiv.org/abs/2512.10858) — von Rütte et al.
7. d1: [Scaling Reasoning in dLLMs](https://arxiv.org/abs/2504.12216) — Zhao et al.
8. LLaDA 2.0: [Scaling to 100B](https://arxiv.org/abs/2512.15745)
9. dLLM framework: [github.com/ZHZisZZ/dllm](https://github.com/ZHZisZZ/dllm)

---

*离散和连续，mask 和噪声，看似对立的两种范式正在融合。DSL 迈出了第一步。*
