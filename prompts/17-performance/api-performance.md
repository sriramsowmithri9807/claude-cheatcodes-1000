---
title: "Optimize API Performance"
category: performance
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [api, performance, caching, optimization]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Optimize my API's performance.

API: [DESCRIBE]
Current latency: [p50, p95, p99]
Target: [TARGET LATENCY]

Profiling:
1. **Add timing headers**: X-Response-Time per request
2. **Distributed tracing**: OpenTelemetry to find bottlenecks
3. **Database monitoring**: pg_stat_statements for slow queries

Optimizations:
4. **N+1 queries**: DataLoader or eager loading
5. **Redis caching**: cache expensive DB queries (1s → 1ms)
6. **Database indexes**: for every WHERE and JOIN condition
7. **Streaming responses**: start sending before all data is ready
8. **Pagination**: limit result sets
9. **Field selection**: GraphQL or ?fields= parameter
10. **Compression**: gzip/brotli (80% size reduction for JSON)
11. **Connection pooling**: PgBouncer, Redis client pooling
12. **Async work**: move non-critical work to a queue

Infrastructure:
13. **CDN caching**: cache GET responses at edge
14. **Horizontal scaling**: more instances behind load balancer

Output: optimized code for my slowest endpoints.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
