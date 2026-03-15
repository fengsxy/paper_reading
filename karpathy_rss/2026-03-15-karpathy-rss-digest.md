# Karpathy RSS Digest - 2026-03-15

> 来源：[Andrej Karpathy Curated RSS](https://youmind.com/rss/pack/andrej-karpathy-curated-rss)
> 时间范围：2026-03-14 15:00 UTC - 2026-03-15 15:00 UTC
> 文章数：11 篇

---

## 🔥 Simon Willison：Agentic Engineering 实战经验谈

**[Simon Willison's Weblog](https://simonwillison.net/2026/Mar/14/pragmatic-summit/#atom-everything)** - 2026-03-14 18:19

Willison 在 Pragmatic Summit 的炉边谈话，干货密度极高。几个关键观点：（1）每次 agent session 都从"这是怎么跑测试的"开始，然后说"用 red-green TDD"——五个 token 就够了；（2）测试现在是免费的，不写测试是不可接受的；（3）他发明了 Showboat 工具，让 agent 用 curl 手动测试 API 并生成可读报告；（4）"conformance-driven development"——让 agent 在 6 个框架上写通用测试套件，然后基于测试反向实现新功能；（5）他承认自己天天用 `--dangerously-skip-permissions` 跑 Claude Code，尽管他是"全世界最清楚为什么不该这么做的人"。

**点评**：这是目前最系统的 coding agent 工程实践总结。Conformance-driven development 这个思路尤其巧妙——本质上是用测试作为规范的可执行替代品。对于研究 AI-assisted coding 的人来说是必读。

---

## 🔥 Jazzband 关停：AI 垃圾 PR 杀死了开放协作模式

**[Simon Willison's Weblog](https://simonwillison.net/2026/Mar/14/jannis-leidel/#atom-everything)** - 2026-03-14 18:41

Python 社区知名的 Jazzband 组织宣布关停。核心原因：GitHub 上 AI 生成的垃圾 PR 泛滥（"slopocalypse"），使得开放成员制 + 共享 push 权限的模式无法安全运行。背景数据触目惊心：AI 生成的 PR 仅 10% 符合项目标准；curl 因确认率低于 5% 关闭了 bug bounty；GitHub 自己也推出了"一键禁用 PR"的应急开关。

**点评**：这是 AI 对开源生态的第一个重大结构性伤害案例。不是 AI 写了坏代码的问题，是 AI 让"信任陌生人贡献"这个开源基石变得不可行了。

---

## 🔥 Ars Technica 记者因 AI 伪造引用被解雇

**[Daring Fireball](https://futurism.com/artificial-intelligence/ars-technica-fires-reporter-ai-quotes)** - 2026-03-14 17:22

Ars Technica 资深记者 Benj Edwards 因文章中出现 AI 编造的假引用被解雇。Ars 撤回了相关报道。

**点评**：讽刺的是，Edwards 本人一直是科技领域的老记者。这说明 AI 工具的便利性正在制造新的伦理陷阱——不是不知道不该用，而是用着用着边界就模糊了。

---

## 🔒 Mullenweg 详述精密 Apple 钓鱼攻击

**[Daring Fireball / ma.tt](https://ma.tt/2026/03/gone-almost-phishin/)** - 2026-03-15 00:37

WordPress 创始人 Matt Mullenweg 记录了一次多阶段 Apple 账户钓鱼攻击：攻击者先触发合法密码重置弹窗，然后冒充他联系 Apple 客服开了真实工单（产生真实的 Apple 签名邮件），最后"Alexander from Apple Support"来电——专业到 Mullenweg 一度感谢对方"工作做得好"。识别要点：`audit-apple.com` ≠ `*.apple.com`。

**点评**：社会工程学的教科书级案例。攻击者利用了 Apple 自身的合法流程作为武器，连 Lockdown Mode 都挡不住。对安全研究者有参考价值。

---

## 💻 MacBook Neo：PC 厂商的噩梦

**[Daring Fireball](https://www.theverge.com/report/894090/macbook-neo-pc-windows-laptop-competition-asus-footinmouth)** - 2026-03-14 20:02
**[Daring Fireball / iFixit](https://www.ifixit.com/News/116152/macbook-neo-is-the-most-repairable-macbook-in-14-years)** - 2026-03-14 22:06

两篇关于 MacBook Neo 的文章。Asus CFO 称 Neo"更像平板"，Gruber 毫不客气地反驳——Neo 的 A18 Pro 单核跑分吊打 2400 美元的 Zenbook Duo。iFixit 拆解则发现 Neo 是 14 年来最可修的 MacBook：螺丝固定电池、简化键盘维修。Gruber 的洞察是：便宜和可修其实是同一件事——组装容易 = 拆解容易。

**点评**：Apple 硬件话题，与 AI/CS 研究关联不大，但 Gruber 的因果分析（价格低→组装简化→可修性高）值得一读。

---

## 📉 Gary Marcus：又一个 scaling 失灵的证据

**[Marcus on AI](https://garymarcus.substack.com/p/breaking-expensive-new-evidence-that)** - 2026-03-14 18:23

两个昂贵的大规模实验失败，Marcus 继续唱衰"scaling is all you need"的叙事。

**点评**：Marcus 的观点一如既往。标题比内容有力。

---

## 📚 轻量内容

- **[Robots in Space 书评](https://shkspr.mobi/blog/2026/03/book-review-robots-in-space-the-secret-lives-of-our-planetary-explorers-by-dr-ezzy-pearson/)** - Terence Eden 评太空机器人探索史，三星半
- **[BertVote 荷兰市政选举 2026](https://berthub.eu/articles/posts/bert-vote-gemeenteraad-2026/)** - Bert Hubert 的荷兰地方选举推荐（荷兰语）
- **[Guided Meditation for Developers](https://nesbitt.io/2026/03/15/guided-meditation-for-developers.html)** - Andrew Nesbitt，"在你的依赖树中寻找平静"（幽默小品）
- **[Lil Finder Guy](https://basicappleguy.com/basicappleblog/lil-finder-guy)** - Apple Finder 图标趣谈
- **[Corrupt Anticorruption](https://pluralistic.net/2026/03/14/ill-have-what-xis-having/)** - Doctorow 时评

---

## 📊 统计

- **AI/编程**：4 篇（agentic engineering、Jazzband AI slop、AI 伪造引用、scaling 争论）
- **安全**：1 篇（Apple 钓鱼攻击）
- **Apple 硬件**：3 篇（MacBook Neo × 2、Finder 图标）
- **轻量/杂项**：3 篇（书评、选举、冥想）

**今日亮点**：Willison 的 agentic engineering 演讲和 Jazzband 关停事件形成有趣对照——coding agent 正在帮助个人开发者大幅提效，却同时以 spam PR 的形式摧毁开源社区的协作信任。这两件事是同一枚硬币的两面。

---

*数据来源: [Andrej Karpathy Curated RSS](https://youmind.com/rss/pack/andrej-karpathy-curated-rss)*
*生成时间: 2026-03-15 15:00 UTC*
