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
