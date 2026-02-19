---
layout: default
type: timeline
series: dwarkesh
title: "Dwarkesh Transcripts"
permalink: /transcripts/dwarkesh/
---

# Dwarkesh Transcripts

This page lists transcripts + analysis for the Dwarkesh Patel podcast.

{% assign items = site.pages | where: "series", "dwarkesh" | where: "type", "transcript" | sort: "episode" %}

{% if items.size == 0 %}
_No episodes yet._
{% else %}
{% for p in items %}
- EP{{ p.episode }}: [Transcript]({{ p.permalink | relative_url }}) · {% if p.analysis_url %}[Analysis]({{ p.analysis_url | relative_url }}){% else %}-{% endif %}
{% endfor %}
{% endif %}
