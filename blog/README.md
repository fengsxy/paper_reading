# Paper Survey Blog Index

Greg Ver Steeg 推荐论文的详细分析 (2026-02-16)

---

## 论文列表

| # | 论文 | 文件 | 核心主题 |
|---|------|------|---------|
| 1 | [Drifting Models](drifting_models.md) | `drifting_models.md` | One-step generation 新范式 |
| 2 | [Wright-Fisher Unified Diffusion](wright_fisher_unified_diffusion.md) | `wright_fisher_unified_diffusion.md` | 统一 discrete/Gaussian/simplicial diffusion |
| 3 | [Information-Estimation Metric](information_estimation_metric.md) | `information_estimation_metric.md` | 用 denoising error 定义距离 |
| 4 | [Parallel Token Generation](parallel_token_generation.md) | `parallel_token_generation.md` | Flow-based 并行生成 |
| 5 | [Hot Mess Theory](hot_mess_theory.md) | `hot_mess_theory.md` | AI 失败的 bias-variance 分析 |
| 6 | [Diffusion for Compression](diffusion_compression.md) | `diffusion_compression.md` | 用 diffusion 做图像压缩 |

---

## 与 dLLM 研究的关联总结

### 最直接相关

1. **Wright-Fisher** → dLLM 的理论基础，selection coefficient 可能解释 optimal ordering
2. **IEM** → Token difficulty metric，可用于 difficulty-based ordering
3. **Hot Mess** → Incoherence 分析，optimal ordering 的目标可以是 minimize variance

### 间接相关

4. **Parallel Token Gen** → 竞争方法，flow 的 Jacobian 可以分析 token 依赖
5. **Drifting Models** → One-step 思想，dLLM 能否做 one-step？
6. **Diffusion Compression** → 压缩视角，"容易压缩" = "先生成"

---

## 核心启发：Optimal Ordering 的理论框架

综合这些论文，一个统一的 optimal ordering 理论框架浮现：

### 定义 Token Difficulty

用 IEM 的思想：
$$D_i = \mathbb{E}[\text{denoising error at position } i]$$

### 定义 Optimal Ordering

用 Hot Mess 的思想：
$$\text{order}^* = \arg\min_{\text{order}} \text{Variance}[\text{output}]$$

### 理论工具

用 Wright-Fisher 的框架：
- Selection coefficient $s_i$ ↔ Token difficulty $D_i$
- Fixation time ↔ Generation order

### 验证方法

1. 计算不同 ordering 的 incoherence
2. 比较 random / confidence / difficulty-based / optimal
3. 分析 bias-variance tradeoff

---

## 下一步

1. 实现 token difficulty metric（基于 IEM）
2. 在 dLLM 上测试 difficulty-based ordering
3. 用 bias-variance 分解评估不同 ordering
4. 尝试用 Wright-Fisher 框架做理论分析
