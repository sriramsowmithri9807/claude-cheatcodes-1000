---
title: "Master Database Migrations"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [migrations, postgresql, nodejs, devops]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Master database migrations for my [Node.js/Python] app.

Current schema: [DESCRIBE CURRENT STATE]
Desired schema: [DESCRIBE TARGET STATE]

Implement using [Flyway / Liquibase / node-pg-migrate / Prisma Migrate]:
1. Migration file naming convention
2. The migration SQL/code for each change
3. Rollback scripts for each migration
4. Data migrations (migrate existing data)
5. Running migrations in CI/CD pipeline
6. Zero-downtime migrations for:
   - Adding a column (always safe)
   - Removing a column (dangerous — show safe approach)
   - Renaming a column (the expand-contract pattern)
   - Adding a NOT NULL constraint to existing column
7. Migration testing in staging before production
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
