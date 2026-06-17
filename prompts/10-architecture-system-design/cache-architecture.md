---
title: "Design a Multi-Layer Cache Architecture"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [caching, architecture, redis, cdn]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a multi-layer cache architecture for my application.

Application type: [READ-HEAVY / WRITE-HEAVY / MIXED]
SLA: [LATENCY TARGET, AVAILABILITY TARGET]

Cache layers:
1. **Browser cache**: Cache-Control headers, service worker
2. **CDN**: Cloudflare/CloudFront for static and semi-static
3. **API gateway**: cache common API responses at gateway
4. **Application L1**: in-process memory cache (LRU, small, fast)
5. **Application L2**: Redis (larger, shared across instances)
6. **Query cache**: database query result cache
7. **DB buffer**: PostgreSQL shared_buffers

Design decisions:
8. Cache-aside vs write-through vs write-behind per layer
9. TTL strategy per data type
10. Cache invalidation: event-driven vs TTL-based
11. Cache warming on deploy
12. Consistency: eventual vs strong for each layer

Draw the cache hierarchy with hit rates.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
