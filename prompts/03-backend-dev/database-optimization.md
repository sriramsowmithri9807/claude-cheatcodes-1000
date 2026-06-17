---
title: "Optimize Database Performance"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [postgresql, optimization, indexes, sql]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Optimize my PostgreSQL database for production performance.

Current issues: [DESCRIBE: slow queries, high CPU, connection exhaustion, etc.]

Implement:
1. **Index analysis**: EXPLAIN ANALYZE on slow queries, add missing indexes
2. **Index types**: B-tree vs GIN vs GiST — when to use each
3. **Query optimization**: rewrite N+1 queries, use CTEs
4. **Connection pooling**: PgBouncer configuration
5. **Partitioning**: partition large tables by date or category
6. **Vacuuming**: configure autovacuum for high-write tables
7. **Read replicas**: route read queries to replica
8. **pg_stat_statements**: identify top slow queries
9. **Caching at application layer**: reduce DB load
10. **Schema changes**: zero-downtime approaches for large tables
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
