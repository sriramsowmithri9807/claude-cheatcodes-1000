---
title: "Write Complex Analytical SQL"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [sql, analytics, postgresql, reporting]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Write complex analytical SQL queries for my business intelligence needs.

Schema: [PASTE YOUR SCHEMA]
Questions to answer:
1. [BUSINESS QUESTION 1]
2. [BUSINESS QUESTION 2]
3. [BUSINESS QUESTION 3]

For each query:
1. SQL with full explanation of each clause
2. EXPLAIN ANALYZE analysis
3. Index recommendations to optimize it
4. Alternative approaches compared

Concepts to use where appropriate:
- CTEs and recursive CTEs
- Window functions
- ROLLUP and CUBE for multi-dimensional aggregation
- LATERAL joins
- JSON aggregation
- Conditional aggregation (SUM CASE WHEN)
- Materialized views for frequently-run queries
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
