## 七、与你的 Linear State Memory 工作的关系

### 直接连接点

1. **实验 backbone 选择**：
   - 用 Efficient-DLM 或 SDAR 转换出的 block-wise dLLM 作为 backbone
   - Block 间已有 KV cache（已解决），block 内的 Information Island 仍存在 → 你的 linear state 填这个空
   - 比在全 bidirectional dLLM 上做 linear state 更实际（全双向推理太慢）

2. **LLaDA 2.0 的 WSD 启示**：
   - WSD 的 Stable 阶段（全 MDLM）学到了全局知识，Decay 阶段蒸馏到 block-wise 时**会损失全局信息**
   - 你的 linear state 可以作为 Decay 阶段的补偿——在 block-wise 结构中用 linear state 保持全局信息
   - Story：**"WSD trains global knowledge, linear state preserves it during block-wise inference"**

3. **Mercury 的商业启示**：
   - dLLM 的商业价值在于速度（1100 tok/s）
   - 如果 linear state memory 能减少 denoising 步数（更少步达到相同质量）→ 直接提升商业价值
   - "架构与 diffusion 正交" → linear attention 做 backbone 也可行

4. **SDAR 的公平对比给了理论支撑**：
   - AR 训练效率 >> MDLM → 先训 AR 再转换是正确路线
   - 你的方案不需要从头训——基于已有的 AR→dLLM 转换模型加 linear state augmentation
   - 成本极低：frozen backbone + 轻量 linear state 模块

### 建议的实验路线

**Phase 0: 选 backbone（1天）**
- 下载 Efficient-DLM 8B 或 SDAR 8B（如果开源）
- 或者自己用 SDAR 方法从 Qwen3 8B 转换（30-50B tokens）

**Phase 1: Linear State > GRU in MetaState（2-3周）**
- 把 MetaState 的 GRU Updater 替换为 Gated DeltaNet
- 在 block-wise backbone 上测试
- 预期：match 或超越 MetaState，训练速度更快

**Phase 2: 与 KV Cache 统一（1-2周）**
- Block 间 KV cache + block 内 linear state
- 测量 speed × quality Pareto

**Phase 3: Schedule-Memory 联合优化（如果投 top venue）**

---

## 八、参考文献

1. Gong et al. "Scaling Diffusion Language Models via Adaptation from Autoregressive Models." ICLR 2025. arXiv:2410.17891.
2. Fu et al. "Efficient-DLM: From Autoregressive to Diffusion Language Models, and Beyond in Speed." arXiv:2512.14067, 2025.
3. Cheng et al. "SDAR: A Synergistic Diffusion-AutoRegression Paradigm." arXiv:2510.06303, 2025.
4. Ye et al. "Dream 7B: Diffusion Large Language Models." arXiv:2508.15487, 2025.
5. Bie et al. "LLaDA 2.0: Scaling Up Diffusion Language Models to 100B." arXiv:2512.15745, 2025.
6. Radical Numerics. "RND1: Simple, Scalable AR-to-Diffusion Conversion." Tech Report, 2025.
7. Khanna et al. "Mercury: Ultra-Fast Language Models Based on Diffusion." arXiv:2506.17298, 2025.
8. Arriola et al. "Block Diffusion: Interpolating Between AR and Diffusion LMs." ICLR 2025 Oral. arXiv:2503.09573.
9. Nie et al. "LLaDA: Large Language Diffusion Models." arXiv:2502.09992, 2025.
10. DiffusionVL. "Translating Any AR Models into Diffusion VLMs." arXiv:2512.15713, 2025.

---

**精读笔记**：完整的论文精读笔记（包含 abstract 看不到的技术细节）见 `research/ar_to_dllm_reading_notes.md`
