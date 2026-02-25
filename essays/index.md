---
layout: default
title: "Essays"
permalink: /essays/
---

# Essays

{% assign pages_in_dir = site.pages | where_exp: "p", "p.url contains '/essays/'" | where_exp: "p", "p.url != '/essays/'" | where_exp: "p", "p.url != '/essays/xiaohongshu/'" | sort: "date" %}
{% assign pages_in_dir = pages_in_dir | reverse %}

{% for p in pages_in_dir %}
{% unless p.url contains '/xiaohongshu/' %}
- [{{ p.title | default: p.url }}]({{ p.url | relative_url }})
{% endunless %}
{% endfor %}

## 小红书版

{% assign xhs_pages = site.pages | where_exp: "p", "p.url contains '/xiaohongshu/'" | sort: "date" %}
{% assign xhs_pages = xhs_pages | reverse %}

{% for p in xhs_pages %}
- [{{ p.title | default: p.url }}]({{ p.url | relative_url }})
{% endfor %}
