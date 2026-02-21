---
layout: default
type: analysis
series: dwarkesh
episode: 37
guest: ""
title: "Jeff Dean & Noam Shazeer — 25 years at Google: from PageRank to AGI - Analysis"
source_url: "https://www.youtube.com/watch?v=v0gjI__RyCY"
transcript_url: /transcripts/dwarkesh/37_jeff_dean_noam_shazeer_25_years_at_google_from_pagerank_to_agi/
permalink: /transcripts/dwarkesh/37_jeff_dean_noam_shazeer_25_years_at_google_from_pagerank_to_agi.analysis/
---

# Analysis: Jeff Dean & Noam Shazeer — 25 Years at Google: from PageRank to AGI

## 0. 3-5 句摘要

Google 首席科学家 Jeff Dean 和 Transformer 共同发明者 Noam Shazeer 回顾了他们在 Google 25年的技术演进历程，从 PageRank 到 Gemini。最令人震撼的数据点是：Google 25%的代码提交已经由 AI 编码模型生成，而 Shazeer 预测未来需要"一百万个自动化研究员"来发明 AI 时代所需的一切。对话揭示了多个关键历史节点：Jeff Dean 1990年的本科论文就实现了数据并行和模型并行（现代大规模训练的两大支柱），Shazeer 2007年构建的两万亿 token n-gram 模型是现代语言模型的直接前身，而 Transformer 的诞生源于"注意力机制可以完全替代循环"这一看似疯狂的想法。两人对量化（quantization）的讨论尤其深刻：从 FP64 到 FP4 甚至 1-bit 的精度下降，本质上是"算术便宜、数据搬运昂贵"这一硬件趋势的算法映射。

## 1. 反共识/非显然观点

- **如果内存成本下降比算术快，AI 可能看起来像20年前的 AI** [09:57-10:13]：Shazeer 提出了一个精彩的反事实——如果硬件趋势相反（查找便宜、计算贵），我们可能仍在使用基于大规模查找表的 AI（类似 n-gram 模型），而非基于矩阵乘法的深度学习。这说明 AI 的发展方向在很大程度上是由硬件经济学而非纯粹的算法洞察驱动的。
- **Transformer 的关键创新不是注意力机制本身，而是"去掉循环"** [约25:00]：注意力机制在 Transformer 之前就存在（Bahdanau attention），但 Shazeer 等人的突破是证明你可以完全用注意力替代 RNN 的循环结构——这使得训练可以完全并行化，从而利用 GPU 的大规模并行计算能力。
- **Google 的 2007 年两万亿 token 语言模型是现代 LLM 的直接祖先** [15:39-18:38]：Jeff Dean 将翻译系统从"12小时翻译一句话"优化到"100毫秒"，通过构建内存中的压缩 n-gram 数据结构。这个系统后来被用于自动补全、拼写纠正等多种用途——本质上就是"用统计模型理解语言"的早期实践。

## 2. 关键洞察

- 量化的进展速度惊人：从 TPUv1 的 INT8（2016年还不确定是否可行）到现在的 FP4 甚至 1-bit，每一步都是"芯片设计师和算法设计师必须同时看到全局"才能实现的协同设计。
- Shazeer 加入 Google 的动机是"赚够钱然后去做 AI 研究"——结果 Google 本身成了最好的 AI 研究平台。这个故事说明了大公司在 AI 研究中的独特优势：提供了个人研究者无法获得的计算资源和数据。
- Larry Page 的名言"我们最大的成本是机会成本"驱动了 Google 的技术决策——包括构建专用 AI 芯片（TPU）而非依赖通用 CPU。
- 世界 GDP 可能因 AI 而增长"数个数量级"——Shazeer 认为"一万亿美元不再酷了，酷的是一千万亿美元"。

## 3. Takeaway

- 对于 AI 从业者：关注硬件-算法协同设计的机会。当前最大的效率提升不在于更好的模型架构，而在于更好地利用硬件特性（低精度计算、并行化、内存层次结构）。Shazeer 的洞察——"算法跟随硬件"——是理解 AI 未来发展方向的关键框架。
