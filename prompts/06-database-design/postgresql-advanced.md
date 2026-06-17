---
title: "Advanced PostgreSQL Features"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [postgresql, advanced, sql, database]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement these advanced PostgreSQL features in my database:

Use case: [DESCRIBE YOUR DATA AND QUERIES]

1. **JSONB**: store and query semi-structured data, GIN index, jsonb_path operators
2. **Full-text search**: tsvector, tsquery, GIN index, ts_rank, tsheadline
3. **Partitioning**: range/list/hash partitioning, partition pruning
4. **CTEs**: WITH clause, recursive CTEs for tree structures
5. **Window functions**: ROW_NUMBER, RANK, LEAD/LAG, running totals
6. **Materialized views**: refresh strategy, incremental refresh
7. **Foreign Data Wrappers**: query external PostgreSQL or CSV
8. **Triggers and rules**: computed columns, audit log
9. **Extensions**: pg_stat_statements, pgcrypto, postgis
10. **EXPLAIN ANALYZE**: read and optimize query plans
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
