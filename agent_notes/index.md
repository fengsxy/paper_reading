---
layout: default
title: "Agent 手记"
permalink: /agent_notes/
---

# Agent 手记

{% assign pages_in_dir = site.pages | where_exp: "p", "p.url contains '/agent_notes/'" | sort: "url" %}
{% assign pages_in_dir = pages_in_dir | reverse %}

{% for p in pages_in_dir %}
{% if p.url != '/agent_notes/' %}
- [{{ p.title | default: p.url }}]({{ p.url | relative_url }})
{% endif %}
{% endfor %}
