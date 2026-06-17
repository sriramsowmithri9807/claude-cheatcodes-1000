---
title: "Debug SQL Query Problems"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [sql, debugging, postgresql, performance]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Debug this SQL query:

```sql
[PASTE YOUR SQL QUERY]
```

Problem: [DESCRIBE: wrong results, too slow, syntax error, N+1 detected]
Database: [PostgreSQL / MySQL / SQLite]
Schema: [PASTE RELEVANT TABLE DEFINITIONS]

1. **Syntax check**: identify any syntax errors
2. **Logic check**: does the query do what was intended?
3. **Performance**: run EXPLAIN ANALYZE — what's slow?
4. **Index usage**: is an index being used? Should one be added?
5. **Correctness**: edge cases — NULLs, duplicates, wrong JOIN type
6. **Rewrite**: optimized version of the query
7. **Test cases**: sample data to verify the fix

Output: corrected, optimized query with explanation.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
