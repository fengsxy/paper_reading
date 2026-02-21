---
title: "2026-02-20-diffusion-dllm"
---

# Scholar Inbox 精选 - 2026-02-20

## Diffusion / dLLM / 表征相关论文（ranking_score >= 0.85）

---

### 1. One-step Language Modeling via Continuous Denoising
**Authors:** Chanhyuk Lee, Jaehoon Yoo, Manan Agarwal, Sheel Shah, Jerry Huang, Aditi Raghunathan, Seunghoon Hong, Nicholas M. Boffi, Jinwoo Kim
**ArXiv:** [2602.16813](https://arxiv.org/abs/2602.16813) ✅
**Ranking Score:** 0.966

**摘要：** 挑战了"离散扩散是离散模态生成建模的必要条件"这一广泛假设。提出 Flow-based Language Model (FLM)，在 one-hot token encoding 上做欧几里得去噪，用交叉熵目标训练，并引入时间重参数化大幅提升训练稳定性。通过蒸馏得到 FMLM，实现 few-step 甚至 one-step 生成——单步生成质量超过现有方法的 8 步质量。在 LM1B 和 OWT 上匹配 SOTA discrete diffusion 的生成质量。

**亮点：** 这篇直接动摇了 dLLM 社区的核心假设：离散扩散未必是离散数据的最优路线。连续流在 one-hot 空间上的建模 + 蒸馏到 flow map 的思路非常优雅，且有代码（[github.com/david3684/flm](https://github.com/david3684/flm)）。对 Yu 的研究方向（diffusion + representation）高度相关——如果连续流能在离散模态上胜出，那 dLLM 的理论基础和实践路线都需要重新审视。

---

### 2. DODO: Discrete OCR Diffusion Models
**Authors:** Sean Man, Roy Ganz, Roi Ronen, Shahar Tsiper, Shai Mazor, Niv Nayman
**ArXiv:** [2602.16872](https://arxiv.org/abs/2602.16872) ✅
**Ranking Score:** 0.868

**摘要：** 首个将 block discrete diffusion 用于 OCR 的 VLM。核心观察：OCR 是高度确定性任务（视觉输入严格决定唯一输出），理论上非常适合扩散模型的并行解码。但现有 masked diffusion 在 OCR 的精确匹配要求下会出现结构性不稳定。DODO 通过将生成分解为 block 来缓解全局扩散的同步误差，实现接近 SOTA 精度的同时推理速度提升 3x。

**亮点：** 有趣的 niche application——扩散模型在"确定性生成"场景下的优势和陷阱。Block decomposition 缓解同步误差的思路可能对其他需要精确输出的 dLLM 应用（代码生成、数学推理）有启发。

---

## 值得关注（0.70-0.85）

### 3. DDiT: Dynamic Patch Scheduling for Efficient Diffusion Transformers
**Authors:** Dahye Kim, Deepti Ghadiyaram, Raghudeep Gadde
**ArXiv:** [2602.16968](https://arxiv.org/abs/2602.16968)
**Ranking Score:** 0.758

**摘要：** 提出动态 tokenization 策略：早期去噪步骤用粗粒度 patch 建模全局结构，后期用细粒度 patch 精炼局部细节。在 FLUX-1.Dev 上实现 3.52x 加速，Wan 2.1 上 3.2x 加速，不损失生成质量和 prompt adherence。

**亮点：** 工程实用性强。动态 patch 调度的思路也可以迁移到 dLLM 的 token-level masking 策略上——不同去噪阶段对不同粒度信息的需求确实不同。

---

*今日 digest 共 7 篇论文，2 篇 ≥ 0.85，1 篇 borderline。整体偏少，但第一篇 FLM 质量很高。*
