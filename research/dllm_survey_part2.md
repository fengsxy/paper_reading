## 四、各类方案详细分析

### 类别①：训练纠错能力（解决错误累积）

#### CDLM — Corrective Diffusion Language Models (ICML 2025)

**核心洞察**：标准 MDLM 训练只在 masked 位置施加 loss，模型从未学过"判断已揭示 token 是否正确"。结果就是：模型对正确 token 和错误 token 给出相似的 confidence，无法定位需要纠正的位置。

**方法**：在训练时引入 absorbing-uniform mixture objective——不仅监督 masked→clean 的预测，还显式监督 visible-but-corrupted token，让模型学会：
- 对错误的已揭示 token 输出低 confidence
- 对正确的已揭示 token 输出高 confidence
- 这样 remasking 时可以用 confidence 精确定位错误位置

**好在哪**：
- 从根本上解决了 MDLM 的"盲区"——模型终于能区分对错
- 在 Code Revision Benchmark 上大幅超越标准 MDLM
- Post-training 方案，不需要改架构

**不足**：
- 需要额外训练，不是 training-free
- 只解决了错误累积，没有解决信息损失
- 需要设计 corruption 策略（如何生成训练用的错误 token）

---

#### ProSeCo — Learn from Your Mistakes (arXiv 2026.02)

**核心洞察**：在 CDLM 基础上更进一步——不仅训练模型识别错误，还训练模型**自动纠正**错误。

**方法**：
1. **ProSeCo SFT**：训练时让模型先预测、再看自己的错误、再纠正，形成 self-correcting 训练循环
2. **ProSeCo Sampling**：推理时在每个 denoising step 之后加 corrector loop——把当前输出喂回模型，让模型重新预测所有位置，用新预测替换旧的已揭示 token
3. 每个 corrector loop 花费 S 次额外 NFE（Neural Function Evaluation）

**好在哪**：
- 在 LLaDA-8B 上：HumanEval 从 48.17→62.20，GSM8K 从 77.48→82.18
- 超越了同体量的 Llama3.1-Instruct（AR 模型）
- 支持 quality-efficiency trade-off：可以调 corrector 频率和步数
- 比 ReMDM 效果更好（ReMDM 在 HumanEval 上反而降了）

**不足**：
- 每个 corrector loop 增加计算开销
- 仍然没有跨步记忆——每次纠正都是独立的 forward pass
