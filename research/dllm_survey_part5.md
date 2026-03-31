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
