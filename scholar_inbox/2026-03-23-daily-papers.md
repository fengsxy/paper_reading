# Daily Papers — 2026-03-23

> 周一 arxiv 恢复正常更新。cs.LG 88 篇新投稿 + 66 篇 cross-list。以下 6 篇与研究方向高度相关。

## Diffusion Language Models

### 1. Mask Is What DLLM Needs: A Masked Data Training Paradigm for Diffusion LLMs
- **Authors:** (多作者)
- **Link:** https://arxiv.org/abs/2603.15803 (Mar 16, 2026)
- **Key:** 指出标准 DLLM 训练中均匀随机噪声调度忽略了真实序列的非均匀信息密度。提出 masked data training，根据 token 信息量调整 masking 概率，使模型关注更难的高信息密度区域。在多个 benchmark 上改进 dLLM 性能。
- **相关性:** ★★★ dLLM 训练方法改进，直接相关。

### 2. Omni-Diffusion: Unified Multimodal Understanding and Generation with Masked Discrete Diffusion
- **Link:** https://arxiv.org/abs/2603.06577 (Mar 6, 2026)
- **Key:** 用 masked discrete diffusion 替代 autoregressive backbone 实现多模态理解与生成统一。展示 diffusion 范式在 MLLM 中的可行性。
- **相关性:** ★★★ dLLM 扩展到多模态。

## Information Theory & Representation Learning

### 3. Neural Uncertainty Principle: A Unified View of Adversarial Fragility and LLM Hallucination
- **Authors:** (多作者)
- **Link:** https://arxiv.org/abs/2603.19562 (Mar 23, 2026 — **今日新出**)
- **Key:** 提出 Neural Uncertainty Principle (NUP)：输入与其 loss gradient 是共轭可观测量，受不可约不确定性下界约束。统一解释视觉模型的对抗脆弱性和 LLM 的幻觉现象——两者源于相同几何结构。建立了 input-gradient 不确定性乘积的理论下界。
- **相关性:** ★★★★ 信息论 × 对抗鲁棒性 × LLM 可信度，与你的多个研究兴趣直接交叉。**强烈推荐精读。**

### 4. GeoLAN: Geometric Learning of Latent Explanatory Directions in LLMs
- **Link:** https://arxiv.org/abs/2603.19460 (Mar 23, 2026 — **今日新出**)
- **Key:** 将 token 表示视为几何轨迹，基于 Kakeya 猜想发展出 KT-CW 和 KT-Attention 两个可微正则化器，约束 LLM 内部表示结构以提升可解释性。跨越纯数学与深度学习的有趣交叉。
- **相关性:** ★★★ 几何视角的表示学习 + 可解释性。

### 5. Continual Learning as Shared-Manifold Continuation Under Compatible Shift
- **Link:** https://arxiv.org/abs/2603.20036 (Mar 23, 2026 — **今日新出**)
- **Key:** 不靠参数正则化或 replay，而是直接约束新旧数据共享同一 latent manifold。几何视角处理 continual learning 的 forgetting 问题。
- **相关性:** ★★☆ 表示学习几何理论。

## Trustworthy AI & Alignment

### 6. The Autonomy Tax: Defense Training Breaks LLM Agents
- **Link:** https://arxiv.org/abs/2603.19423 (Mar 23, 2026 — **今日新出**)
- **Key:** 揭示 capability-alignment paradox：防御训练（抵抗 prompt injection）显著降低 agent 执行多步工具调用的能力。安全与能力之间存在根本性张力。对部署 LLM agent 的 safety 策略有重要启示。
- **相关性:** ★★★ Trustworthy AI / alignment。

---

### 值得留意但次优先

- **Residual Stream Is All You Need** (2603.19664): 证明 KV cache 完全冗余——key/value 是 residual stream 的确定性投影，可零误差重算。挑战 transformer 推理中的核心假设。
- **LeWorldModel** (2603.19312): 首个无需 EMA/预训练编码器/辅助损失的稳定 end-to-end JEPA。自稳定表示学习。
- **EvidenceRL** (2603.19532): 用 RL 强化证据一致性减少 LLM 幻觉，trustworthy AI 方向。
- **Do Post-Training Algorithms Actually Differ?** (2603.19335): OXRL 框架实现 51 种 post-training 算法的公平对比，发现排名随模型规模反转。
