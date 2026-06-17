---
title: "Debug Database Query Issues"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [database, sql, orm, debugging]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Debug database query issues in my application.

ORM/Query builder: [Prisma / Drizzle / TypeORM / raw SQL]
Schema: [PASTE RELEVANT SCHEMA]
Query code: [PASTE QUERY]
Problem: [DESCRIBE: wrong results / slow / error / no results]

1. Log the generated SQL: `DEBUG=prisma:query` or `.explain()`
2. Run the SQL directly in psql/pgAdmin — same result?
3. Check WHERE conditions — are they correct?
4. Check JOINs — LEFT JOIN vs INNER JOIN matters
5. Check NULL handling — `= NULL` doesn't work, use `IS NULL`
6. Check case sensitivity — text comparison is case-sensitive
7. Check timezone — TIMESTAMPTZ vs TIMESTAMP
8. Add EXPLAIN ANALYZE if it's slow
9. Fix the query
10. Write a test that confirms correct results
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
