# Daily Paper Review — 2026-04-22

**Paper**: On the Quantization Robustness of Diffusion Language Models in Coding Benchmarks
**arXiv ID**: 2604.20079v1
**Date**: 2026-04-22
**Tag**: dLLM / Quantization / Efficiency

---

## 1. Task

**问题形式化**：

AR LLM 在 coding 任务上性能强，但推理成本高（memory 和 latency）。Diffusion-based LLM（d-LLM）通过 iterative denoising 提供 bounded inference cost，但其 **post-training quantization（PTQ）行为** 几乎未被探索。

论文首次系统研究 PTQ（GPTQ + modified HAWQ）在 **CoDA**（diffusion-based coding LLM）上的效果，并与 AR counterpart（Qwen3-1.7B）对比。

---

## 2. Challenge

| 方法 | 困境 |
|------|------|
| AR coding LLM 量化 | 已被充分研究，效果已知 |
| d-LLM 量化 | 几乎未被探索，是否有同样的鲁棒性未知 |
| Low bitwidth 量化 | 2-4 bit 时 AR 模型性能崩溃，d-LLM 是否也不同 |

---

## 3. Insight & Novelty

**核心发现**：d-LLM 在 low bitwidth 量化下比 AR 更鲁棒。

> 在 2-4 bit 时，CoDA 的精度下降幅度显著小于 Qwen3-1.7B。在 HumanEval 和 MBPP benchmarks 上，CoDA 的性能衰减更小。

**为什么？** 论文提出几个可能原因：

1. d-LLM 的 iterative denoising 过程可能对 quantization noise 有天然的平滑效应
2. 多步 denoising 的 error averaging 可能弥补单步的 quantization 误差

**创新点 1**：HAWQ 的 modified version 用于 d-LLM
- **解决的问题**：如何为 d-LLM 定制量化方法
- **具体设计**：调整 HAWK 的 Hessian-aware 权重选择，适配 d-LLM 的特性

**创新点 2**：Mixed-precision 配置提供 smooth trade-off
- **解决的问题**：如何在 accuracy、latency、memory 之间做权衡
- **具体设计**：不同 layer 用不同 bitwidth，找到最优配置

---

## 4. Potential Flaw

- **只在 CoDA 上验证**：其他 d-LLM 架构是否同样鲁棒未知
- **Coding 任务专项**：通用语言建模的量化鲁棒性可能不同
- **4-bit 以下**：2-bit 及以下的极端量化未充分测试

---

## 5. Motivation

**General idea**：d-LLM 的 iterative denoising 天然地做 error averaging——每一步的 quantization error 在下一个 step 会被部分纠正。这个特性让 d-LLM 比 AR 更能容忍 quantization noise。
