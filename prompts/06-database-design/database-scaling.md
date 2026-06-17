---
title: "Scale Your Database"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [scaling, postgresql, read-replicas, sharding]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Create a database scaling plan for my application.

Current: [SINGLE DB, SIZE, QUERIES/SEC]
Projected: [10x / 100x GROWTH over N months]

Scaling ladder (do these in order):
1. **Optimize queries and indexes** (free, do first)
2. **Vertical scaling**: bigger instance (quick fix, but has ceiling)
3. **Connection pooling**: PgBouncer (handle more concurrent connections)
4. **Read replicas**: route reads to replica (helps 80% of workloads)
5. **Caching layer**: Redis for hot data (reduce DB load 50-90%)
6. **Partitioning**: split large tables (time-based or range)
7. **Horizontal sharding**: Citus or app-level sharding (last resort)
8. **CQRS**: separate read and write models

For each step: when to do it (trigger metric) + implementation time.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
