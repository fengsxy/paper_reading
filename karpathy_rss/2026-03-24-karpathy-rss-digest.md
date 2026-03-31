# Karpathy RSS Digest - 2026-03-24

> 来源：[Andrej Karpathy Curated RSS](https://youmind.com/rss/pack/andrej-karpathy-curated-rss)
> 时间范围：2026-03-23 15:00 UTC - 2026-03-24 15:00 UTC
> 文章数：至少 13 篇（排除广告/低质量内容后 3 篇核心推荐）

---

## 🔥 深度推荐

### Cory Doctorow：预测市场不是在发现信息，而是在制造腐败

**[Pluralistic](https://pluralistic.net/2026/03/24/degenerated-gambling/)** - 2026-03-24 11:18

深入剖析预测市场的根本缺陷。Goodhart 定律在这里被推向极端：参与者不是让指标反映现实，而是"把枪顶在指标头上"——通过威胁、贿赂记者等信息源，直接扭曲信息本身。以 Polymarket 上伊朗导弹袭击的 1400 万美元赌局为例，记者因发布客观报道而遭死亡威胁。Doctorow 指出：预测市场不是在"发现"信息，而是在"制造"腐败；它们需要的预言者(oracle)恰恰是最易被腐蚀的环节。这是一篇融合政治经济学批判与技术治理的必读长文。

**关键词**: prediction markets, Goodhart's Law, oracle capture, information corruption

### Simon Willison：流式专家技术突破，万亿参数模型跑在消费级硬件

**[Simon Willison's Weblog](https://simonwillison.net/2026/Mar/24/streaming-experts/)** - 2026-03-24 05:09

Dan Woods 的"streaming experts"技术迭代迅速：五天内 Qwen3.5-397B-A17B 从 48GB RAM 运行，升级到 Kimi K2.5 —— 一个 1 万亿参数、32B 激活权重的模型 —— 在 M2 Max MacBook Pro (96GB) 上运行。更惊人的是，同一模型已在 iPhone 上以 0.6 tokens/s 的速度运行。技术核心：把专家权重流式从 SSD 加载到内存，避免全量加载。Dan 团队继续运行 auto-research loops 寻找更多优化点。这意味着 MoE 模型正在快速走向消费级设备。

**关键词**: streaming experts, MoE, local LLMs, flash-moe, Qwen, Kimi

### Susam Pal：Wander 0.2.0 —— 去中心化网页推荐系统

**[Susam Pal](https://susam.net/code/news/wander/0.2.0.html)** - 2026-03-24 00:00

Wander 是一个小型、去中心化、自托管的网页控制台，让访客探索由独立站长推荐的页面。0.2.0 版本重点强化安全与可定制性：远程 `wander.js` 和推荐页面均运行在 sandbox iframe 中；站长可添加自定义 CSS/JS，可屏蔽特定 URL；对话框扩展，展示配置详情、漫游历史和发现的 Console 列表。发布不到一周，已吸引 30+ 站长部署，推荐 100+ 页面。项目托管在 Codeberg，崇尚真正的去中心化。

**关键词**: decentralized web, Wander, sandbox iframe, self-hosted

---

## 📱 科技观察（略）

- **Simon Willison** 今日还有多篇短更新（DNS工具、beats加注释等）
- **matduggan.com**: Markdown 如何吞掉世界（延续昨日）
- **The Silicon Underground**: eMachines 历史趣谈
- **Troy Hunt**: Weekly Update 496 提及 OpenClaw

---

## 💤 跳过

- **Daring Fireball**: WorkOS 赞助广告（营销）
- **Westenberg**: 订阅推广为主，实质内容极少
- **Works on My Machine**: 内容过简，仅一句话
- **Joan Westenberg**: 付费墙/Cta 占比过高

---

*数据来源: [Andrej Karpathy Curated RSS](https://youmind.com/rss/pack/andrej-karpathy-curated-rss)*
*生成时间: 2026-03-24 15:00 UTC*
