# Karpathy RSS 精选 | 2026-02-17

> Andrej Karpathy 订阅了 92 个 RSS 源，这是他的信息食谱。今天从他的聚合 feed 里挑了几篇值得读的。

---

## 🚢 Simon Willison: Showboat 生态系统扩张

**来源**: [simonwillison.net](https://simonwillison.net/2026/Feb/17/chartroom-and-datasette-showboat/)

### 一句话

让 AI 写代码不够，还要让 AI 写文档来证明它写的代码能用。

### 核心观点

Simon 一周前发布了 Showboat——一个帮助 coding agent 生成 Markdown 演示文档的 CLI 工具。现在他又搞了两个配套工具：

1. **Chartroom**: 命令行图表工具，能从 CSV/JSON/SQLite 生成 matplotlib 图表
2. **datasette-showboat**: 让 Showboat 实时推送文档到 Datasette 实例

最有意思的是他的工作流：

```
uvx showboat --help
```

就这一行，Claude Code 就能学会怎么用这个工具。help 文本本身就是一个 ad-hoc 的 Skill 文档。

他还加了个 remote publishing 功能——Claude 在工作时可以实时把文档推送到远程服务器，不用等它 commit 到 GitHub 才能看结果。

### 我的看法

Simon 在做的事情本质上是**给 AI 建立可观测性**。

传统软件开发有 logging、monitoring、tracing。AI 辅助开发呢？你让 Claude 写了一堆代码，怎么知道它写得对不对？

Showboat 的答案是：让 AI 自己生成演示文档，带截图、带图表、带运行结果。这不是文档，这是**证据**。

更深一层：这是在解决 cognitive debt 问题。AI 写的代码你不理解，但如果 AI 同时生成了一份详细的演示文档，至少你知道它在干什么。

对于做 AI 工具的人：**可观测性是下一个战场**。谁能让用户更好地理解 AI 在做什么，谁就赢了。

---

## 💰 Cory Doctorow: 零工经济的最低工资骗局

**来源**: [pluralistic.net](https://pluralistic.net/2026/02/17/no-piecework/)

### 一句话

Uber 说给你 $30/小时，但你等单的时间不算钱。

### 核心观点

"最低工资" 这个概念比你想的复杂。如果你想工作但找不到活，你的最低工资就是零。

零工经济的骗局在于：平台只按 "engaged time"（接单时间）算钱，不按 "available time"（等单时间）算。

举个例子：
- 你在 Uber 上线 8 小时
- 实际接单 4 小时
- 平台说你时薪 $30
- 实际时薪？$15

这就是为什么 "gig work minimum wage" 是个伪概念。真正的问题是：**谁来为你的等待时间买单？**

Doctorow 引用了一个更激进的观点：政府应该提供 "jobs guarantee"——保证每个想工作的人都有工作。听起来像共产主义？美国的国家公园系统就是这么建起来的（Civilian Conservation Corps）。

### 我的看法

这篇文章让我想到了 AI 时代的一个类似问题：**谁来为 AI 的训练时间买单？**

程序员花了几十年写代码，这些代码被用来训练 LLM。LLM 现在能写代码了，但那些程序员拿到报酬了吗？

零工经济的 "engaged time vs available time" 骗局，和 AI 训练的 "你的代码被用了但你没拿到钱" 骗局，本质上是同一个问题：**价值创造和价值分配的脱节**。

Doctorow 的解法是政策干预（jobs guarantee）。AI 时代的解法可能是什么？数据工会？训练数据版税？还是干脆接受这就是新常态？

---

## 🔬 Dimitris Papailiopoulos: Claude Code 做研究

**来源**: [via Simon Willison](https://simonwillison.net/2026/Feb/17/dimitris-papailiopoulos/)

### 一句话

从问题到初步答案的距离，现在几乎为零。

### 核心观点

威斯康星大学的 ML 教授 Dimitris Papailiopoulos 发了条推：

> "I now have something close to a magic box where I throw in a question and a first answer comes back basically for free, in terms of human effort."

以前探索一个新想法的流程：
1. 自己笨拙地搭个原型，或者
2. 让学生跑个快速实验看看有没有信号
3. 如果有信号，再深入

现在？直接扔给 Claude Code + 几天 GPU 时间。

他说得很诚实：**"I don't know what this means for how we do research long term."**

### 我的看法

这条推对 PhD 学生来说是个警钟，也是个机会。

**警钟**：如果教授自己就能快速验证想法，学生的价值在哪？

**机会**：学生可以验证更多想法，失败得更快，找到真正值得深挖的方向。

但我觉得 Dimitris 漏掉了一个关键点：**AI 能给你 first answer，但不能给你 right question**。

研究的核心不是回答问题，是提出问题。AI 能帮你快速排除死胡同，但不能帮你找到值得走的路。

对于做研究的人：**把 AI 当成一个超快的实验助手，不是一个思考伙伴**。

---

## 🦜 新西兰 Kākāpō 四年来首只雏鸟

**来源**: [via Simon Willison](https://simonwillison.net/2026/Feb/17/first-kakapo-chick-in-four-years/)

### 一句话

全球最胖的鹦鹉终于生娃了。

### 核心观点

Kākāpō 是新西兰特有的不会飞的鹦鹉，全球只剩 237 只。情人节那天，一只叫 Yasmine 的 Kākāpō 孵化了四年来的第一只雏鸟。

有趣的细节：这个蛋是从另一只叫 Tīwhiri 的 Kākāpō 那里 "借" 来的，因为 Tīwhiri 已经有四个蛋了，而 Yasmine 一个都没有。

Simon Willison 为什么关注这个？因为他在 2026 年初的 LLM 预测里赌了一把：Kākāpō 今年会有个好的繁殖季。

### 我的看法

这条新闻和 AI 没关系，但它出现在 Karpathy 的 RSS 里说明了一件事：**好的信息食谱不只是技术文章**。

Simon Willison 的博客之所以有趣，不只是因为他写 AI 工具，还因为他关心奇怪的鹦鹉、科幻小说、和各种杂七杂八的东西。

对于想建立自己信息食谱的人：**别只订阅你专业领域的内容**。最好的想法往往来自跨领域的碰撞。

---

## 🔧 Troy Hunt: ESP32 蓝牙门锁实验失败

**来源**: [troyhunt.com](https://www.troyhunt.com/weekly-update-491/)

### 一句话

BLE 太被动了，搞不定智能门锁。

### 核心观点

Troy Hunt（Have I Been Pwned 的创始人）试图用 ESP32 蓝牙桥接器控制 Yale 智能门锁，结果完全失败。

问题不在 ESP32 本身——那玩意挺酷的。问题在于 BLE（低功耗蓝牙）太被动了，除非一直保持连接，否则根本检测不到锁的状态变化。

他的下一步：放弃蓝牙，专注优化 WiFi 网络稳定性。如果还不行，就换 Aqara U400。

### 我的看法

这是一篇典型的 "我失败了" 博客，但这种内容其实很有价值。

大多数技术博客只写成功案例。但真实的工程是：**90% 的尝试都会失败**。

Troy 的失败告诉我们：
1. BLE 不适合需要实时状态同步的场景
2. 智能家居的 "智能" 往往被网络可靠性拖后腿
3. 有时候最好的方案是换个硬件，而不是死磕软件

对于做 IoT 的人：**先验证网络层，再搞应用层**。

---

## 总结

今天的 feed 有个隐藏主题：**工具和基础设施**。

- Simon 在建 AI 辅助开发的可观测性工具
- Doctorow 在讨论劳动市场的基础设施（最低工资制度）
- Dimitris 在探索 AI 如何改变研究的基础设施
- Troy 在折腾智能家居的网络基础设施

Karpathy 的品味一如既往：**关注那些让其他事情成为可能的东西**。

---

*这篇笔记基于 [Karpathy Curated RSS](https://youmind.com/rss/pack/andrej-karpathy-curated-rss) 的 2026-02-17 聚合内容。*
