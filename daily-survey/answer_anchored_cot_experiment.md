# Answer-Anchored CoT 实验设计方案

**日期:** 2026-02-16  
**作者:** Longxuan Yu  
**状态:** 实验设计稿

---

## 1. 核心假设与动机

### 1.1 核心假设

**dLLM 是 difficulty-aware 的：** 离散扩散语言模型的 confidence 分布天然反映 token 难度。如果我们预先给定"难" token（如数学题的答案），模型应该能更高效地填充"简单" token（如推理步骤）。

### 1.2 理论动机

传统 AR 模型的 CoT：
```
Question → Step 1 → Step 2 → ... → Answer
```
- 必须按顺序生成，无法跳过
- 如果中间步骤出错，答案必然错误

dLLM 的潜在优势：
```
Question + [MASK]...[MASK] + Answer → 填充中间步骤
```
- 答案作为 anchor，约束推理方向
- 模型可以从两端向中间填充
- 类似人类"逆向推理"

### 1.3 与 Latent Forcing 的类比

Stanford 的 Latent Forcing (ICML 2026) 在图像生成中证明：
- Latents（高层结构）先 denoise
- Pixels（低层细节）后 denoise
- "Generation best starts with high-level structure before low-level detail"

**类比到 CoT：**
- Answer = 高层结构（先确定）
- CoT steps = 低层细节（后填充）

---

## 2. 模型选择

### 2.1 主选：LLaDA

**理由：**
1. **开源可用：** LLaDA 1.1 (8B) 和 LLaDA 2.1 都有开源权重
2. **性能验证：** LLaDA 2.1 在 GSM8K 上已有 baseline 数据
3. **Remask 机制：** LLaDA 支持 confidence-based remasking，与实验设计契合
4. **社区活跃：** 有较多复现和扩展工作

**具体版本：**
- 主实验：`LLaDA-8B-Instruct` (LLaDA 2.1)
- 消融实验：`LLaDA-8B-Base` (验证 instruction tuning 的影响)

### 2.2 备选：Dream

**理由：**
1. Dream 在某些任务上表现更好
2. 不同架构可以验证结论的普适性

**具体版本：**
- `Dream-7B` (如果可用)

### 2.3 不选 MDLM/SEDD

- 模型规模较小（通常 <1B）
- 主要用于 unconditional generation
- 缺乏 instruction following 能力

---

## 3. Benchmark 选择

### 3.1 主选：GSM8K

**理由：**
1. **难度适中：** 小学数学，CoT 步骤清晰
2. **答案格式统一：** 数字答案，易于提取和验证
3. **Baseline 丰富：** AR 模型和 dLLM 都有大量数据
4. **CoT 结构明确：** 通常 3-8 步推理

**数据集信息：**
- 训练集：7,473 题
- 测试集：1,319 题
- 答案格式：`#### <number>`

### 3.2 扩展：MATH (Level 1-3)

**理由：**
1. 验证在更难问题上的表现
2. MATH Level 1-3 难度适中，Level 4-5 可能超出 8B 模型能力

**数据集信息：**
- 测试集：5,000 题
- 按难度分级：Level 1 (最简单) → Level 5 (最难)
- 主要用 Level 1-3 (约 2,500 题)

### 3.3 不选 MMLU/ARC

- 多选题格式，CoT 不是必需
- 答案不是数值，harder to anchor

---

## 4. Prompt 格式设计

### 4.1 Baseline: Standard CoT (无 anchor)

```
<|system|>
You are a helpful math assistant. Solve the problem step by step.
<|user|>
{question}
<|assistant|>
Let me solve this step by step.
[MASK] [MASK] ... [MASK]
#### [MASK]
```

模型需要同时生成 CoT 和答案。

### 4.2 实验组 A: Answer-Anchored CoT (答案已知)

```
<|system|>
You are a helpful math assistant. The answer is given. Explain the reasoning.
<|user|>
{question}
The answer is {answer}.
<|assistant|>
Let me explain how to get {answer}.
[MASK] [MASK] ... [MASK]
#### {answer}
```

答案预先填入，模型只需填充 CoT。

### 4.3 实验组 B: Partial Answer Anchor (部分答案)

```
<|system|>
You are a helpful math assistant. Solve the problem step by step.
<|user|>
{question}
<|assistant|>
Let me solve this step by step.
[MASK] [MASK] ... [MASK]
#### {first_digit}[MASK]
```

只给答案的第一位数字，测试部分 anchor 的效果。

### 4.4 实验组 C: Wrong Answer Anchor (错误答案)

```
<|system|>
You are a helpful math assistant. The answer is given. Explain the reasoning.
<|user|>
{question}
The answer is {wrong_answer}.
<|assistant|>
Let me explain how to get {wrong_answer}.
[MASK] [MASK] ... [MASK]
#### {wrong_answer}
```

给错误答案，测试模型是否会"强行解释"或拒绝。

### 4.5 实验组 D: Self-Generated Anchor (两阶段)

**阶段 1：** 用 dLLM 快速生成答案（少量 diffusion steps）
```
<|user|>
{question}
<|assistant|>
#### [MASK]
```

**阶段 2：** 用生成的答案作为 anchor，填充 CoT
```
<|user|>
{question}
The answer is {self_generated_answer}.
<|assistant|>
Let me explain how to get {self_generated_answer}.
[MASK] [MASK] ... [MASK]
#### {self_generated_answer}
```

这是最实用的设置——不需要 oracle 答案。

---

## 5. 评估指标

### 5.1 主要指标

| 指标 | 定义 | 目的 |
|------|------|------|
| **Accuracy** | 最终答案正确率 | 核心性能指标 |
| **CoT Validity** | CoT 逻辑是否正确（人工/GPT-4 评估） | 验证 CoT 质量 |
| **Steps** | 平均 diffusion steps 数 | 效率指标 |
| **Latency** | 端到端生成时间 | 实际效率 |

### 5.2 分析指标

| 指标 | 定义 | 目的 |
|------|------|------|
| **Token Confidence Distribution** | 各位置的 confidence 分布 | 验证 difficulty-aware 假设 |
| **Generation Order** | Token 实际生成顺序 | 分析模型行为 |
| **Anchor Influence** | 有/无 anchor 时 confidence 变化 | 量化 anchor 效果 |

### 5.3 消融指标

| 指标 | 定义 | 目的 |
|------|------|------|
| **Accuracy vs. Steps** | 不同 step 数下的准确率 | 找到最优 step 数 |
| **Accuracy vs. Anchor Position** | Anchor 在不同位置的效果 | 理解位置敏感性 |

---

## 6. Baseline 对比

### 6.1 dLLM Baselines

| Baseline | 描述 | 来源 |
|----------|------|------|
| **LLaDA Standard** | 标准 LLaDA 推理，无 anchor | LLaDA 2.1 paper |
| **LLaDA + Remask** | 带 confidence-based remasking | LLaDA 2.1 paper |
| **Random Ordering** | 随机 token 生成顺序 | 消融实验 |
| **Confidence Ordering** | 高 confidence 先生成 | McDiffuSE 风格 |

### 6.2 AR Baselines

| Baseline | 描述 | 来源 |
|----------|------|------|
| **Llama-3-8B CoT** | 标准 AR CoT | Meta |
| **Llama-3-8B + Self-Consistency** | 多次采样取多数 | Wang et al. |
| **GPT-4 CoT** | 上界参考 | OpenAI |

### 6.3 对比维度

| 维度 | 对比内容 |
|------|----------|
| **Accuracy** | Answer-Anchored vs. Standard |
| **Efficiency** | Steps/Latency 对比 |
| **Robustness** | Wrong anchor 时的行为 |
| **Scalability** | 不同难度问题的表现 |

---

## 7. 实验流程

### 7.1 Phase 1: Pilot Study (1 周)

**目标：** 验证实验设置可行性

**任务：**
1. 搭建 LLaDA 推理环境
2. 在 GSM8K 测试集的 100 题上运行 baseline
3. 实现 Answer-Anchored prompt 格式
4. 验证 token confidence 可以提取

**产出：**
- 环境配置文档
- Baseline 数据
- 初步可行性报告

### 7.2 Phase 2: Main Experiments (2 周)

**目标：** 完成主要实验

**任务：**
1. GSM8K 全测试集 (1,319 题) 实验
2. 实验组 A-D 全部运行
3. 收集所有评估指标
4. 统计显著性检验

**产出：**
- 主实验结果表格
- Confidence 分布可视化
- 生成顺序分析

### 7.3 Phase 3: Analysis & Extension (1 周)

**目标：** 深入分析 + 扩展验证

**任务：**
1. MATH Level 1-3 扩展实验
2. Dream 模型验证（如果可用）
3. 消融实验（step 数、anchor 位置）
4. 错误案例分析

**产出：**
- 扩展实验结果
- 消融分析
- 论文初稿的实验部分

---

## 8. 预期结果与假设检验

### 8.1 主假设

**H1: Answer-Anchored CoT 提升准确率**
- 预期：实验组 A > Baseline，提升 5-15%
- 原因：答案约束减少搜索空间

**H2: Answer-Anchored CoT 减少 diffusion steps**
- 预期：实验组 A 需要更少 steps 达到相同准确率
- 原因：答案提供强约束，加速收敛

**H3: dLLM 的 confidence 分布反映 token difficulty**
- 预期：CoT 中间步骤的 confidence 低于答案位置
- 验证方法：可视化 confidence heatmap

### 8.2 次要假设

**H4: 部分 anchor 也有效**
- 预期：实验组 B > Baseline，但 < 实验组 A
- 意义：实际应用中可能只有部分信息

**H5: 错误 anchor 导致错误 CoT**
- 预期：实验组 C 生成"合理但错误"的 CoT
- 意义：理解模型的 anchor 依赖程度

**H6: Self-Generated Anchor 可行**
- 预期：实验组 D ≈ 实验组 A（如果第一阶段准确率高）
- 意义：实际应用的可行性

### 8.3 失败情况分析

**如果 H1 不成立：**
- 可能原因：LLaDA 的 bidirectional attention 不够强
- 后续：尝试 Dream 或其他架构

**如果 H2 不成立：**
- 可能原因：Anchor 没有被有效利用
- 后续：分析 attention pattern

**如果 H3 不成立：**
- 可能原因：Confidence 不是 difficulty 的好 proxy
- 后续：重新思考 difficulty 的定义

---

## 9. 资源需求

### 9.1 计算资源

| 资源 | 需求 | 备注 |
|------|------|------|
| GPU | 1x A100 80GB 或 2x A100 40GB | LLaDA-8B 推理 |
| 时间 | ~50 GPU hours | 全部实验 |
| 存储 | ~100GB | 模型权重 + 结果 |

### 9.2 人力资源

| 任务 | 时间 | 备注 |
|------|------|------|
| 环境搭建 | 2 天 | |
| 代码实现 | 3 天 | Prompt 格式 + 评估脚本 |
| 实验运行 | 5 天 | 包括 debug |
| 分析写作 | 4 天 | |
| **总计** | **~3 周** | |

---

## 10. 代码结构

```
answer_anchored_cot/
├── configs/
│   ├── llada_gsm8k.yaml
│   └── llada_math.yaml
├── data/
│   ├── gsm8k/
│   └── math/
├── src/
│   ├── model.py          # LLaDA 加载和推理
│   ├── prompts.py        # Prompt 模板
│   ├── evaluate.py       # 评估脚本
│   ├── analyze.py        # Confidence 分析
│   └── visualize.py      # 可视化
├── scripts/
│   ├── run_baseline.sh
│   ├── run_anchored.sh
│   └── run_ablation.sh
├── results/
│   └── ...
└── README.md
```

---

## 11. 风险与缓解

| 风险 | 可能性 | 影响 | 缓解措施 |
|------|--------|------|----------|
| LLaDA 不支持 partial mask | 中 | 高 | 提前验证，必要时修改代码 |
| Confidence 提取困难 | 低 | 中 | 查阅 LLaDA 源码 |
| 计算资源不足 | 低 | 高 | 使用云 GPU |
| 结果不显著 | 中 | 高 | 准备多个消融实验 |

---

## 12. 时间线

```
Week 1 (Feb 16-22):
├── Day 1-2: 环境搭建，LLaDA 部署
├── Day 3-4: Baseline 实验 (100 题 pilot)
└── Day 5-7: 实现 Answer-Anchored prompt

Week 2 (Feb 23 - Mar 1):
├── Day 1-3: GSM8K 全量实验
├── Day 4-5: 实验组 A-D 运行
└── Day 6-7: 初步结果分析

Week 3 (Mar 2-8):
├── Day 1-2: MATH 扩展实验
├── Day 3-4: 消融实验
├── Day 5-6: 可视化 + 深入分析
└── Day 7: 实验报告初稿
```

---

## 13. 成功标准

### 13.1 最低标准（论文可发）

- Answer-Anchored CoT 在 GSM8K 上准确率提升 ≥5%
- 或 diffusion steps 减少 ≥30% 且准确率不降
- Confidence 分布可视化支持 difficulty-aware 假设

### 13.2 理想标准（强论文）

- 准确率提升 ≥10%
- 在 GSM8K 和 MATH 上都有效
- Self-Generated Anchor (实验组 D) 可行
- 理论分析解释为什么有效

### 13.3 超预期标准（顶会）

- 提出通用的 Anchor-based dLLM 推理框架
- 在多个任务上验证（不只是数学）
- 与 ordering theory 结合，形成完整理论

---

## 14. 后续方向

如果实验成功，可以扩展到：

1. **Anchor 类型扩展：** 不只是答案，还可以是关键中间步骤
2. **多任务验证：** 代码生成、逻辑推理、常识问答
3. **与 Speculative Decoding 结合：** 用 anchor 指导 draft
4. **理论分析：** 为什么 anchor 有效？信息论解释

---

## 附录 A: GSM8K 示例

**问题：**
```
Janet's ducks lay 16 eggs per day. She eats three for breakfast every morning 
and bakes muffins for her friends every day with four. She sells the remainder 
at the farmers' market daily for $2 per fresh duck egg. How much in dollars 
does she make every day at the farmers' market?
```

**标准 CoT：**
```
Janet's ducks lay 16 eggs per day.
She eats 3 for breakfast, so 16 - 3 = 13 eggs remain.
She uses 4 for muffins, so 13 - 4 = 9 eggs remain.
She sells each egg for $2, so 9 × $2 = $18.
#### 18
```

**Answer-Anchored CoT：**
```
The answer is 18.
Janet's ducks lay 16 eggs per day.
She eats 3 for breakfast, so 16 - 3 = 13 eggs remain.
She uses 4 for muffins, so 13 - 4 = 9 eggs remain.
She sells each egg for $2, so 9 × $2 = $18.
#### 18
```

---

## 附录 B: 相关论文

| 论文 | 关联 |
|------|------|
| LLaDA 2.1 | 主要模型 |
| McDiffuSE | Ordering 优化 |
| dVoting | Token uncertainty 分析 |
| DAWN | 依赖图方法 |
| Latent Forcing | 理论启发 |
| Self-Consistency | AR baseline |
