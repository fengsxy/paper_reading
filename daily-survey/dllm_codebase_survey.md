# Discrete Diffusion LLM (dLLM) 代码库调研报告

**调研日期**: 2026-02-16  
**目的**: 为 Yu 选择最适合做实验的 baseline

---

## 概览对比

| 项目 | 规模 | 论文 | Checkpoints | 文档质量 | 易用性 | 推荐度 |
|------|------|------|-------------|----------|--------|--------|
| **LLaDA** | 8B | arXiv 2502.09992 | ✅ HF (Base+Instruct) | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Dream** | 7B | arXiv 2508.15487 | ✅ HF (Base+Instruct) | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **MDLM** | Small | NeurIPS 2024 | ✅ HF + GDrive | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **SEDD** | Small/Medium | ICML 2024 Best Paper | ✅ HF | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **DUO** | Small | ICML 2025 | ✅ HF + GDrive | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **SMDM** | 170M-1.1B | ICLR 2025 | ✅ HF | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |

---

## 详细评估

### 1. LLaDA (Large Language Diffusion with mAsking)
**GitHub**: https://github.com/ML-GSAI/LLaDA

**优点**:
- 8B 规模，与 LLaMA3 8B 性能相当
- HuggingFace 直接加载 (`transformers==4.38.2`)
- 提供 Base 和 Instruct 两个版本
- 有 Gradio demo、chat.py 可直接对话
- 文档清晰，FAQ 详尽
- 后续工作活跃: LLaDA-V (视觉), LLaDA 1.5 (VRPO), LLaDA-MoE

**缺点**:
- 不开源训练框架和数据（但提供 GUIDELINES.md 指导）
- 采样速度比 AR 慢（无 KV-Cache）

**Checkpoints**:
- `GSAI-ML/LLaDA-8B-Base`
- `GSAI-ML/LLaDA-8B-Instruct`

**代码质量**: 结构清晰，`generate.py` 和 `get_log_likelihood.py` 分离，基于 lm-evaluation-harness 评估

---

### 2. Dream 7B
**GitHub**: https://github.com/DreamLM/Dream

**优点**:
- 7B 规模，性能与同规模 AR 模型竞争
- HuggingFace 直接加载 (`transformers==4.46.2`)
- 提供完整训练代码（SFT）
- `diffusion_generate()` 接口设计优雅，支持多种采样策略
- 有 Dream-Coder (代码) 和 DreamOn (变长生成) 扩展

**缺点**:
- 上下文长度限制 2048
- 需要 20GB+ GPU 显存

**Checkpoints**:
- `Dream-org/Dream-v0-Base-7B`
- `Dream-org/Dream-v0-Instruct-7B`

**代码质量**: 模块化好，hook 机制灵活，支持 token 级控制

---

### 3. MDLM (Masked Diffusion Language Model)
**GitHub**: https://github.com/kuleshov-group/mdlm

**优点**:
- NeurIPS 2024，理论扎实
- 代码组织极佳：`noise_schedule.py`, `diffusion.py`, `dataloader.py` 分离
- 支持 DiT, AR transformer, Mamba 多种 backbone
- 提供 SEDD, D3PM 等 baseline 实现
- `ddpm_cache` sampler 比 SEDD 快 3-4x
- 支持 Semi-AR 生成

**缺点**:
- 模型规模较小（主要在 OWT/LM1B 上验证）
- 需要 Slurm 环境

**Checkpoints**:
- `kuleshov-group/mdlm-owt` (HuggingFace)
- AR/SEDD baselines (Google Drive)

**代码质量**: ⭐⭐⭐⭐⭐ 最适合做研究实验的代码库

**后续**: 已有改进版 DUO (ICML 2025) 和 Eso-LMs (KV caching)

---

### 4. SEDD (Score Entropy Discrete Diffusion)
**GitHub**: https://github.com/louaaron/Score-Entropy-Discrete-Diffusion

**优点**:
- ICML 2024 Best Paper
- 理论创新：通过估计数据分布比率进行离散扩散
- 代码模块化：`noise_lib.py`, `graph_lib.py`, `sampling.py`
- 支持 uniform 和 absorb 两种 graph type

**缺点**:
- 文档相对简洁
- 采样速度较慢

**Checkpoints**:
- `louaaron/sedd-small`
- `louaaron/sedd-medium`

**代码质量**: 研究导向，适合理解离散扩散理论

---

### 5. DUO (Diffusion Duality)
**GitHub**: https://github.com/s-sahoo/duo

**优点**:
- ICML 2025，MDLM 的改进版
- 支持 Discrete Consistency Distillation（少步生成）
- Curriculum Learning 加速训练
- Greedy-tail sampler（类似 AR 的 nucleus sampling）

**缺点**:
- 需要预计算 integral cache
- Curriculum Learning 增加显存消耗

**Checkpoints**:
- `s-sahoo/duo` (undistilled)
- `s-sahoo/duo-distilled`

**代码质量**: 基于 MDLM，继承其优点

---

### 6. SMDM (Scaling up Masked Diffusion Models)
**GitHub**: https://github.com/ML-GSAI/SMDM

**优点**:
- ICLR 2025，首个 MDM scaling law
- 模型规模 170M-1.1B
- 提供完整预训练和 SFT 代码
- 支持 unsupervised CFG
- 在 reverse curse 任务上超越 13B Llama-2

**缺点**:
- 依赖 TinyLlama 环境
- 多机训练配置复杂

**Checkpoints**: HuggingFace `nieshen/SMDM` (全系列)

**代码质量**: 完整的训练 pipeline，适合 scaling 研究

---

### 7. 加速工具: Fast-dLLM
**GitHub**: https://github.com/NVlabs/Fast-dLLM

**优点**:
- ICLR 2026，NVIDIA 出品
- 支持 LLaDA 和 Dream 的推理加速
- KV Cache + Parallel Decoding，8-11x 加速
- 已集成到 LLaDA-V

**用途**: 推理加速，不是 baseline 但值得关注

---

## 推荐方案

### 🏆 首选: MDLM + DUO 组合

**理由**:
1. **代码质量最高**: 模块化清晰，易于修改和扩展
2. **规模适中**: 适合在有限资源上快速迭代
3. **理论完整**: SUBS parameterization 简化了 loss 计算
4. **生态完善**: 有 DUO (distillation), Eso-LMs (KV cache) 等后续工作
5. **Baseline 齐全**: 同一代码库包含 AR, SEDD, D3PM 实现

**实验路径**:
```
MDLM (理解基础) → DUO (少步生成) → 自己的改进
```

### 🥈 备选: LLaDA / Dream

**适用场景**:
- 需要大规模模型验证
- 研究 instruction following / chat 能力
- 需要与 LLaMA 级别模型对比

**注意**: 这两个不开源完整训练代码，更适合做推理实验或 fine-tuning

---

## 快速上手命令

### MDLM 采样
```bash
python main.py \
  mode=sample_eval \
  eval.checkpoint_path=kuleshov-group/mdlm-owt \
  data=openwebtext-split \
  model.length=1024 \
  sampling.predictor=ddpm_cache \
  sampling.steps=1000
```

### LLaDA 推理
```python
from transformers import AutoModel, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained('GSAI-ML/LLaDA-8B-Instruct', trust_remote_code=True)
model = AutoModel.from_pretrained('GSAI-ML/LLaDA-8B-Instruct', trust_remote_code=True, torch_dtype=torch.bfloat16)
```

### Dream 推理
```python
from transformers import AutoModel, AutoTokenizer
import torch

model = AutoModel.from_pretrained("Dream-org/Dream-v0-Instruct-7B", torch_dtype=torch.bfloat16, trust_remote_code=True)
output = model.diffusion_generate(input_ids, max_new_tokens=512, steps=512, alg="entropy")
```

---

## 总结

| 研究方向 | 推荐代码库 |
|----------|-----------|
| 理论研究/算法改进 | MDLM, SEDD |
| Scaling 研究 | SMDM |
| 少步生成/蒸馏 | DUO |
| 大模型实验 | LLaDA, Dream |
| 推理加速 | Fast-dLLM |

**最终建议**: 从 MDLM 开始，它是目前最适合做研究实验的 baseline。代码清晰、文档完善、checkpoint 可用，且有活跃的后续工作可以参考。
