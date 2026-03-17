# Karpathy RSS Digest - 2026-03-17

> 来源：[Andrej Karpathy Curated RSS](https://youmind.com/rss/pack/andrej-karpathy-curated-rss)
> 时间范围：2026-03-16 15:00 UTC - 2026-03-17 15:00 UTC
> 文章数：19 篇（排除 1 篇赞助广告）

---

## 🔥 深度推荐

### Subagents — Agentic Engineering Patterns

**[Simon Willison's Weblog](https://simonwillison.net/guides/agentic-engineering-patterns/subagents/#atom-everything)** - 2026-03-17 12:32

Simon 继续扩展他的 Agentic Engineering Patterns 系列，本篇聚焦 subagents：LLM 的 context window 有限（通常 100 万 token 上限，20 万以下效果最佳），subagents 通过独立 context 完成子任务来节省主 agent 的 token 预算。文中以 Claude Code 的 Explore subagent 为例，展示了 agent 如何自我 prompt、分派探索任务并汇总结果。还讨论了并行 subagents 和专业化角色（code reviewer、test runner、debugger）。

**点评**：对做 agent 系统的人来说是实用参考，直接揭示了 Claude Code / Codex 内部的 subagent 调度机制。

### Use subagents and custom agents in Codex

**[Simon Willison's Weblog](https://simonwillison.net/2026/Mar/16/codex-subagents/#atom-everything)** - 2026-03-16 23:03

OpenAI Codex 正式 GA subagents 功能，支持 explorer/worker/default 三种默认角色，可在 `~/.codex/agents/` 定义自定义 TOML agent（指定模型、system prompt）。Simon 汇总了目前所有支持 subagents 的 coding agent 平台：Claude Code、Gemini CLI、Mistral Vibe、OpenCode、VS Code Copilot、Cursor。

**点评**：Subagents 已成为 coding agent 的标配模式，这是一个重要的行业趋同信号。

### Introducing Mistral Small 4

**[Simon Willison's Weblog](https://simonwillison.net/2026/Mar/16/mistral-small-4/#atom-everything)** - 2026-03-16 23:41

Mistral 发布 Small 4：Apache 2 开源，119B 参数 MoE（6B 活跃），首次将 Magistral（推理）、Pixtral（多模态）、Devstral（agentic coding）统一到单一模型。支持 reasoning_effort 参数。HuggingFace 上 242GB。同日还发布了 Leanstral，专门调优 Lean 4 形式化证明语言。

**点评**：开源 MoE 继续卷，6B 活跃参数做到 flagship 级能力是很有竞争力的定位。

### Anthropic 的对齐团队与五角大楼的"勒索演练"

**[Simon Willison's Weblog](https://simonwillison.net/2026/Mar/16/blackmail/#atom-everything)** - 2026-03-16 21:38

引用 New Yorker 长文：Anthropic 对齐科学团队的"勒索演练"目的是为政策制定者提供直观的 misalignment 风险案例——"让从未思考过这个问题的人真正感受到风险的存在"。

**点评**：AI safety 从论文走向政策游说的实操缩影。

### Coding agents for data analysis

**[Simon Willison's Weblog](https://simonwillison.net/2026/Mar/16/coding-agents-for-data-analysis/#atom-everything)** - 2026-03-16 20:12

Simon 为 NICAR 2026 准备的 workshop handout，教数据记者如何用 coding agents 做数据分析。

### Apple Exclaves 与 MacBook Neo 的安全摄像头指示灯

**[John Gruber / Daring Fireball](https://daringfireball.net/2026/03/apple_enclaves_neo_camera_indicator)** - 2026-03-16 17:27

MacBook Neo 没有硬件摄像头指示灯，改用软件指示灯——但运行在 secure exclave 中，连内核级漏洞也无法在不亮灯的情况下开启摄像头。指示灯直接 blit 到屏幕硬件上，绕过内核。

**点评**：Apple 安全架构的精巧设计，exclave ≠ enclave，这个区分值得关注。

---

## 📱 科技观察

### Samsung 三折叠手机上市仅 3 个月即停产

**[John Gruber → The Verge](https://www.theverge.com/tech/895879/samsung-galaxy-z-trifold-discontinued-stock-sold-out)** - 2026-03-17 13:49

$2,899 Galaxy Z TriFold 将先在韩国停售，再清完美国库存。Gruber 调侃："也许剃刀上五个刀片确实太多了？"

### Apple 发布 AirPods Max 2

**[John Gruber → Apple Newsroom](https://www.apple.com/newsroom/2026/03/apple-introduces-airpods-max-2-powered-by-h2/)** - 2026-03-16 17:57

搭载 H2 芯片，ANC 和音质全面升级。

### Your Startup Is Probably Dead On Arrival

**[Steve Blank](https://steveblank.com/2026/03/17/your-startup-is-probably-dead-on-arrival/)** - 2026-03-17 13:00

Steve Blank 警告：如果你的公司成立超过两年，很多假设可能已经失效。停下来重新评估，否则公司会死。

### 'The Last Quiet Thing'

**[John Gruber → Terry Godier](https://www.terrygodier.com/the-last-quiet-thing)** - 2026-03-16 17:58

关于设计与注意力的优秀散文。

### F Cancer

**[Marcus on AI](https://garymarcus.substack.com/p/f-cancer)** - 2026-03-16 19:10

Gary Marcus 探讨 AI 在癌症领域的真正考验。

---

## 📚 轻量内容

- **[Windows stack limit checking: x86-32, second try](https://devblogs.microsoft.com/oldnewthing/20260317-00/?p=112144)** - The Old New Thing
- **[Lil Finder Guy Wallpapers](https://512pixels.net/2026/03/lil-finder-5k-wallpapers/)** - 512 Pixels
- **[Help I'm being persecuted](https://www.experimental-history.com/p/help-im-being-persecuted)** - Experimental History
- **[Toshiba's Soviet nuclear submarine scandal](https://dfarq.homeip.net/toshibas-soviet-nuclear-submarine-scandal/)** - The Silicon Underground
- **[Weekly Update 495](https://www.troyhunt.com/weekly-update-495/)** - Troy Hunt
- **[Esqueleto Tutorial](https://entropicthoughts.com/esqueleto-tutorial)** - Entropic Thoughts
- **[Quoting Guilherme Rambo](https://simonwillison.net/2026/Mar/16/guilherme-rambo/#atom-everything)** - Simon Willison（MacBook Neo 摄像头指示灯细节引用）
- **[Updates OpenTK](https://berthub.eu/articles/posts/updates-opentk-maart-2026/)** - Bert Hubert（荷兰语，Parliament 追踪工具更新）

---

*排除: [Sponsor] Mux — Video API for Developers（赞助广告）*

*数据来源: [Andrej Karpathy Curated RSS](https://youmind.com/rss/pack/andrej-karpathy-curated-rss)*
*生成时间: 2026-03-17 15:00 UTC*
