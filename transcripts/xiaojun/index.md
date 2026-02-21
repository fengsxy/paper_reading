---
date: 2024-01-01
title: 张小珺访谈 Timeline
permalink: /transcripts/xiaojun/
---

# 张小珺访谈 Timeline

这里按时间轴/期数整理：每期两份文件（转录原文 + 分析）。

## Timeline

{% assign items = site.pages | where: "series", "xiaojun" | where: "type", "transcript" | sort: "episode" %}

{% for p in items %}
{% assign analyses = site.pages | where: "series", "xiaojun" | where: "type", "analysis" | where: "episode", p.episode %}
{% assign a = analyses | first %}
- **EP{{ p.episode }}** ({{ p.date }}) {{ p.guest }} — {{ p.title }}  
  [Transcript]({{ site.baseurl }}{{ p.url }}){% if a %} · [Analysis]({{ site.baseurl }}{{ a.url }}){% endif %}
{% endfor %}

---

## 说明

- `Transcript` 文件是可检索的原文转录（带时间戳）。
- `Analysis` 文件聚焦：反共识点、可学习点、提问技巧，以及可验证的坑。
