---
title: "Build a URL Shortener Service"
category: fullstack-projects
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [url-shortener, redis, analytics, fullstack]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a URL shortener with analytics (like Bit.ly).

Stack: Node.js + Redis + PostgreSQL + Next.js

Features:
1. Shorten any URL: generate 6-char base62 code
2. Custom aliases: user picks their own slug
3. QR code generation
4. Redirect: GET /:code → 301 redirect (cache in Redis, 1ms response)
5. Analytics per link: clicks, unique visitors, countries, referrers, devices
6. Click tracking: async (don't slow the redirect)
7. Link expiry: optional TTL
8. Password-protected links
9. API: programmatic shortening with API key
10. Dashboard: all links, stats, delete, edit

Performance target: redirect in < 5ms (Redis-first lookup).
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
