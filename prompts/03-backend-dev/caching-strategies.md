---
title: "Implement Advanced Caching Strategies"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [redis, caching, backend, performance]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement a comprehensive caching strategy for my Node.js API.

Endpoints/data to cache: [LIST YOUR HEAVY QUERIES]

Implement:
1. **Redis setup**: connection pooling, cluster mode support
2. **Cache-aside pattern**: check cache → miss → query DB → populate cache
3. **Write-through**: update cache on every DB write
4. **TTL strategy**: different expiry per data type
5. **Cache invalidation**: tag-based invalidation
6. **Distributed lock**: prevent cache stampede (Redis SETNX)
7. **Local + distributed cache**: L1 (in-memory) + L2 (Redis)
8. **Cache warming**: pre-populate on startup
9. **Cache key naming convention**
10. **Monitoring**: cache hit rate, eviction rate metrics
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
