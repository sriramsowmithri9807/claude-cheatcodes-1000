---
title: "Master Database Indexing"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [indexes, postgresql, performance, sql]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design the optimal index strategy for my database.

Schema: [PASTE YOUR TABLES]
Frequent queries: [DESCRIBE OR PASTE YOUR TOP 10 QUERIES]

1. **When to index**: high cardinality, frequent WHERE, JOIN, ORDER BY
2. **When NOT to index**: write-heavy tables, low cardinality, small tables
3. **B-tree indexes**: default, range queries, equality
4. **Composite indexes**: column order matters — explain how
5. **Partial indexes**: index WHERE condition (only index what you query)
6. **Covering indexes**: INCLUDE extra columns to avoid table lookup
7. **GIN indexes**: for arrays, JSONB, full-text search
8. **Index bloat**: REINDEX, VACUUM impact
9. **Unused indexes**: find and drop them (pg_stat_user_indexes)
10. **Index-only scans**: when possible

Output: exact CREATE INDEX statements for my queries.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
