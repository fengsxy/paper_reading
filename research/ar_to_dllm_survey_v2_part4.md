## 五、综合对比表

| 方案 | 注意力转换 | KV Cache | 转换成本 | 最大规模 | 核心优势 | 核心不足 |
|------|-----------|----------|----------|----------|----------|----------|
| **DiffuLLaMA** | 渐进退火→全bidir | ❌ | ~200B tokens (10%) | 7B | 理论数学基础最强 | 无KV cache，成本中等 |
| **Dream 7B** | 直接初始化→全bidir | ❌ | ~0.6T tokens | 7B | CART创新，planning碾压AR | 无KV cache，reasoning差距 |
| **RND1** | 直接切换→全bidir | ❌ | 中等 | 30B MoE | 最简单，layer-specific LR | 无KV cache |
| **Efficient-DLM** | Block-wise (间causal+内bidir) | ✅ | 10-100B tokens | 8B | 当前accuracy最优，clean context | Block size超参 |
| **SDAR** | Block-wise paradigm转换 | ✅ | 30-50B tokens (3-5%) | 30B MoE | 转换成本最低，推理超越AR | 无clean context/pos-dep mask |
| **LLaDA 2.0** | WSD三阶段渐进 | ✅ | 三阶段（最高） | 100B MoE | 规模最大，post-training最完整 | 训练成本最高 |
| **Mercury** | Block diffusion (商业) | ✅ | 万亿级（从头） | 未公开 | 1100 tok/s，商业可用 | 闭源 |
| **LLaDA** (对照) | 从头训练 全bidir | ❌ | 2.3T tokens | 8B | 充分训练可匹配AR | 计算成本极高 |

---

## 六、关键洞察（精读后的深层理解）

### 洞察1：Block-wise 是当前最优转换范式，原因在于 weight drift

Efficient-DLM 的 Figure 2e 给出了**定量证据**：
- Full bidir 转换后，attention 层和 FFN 层的 weight drift 都很大
- Block-wise + clean context 转换后，两者都很小
- Weight drift 越小 → 知识保留越多 → 转换后性能越好

DiffuLLaMA 的 annealing 试图缓解这个问题，但只是减慢了 drift，没有从根本上解决。Block-wise 从架构层面保证了大部分位置仍是 causal → 根本性地减少 drift。

### 洞察2：Clean context 是被严重低估的技术

Efficient-DLM 发现 clean context 贡献了 +9.46% 的提升——比 position-dependent masking (+4.38%) 和去掉 shift (+0.72%) 加起来都大。

但 SDAR 没有使用 clean context，LLaDA 2.0 在 Stable 阶段也没有。这意味着**现有最强方案还没有用上最强技巧**。组合 SDAR 的低成本 + Efficient-DLM 的 clean context 是一个低垂果实。

### 洞察3：AR 训练效率远高于 MDLM（SDAR 的公平对比）

同架构同数据对比：AR 大幅超越 MDLM。原因：
- AR 优化 NLL，每个 token 都参与梯度
- MDLM 优化 NELBO（loose upper bound），只有 masked tokens 参与 loss
- **结论：先训 AR 再转换永远比从头训 dLLM 更高效**

LLaDA 2.0 的 100B 实验也支持这个结论：AR 初始化的 dLLM 在训练早期就已经很好，从头训的需要更多 compute 才能追上。

### 洞察4：dLLM 在 planning/constraint satisfaction 上有范式级优势

Dream 7B 的 Sudoku 结果（81.0 vs AR 的 21.0）不是偶然——这是 diffusion 的并行+双向+迭代修正带来的固有优势。SDAR 在科学推理上超越 AR 也验证了这一点。

这个优势在 block-wise 方案中被部分保留（block 内有双向+迭代），但 block 间仍是 sequential。**如何在保持 KV cache 的同时最大化 diffusion 的 planning 优势，是一个开放问题。**

### 洞察5：Token shift 的必要性取决于 attention 模式

- 全 bidirectional 时：shift 有用（DiffuLLaMA, Dream 都用了）
- Block-wise + clean context 时：shift 有害（Efficient-DLM 不用更好）
- 原因：shift 是为了在全 bidir 下保留 AR 权重分布，但 block-wise 本身已解决这个问题

### 洞察6：LLaDA 2.0 的 WSD 揭示了一个重要设计空间

WSD 的核心思路是"先在全 MDLM 下学全局知识，再蒸馏到 block-wise"。这暗示：
- 全 MDLM 的全局建模能力 > block-wise 的局部建模能力
- 但全 MDLM 推理太慢
- **理想方案：训练时用全 MDLM，推理时用 block-wise + linear state 保持全局信息**
