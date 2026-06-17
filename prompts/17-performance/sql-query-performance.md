---
title: "Write High-Performance SQL Queries"
category: performance
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [sql, performance, postgresql, optimization]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Write high-performance SQL queries for my use case.

Schema: [PASTE YOUR TABLES]
Queries to optimize: [PASTE SLOW QUERIES]

Query writing principles:
1. **SELECT specific columns**: avoid SELECT *
2. **Filter early**: WHERE before GROUP BY
3. **EXISTS vs IN**: EXISTS is often faster for subqueries
4. **Avoid functions on indexed columns**: `WHERE LOWER(email) =` prevents index use
5. **Batch inserts**: INSERT with multiple value rows
6. **RETURNING**: get inserted row without second query
7. **CTEs**: improve readability (materialized in PostgreSQL 12+)
8. **Window functions**: avoid self-joins for running totals
9. **LATERAL joins**: for per-row subqueries
10. **DISTINCT vs GROUP BY**: GROUP BY often more optimizable
11. **LIMIT early**: push limit into subqueries
12. **Index-only scans**: covering index eliminates table access

For my specific queries:
- EXPLAIN ANALYZE interpretation
- Rewritten optimized version
- Index to create

Output: optimized queries + index strategy.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
