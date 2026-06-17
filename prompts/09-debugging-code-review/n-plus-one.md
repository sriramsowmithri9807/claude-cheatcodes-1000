---
title: "Fix N+1 Query Problems"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [n-plus-one, sql, orm, performance]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Fix the N+1 query problem in my code.

Code: [PASTE CODE WITH N+1]
ORM: [Prisma / TypeORM / Sequelize / raw SQL]
Symptom: [DESCRIBE: slow API, thousands of queries in logs]

Detect N+1:
1. Log all SQL queries (enable ORM query logging)
2. Count queries — if N records → N+1 queries, that's N+1
3. Identify which relation causes the N+1

Fix:
4. Eager loading: `include` related models in one query
5. DataLoader pattern: batch multiple lookups into one query
6. JOIN query: write it as a single JOIN instead of multiple queries
7. Select only needed fields (avoid over-fetching)

Before and after: show query count reduction.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
