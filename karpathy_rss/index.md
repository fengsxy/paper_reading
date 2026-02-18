---
layout: default
title: "Karpathy RSS Digest"
permalink: /karpathy_rss/
---

# Karpathy RSS Digest

Curated picks from Andrej Karpathy's RSS feeds.

## Daily Digests (Auto Index)

{% assign pages_in_dir = site.pages | where_exp: "p", "p.url contains '/karpathy_rss/'" | sort: "url" %}
{% assign pages_in_dir = pages_in_dir | reverse %}

{% for p in pages_in_dir %}
{% if p.url != '/karpathy_rss/' and p.url contains '/202' %}
- [{{ p.title | default: p.url }}]({{ p.url | relative_url }})
{% endif %}
{% endfor %}
