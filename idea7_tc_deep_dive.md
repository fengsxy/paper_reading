# Idea 7 深挖：Total Correlation 视角分析 dLLM

*完整研究计划 - 2026-02-16*

---

## 📖 理论背景

### Total Correlation (TC) 是什么？

**定义：**
```
TC(X1, X2, ..., Xn) = Σ H(Xi) - H(X1, X2, ..., Xn)
                    = KL(P(X1,...,Xn) || Π P(Xi))
```

**直觉：**
- TC 衡量变量之间的 **总体依赖性**
- TC = 0 → 变量完全独立
- TC 高 → 变量之间有很多 redundancy/correlation

**与 Mutual Information 的关系：**
- MI 只能衡量两个变量之间的依赖
- TC 可以衡量任意多个变量之间的依赖
- TC 是 MI 的多变量推广

### Greg 的 CorEx 方法

**核心思想：**
```
找到 latent factors Y 使得：
TC(X) ≈ TC(X; Y) + TC(X | Y)

其中 TC(X; Y) 是 Y 解释的 correlation
TC(X | Y) 是剩余的 correlation
```

**CorEx 的优势：**
1. 无需模型假设
2. 线性复杂度 O(n)
3. 可以构建层次结构
4. 可解释性强

### 关键论文

1. **Discovering Structure in High-Dimensional Data Through Correlation Explanation** (NIPS 2014)
   - 原始 CorEx 论文
   - 核心：用 TC 发现数据中的结构

2. **Maximally Informative Hierarchical Representations** (AISTATS 2015)
   - 层次化 CorEx
   - 核心：每一层解释一部分 TC

3. **Fast structure learning with modular regularization** (NeurIPS 2019)
   - 更快的版本
   - 核心：模块化结构学习

---

## 🎯 核心研究问题

### 主问题：dLLM 和 AR 的 representation 在 TC 上有什么差异？

**假设 1：dLLM 的 token representations 有更低的 TC**
- 理由：dLLM 的 bidirectional attention 允许信息分布在不同 tokens
- AR 的每个 token 必须 encode 所有前面的信息 → 高 redundancy

**假设 2：dLLM 的 TC 结构更 "modular"**
- 理由：dLLM 可能学到更好的 factorization
- AR 的因果结构可能导致 entangled representations

**假设 3：TC 与 reasoning 能力相关**
- 理由：低 TC 意味着更好的 disentanglement
- Disentangled representations 可能更适合 reasoning

---

## 🔬 实验设计

### 实验 1：基础 TC 对比

**目标：** 比较 LLaDA vs LLaMA 的 token-level TC

**方法：**
```python
# 1. 准备数据
texts = load_benchmark_texts()  # 多种类型：reasoning, generation, etc.

# 2. 提取 hidden states
llada_states = extract_hidden_states(llada_model, texts)  # [batch, seq, hidden]
llama_states = extract_hidden_states(llama_model, texts)  # [batch, seq, hidden]

# 3. 计算 TC
# 方法 A: 直接在 hidden dimension 上计算
tc_llada = compute_tc(llada_states)  # TC across hidden dimensions
tc_llama = compute_tc(llama_states)

# 方法 B: 在 token positions 上计算
tc_llada_pos = compute_tc_across_positions(llada_states)
tc_llama_pos = compute_tc_across_positions(llama_states)
```

**预期结果：**
- dLLM 的 TC 更低（更 disentangled）
- 或者 dLLM 的 TC 结构不同（更 modular）

**挑战：**
- Hidden dimension 是 4096，直接计算 TC 可能不可行
- 需要降维或采样

**解决方案：**
```python
# 方案 1: PCA 降维
states_pca = PCA(n_components=100).fit_transform(states)
tc = compute_tc(states_pca)

# 方案 2: 随机采样 dimensions
sampled_dims = np.random.choice(4096, 100, replace=False)
tc = compute_tc(states[:, :, sampled_dims])

# 方案 3: 用 CorEx 的层次方法
corex = Corex(n_hidden=50)
corex.fit(states)
tc_explained = sum(corex.tcs)
```

### 实验 2：Layer-wise TC 分析

**目标：** 分析 TC 在不同 layers 的变化

**方法：**
```python
for layer_idx in range(num_layers):
    states = extract_layer_states(model, texts, layer_idx)
    tc[layer_idx] = compute_tc(states)

# 画出 TC vs layer 的曲线
plot(tc_llada, label='LLaDA')
plot(tc_llama, label='LLaMA')
```

**预期结果：**
- AR 模型：TC 可能随 layer 增加（信息累积）
- dLLM：TC 可能先增后减（类似 information bottleneck）

### 实验 3：TC 与 Task Performance 的关系

**目标：** 验证 TC 是否与 reasoning 能力相关

**方法：**
```python
# 1. 在不同任务上测试
tasks = ['gsm8k', 'arc', 'hellaswag', 'winogrande']

for task in tasks:
    # 提取该任务的 hidden states
    states = extract_states_for_task(model, task)
    tc = compute_tc(states)
    accuracy = evaluate_task(model, task)
    
    # 记录 (tc, accuracy) pair
    results.append((tc, accuracy))

# 2. 分析相关性
correlation = compute_correlation(tcs, accuracies)
```

**预期结果：**
- Reasoning tasks: 低 TC 与高 accuracy 相关
- Generation tasks: 可能没有明显相关

### 实验 4：CorEx 结构分析

**目标：** 用 CorEx 发现 dLLM vs AR 的 representation 结构差异

**方法：**
```python
# 1. 对 hidden states 应用 CorEx
corex_llada = Corex(n_hidden=50)
corex_llada.fit(llada_states)

corex_llama = Corex(n_hidden=50)
corex_llama.fit(llama_states)

# 2. 分析 cluster 结构
clusters_llada = corex_llada.clusters
clusters_llama = corex_llama.clusters

# 3. 可视化
visualize_clusters(clusters_llada, title='LLaDA')
visualize_clusters(clusters_llama, title='LLaMA')
```

**预期结果：**
- dLLM 可能有更 modular 的 cluster 结构
- AR 可能有更 entangled 的结构

---

## 📊 具体实验步骤

### Week 1: 环境搭建

```bash
# 1. 安装依赖
pip install torch transformers
pip install corex  # 或者 bio_corex
pip install scikit-learn matplotlib

# 2. 下载模型
# LLaDA-8B
git clone https://github.com/ML-GSAI/LLaDA
# 下载 checkpoint

# LLaMA-8B
# 从 HuggingFace 下载
```

### Week 2: 基础实验

```python
# extract_states.py
import torch
from transformers import AutoModel, AutoTokenizer

def extract_hidden_states(model, tokenizer, texts, layer=-1):
    """提取指定 layer 的 hidden states"""
    states = []
    for text in texts:
        inputs = tokenizer(text, return_tensors='pt')
        with torch.no_grad():
            outputs = model(**inputs, output_hidden_states=True)
        # outputs.hidden_states[layer]: [1, seq_len, hidden_dim]
        states.append(outputs.hidden_states[layer].squeeze(0))
    return states

# compute_tc.py
import numpy as np
from corex import Corex

def compute_tc_corex(states, n_hidden=50):
    """用 CorEx 估计 TC"""
    # states: [n_samples, n_features]
    corex = Corex(n_hidden=n_hidden)
    corex.fit(states)
    return sum(corex.tcs)

def compute_tc_direct(states):
    """直接计算 TC (需要离散化)"""
    # 离散化
    n_bins = 10
    states_discrete = np.digitize(states, np.linspace(states.min(), states.max(), n_bins))
    
    # 计算 TC = sum(H(Xi)) - H(X)
    from scipy.stats import entropy
    h_marginal = sum(entropy(np.bincount(states_discrete[:, i])) for i in range(states_discrete.shape[1]))
    # H(X) 需要更复杂的估计...
    pass
```

### Week 3: 分析与可视化

```python
# analyze.py
import matplotlib.pyplot as plt

def plot_tc_comparison(tc_llada, tc_llama, layers):
    plt.figure(figsize=(10, 6))
    plt.plot(layers, tc_llada, 'b-o', label='LLaDA')
    plt.plot(layers, tc_llama, 'r-s', label='LLaMA')
    plt.xlabel('Layer')
    plt.ylabel('Total Correlation')
    plt.legend()
    plt.title('TC across layers: dLLM vs AR')
    plt.savefig('tc_comparison.png')

def plot_corex_clusters(corex, title):
    # 可视化 cluster 结构
    pass
```

### Week 4: 写 Initial Findings

- 整理实验结果
- 与 Greg 讨论
- 决定下一步方向

---

## 🎯 预期贡献

### 如果假设成立（dLLM TC 更低）：

1. **理论贡献：** 首次用 TC 框架分析 dLLM
2. **解释性贡献：** 解释为什么 dLLM 在 reasoning 上好
3. **方法贡献：** 提出用 TC 作为 representation quality 的 metric

### 如果假设不成立：

1. **Negative result 也有价值：** 说明 TC 不是 dLLM 优势的来源
2. **可以 pivot：** 转向其他 information-theoretic measures
3. **至少建立了 baseline：** 为后续研究提供参考

---

## ⚠️ 风险与缓解

### 风险 1: TC 计算在高维空间不准

**缓解：**
- 用 CorEx 的层次方法
- 用 PCA 降维
- 用多种方法交叉验证

### 风险 2: LLaDA 和 LLaMA 不是 fair comparison

**缓解：**
- 控制模型大小（都用 8B）
- 控制训练数据（如果可能）
- 分析 per-layer 差异而不是 overall 差异

### 风险 3: 结果不显著

**缓解：**
- 在多种任务上测试
- 用统计检验
- 如果不显著，分析为什么

---

## 📚 必读材料

### Greg 的论文（按重要性排序）

1. **Discovering Structure in High-Dimensional Data Through Correlation Explanation** (NIPS 2014)
   - https://arxiv.org/abs/1406.1222
   - 核心 CorEx 论文，必读

2. **Maximally Informative Hierarchical Representations** (AISTATS 2015)
   - https://arxiv.org/abs/1410.7404
   - 层次化 CorEx

3. **The Information Sieve** (ICML 2016)
   - 信息筛选方法

### 代码资源

1. **CorEx 原版：** https://github.com/gregversteeg/CorEx
2. **Bio CorEx（更完整）：** https://github.com/gregversteeg/bio_corex
3. **LLaDA：** https://github.com/ML-GSAI/LLaDA

---

## 🗓️ Timeline

| Week | 任务 | 产出 |
|------|------|------|
| 1 | 读 Greg 的论文，搭建环境 | 理解 TC/CorEx |
| 2 | 提取 hidden states，计算 TC | 初步数据 |
| 3 | Layer-wise 分析，可视化 | 图表 |
| 4 | 与 Greg 讨论，写 findings | Initial report |
| 5-6 | 根据讨论深入 | 更多实验 |
| 7-8 | 写 workshop paper | Draft |

---

## 💬 与 Greg 讨论的问题

1. **TC 在高维空间的估计：** 有什么推荐的方法？
2. **CorEx 的 hyperparameters：** n_hidden 怎么选？
3. **TC 与 reasoning 的关系：** 有没有理论支持？
4. **其他 information-theoretic measures：** 除了 TC 还有什么值得看的？

---

*这个计划的核心优势：与 Greg 的 expertise 完美匹配，有成熟工具，novelty 高*
