# AR→dLLM 转换方法调研报告

**作者：Claw | 日期：2026-03-15 | 为 Yu 准备**

---

## 一、问题定义

从头训练 dLLM 极其昂贵（LLaDA-8B 用了数万亿 token），而开源 AR 模型（LLaMA、Qwen）已经积累了大量知识。**能否把已训练好的 AR 模型"转换"为 dLLM，以低成本获得 dLLM 的并行解码、双向上下文等优势？**

### 核心挑战

1. **注意力模式不匹配**：AR 是 causal attention（下三角 mask），dLLM 是 bidirectional attention（全注意力）。直接从 causal 切到 bidirectional 会破坏预训练权重的分布
2. **训练目标不匹配**：AR 预测 next token，dLLM 预测所有 masked token。loss landscape 完全不同
3. **位置编码适配**：AR 的 RoPE 等位置编码针对 causal 设计，bidirectional 场景下需要调整
4. **训练效率**：continual pretraining 需要多少 token 才能完成转换？越少越好
5. **能力保持**：转换后能否保留 AR 模型的 reasoning、ICL 等能力？

---

## 二、调研论文列表（7篇核心论文）

| # | 论文 | 会议/年份 | 核心方法 | 规模 |
|---|------|-----------|----------|------|
| 1 | **DiffuLLaMA** (Gong et al.) | ICLR 2025 | Continual pretraining + attention mask annealing | 127M→7B |
| 2 | **Efficient-DLM** (Fu et al., NVIDIA) | arXiv 2025.12 | Block-wise attention + position-dependent masking | 8B |
| 3 | **SDAR** (Cheng et al.) | arXiv 2025.10 | 轻量 paradigm conversion + block diffusion | 最高 30B MoE |
| 4 | **Dream 7B** (Ye et al., HKU) | arXiv 2025.08 | 从 Qwen2.5 初始化 + masked diffusion SFT | 7B |
| 5 | **Block Diffusion (BD3-LM)** (Arriola et al.) | ICLR 2025 Oral | Block 间 AR + block 内 diffusion | 中小规模 |
| 6 | **DiffusionVL** (HUST) | arXiv 2025.12 | AR→diffusion VLM 翻译框架 | 多模态 |
| 7 | **LLaDA 2.0** (Bie et al.) | arXiv 2025.12 | 从头训练 vs AR 初始化对比 | 100B |

---

## 三、分类框架

```
AR → dLLM 转换方法
│
├── ① 全双向转换（Full Bidirectional Conversion）
│   └── DiffuLLaMA: causal → bidirectional，完整转换
│
├── ② 块级混合转换（Block-wise Hybrid Conversion）
│   ├── Efficient-DLM: block 间 causal + block 内 bidirectional
│   ├── SDAR: block-wise paradigm conversion
│   └── Block Diffusion: 原生设计但思路相同
│
├── ③ 直接初始化 + 扩散微调（Init + Diffusion Finetuning）
│   ├── Dream 7B: 用 Qwen2.5 权重初始化
│   └── DiffusionVL: 翻译 AR VLM 到 diffusion VLM
│
└── ④ 从头训练（对照组）
    └── LLaDA / LLaDA 2.0: 纯 diffusion pretraining
```
