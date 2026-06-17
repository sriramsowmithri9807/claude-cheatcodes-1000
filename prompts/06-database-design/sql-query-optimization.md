---
title: "Optimize Slow SQL Queries"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [sql, optimization, indexes, postgresql]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Optimize these slow SQL queries:

[PASTE YOUR SLOW QUERIES AND THEIR EXPLAIN ANALYZE OUTPUT]

Optimization techniques:
1. **Read EXPLAIN ANALYZE**: identify seq scan, hash join, sort spills
2. **Index creation**: B-tree, GIN, GiST, partial, covering indexes
3. **Query rewriting**: EXISTS vs IN, CTEs vs subqueries, avoiding DISTINCT
4. **JOIN optimization**: order, type (hash/nested loop/merge), conditions
5. **Filter pushdown**: move WHERE conditions to reduce rows early
6. **N+1 elimination**: single JOIN vs multiple queries
7. **Pagination**: cursor-based vs OFFSET
8. **Materialized views**: precompute expensive aggregations
9. **Statistics**: ANALYZE, pg_stats for planner accuracy
10. **Partitioning**: for very large tables

Before/after EXPLAIN ANALYZE comparison.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
