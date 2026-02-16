# Token Difficulty 相关工作调研

> 调研目标：AR LLM 中的 adaptive computation、early exit、token importance 等工作，探索可迁移到 dLLM 的思想
> 调研时间：2026-02-16

---

## 1. 核心概念：Token Difficulty 的定义

Token difficulty 指的是模型生成或处理不同 token 时所需的计算量差异。核心观察：
- **不是所有 token 都同等困难**：常见词（"the", "is"）vs 专业术语、代码关键字
- **上下文依赖性**：同一 token 在不同上下文中难度不同
- **可预测性**：模型内部状态（entropy、attention pattern）可以预测 token 难度

---

## 2. AR LLM 中的 Adaptive Computation 方法

### 2.1 Speculative Decoding 系列

#### Speculative Decoding (Leviathan et al., 2022)
- **核心思想**：用小模型（draft model）快速生成多个候选 token，大模型并行验证
- **关键洞察**：简单 token 可以被小模型准确预测，只有困难 token 需要大模型
- **加速比**：2-3x on T5-XXL
- **迁移启示**：dLLM 可以用类似思想——简单位置少迭代，困难位置多迭代

#### Speculative Sampling (Chen et al., 2023)
- **改进**：modified rejection sampling 保持目标分布
- **加速比**：2-2.5x on Chinchilla 70B
- **迁移启示**：dLLM 的 token-level 迭代次数分配可以借鉴 rejection sampling 思想

#### Medusa (Cai et al., 2024)
- **核心思想**：在 LLM 上添加多个 decoding heads，并行预测后续多个 token
- **优势**：无需单独的 draft model，tree-based attention 验证
- **加速比**：2.2-3.6x
- **迁移启示**：dLLM 可以设计 multi-head predictor 预测哪些位置需要更多迭代

#### DistillSpec (Zhou et al., 2023)
- **核心思想**：用知识蒸馏对齐 draft model 和 target model
- **关键发现**：on-policy data generation + tailored divergence function 是关键
- **加速比**：10-45% speedup over standard SD
- **迁移启示**：dLLM 的 difficulty predictor 可以通过蒸馏从 full-iteration 模型学习

### 2.2 Mixture-of-Depths (MoD)

#### Mixture-of-Depths (Raposo et al., 2024)
- **核心思想**：动态分配 FLOPs 到序列中的特定位置
- **机制**：top-k routing 决定哪些 token 参与 self-attention 和 MLP 计算
- **关键特性**：
  - 静态计算图（k 预先定义）
  - 动态 token 选择（哪些 token 被选中是 fluid 的）
  - 不同层可以选择不同 token
- **效果**：匹配 baseline 性能，推理快 50%+
- **迁移启示**：**这是最直接相关的工作！** dLLM 可以学习 per-token 的迭代次数分配

### 2.3 Early Exit 方法

#### FFN Layers Build Predictions (Geva et al., 2022)
- **核心发现**：FFN 层逐步在 vocabulary space 构建预测
- **应用**：基于 early exit rule 节省 20% 计算
- **迁移启示**：dLLM 可以监控每个位置的 "prediction confidence" 决定是否继续迭代

#### Layer Dropping (Durrani et al., 2020)
- **发现**：可以剪掉 40% 的层，保持 98% 性能
- **关键观察**：
  - 底层最关键
  - 不同任务对 layer dropping 的鲁棒性不同
- **迁移启示**：dLLM 不同位置可能需要不同"深度"的处理

#### ShortGPT (Wang et al., 2024)
- **核心发现**：LLM 很多层高度相似，存在大量冗余
- **方法**：Block Influence (BI) 指标衡量层重要性，直接删除冗余层
- **迁移启示**：dLLM 的迭代过程中，某些位置可能很快收敛（类似冗余层）

### 2.4 Contextual Sparsity

#### Deja Vu (Liu et al., 2023)
- **核心概念**：Contextual Sparsity —— 输入相关的稀疏激活
- **发现**：存在小的、输入相关的 attention heads 和 MLP 参数子集，能近似 dense 输出
- **方法**：低成本算法预测每层的 contextual sparsity
- **加速比**：2x over FasterTransformer, 6x over HuggingFace
- **迁移启示**：dLLM 可以预测每个位置需要激活的"计算子集"

#### FastGen / Adaptive KV Cache (Ge et al., 2023)
- **核心思想**：根据 attention head 的结构特性自适应构建 KV cache
- **三种模式**：
  - Local context heads → evict long-range
  - Special token heads → discard non-special
  - Broad attention heads → standard KV cache
- **迁移启示**：dLLM 不同位置可能需要不同的 attention pattern

---

## 3. Token Importance / Difficulty 的度量方法

### 3.1 基于 Entropy 的方法

#### CoT-Decoding (Wang et al., 2024)
- **发现**：CoT 路径的存在与模型对答案的 confidence 相关
- **方法**：检查 top-k alternative tokens 发现 CoT paths
- **迁移启示**：dLLM 可以用 entropy 作为 difficulty 的 proxy

### 3.2 基于 Attention 的方法

- **Attention entropy**：高 entropy = 不确定 = 困难
- **Attention pattern**：某些 token 被广泛 attend = 重要
- **迁移启示**：dLLM 可以用 cross-attention 或 self-attention 模式判断 difficulty

### 3.3 基于 Gradient 的方法

#### LISA (Pan et al., 2024)
- **发现**：不同层的 weight norm 存在 skewness
- **方法**：Layerwise Importance Sampling，随机冻结中间层
- **迁移启示**：dLLM 可以用类似思想，对不同位置采样不同的迭代深度

---

## 4. 模型压缩与效率相关工作

### 4.1 Quantization

#### BitNet b1.58 (Ma et al., 2024)
- **核心**：1.58-bit (ternary {-1, 0, 1}) LLM
- **效果**：匹配 FP16 性能，显著降低 latency/memory/energy
- **迁移启示**：dLLM 的 difficulty predictor 可以是极轻量的

#### BiLLM (Huang et al., 2024)
- **方法**：1-bit post-training quantization
- **关键**：识别 salient weights + binary residual approximation
- **迁移启示**：dLLM 可以识别"salient positions"给予更多计算

### 4.2 Sparse Activation

#### ReLU² Wins (Zhang et al., 2024)
- **发现**：ReLU² 在 sparsity-performance trade-off、predictivity、hardware affinity 三方面最优
- **迁移启示**：dLLM 的 difficulty predictor 可以利用 sparse activation 特性

### 4.3 KV Cache Compression

#### Dynamic Memory Compression (Nawrot et al., 2024)
- **核心**：模型学习在不同 head/layer 应用不同压缩率
- **效果**：7x throughput increase
- **迁移启示**：dLLM 可以学习 per-position 的"压缩率"（即迭代次数）

---

## 5. Elastic / Nested 架构

### MatFormer (Devvrit et al., 2023)
- **核心思想**：Nested FFN block structure，训练时优化多个嵌套子模型
- **效果**：提取数百个准确的小模型，无额外计算成本
- **应用**：speculative decoding 用提取的子模型作为 draft
- **迁移启示**：dLLM 可以设计 nested iteration structure，不同位置用不同"深度"的子模型

---

## 6. Diffusion LLM 特有的相关工作

### MDLM (Sahoo et al., 2024)
- **核心**：Simple masked discrete diffusion
- **发现**：masked diffusion 比之前认为的更强
- **方法**：Rao-Blackwellized objective = mixture of masked LM losses
- **迁移启示**：dLLM 的 token difficulty 可以通过 mask prediction confidence 度量

---

## 7. 迁移到 dLLM 的具体思路

### 7.1 Difficulty Predictor 设计

| 方法 | 输入 | 输出 | 复杂度 |
|------|------|------|--------|
| Entropy-based | 当前 logits | per-token difficulty score | O(V) |
| Attention-based | attention weights | per-token importance | O(L×H) |
| Learned predictor | hidden states | iteration count | O(d) |
| Routing-based (MoD style) | hidden states | top-k selection | O(n×d) |

### 7.2 Adaptive Iteration 策略

1. **Static budget, dynamic allocation** (类似 MoD)
   - 总迭代次数固定
   - 学习如何分配到不同位置

2. **Early exit per position**
   - 每个位置独立判断是否收敛
   - 收敛标准：entropy < threshold 或 prediction stable

3. **Speculative iteration**
   - 先用少量迭代生成初始预测
   - 识别困难位置，只对这些位置继续迭代

4. **Nested iteration** (类似 MatFormer)
   - 不同位置用不同"深度"的迭代
   - 简单位置：shallow iteration
   - 困难位置：deep iteration

### 7.3 训练策略

1. **Joint training**：difficulty predictor 和 denoising model 联合训练
2. **Distillation**：从 full-iteration 模型蒸馏 difficulty knowledge
3. **Curriculum**：先学简单 token 的 difficulty，再学困难的

---

## 8. 关键论文列表

### 必读论文（直接相关）
1. **Mixture-of-Depths** (arXiv:2404.02258) - 最直接相关
2. **Speculative Decoding** (arXiv:2211.17192) - 经典方法
3. **Medusa** (arXiv:2401.10774) - 无 draft model 的加速
4. **Deja Vu** (arXiv:2310.17157) - Contextual sparsity
5. **MDLM** (arXiv:2406.07524) - Masked diffusion LM

### 推荐阅读（思想借鉴）
6. **MatFormer** (arXiv:2310.07707) - Nested architecture
7. **ShortGPT** (arXiv:2403.03853) - Layer redundancy
8. **FastGen** (arXiv:2310.01801) - Adaptive KV cache
9. **Dynamic Memory Compression** (arXiv:2403.09636) - Learned compression
10. **LISA** (arXiv:2403.17919) - Layerwise importance

### 背景知识
11. **FFN Builds Predictions** (arXiv:2203.14680) - Transformer 内部机制
12. **DistillSpec** (arXiv:2310.08461) - 蒸馏对齐
13. **BitNet b1.58** (arXiv:2402.17764) - 极致压缩

---

## 9. 总结与下一步

### 核心洞察
1. **Token difficulty 是真实存在的**：AR LLM 的大量工作证明了这一点
2. **可以被预测**：通过 entropy、attention、learned predictor 等方式
3. **可以被利用**：speculative decoding、MoD、early exit 等方法已经成功利用

### dLLM 的独特机会
- AR LLM 的 difficulty 体现在"需要多少 context"
- dLLM 的 difficulty 体现在"需要多少 iteration"
- dLLM 天然支持 parallel processing，更容易实现 adaptive computation

### 建议的研究方向
1. **Mixture-of-Iterations**：借鉴 MoD，学习 per-token iteration allocation
2. **Speculative Denoising**：借鉴 speculative decoding，先粗后细
3. **Difficulty-aware Training**：训练时就考虑 token difficulty
