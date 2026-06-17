---
title: "Database DevOps: Migrations in CI/CD"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [database, migrations, ci-cd, devops]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Integrate database migrations safely into CI/CD pipeline.

Stack: PostgreSQL + Flyway (or Liquibase)
CI: GitHub Actions

1. **Migration file standards**: naming, rollback scripts, idempotency
2. **CI**: validate migration syntax on every PR
3. **Staging deploy**: run migrations before app deploy
4. **Production**: run migrations before rolling app deploy
5. **Zero-downtime patterns**:
   - New column: add nullable first, backfill, add NOT NULL constraint later
   - Drop column: two-phase (stop reading → deploy → drop)
   - Rename: expand-contract pattern
6. **Rollback**: automated rollback if migration fails
7. **Drift detection**: alert if prod schema differs from expected
8. **Data migrations**: separate from schema migrations (async job)
9. **Migration testing**: test against prod data copy weekly
10. **Permissions**: migration runner has limited privileges
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
