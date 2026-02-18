---
layout: default
title: "Scholar Inbox"
permalink: /scholar_inbox/
---

# Scholar Inbox

Daily curated papers pulled from Scholar Inbox.

## Daily Digests (Auto Index)

{% assign digest_pages = site.pages
  | where_exp: "p", "p.url contains '/scholar_inbox/'"
  | where_exp: "p", "p.url contains 'diffusion'"
  | where_exp: "p", "p.url contains '/202'"
  | sort: "url" %}

{% assign digest_pages = digest_pages | reverse %}

{% for p in digest_pages %}
{% if p.url != '/scholar_inbox/' %}
- [{{ p.title | default: p.url }}]({{ p.url | relative_url }})
{% endif %}
{% endfor %}

---

## Notes

Per-paper notes live in `scholar_inbox/`. This page only indexes daily digest pages.
