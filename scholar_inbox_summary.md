# Scholar Inbox 论文总结 (2025.09 - 2026.02)

**总计: 481 篇论文**

---

## 📊 研究主题分布

| 主题 | 数量 | 占比 | 趋势 |
|------|------|------|------|
| Vision-Language Model | 89 | 18.5% | 🔥 热门 |
| Image Generation | 61 | 12.7% | 稳定 |
| Efficiency & Compression | 58 | 12.1% | 🔥 热门 |
| RAG & Retrieval | 45 | 9.4% | 稳定 |
| **Diffusion LM** | 43 | 8.9% | 📈 上升 |
| Interpretability | 28 | 5.8% | 📈 上升 |
| Alignment & RLHF | 26 | 5.4% | 稳定 |
| Architecture | 18 | 3.7% | 稳定 |
| Safety & Robustness | 14 | 2.9% | 偏少 |
| Representation Learning | 13 | 2.7% | 偏少 |
| Agent & Tool Use | 13 | 2.7% | 稳定 |
| Video | 12 | 2.5% | 稳定 |
| Reasoning & CoT | 12 | 2.5% | 稳定 |

---

## 🎯 六大核心问题

### 1. 如何让模型"看懂"？(31% = VLM + Image + Video)
- Vision-Language Models 是最大热点
- 图像生成持续活跃
- 视频理解/生成开始起步

### 2. 如何让模型更快？(12%)
- KV Cache 优化
- 模型压缩 (量化、剪枝、蒸馏)
- 推理加速

### 3. 如何让模型更聪明？(9% = Diffusion LM)
- dLLM 作为新范式快速崛起
- 主要在做加速和 decoding 优化
- 理论理解仍然不足

### 4. 如何让模型更可靠？(9% = RAG + Retrieval)
- 检索增强生成
- 知识注入
- 减少幻觉

### 5. 如何理解模型？(6%)
- Mechanistic Interpretability
- Circuit Analysis
- Probing

### 6. 如何让模型更安全？(3%)
- Jailbreak 防御
- 幻觉检测
- 对抗鲁棒性
- **严重不足！**

---

## 🔍 dLLM 子领域分析 (43 篇)

| 方向 | 数量 | 代表工作 |
|------|------|----------|
| 加速/效率 | ~20 | FOCUS, DAWN, FlashBlock |
| Decoding 策略 | ~10 | ρ-EOS, FourierSampler, TAPS |
| Training | ~8 | AlignmentFlex, XDLM |
| 理论/机制 | ~3 | Flexibility Trap, Top 10 Challenges |
| 应用 | ~2 | DICE (code), DiffuSpeech |

**关键观察：**
- 49% 在做加速 → 说明速度是核心痛点
- 只有 7% 在做理论 → 机制理解严重不足
- 几乎没有 safety 研究 → 空白领域

---

## 💡 Research Opportunities

### 高价值 + 低竞争
1. **dLLM 理论理解** - 只有 3 篇在做
2. **dLLM Safety** - 几乎空白
3. **Representation Learning + dLLM** - 无人涉足

### 高价值 + 高竞争
1. **VLM** - 太多人在做
2. **效率优化** - 太多人在做

### 被忽视的问题
1. Diffusion 是 essential 还是 incidental？
2. 什么任务真正需要 dLLM？
3. Optimal generation order 是什么？

---

## 📈 时间线趋势

```
2025-09: 早期探索
2025-10: dLLM 爆发 (LLaDA 热度)
2025-11: 平静期
2025-12: 系统优化
2026-01: 理论质疑开始 (Flexibility Trap)
2026-02: 多样化发展
```

---

*Generated: 2026-02-15*
