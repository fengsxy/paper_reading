### 类别③：保持跨步连续信息（解决信息损失，表示层干预）

#### MetaState — Persistent Working Memory for dLLMs (arXiv 2026.03)

**核心洞察**：dLLM 每步的 hidden state h_t 包含丰富的语义信息（长程依赖、不确定性、token 间关系），但采样+remasking 后全部丢弃。这就是 "Information Island" 问题。

**方法**：三个轻量模块组成的循环记忆：
1. **Mixer**（cross-attention）：从 backbone hidden state 读取信息到 M 个固定 memory slots
2. **Updater**（GRU）：用 gating 机制融合新旧信息，跨步传递
3. **Injector**（cross-attention）：把更新后的 memory 写回 backbone
- Memory 大小 M×D_s 与序列长度 N 无关 → O(NM) 额外计算
- K-step unrolling 训练：展开 K 步 denoising，梯度可以流过整个 recurrent chain

**好在哪**：
- 直接解决 Information Island——第一个为 dLLM 设计持久记忆的工作
- Backbone-agnostic：在 LLaDA-8B 和 Dream-7B 上都有提升
- Backbone frozen，只训练轻量模块（参数开销很小）
- 在 reasoning 和 coding benchmark 上一致提升

**不足（也是你的机会）**：
- **用了 GRU** 作为 Updater——GRU 是非线性门控 RNN，存在：
  - 无法并行化（严格顺序依赖）
  - 长程依赖建模能力有限（梯度消失）
  - 信息容量受限于 hidden size
- 没有与 KV cache 复用方案结合
- K-step unrolling 训练成本随 K 增长

---

#### Soft-Masked DLM (arXiv 2025.10)

**核心洞察**：hard mask（0或1）是信息损失的直接原因。如果用连续概率分布代替 hard mask，就能保留部分信息。

**方法**：
- 不再用 [MASK] token，而是用 token 概率分布作为输入
- 每步输出不采样为离散 token，而是保持为 probability vector
- 下一步的输入 = 上一步的 soft probability（类似 soft token）
- 需要从头训练

**好在哪**：
- 从根本上消除了 hard mask 的信息瓶颈
- 模型可以看到上一步"不太确定"的 token 的概率分布，而非被迫选择一个
- 理论上优雅

**不足**：
- **需要从头预训练**——不能直接用现有的 LLaDA/Dream
- 训练效率问题：soft token 需要维护 |V|×d 的 embedding 矩阵运算
- 实际效果在大规模 LLM 上未验证

---

#### CANDI — Hybrid Discrete-Continuous Diffusion (arXiv 2025.10)

**核心洞察**：纯离散扩散丢失连续信号，纯连续扩散在离散数据上效果差。能否结合两者？

**方法**：
- 在离散 masking process 之外，额外引入连续 latent variable
- 离散部分处理 token identity，连续部分保持 hidden representation
- 两个通道共同演化

**好在哪**：
- 保留了离散扩散的优势（masked diffusion 的训练简单性）
- 连续通道弥补了信息损失

**不足**：
- 需要修改训练过程
- 复杂度显著增加
- 在大规模 LLM 上的可行性存疑
