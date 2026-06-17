---
title: "Learn SQL from Beginner to Intermediate"
category: student-learning
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [sql, databases, learning, postgresql]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Teach me SQL from beginner to intermediate.

Database: PostgreSQL
Context: [WHY YOU WANT TO LEARN SQL]

**Week 1 — SELECT**:
1. `SELECT` columns `FROM` table
2. `WHERE` to filter rows
3. `ORDER BY` to sort results
4. `LIMIT` and `OFFSET` for pagination
5. `DISTINCT` for unique values
6. String functions: UPPER, LOWER, LENGTH, LIKE
7. Date functions: NOW(), DATE_PART(), AGE()

**Week 2 — Aggregation**:
8. `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`
9. `GROUP BY`: aggregate per group
10. `HAVING`: filter groups
11. `CASE WHEN`: conditional in SELECT

**Week 3 — JOINs**:
12. `INNER JOIN`: rows matching in both
13. `LEFT JOIN`: all from left, matching from right
14. `RIGHT JOIN` and `FULL OUTER JOIN`
15. Self joins: table joined to itself

**Week 4 — Advanced**:
16. Subqueries
17. Window functions: `ROW_NUMBER`, `RANK`, `LAG`
18. CTEs: `WITH` clause

For each: explanation + practice queries on sample data.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
