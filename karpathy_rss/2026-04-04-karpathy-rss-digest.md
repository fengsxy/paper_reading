# Karpathy RSS Digest - 2026-04-04

> 来源：[Andrej Karpathy Curated RSS](https://youmind.com/rss/pack/andrej-karpathy-curated-rss)
> 时间范围：2026-04-03 15:00 UTC - 2026-04-04 15:00 UTC
> 文章数：共 16 篇（精选 6 篇深度内容）

## 🔥 深度推荐

### Vulnerability Research Is Cooked

**[Simon Willison](https://simonwillison.net/2026/Apr/3/vulnerability-research-is-cooked/)** 转引 Thomas Ptacek - 2026-04-03

Thomas Ptacek 认为前沿模型正在对漏洞研究领域产生巨大冲击。Coding agents 将在数月内彻底改变漏洞挖掘的实践和经济模型——只需将 agent 指向源码树并输入"find me zero days"。LLM 天然编码了海量源码关联和已知 bug 类别（stale pointers、type confusion、allocator grooming 等），漏洞发现本质上是模式匹配 + 约束求解，恰好是 LLM 最擅长的隐式搜索问题。

---

### Writing an LLM from scratch, part 32h — Full Fat Float32

**[Giles Thomas](https://www.gilesthomas.com/2026/04/llm-from-scratch-32h-interventions-full-fat-float32)** - 2026-04-03

从零训练 GPT-2 small 系列的最后一篇干预实验：关闭 AMP（自动混合精度）和 TF32 矩阵乘法优化，使用纯 float32 训练。结果：训练时间翻倍（8h7m vs 3h24m），成本翻三倍（$135 vs $42），但 test loss 仅从 3.692 改善到 3.679（提升 0.013）。结论是 AMP 的精度损失微乎其微，性价比极高。实践中还需手动处理 non-finite gradients（AMP scaler 原本自动跳过）。

---

### The Cognitive Impact of Coding Agents

**[Simon Willison](https://simonwillison.net/2026/Apr/3/cognitive-cost/)** - 2026-04-03

Willison 与 Lenny Rachitsky 播客的一个 48 秒短视频片段在 Twitter 获得 110 万+ 播放，讨论 coding agents 带来的认知成本问题。完整对话 1 小时 40 分钟。

---

### AI Security Reports: Slop vs Signal

**Simon Willison** 转引多人 - 2026-04-03

三条相关引用串联了 AI 对开源安全的影响：
- **Willy Tarreau**（Linux kernel）：内核安全列表的报告量出现巨大跳升
- **Daniel Stenberg**（curl 作者）：AI 在开源安全中的挑战已从"AI slop"转变
- **Greg Kroah-Hartman**：数月前收到的是"AI slop"，现在情况在演变

链接：[Tarreau](https://simonwillison.net/2026/Apr/3/willy-tarreau/) | [Stenberg](https://simonwillison.net/2026/Apr/3/daniel-stenberg/) | [Kroah-Hartman](https://simonwillison.net/2026/Apr/3/greg-kroah-hartman/)

---

### EU Ready to Cave to Trump on Tech

**[Cory Doctorow / Pluralistic](https://pluralistic.net/2026/04/04/digital-subjugation/)** - 2026-04-04

欧盟委员会内部出现向 Trump 政权妥协的派系，计划就 DMA/DSA 执法与美方"对话"。Doctorow 认为这是放弃欧洲数字主权的致命决定——美国科技巨头已公然拒绝合规，Trump 已制裁参与起草 DSA 的欧洲官员。文章呼吁欧洲加速推进"后美国互联网"（Eurostack），而非等待更大危机。

---

### The AI Writing Witchhunt Is Pointless

**[Joan Westenberg](https://www.joanwestenberg.com/the-ai-writing-witchhunt-is-pointless/)** - 2026-04-04

以大仲马和 Auguste Maquet 的合作关系为引子，论证对 AI 写作的"猎巫"毫无意义。

---

## 📌 其他值得一看

| 文章 | 来源 | 简述 |
|------|------|------|
| [GitHub 活动激增](https://simonwillison.net/2026/Apr/4/kyle-daigle/) | Simon Willison | GitHub COO: 每周 2.75 亿 commits，年化 140 亿；Actions 从 5 亿分钟/周增至 21 亿 |
| [AI Isn't Too Big To Fail](https://www.wheresyoured.at/premium-ai-isnt-too-big-to-fail/) | Ed Zitron | AI 产业泡沫批评（付费文章） |
| [What does Open Source mean?](https://nesbitt.io/2026/04/04/what-does-open-source-mean.html) | Andrew Nesbitt | 开源定义的多重矛盾期望 |
| [CSP Meta Tag Iframe Escape](https://simonwillison.net/2026/Apr/3/test-csp-iframe-escape/) | Simon Willison | JS 能否逃逸 iframe 内的 CSP meta tag 研究 |
| [Reading List 04/04/2026](https://www.construction-physics.com/p/reading-list-04042026) | Construction Physics | 铝供应中断、EV 锈带、变压器短缺、SpaceX IPO |
| [Welcome to RSS Club](https://shkspr.mobi/blog/2026/04/welcome-to-rss-club/) | Terence Eden | 仅 RSS 订阅者可见的"秘密社交网络" |
| [Apple iOS 18 安全更新](https://sixcolors.com/post/2026/04/apple-releases-ios-18-security-updates-for-ios-26-holdouts/) | John Gruber | Apple 为未升级 iOS 26 的用户发布 iOS 18 安全补丁 |
| [Apple's The Savant 仍在搁置](https://www.macstories.net/news/coming-soon-whats-next-on-apple-tv-and-apple-arcade-in-april-2026/) | John Gruber | Jessica Chastain 主演剧集上线 7 个月后仍未首播 |

---

*数据来源: [Andrej Karpathy Curated RSS](https://youmind.com/rss/pack/andrej-karpathy-curated-rss)*
*生成时间: 2026-04-04 15:00 UTC*
