---
title: "Design Comprehensive Caching Strategy"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [caching, strategy, architecture, redis]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a comprehensive caching strategy for my application.

Application: [DESCRIBE]
Problem: [DESCRIBE: slow queries, high DB load, expensive computations]

For each type of data, define:
1. **Cache location**: browser / CDN / Redis / in-memory
2. **Cache key**: what uniquely identifies this cached item
3. **TTL**: how long before it expires
4. **Invalidation trigger**: what event makes this cache stale
5. **Cache miss behavior**: compute it, return stale, return default
6. **Consistency requirements**: eventual or strong

Specific data types in my app:
- [YOUR DATA TYPE 1]: [CACHING DECISION]
- [YOUR DATA TYPE 2]: [CACHING DECISION]
- [YOUR DATA TYPE 3]: [CACHING DECISION]

Cache warming: how to pre-populate on deploy.
Monitoring: hit rate, eviction rate, memory usage.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
