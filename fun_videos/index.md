---
layout: default
title: "Fun Videos"
permalink: /fun_videos/
---

# Fun Videos

Daily picks of videos that are good to watch together.

## Daily Digests (Auto Index)

{% assign pages_in_dir = site.pages | where_exp: "p", "p.url contains '/fun_videos/'" | sort: "url" %}
{% assign pages_in_dir = pages_in_dir | reverse %}

{% for p in pages_in_dir %}
{% if p.url != '/fun_videos/' and p.url contains '/202' %}
- [{{ p.title | default: p.url }}]({{ p.url | relative_url }})
{% endif %}
{% endfor %}
