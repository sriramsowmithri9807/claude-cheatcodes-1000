---
title: "Master SQL Window Functions"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [sql, window-functions, postgresql, analytics]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Master SQL window functions for analytics queries.

My data: [DESCRIBE YOUR TABLES]
Analytics questions: [WHAT DO YOU NEED TO CALCULATE]

Teach me with my data:
1. **ROW_NUMBER()**: assign unique row numbers within partition
2. **RANK() / DENSE_RANK()**: rankings with ties
3. **NTILE(n)**: divide rows into N buckets
4. **LAG() / LEAD()**: access previous/next row value
5. **FIRST_VALUE() / LAST_VALUE()**: first/last value in window
6. **SUM() / AVG() / COUNT()**: running totals and rolling averages
7. **PARTITION BY**: reset window per group
8. **ROWS BETWEEN**: define frame: current row, N preceding, unbounded

For each: SQL query against my data + result explanation.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
