---
title: "Design Infrastructure Caching"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [caching, cdn, cloudfront, redis]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a multi-layer caching infrastructure for my application.

App: [DESCRIBE]

Layer 1 — CDN (Cloudflare or CloudFront):
1. Cache static assets (JS, CSS, images) at edge
2. Cache API responses at edge for public content
3. Cache-Control headers for each asset type
4. Cache invalidation on deploy

Layer 2 — Nginx caching:
5. `proxy_cache` for upstream responses
6. Cache by URL, vary by auth header

Layer 3 — Application cache (Redis):
7. Cache expensive DB queries
8. Cache external API responses
9. Rate limiting counters

Layer 4 — Database cache:
10. PostgreSQL shared_buffers (25% RAM)
11. Materialized views for expensive reports

Draw the request flow showing which layer serves each request type.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
