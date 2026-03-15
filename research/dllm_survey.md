# 离散扩散语言模型(dLLM)两大核心问题调研报告

**作者：Claw | 日期：2026-03-15 | 为 Yu 准备**

---

## 一、问题定义

离散扩散语言模型(dLLM)通过迭代去噪生成文本：从全 [MASK] 序列出发，每步预测并揭示部分 token。与自回归模型相比，dLLM 支持并行解码、双向上下文、灵活生成模式。但存在 **两个核心瓶颈**：

### 问题 A：错误累积 (Error Accumulation)
- **本质**：一旦某步揭示了错误 token，该错误在后续步骤中被视为"正确上下文"，误导后续预测
- **原因**：标准 masked diffusion 训练只监督 masked 位置，模型无法区分已揭示 token 的正确/错误
- **表现**：并行解码越激进（每步揭示越多 token），错误累积越严重；quality-speed Pareto 曲线急剧下降

### 问题 B：信息损失 (Information Loss / Information Island)
- **本质**：每步去噪后，采样+remasking 将连续 hidden state h_t 压缩为离散 token，丢弃了丰富的中间表示
- **原因**：标准 dLLM 的 reverse process 是 Markovian 的：p(x_{t-1}|x_t)，只依赖当前离散序列
- **表现**：跨步不一致（实体漂移、前后矛盾）、全局结构丢失、重复重建上下文的计算浪费

### 两个问题的关系
这两个问题**不独立**：信息损失加剧错误累积（因为模型每步都从头重建上下文，没有"记忆"来维持一致性）；错误累积反过来产生更多噪声上下文，使信息损失更严重。理想方案应该**同时缓解**两个问题。

---

## 二、调研论文列表 (10篇核心论文)

| # | 论文 | 会议/年份 | 解决问题 | 核心方法 |
|---|------|-----------|----------|----------|
| 1 | **MetaState** (Xia et al.) | arXiv 2026.03 | 信息损失 | GRU 持久记忆跨步传递 |
| 2 | **ReMDM** (Wang et al.) | NeurIPS 2025 | 错误累积 | 推理时 remasking + 纠错 |
| 3 | **CDLM** (Corrective DLM) | ICML 2025 | 错误累积 | 训练时监督错误 token |
| 4 | **ProSeCo** (Learn from Mistakes) | arXiv 2026.02 | 错误累积 | 自纠正 SFT + corrector loop |
| 5 | **Soft-Masked DLM** | arXiv 2025.10 | 信息损失 | 连续概率代替 hard mask |
| 6 | **Elastic-Cache** | arXiv 2025.10 | 信息损失(计算) | 自适应 KV cache 复用 |
| 7 | **dKV-Cache** (Ma et al.) | arXiv 2025.05 | 信息损失(计算) | 延迟 KV cache 策略 |
| 8 | **Block Diffusion (BD3-LM)** | ICLR 2025 Oral | 两者兼顾 | 块级 AR + 块内扩散 |
| 9 | **STaRR** | arXiv 2026.01 | 错误累积 | 时空动态感知 remasking |
| 10 | **Gated DeltaNet** (Yang et al.) | ICLR 2025 | 信息损失(架构) | 线性注意力 + delta rule |

---

## 三、分类框架与详细分析

我把现有解决方案按 **"解决什么问题" × "在哪个阶段干预"** 分成四大类：

```
                    ┌─────────────────────────────────────────┐
                    │          解决错误累积                      │
                    │                                         │
  训练时干预 ──────► │ ① 训练纠错能力                           │
                    │    CDLM, ProSeCo                        │
                    │                                         │
  推理时干预 ──────► │ ② Remasking 策略                        │
                    │    ReMDM, STaRR, Dream (low-conf remask) │
                    └─────────────────────────────────────────┘
                    
                    ┌─────────────────────────────────────────┐
                    │          解决信息损失                      │
                    │                                         │
  表示层干预 ──────► │ ③ 保持跨步连续信息                       │
                    │    MetaState, Soft-Masked DLM, CANDI     │
                    │                                         │
  计算层干预 ──────► │ ④ KV Cache 复用                         │
                    │    Elastic-Cache, dKV-Cache, Fast-dLLM   │
                    └─────────────────────────────────────────┘
                    
                    ┌─────────────────────────────────────────┐
                    │          两者兼顾                         │
                    │                                         │
  架构层干预 ──────► │ ⑤ 混合架构                              │
                    │    Block Diffusion, SDAR                 │
                    └─────────────────────────────────────────┘
```
## 四、各类方案详细分析

### 类别①：训练纠错能力（解决错误累积）

#### CDLM — Corrective Diffusion Language Models (ICML 2025)

**核心洞察**：标准 MDLM 训练只在 masked 位置施加 loss，模型从未学过"判断已揭示 token 是否正确"。结果就是：模型对正确 token 和错误 token 给出相似的 confidence，无法定位需要纠正的位置。

**方法**：在训练时引入 absorbing-uniform mixture objective——不仅监督 masked→clean 的预测，还显式监督 visible-but-corrupted token，让模型学会：
- 对错误的已揭示 token 输出低 confidence
- 对正确的已揭示 token 输出高 confidence
- 这样 remasking 时可以用 confidence 精确定位错误位置

**好在哪**：
- 从根本上解决了 MDLM 的"盲区"——模型终于能区分对错
- 在 Code Revision Benchmark 上大幅超越标准 MDLM
- Post-training 方案，不需要改架构

**不足**：
- 需要额外训练，不是 training-free
- 只解决了错误累积，没有解决信息损失
- 需要设计 corruption 策略（如何生成训练用的错误 token）

---

#### ProSeCo — Learn from Your Mistakes (arXiv 2026.02)

**核心洞察**：在 CDLM 基础上更进一步——不仅训练模型识别错误，还训练模型**自动纠正**错误。

**方法**：
1. **ProSeCo SFT**：训练时让模型先预测、再看自己的错误、再纠正，形成 self-correcting 训练循环
2. **ProSeCo Sampling**：推理时在每个 denoising step 之后加 corrector loop——把当前输出喂回模型，让模型重新预测所有位置，用新预测替换旧的已揭示 token
3. 每个 corrector loop 花费 S 次额外 NFE（Neural Function Evaluation）

**好在哪**：
- 在 LLaDA-8B 上：HumanEval 从 48.17→62.20，GSM8K 从 77.48→82.18
- 超越了同体量的 Llama3.1-Instruct（AR 模型）
- 支持 quality-efficiency trade-off：可以调 corrector 频率和步数
- 比 ReMDM 效果更好（ReMDM 在 HumanEval 上反而降了）

**不足**：
- 每个 corrector loop 增加计算开销
- 仍然没有跨步记忆——每次纠正都是独立的 forward pass
### 类别②：Remasking 策略（解决错误累积，推理时干预）

#### ReMDM — Remasking Discrete Diffusion Models (NeurIPS 2025)

**核心洞察**：标准 masked diffusion 一旦揭示 token 就不能改了。ReMDM 引入"反悔机制"——允许已揭示的 token 被重新 mask 掉，再重新预测。

**方法**：
- 定义一个自定义 backward process，其中包含 remasking 概率
- 推理时每步可以把低 confidence 的已揭示 token 重新 mask
- 从连续时间 discrete diffusion 框架严格推导，不是 ad-hoc heuristic
- 增加采样步数 → 质量提升（inference-time compute scaling）

**好在哪**：
- Training-free，直接应用到预训练 MDLM 上
- 理论上有保证（从 CTMC 框架推导）
- 在分子设计等科学领域效果显著
- 支持 inference-time scaling：更多步 → 接近 AR 质量

**不足**：
- 在 LLM 任务上提升有限（HumanEval 上不降不升：40.24→40.24）
- 每步需要额外的 remasking 决策，增加了推理复杂度
- 没有利用历史信息，每步重新判断

---

#### STaRR — Spatial-Temporal Token-Dynamics-Aware Responsive Remasking (arXiv 2026.01)

**核心洞察**：现有 remasking 策略用静态 confidence 阈值，忽略了 token confidence 的**时空动态**——同一位置在不同步骤的 confidence 变化趋势才是关键信号。

**方法**：
- **时间维度**：追踪每个 token position 的 confidence 随 denoising step 的变化趋势（上升=稳定，下降=不可靠）
- **空间维度**：考虑相邻 token 的 confidence 相关性（一个错误 token 周围的 token 也可能不可靠）
- 动态调整 remasking 概率，避免不必要的 remask（静态阈值会 remask 太多正确 token）

**好在哪**：
- Training-free
- 比 ReMDM 更精准——减少了对正确 token 的误 remask
- 利用了跨步的 confidence 动态信息（某种程度上缓解了信息损失）

**不足**：
- 需要维护每个 position 的 confidence 历史（额外内存）
- 仍然在 token level 操作，没有 hidden state level 的信息保持
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
### 类别④：KV Cache 复用（解决信息损失/计算冗余，计算层干预）

#### Elastic-Cache (arXiv 2025.10)

**核心洞察**：dLLM 每步对所有 token 重算 QKV，但大多数 token 的 KV 在相邻步骤间变化极小（尤其浅层）。这是巨大的计算浪费。

**方法**：三个关键观察 → 一个自适应策略
1. 远处的 [MASK] token 主要提供 length bias，可以 block-wise cache
2. KV 变化随层深度增加 → 浅层可以安全 cache，深层需要刷新
3. 最高 attention 的 token KV drift 最小 → 用它作为"是否需要刷新"的保守指标

**Elastic-Cache** = when to refresh（attention-aware drift test）+ where to refresh（从第 l* 层开始往深层刷新）

**好在哪**：
- Training-free，architecture-agnostic
- 8.7× 加速（GSM8K 256 tokens），45.1× 加速（长序列）
- 精度几乎无损
- 比 confidence-based 方案（如 Fast-dLLM）高 6.8× throughput

**不足**：
- 只解决计算效率，不解决信息损失的质量问题
- KV cache 复用的隐含假设：adjacent steps 的 hidden state 相似 → 在 high noise 阶段可能不成立
- 没有跨步信息传递的语义增强

---

#### dKV-Cache (arXiv 2025.05)

**核心洞察**：不同 token 在 diffusion 过程中的表示变化速度不同。已揭示的 token 表示趋于稳定，masked token 变化剧烈。

**方法**：两个变体
1. **dKV-Cache-Decode**：延迟缓存——token 被揭示后，延迟几步再开始 cache 其 KV（等表示稳定）
   - 几乎无损，甚至在长序列上**提升**性能（说明现有 dLLM 推理时 under-utilize 了上下文）
2. **dKV-Cache-Greedy**：更激进的缓存，缩短 cache 生命周期，从 O(L³) 降到 O(L²)
   - 更快但有质量损失

**好在哪**：
- Training-free
- 2-10× 加速
- dKV-Cache-Decode 的发现很有启发：cache 不仅加速，还能提升质量——说明 **信息保持本身就有价值**

**不足**：
- Cache 的是 KV pair（注意力层的中间产物），不是更高层的语义信息
- 没有学习"保持什么、忘记什么"的能力

---

#### Fast-dLLM & Fast-dLLM v2 (arXiv 2025)

**方法**：Block-wise KV cache + confidence-aware parallel decoding
- DualCache：维护 prefix 和 suffix 两个 KV cache
- v2 进一步结合 Block Diffusion 的左到右块级解码

**好在哪**：
- 第一个将 KV cache 引入 dLLM 的工作
- DualCache 设计巧妙：prefix cache 存已解码内容，suffix cache 存 [MASK] 上下文

**不足**：
- 依赖 block-wise 解码假设
- Approximate cache，有精度损失
### 类别⑤：混合架构（两者兼顾）

#### Block Diffusion / BD3-LM (ICLR 2025 Oral)

**核心洞察**：纯 dLLM 无法用 KV cache（双向注意力），纯 AR 无法并行。把序列分成 block，block 间 AR、block 内 diffusion，就能两全。

**方法**：
- 序列分成固定大小的 block
- Block 间：自回归地从左到右生成（前一个 block 作为 context）
- Block 内：masked diffusion 并行去噪
- 前面 block 的 KV 可以直接 cache（已完全 decode，不会再变）

**好在哪**：
- KV cache 自然可用（block 间是因果的）
- 支持任意长度生成（不再需要固定序列长度）
- 在 language modeling benchmark 上 SOTA（diffusion 模型中）
- 错误不会跨 block 传播（每个 block 独立 denoise）

**不足**：
- Block 内仍然有标准 dLLM 的两个问题
- Block 边界处的连贯性依赖 AR 的上下文传递
- Block 大小是超参数，影响 speed-quality trade-off

---

#### Gated DeltaNet (ICLR 2025) — 作为 MetaState Updater 的替代

**这不是 dLLM 论文**，但它是你方案的核心组件。

**核心思想**：结合 gating（自适应遗忘）和 delta rule（精确记忆修改），得到一个线性时间的序列模型。

**Delta Rule 更新**：
```
S_t = (1 - β_t * k_t * k_t^T) * S_{t-1} + β_t * v_t * k_t^T
```
- β_t: 学习率（学习的）
- k_t: key（要写入的地址）
- v_t: value（要写入的内容）
- 先"擦除"旧的 k_t 对应的记忆，再写入新的 v_t

**加上 Gating**：
```
S_t = α_t ⊙ S_{t-1} + β_t * v_t * k_t^T
```
- α_t: 遗忘门（scalar 或 channel-wise）
- 控制保留多少旧记忆

**为什么适合替代 GRU**：
1. **可并行**：chunk-wise 并行算法，O(L) 但高度 GPU 友好
2. **精确记忆修改**：delta rule 的 "擦除-写入" 比 GRU 的 "混合" 更精确
3. **已在大规模验证**：Qwen3.5 用 Gated DeltaNet 做 3:1 hybrid（3层 GDN : 1层 full attention）
4. **信息容量更大**：state 是 d×d 矩阵（vs GRU 的 d 向量）

**Kimi Linear (KDA)** 进一步改进：scalar gate → channel-wise gate，每个特征维度独立遗忘。
## 五、综合对比表

| 方案 | 解决问题 | 干预阶段 | 需要训练? | 兼容现有dLLM? | 核心优势 | 核心不足 |
|------|----------|----------|-----------|---------------|----------|----------|
| **CDLM** | 错误累积 | 训练 | ✅ Post-train | ✅ | 模型学会区分对错 | 需设计corruption策略 |
| **ProSeCo** | 错误累积 | 训练+推理 | ✅ SFT | ✅ | 自纠正，超越AR模型 | Corrector loop增加NFE |
| **ReMDM** | 错误累积 | 推理 | ❌ | ✅ | 理论严格，inference-time scaling | LLM任务提升有限 |
| **STaRR** | 错误累积 | 推理 | ❌ | ✅ | 精准remask，减少误杀 | 需维护confidence历史 |
| **MetaState** | 信息损失 | 训练 | ✅ 轻量 | ✅ (frozen backbone) | 首个跨步记忆方案 | GRU瓶颈，不可并行 |
| **Soft-Masked** | 信息损失 | 训练 | ✅ 从头 | ❌ | 从根本消除hard mask | 需从头预训练 |
| **Elastic-Cache** | 计算冗余 | 推理 | ❌ | ✅ | 45×加速，几乎无损 | 不提升生成质量 |
| **dKV-Cache** | 计算冗余 | 推理 | ❌ | ✅ | Cache反而提升质量 | 只cache KV，非语义 |
| **Block Diffusion** | 两者 | 架构 | ✅ 从头 | ❌ | KV cache天然可用 | Block内问题仍在 |
| **Gated DeltaNet** | (组件) | 架构 | - | - | 线性时间，可并行，大规模验证 | 需要适配到dLLM |

---

## 六、关键洞察：这些方案好在哪？为什么好？

### 洞察1：错误累积的本质是"训练-推理不匹配"
- MDLM训练时只见 masked position，推理时需要判断 visible token 对不对
- CDLM/ProSeCo 的成功说明：**让模型在训练时看到错误**是解决错误累积的最有效方式
- ReMDM 效果不如 ProSeCo，因为 remask 只是给了"第二次机会"，但模型仍然不知道哪里错了

### 洞察2：信息损失的本质是"接口瓶颈"
- dLLM 的连续 hidden state → 离散 token 的映射是 lossy channel
- MetaState 的成功证明：**bypass 这个 channel**（用 side channel 传递连续信息）是有效的
- dKV-Cache 的意外发现（cache 提升质量）进一步验证：**跨步信息保持本身就有价值**

### 洞察3：KV Cache 和跨步记忆是两个不同层面的问题
- KV Cache（Elastic-Cache, dKV-Cache）：解决的是**计算效率**——避免重复计算相似的 KV
- 跨步记忆（MetaState）：解决的是**信息质量**——保持语义信息跨步传递
- 前者是后者的近似子集：cache KV 隐含地保持了部分信息，但没有"学习保持什么"的能力
## 七、你的机会：Story 怎么讲

### 现有方案的空白地带

从上面的分类可以看出一个清晰的空白：

**没有人同时解决信息损失和错误累积，且用高效的线性记忆机制。**

- MetaState 解决了信息损失，但用 GRU（慢、容量小、不可并行）
- ProSeCo/CDLM 解决了错误累积，但没有跨步记忆
- KV Cache 方案只解决计算效率，没有语义增强
- Block Diffusion 需要从头训练，且 block 内问题仍在

### 提议的 Story

**标题方向**：Linear State Memory for Discrete Diffusion Language Models

**核心论点**：
> dLLM 的跨步信息流可以用 linear state space 来建模。Linear state 不只是"更好的 GRU"，而是 denoising trajectory 上的 **sufficient statistic 近似**——它在跨步传递过程中以 O(1) 空间保留了 posterior estimate 的关键信息，同时天然支持并行训练和高效推理。

**三层贡献**：

1. **理论层**（从信息论角度重新理解 Information Island）：
   - 每步的 h_t → x_t 是一个 rate-distortion 问题
   - Linear state S_t = α_t ⊙ S_{t-1} + β_t v_t k_t^T 是在 capacity constraint 下的最优线性近似
   - 可以分析：给定 state 容量 M×d，什么样的 gating schedule 最大化跨步互信息 I(h_t; S_t)?

2. **方法层**（替换 MetaState 的 GRU → Gated DeltaNet/KDA）：
   - Delta rule 的"擦除-写入"语义天然适合 denoising：
     - 早期（高噪声）：大量写入，建立全局结构
     - 晚期（低噪声）：精确修改，局部细节
   - Gating 控制遗忘：随 denoising 进展，保留已确定的信息，遗忘不确定的
   - 可并行训练（chunk-wise algorithm），解决 K-step unrolling 的效率问题

3. **系统层**（与 KV Cache 统一）：
   - Linear state 的更新和 KV cache 的复用可以统一：
     - 已稳定 token 的 KV → cache（Elastic-Cache 方式）
     - 变化中 token 的信息 → 写入 linear state
   - 这样 linear state 只需要 focus 在 "正在变化的信息" 上，capacity 更高效
   - 推理时：shallow layers cache + deep layers refresh + linear state side channel

### 与你之前的 Diffusion Optimal Path 工作的连接

你之前做的 temporal score rescaling、flow matching 离散化误差分析，跟 Information Island 是同一个问题的不同面：

- **Optimal path**：什么样的 denoising schedule 最小化离散化误差？
- **Optimal memory**：给定 linear state 容量，什么样的 gating schedule 最大化跨步信息保持？

联合优化 = **schedule + memory co-optimization**：
- denoising schedule 决定每步揭示多少 token（信息生产速率）
- gating schedule 决定 state 保留/遗忘多少（信息保持容量）  
- 两者应该协同：高噪声阶段 state 写入多、遗忘快；低噪声阶段 state 保留多、写入少

这就把 "换个模块" 的工作升级为 "信息论驱动的 dLLM 跨步优化框架"。

### 实验计划建议

**Phase 1: 验证 Linear State > GRU（2-3周）**
- 在 MetaState 的 codebase 上，把 GRU Updater 替换为 Gated DeltaNet
- 控制变量：相同的 Mixer/Injector，相同的训练配置
- Backbone: LLaDA-8B（跟 MetaState 论文一致）
- Benchmarks: GSM8K, HumanEval, MBPP, ARC, HellaSwag
- 预期：至少 match MetaState，训练速度更快（可并行 unrolling）

**Phase 2: 与 KV Cache 结合（1-2周）**
- 将 Elastic-Cache 的浅层 cache + 深层 refresh 与 linear state 结合
- 测量：推理速度提升 + 质量变化
- 预期：速度接近 Elastic-Cache，质量超过纯 Elastic-Cache

**Phase 3: Schedule-Memory 联合优化（如果做 top venue）**
- 对 denoising schedule 和 gating schedule 做联合搜索/优化
- 理论分析：mutual information bound
- 这部分可以作为最大的 novelty

---

## 八、参考文献

1. Xia et al. "MetaState: Persistent Working Memory for Discrete Diffusion Language Models." arXiv:2603.01331, 2026.
2. Wang et al. "Remasking Discrete Diffusion Models with Inference-Time Scaling." NeurIPS 2025. arXiv:2503.00307.
3. Zhang et al. "Corrective Diffusion Language Models." ICML 2025. arXiv:2512.15596.
4. Peng et al. "Learn from Your Mistakes: Self-Correcting Masked Diffusion Models (ProSeCo)." arXiv:2602.11590, 2026.
5. Xie et al. "Soft-Masked Diffusion Language Models." arXiv:2510.17206, 2025.
6. Ranjan et al. "Elastic-Cache: Attention Is All You Need for KV Cache in Diffusion LLMs." arXiv:2510.14973, 2025.
7. Ma et al. "dKV-Cache: The Cache for Diffusion Language Models." arXiv:2505.15781, 2025.
8. Arriola et al. "Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models." ICLR 2025 Oral. arXiv:2503.09573.
9. Lu et al. "STaRR: Spatial-Temporal Token-Dynamics-Aware Responsive Remasking." arXiv:2601.04205, 2026.
10. Yang et al. "Gated Delta Networks: Improving Mamba2 with Delta Rule." ICLR 2025. arXiv:2412.06464.

**补充参考：**
- Nie et al. "LLaDA: Large Language Diffusion Models." arXiv:2502.09992, 2025.
- Ye et al. "Dream 7B: Diffusion Large Language Models." arXiv:2508.15487, 2025.
- Sahoo et al. "MDLM: Simple and Effective Masked Diffusion Language Models." NeurIPS 2024.
- Zhang et al. "Kimi Linear: An Expressive, Efficient Attention Architecture." arXiv:2510.26692, 2025.
- Liu et al. "Plug-and-Play Context Feature Reuse for Efficient Masked Generation (ReCAP)." NeurIPS 2025.
- Pynadath et al. "CANDI: Hybrid Discrete-Continuous Diffusion Models." arXiv:2510.22510, 2025.
- Wu et al. "Fast-dLLM: Training-free Acceleration of Diffusion LLM." arXiv:2505.22618, 2025.
