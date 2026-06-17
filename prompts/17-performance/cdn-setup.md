---
title: "Set Up CDN for Maximum Performance"
category: performance
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [cdn, cloudflare, performance, assets]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Set up and configure a CDN for maximum performance.

App: [DESCRIBE]
CDN options: Cloudflare (recommended) / CloudFront / Fastly

**Cloudflare setup**:
1. Add site to Cloudflare
2. Change DNS nameservers
3. Enable proxy (orange cloud) on A/CNAME records
4. SSL mode: Full (Strict) — encrypt everywhere
5. HTTPS upgrade: always redirect HTTP → HTTPS

**Performance rules**:
6. Cache static assets: CSS/JS/images (1 year)
7. Cache API responses: GET endpoints < 60s
8. Minify: HTML, CSS, JavaScript
9. Brotli compression: smaller than gzip
10. HTTP/2 + HTTP/3: enable both
11. Early hints: preconnect to origins

**Cache purging**:
12. Purge on deploy: `cloudflare.purgeCache()` in deploy script
13. Cache tags: purge specific content by tag

**Analytics**:
14. Real User Monitoring in Cloudflare dashboard
15. Cache hit rate target: > 80%

Output: Cloudflare configuration + deploy script.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
