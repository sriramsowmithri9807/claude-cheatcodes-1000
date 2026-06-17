---
title: "Optimize Database Performance"
category: performance
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [database, postgresql, performance, indexes]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Optimize database performance for my application.

Database: PostgreSQL
Slow queries: [PASTE QUERIES OR DESCRIBE]
Current scale: [ROWS, RPS, LATENCY]

Query optimization:
1. **EXPLAIN ANALYZE**: read and understand the plan
2. **Seq scan → Index scan**: add the right index
3. **Composite indexes**: order matters (equality first, range last)
4. **Partial indexes**: index WHERE condition reduces size
5. **Covering indexes**: INCLUDE columns to avoid heap access
6. **N+1**: eliminate with JOIN or DataLoader

Schema optimization:
7. **VACUUM ANALYZE**: update statistics for planner
8. **Table bloat**: find and fix bloated tables
9. **Index bloat**: rebuild bloated indexes (REINDEX CONCURRENTLY)
10. **Partitioning**: for very large tables

Configuration:
11. **shared_buffers**: 25% of RAM
12. **work_mem**: per-sort allocation
13. **Connection pooling**: PgBouncer

Monitoring:
14. pg_stat_statements: find slowest queries
15. pg_activity: see what's running now

Output: optimized queries + index strategy.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
