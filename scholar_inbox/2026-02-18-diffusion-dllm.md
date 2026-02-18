# Scholar Inbox 精选 - 2026-02-18

## Diffusion / dLLM / 表征相关论文（ranking_score >= 0.85）

---

### 1. MAGE: All-[MASK] Block Already Knows Where to Look in Diffusion LLM
**Authors:** Omin Kwon, Yeonjae Kim, Doyeon Kim, Minseo Kim, Yeonhong Park, Jae W. Lee  
**ArXiv:** [2602.14209](https://arxiv.org/abs/2602.14209) ✅

**摘要：** 关注 block/masked diffusion LLM 在长上下文场景下的推理瓶颈：KV cache + 频繁内存访问使得 memory access 成为主要瓶颈。论文从注意力/访存视角出发，尝试让“全 [MASK] 的 block”更高效地定位需要看的上下文位置，从而减少无效计算与访存。

**亮点：** 这类工作很可能直接影响 dLLM 的工程落地（长上下文吞吐/延迟），比单纯提升指标更“可用”。

---

### 2. Scaling Beyond Masked Diffusion Language Models
**Authors:** Subham Sekhar Sahoo et al.  
**ArXiv:** [2602.15014](https://arxiv.org/abs/2602.15014) ✅

**摘要：** 讨论离散扩散语言模型中“masked diffusion”一枝独秀的现状，并尝试给出更可扩展（beyond masked）的建模/训练/采样路线，以改善扩散 LM 在生成速度与质量之间的折中。

**亮点：** 如果你在做 dLLM 路线选型/下一代架构，这篇更像是“路线图/反思 + 推进”的论文，值得通读。

---

### 3. LaViDa-R1: Advancing Reasoning for Unified Multimodal Diffusion Language Models
**Authors:** Shufan Li et al.  
**ArXiv:** [2602.14147](https://arxiv.org/abs/2602.14147) ✅

**摘要：** 面向统一多模态 dLLM 的推理能力提升，方法上更接近“R1/推理强化”思路：把多模态理解与生成纳入同一 diffusion LM 框架，并强化其 reasoning 行为（paper 侧重点是 reasoning，而非仅做多模态生成）。

**亮点：** 多模态 dLLM 目前还在早期阶段，reasoning 方向的探索可能比单纯的感知/生成指标更能拉开差距。

---

### 4. Language Model Memory and Memory Models for Language
**Author:** Benjamin L. Badger  
**ArXiv:** [2602.13466](https://arxiv.org/abs/2602.13466) ✅

**摘要：** 从“表征作为记忆”的角度分析语言模型 embedding/hidden state 中到底能存多少输入信息、信息以什么形式存在，以及这种“隐式记忆”与显式记忆机制（memory models）之间的关系。

**亮点：** 适合和 information theory / representation 的问题串起来看：当你在做长上下文、检索增强、或可解释性时，它提供一个更“可度量”的切入点。

---

### 5. DriveFine: Refining-Augmented Masked Diffusion VLA for Precise and Robust Driving
**Authors:** Chenxu Dang et al.  
**ArXiv:** [2602.14577](https://arxiv.org/abs/2602.14577) ✅

**摘要：** 将 masked diffusion 引入驾驶场景的 VLA（Vision-Language-Action）生成式规划，并通过“refining-augmented”的方式强化规划精度与鲁棒性，缓解扩散式 planner 的对齐与稳定性问题。

**亮点：** diffusion 不只做文本：在 VLA/具身/自动驾驶里，扩散式生成规划+后验 refine 可能是一个可复制的范式。
