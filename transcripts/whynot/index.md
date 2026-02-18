---
layout: default
title: "WhynotTV Transcripts"
series: whynot
permalink: /transcripts/whynot/
---

# WhynotTV Transcripts

{% assign items = site.pages | where: "series", "whynot" | where: "type", "transcript" | sort: "episode" %}

| Episode | Guest | Title | Transcript | Analysis |
|---:|---|---|---|---|
{% for p in items %}
| {{ p.episode }} | {{ p.guest | default: "" }} | {{ p.title }} | [Transcript]({{ p.permalink | relative_url }}) | [Analysis]({{ p.analysis_url | relative_url }}) |
{% endfor %}
