# Karpathy RSS 精选 | 2026-02-18

> Karpathy 订阅了 92 个 RSS 源，这是他的信息食谱。今天过去 24 小时里冒出来的东西不少：模型更新、软件分发基础设施、以及开源社区被 AI PR 淹没后的“自救指南”。

---

## 🧠 Simon Willison: Claude Sonnet 4.6（以及“模型迁移细节才是地狱”）

**来源**: [simonwillison.net](https://simonwillison.net/2026/Feb/17/claude-sonnet-46/#atom-everything)

### 一句话
新模型发布最吓人的从来不是分数，而是“迁移指南里那堆你不得不改的细节”。

### 核心观点
- Anthropic 发布 Claude Sonnet 4.6：主打“接近 Opus 4.5 的能力，但保持 Sonnet 的价格带”。
- 更关键的更新其实在接口/行为层：例如自适应思考（adaptive thinking）、不再支持某些 prefixes 等迁移细节。
- Simon 顺手把 `llm-anthropic` 升级到支持新模型，而且吐槽点很工程化：不是写代码难，是“规格变动 + 细碎兼容性”最耗命。

### 我的看法
行业现在进入了一个很尴尬但真实的阶段：

- **模型能力提升 ≠ 生产力线性提升**。真正卡住团队的，往往是边角行为、token 预算、工具链兼容、以及“你以为稳定但其实会变”的隐性契约。
- **“migration guide” 正在变成新的“semver”**：表面是版本号，背后是生态的协调成本。

顺便说一句：Simon 用“鹈鹕骑自行车 SVG”当回归测试，挺好——比一堆 benchmark 更诚实：你关心的是输出风格、可控性、以及“这玩意会不会突然换性格”。

---

## 📦 Nesbitt: 包管理器为什么不学 OCI？

**来源**: [nesbitt.io](https://nesbitt.io/2026/02/18/what-package-registries-could-borrow-from-oci.html)

### 一句话
“全世界都在发压缩包，但每个生态都要发明一种新压缩包。”

### 核心观点
- 文章梳理了一堆生态的包格式：npm、PyPI、RubyGems、Deb、RPM、Alpine……各自都有历史包袱。
- 容器世界反而收敛到 OCI：核心原语是 **manifest + blobs（按 digest 寻址）+ tags**。
- OCI v1.1 引入 `artifactType` / `subject`，让 registry 更像通用的“工件仓库”，不仅能存镜像，还能存 Helm chart、WASM、AI 模型等。
- 关键收益不是格式优雅，而是：**云厂商 registry 早就把鉴权、复制、CDN、存储规模化**解决了。

### 我的看法
这篇文章其实在说一件更大的事：

- 我们在软件供应链上最浪费的地方，往往不是计算，而是**重复造“分发/存储/验真”的轮子**。
- 如果 OCI 真成了“通用工件底座”，那未来的争夺点会从“谁的包格式更好”变成“谁能把签名、SBOM、溯源、策略执行（policy）做成默认配置”。

吐槽一句：今天的包管理生态像中世纪度量衡——每个城邦一套单位，直到有人受不了才统一。

---

## 📝 Tedium: Markdown for Agents（Markdown 可能变成 2026 的 RSS？）

**来源**: [tedium.co](https://tedium.co/2026/02/17/markdown-growing-influence-cloudflare-ai/)

### 一句话
人类想要“轻量内容”，AI 更想要——因为它们会把你的网页解析成本直接烧成钱。

### 核心观点
- Cloudflare/Vercel/Laravel 等在推“Markdown for Agents”：通过 HTTP 内容协商（content negotiation）给同一页面提供 Markdown 版本。
- 论点很务实：HTML 页面可能 500KB，Markdown 可能 2KB，**对爬取/代理（agents）来说是巨幅降本**。
- 文章也提到质疑：这会不会变成 AI 时代的 AMP（“平台要求你适配某种格式”）？

### 我的看法
我更愿意把它看成“网站对抗 AI 抓取洪水”的防洪工程：

- 不是为了让 agent “更聪明”，而是让它们**别把你的动态站点当免费 API 然后把账单甩给你**。
- 如果你提供结构化、低噪音的内容端点，AI 抓取会更像“正常的流量”，而不是 DDoS 式的粗暴渲染与解析。

顺带：Markdown 这波复兴很讽刺——人类当年用它是为了写得快；现在是为了被机器读得快。

---

## 🛡️ Joan Westenberg: 开源需要“行会式 gatekeeping”来对抗 AI PR 垃圾洪水

**来源**: [joanwestenberg.com](https://www.joanwestenberg.com/the-case-for-gatekeeping-or-why-medieval-guilds-had-it-figured-out/)

### 一句话
开源的“开放”，从来不是“任何 PR 都值得你花时间”。

### 核心观点
- 维护者抱怨：AI 生成的批量 PR 让 repo 变成“雪堆”，看起来像贡献，其实大多是垃圾。
- 作者用中世纪行会类比：行会解决的是“分布式生产下的质量与信任”。
- 提议一种现代版机制：类似 Debian Web of Trust 的 **vouching（担保）/信誉网络**，让维护者能按信任级别过滤贡献。

### 我的看法
这篇文章点中一个现实：AI 让“提交成本”接近 0，但“审查成本”依然是人类的时间。

- 如果开源不引入新的信号机制，维护者就会被迫把项目变成“半封闭社区”（不一定坏，但会改变文化）。
- 最可能的演化不是彻底关门，而是**默认 gatekeeping + 公开 fork 权**：代码仍然开放，人类注意力开始收费（以信誉/关系/历史贡献的形式）。

吐槽一句：AI 把 GitHub 的绿格子变成了新的 KPI，结果大家都开始优化 KPI，而不是优化软件。

---

## 🧯 Gary Marcus: “AGI 已到来”的说法大概率是在偷换定义

**来源**: [garymarcus.substack.com](https://garymarcus.substack.com/p/rumors-of-agis-arrival-have-been)

### 一句话
把 benchmark 做高，不等于你造出了“能在现实里活下去”的通用智能。

### 核心观点
- Marcus 反驳近期“AGI 已实现”的论调：很多论证把 **任务/基准上的表现** 等同于 **面对新环境的鲁棒泛化**。
- 强调 AGI 的传统定义更接近 Legg & Hutter 那套：跨环境达成目标的能力，重点在适应性与迁移。
- 认为一些文章是在重定义 AGI（比如把“经济上有用”或“通过某类测试”直接当 AGI）。

### 我的看法
Marcus 的观点经常被嫌“扫兴”，但这里扫得挺对：

- 现在最危险的不是模型不够强，而是**组织用错指标做决策**：把 demo/benchmark 当能力，把偶然成功当可靠性。
- 你可以说“我们已经有很强的通用工具”，但把它叫 AGI，会导致预期、监管、投资、甚至安全讨论全部跑偏。

真正的分界线可能不是“智力”，而是：系统在开放世界里能否持续稳定地产生价值（并且可控）。

---

## 总结

今天这些文章隐约指向同一个主题：**当 AI 把生成变得廉价，真正稀缺的东西会重新被定价**。

- 模型迭代很快，但迁移/兼容的摩擦才是“工程现实”。
- 分发与供应链会向更通用的底座（OCI/registry）收敛。
- 内容端点开始为机器优化（Markdown for Agents）。
- 开源社区开始为人类注意力设闸（信誉/担保/过滤）。
- “AGI” 这种词，继续被当营销话术用的话，迟早会反噬讨论质量。

---

*这篇笔记基于 [Karpathy Curated RSS](https://youmind.com/rss/pack/andrej-karpathy-curated-rss) 过去 24 小时内的聚合条目。*