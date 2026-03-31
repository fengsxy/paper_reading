### 类别③：直接初始化 + 扩散微调

#### Dream 7B — Diffusion Large Language Models (HKU, arXiv 2025.08)

**核心洞察**：用强大的 AR 模型（Qwen2.5-7B）的权重直接初始化 dLLM backbone，然后用 masked diffusion objective 做 continual pretraining。

**方法**：
1. **初始化**：直接加载 Qwen2.5-7B 的全部权重
2. **转换训练**：用 masked diffusion objective（predict masked tokens）做 continual pretraining
3. **SFT**：标准 instruction tuning，但用 diffusion 训练范式
4. **推理创新**：
   - 低 confidence remasking（类似 ReMDM 思路）
   - Picard iteration 式的 iterative refinement

**结果**：
- 在多个 benchmark 上与 Qwen2.5-7B 匹配或接近
- 支持 variable-length generation（DreamOn 扩展）
- 比从头训练的 LLaDA-8B 在某些任务上更好

**好在哪**：
- 最直接的方案：拿 AR 权重，换训练 objective，done
- 验证了 Qwen2.5 的知识可以迁移到 diffusion 范式
- HKU NLP 组的工程质量好，开源完整

**不足**：
- 没有 block-wise 设计 → 全 bidirectional → 无 KV cache
- Continual pretraining 数据量未明确优化
- 与 AR 原版仍有不小差距（尤其 reasoning）

---

#### DiffusionVL — Translating AR Models into Diffusion VLMs (HUST, arXiv 2025.12)

**核心洞察**：当前 diffusion VLM 受限于 base dLLM 的能力。与其等 dLLM 变强，不如直接把强大的 AR VLM"翻译"成 diffusion VLM。

**方法**：
1. 拿任意预训练 AR VLM（如 LLaVA、Qwen-VL 等）
2. 用 diffusion finetuning 框架转换：
   - 保留 vision encoder
   - 将 language decoder 从 AR → diffusion
   - 设计 adaptation 策略保留视觉理解能力

**好在哪**：
- 扩展到多模态领域
- 证明 AR→diffusion 转换不限于纯文本

**不足**：
- 多模态的复杂度增加
- 视觉 token 和文本 token 的 masking 策略需要不同处理

---

### 类别④：从头训练（对照组）

#### LLaDA / LLaDA 2.0 — Large Language Diffusion Models (arXiv 2025/2025.12)

**为什么列为对照**：LLaDA 是从头训练 dLLM 的代表，不涉及 AR→dLLM 转换，但提供了重要的 baseline 和 insights。

**LLaDA 关键发现**：
- dLLM 从头训练 **可以** 达到 AR 水平（LLaDA-8B vs LLaMA3-8B）
- 天然解决 reversal curse（AR 模型的固有缺陷）
- 支持 ICL、instruction following

**LLaDA 2.0 (100B scale) 关键发现**：
- AR 初始化的 dLLM 在**训练早期**更好，但从头训练的 dLLM 在充分训练后可以追上
- 结论："Given sufficient compute, training from scratch can match AR-initialized models"
- 但 "sufficient compute" = 非常大量的 token

**对比启示**：
- 如果计算预算有限（大多数情况）→ AR→dLLM 转换是更实际的路线
- 如果追求最优性能且不限计算 → 从头训练可能更好（可以设计更好的架构）
