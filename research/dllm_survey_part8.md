## 七、你的机会：Story 怎么讲

### 现有方案的空白地带

从上面的分类可以看出一个清晰的空白：

**没有人同时解决信息损失和错误累积，且用高效的线性记忆机制。**

- MetaState 解决了信息损失，但用 GRU（慢、容量小、不可并行）
- ProSeCo/CDLM 解决了错误累积，但没有跨步记忆
- KV Cache 方案只解决计算效率，没有语义增强
- Block Diffusion 需要从头训练，且 block 内问题仍在

### 提议的 Story

**标题方向**：Linear State Memory for Discrete Diffusion Language Models

**核心论点**：
> dLLM 的跨步信息流可以用 linear state space 来建模。Linear state 不只是"更好的 GRU"，而是 denoising trajectory 上的 **sufficient statistic 近似**——它在跨步传递过程中以 O(1) 空间保留了 posterior estimate 的关键信息，同时天然支持并行训练和高效推理。

**三层贡献**：

1. **理论层**（从信息论角度重新理解 Information Island）：
   - 每步的 h_t → x_t 是一个 rate-distortion 问题
   - Linear state S_t = α_t ⊙ S_{t-1} + β_t v_t k_t^T 是在 capacity constraint 下的最优线性近似
   - 可以分析：给定 state 容量 M×d，什么样的 gating schedule 最大化跨步互信息 I(h_t; S_t)?

2. **方法层**（替换 MetaState 的 GRU → Gated DeltaNet/KDA）：
   - Delta rule 的"擦除-写入"语义天然适合 denoising：
     - 早期（高噪声）：大量写入，建立全局结构
     - 晚期（低噪声）：精确修改，局部细节
   - Gating 控制遗忘：随 denoising 进展，保留已确定的信息，遗忘不确定的
   - 可并行训练（chunk-wise algorithm），解决 K-step unrolling 的效率问题

3. **系统层**（与 KV Cache 统一）：
   - Linear state 的更新和 KV cache 的复用可以统一：
     - 已稳定 token 的 KV → cache（Elastic-Cache 方式）
     - 变化中 token 的信息 → 写入 linear state
   - 这样 linear state 只需要 focus 在 "正在变化的信息" 上，capacity 更高效
   - 推理时：shallow layers cache + deep layers refresh + linear state side channel

### 与你之前的 Diffusion Optimal Path 工作的连接

你之前做的 temporal score rescaling、flow matching 离散化误差分析，跟 Information Island 是同一个问题的不同面：

- **Optimal path**：什么样的 denoising schedule 最小化离散化误差？
- **Optimal memory**：给定 linear state 容量，什么样的 gating schedule 最大化跨步信息保持？

联合优化 = **schedule + memory co-optimization**：
- denoising schedule 决定每步揭示多少 token（信息生产速率）
- gating schedule 决定 state 保留/遗忘多少（信息保持容量）  
- 两者应该协同：高噪声阶段 state 写入多、遗忘快；低噪声阶段 state 保留多、写入少

这就把 "换个模块" 的工作升级为 "信息论驱动的 dLLM 跨步优化框架"。

### 实验计划建议

**Phase 1: 验证 Linear State > GRU（2-3周）**
- 在 MetaState 的 codebase 上，把 GRU Updater 替换为 Gated DeltaNet
- 控制变量：相同的 Mixer/Injector，相同的训练配置
- Backbone: LLaDA-8B（跟 MetaState 论文一致）
- Benchmarks: GSM8K, HumanEval, MBPP, ARC, HellaSwag
- 预期：至少 match MetaState，训练速度更快（可并行 unrolling）

**Phase 2: 与 KV Cache 结合（1-2周）**
- 将 Elastic-Cache 的浅层 cache + 深层 refresh 与 linear state 结合
- 测量：推理速度提升 + 质量变化
- 预期：速度接近 Elastic-Cache，质量超过纯 Elastic-Cache

**Phase 3: Schedule-Memory 联合优化（如果做 top venue）**
- 对 denoising schedule 和 gating schedule 做联合搜索/优化
- 理论分析：mutual information bound
- 这部分可以作为最大的 novelty

---

## 八、参考文献

1. Xia et al. "MetaState: Persistent Working Memory for Discrete Diffusion Language Models." arXiv:2603.01331, 2026.
2. Wang et al. "Remasking Discrete Diffusion Models with Inference-Time Scaling." NeurIPS 2025. arXiv:2503.00307.
3. Zhang et al. "Corrective Diffusion Language Models." ICML 2025. arXiv:2512.15596.
4. Peng et al. "Learn from Your Mistakes: Self-Correcting Masked Diffusion Models (ProSeCo)." arXiv:2602.11590, 2026.
5. Xie et al. "Soft-Masked Diffusion Language Models." arXiv:2510.17206, 2025.
6. Ranjan et al. "Elastic-Cache: Attention Is All You Need for KV Cache in Diffusion LLMs." arXiv:2510.14973, 2025.
7. Ma et al. "dKV-Cache: The Cache for Diffusion Language Models." arXiv:2505.15781, 2025.
8. Arriola et al. "Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models." ICLR 2025 Oral. arXiv:2503.09573.
9. Lu et al. "STaRR: Spatial-Temporal Token-Dynamics-Aware Responsive Remasking." arXiv:2601.04205, 2026.
10. Yang et al. "Gated Delta Networks: Improving Mamba2 with Delta Rule." ICLR 2025. arXiv:2412.06464.

**补充参考：**
- Nie et al. "LLaDA: Large Language Diffusion Models." arXiv:2502.09992, 2025.
- Ye et al. "Dream 7B: Diffusion Large Language Models." arXiv:2508.15487, 2025.
- Sahoo et al. "MDLM: Simple and Effective Masked Diffusion Language Models." NeurIPS 2024.
- Zhang et al. "Kimi Linear: An Expressive, Efficient Attention Architecture." arXiv:2510.26692, 2025.
- Liu et al. "Plug-and-Play Context Feature Reuse for Efficient Masked Generation (ReCAP)." NeurIPS 2025.
- Pynadath et al. "CANDI: Hybrid Discrete-Continuous Diffusion Models." arXiv:2510.22510, 2025.
- Wu et al. "Fast-dLLM: Training-free Acceleration of Diffusion LLM." arXiv:2505.22618, 2025.
