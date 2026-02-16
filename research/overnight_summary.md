# 🌙 Overnight Research Summary

**日期:** 2026-02-16  
**为:** Longxuan Yu (Ted)

---

## 1. Karpathy 关键 Insights

### nanochat 项目 (43.4k stars)
- **核心理念:** 用 $100 / 3小时 训练 ChatGPT 级别模型
- **单一复杂度参数 `--depth`** 控制所有超参数 — 极简主义设计
- **Leaderboard 驱动开发:** "Time-to-GPT-2" 激励社区贡献

### 对 dLLM 研究的启发
1. **Scaling Laws 框架:** nanochat 的 `runs/scaling_laws.sh` 可作为 dLLM scaling 实验参考
2. **研究问题:** dLLM 能否达到同样的 CORE 分数？需要多少时间/成本？
3. **长期目标:** 建立 dLLM 的 "nanochat" — 极简、可复现、可 fork

---

## 2. 最推荐的研究方向

### 🏆 Token Ordering 理论 (最有潜力)

**核心假设:** "Easy First, Hard Later" — 低 entropy token 应先生成

**理论框架:**
- 最优 ordering $\pi^*$ 最小化总条件熵
- 等价于最大化每步互信息增益
- 与 Mixture-of-Depths (MoD) 思想高度契合

**论文 Outline 已完成:** `ordering_paper_outline.md`
- 目标会议: NeurIPS 2026 / ICML 2026
- 预计 8-9 页主文 + 3-5 页附录

### 🥈 Answer-Anchored CoT (实验验证)

**核心假设:** 预先给定答案，dLLM 能更高效填充推理步骤

**实验设计已完成:** `answer_anchored_cot_experiment.md`
- 主模型: LLaDA 8B Instruct
- 主 Benchmark: GSM8K
- 4 个实验条件 + 完整 metrics

### 🥉 Adaptive Iteration (借鉴 AR 方法)

**相关工作调研完成:** `token_difficulty_related_work.md`
- Speculative Decoding → Speculative Denoising
- Mixture-of-Depths → Mixture-of-Iterations
- Early Exit → Per-position convergence

---

## 3. 最成熟的代码库

### 🏆 首选: MDLM + DUO 组合

| 优势 | 说明 |
|------|------|
| 代码质量 | ⭐⭐⭐⭐⭐ 模块化清晰，易于修改 |
| 规模适中 | 适合有限资源快速迭代 |
| 理论完整 | SUBS parameterization |
| 生态完善 | DUO (蒸馏), Eso-LMs (KV cache) |

**实验路径:** MDLM (理解基础) → DUO (少步生成) → 自己的改进

### 🥈 备选: LLaDA / Dream (大规模验证)

- LLaDA 8B: HuggingFace 直接加载，有 Instruct 版本
- Dream 7B: 提供完整 SFT 训练代码
- 适合需要与 LLaMA 级别模型对比的场景

---

## 4. 下一步行动建议

### 本周 (优先级高)

1. **精读 Mixture-of-Depths 论文** (arXiv:2404.02258)
   - 这是 ordering 理论最直接相关的工作
   - 理解 top-k routing 机制

2. **搭建 MDLM 实验环境**
   ```bash
   git clone https://github.com/kuleshov-group/mdlm
   # 跑通 sample_eval 验证环境
   ```

3. **设计 ordering 实验的 pilot study**
   - 在 MDLM 上对比 random vs confidence-based vs entropy-based ordering
   - 验证 "easy first" 假设

### 下周

4. **完善 ordering 理论框架**
   - 补充 Theorem 1 的精确假设
   - 证明 greedy easy-first 的近似比

5. **开始 Answer-Anchored CoT 实验**
   - 下载 LLaDA 8B Instruct
   - 在 GSM8K 上跑 baseline

### 本月

6. **撰写 ordering 论文初稿**
   - 目标: 2 月底完成 Section 1-4
   - 3 月中完成实验

---

## 📁 生成的文件清单

| 文件 | 内容 |
|------|------|
| `karpathy_insights.md` | Karpathy 最新项目分析 |
| `dllm_codebase_survey.md` | 6 个 dLLM 代码库详细评估 |
| `token_difficulty_related_work.md` | AR LLM adaptive computation 调研 |
| `ordering_theory_draft.md` | 信息论框架理论草稿 |
| `ordering_paper_outline.md` | 完整论文 outline |
| `answer_anchored_cot_experiment.md` | 实验设计方案 |

---

*Generated: 2026-02-16 16:01 UTC*
