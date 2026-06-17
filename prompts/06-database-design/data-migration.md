---
title: "Plan and Execute Data Migration"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [migration, postgresql, etl, data]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Plan and execute a data migration for: [DESCRIBE WHAT YOU'RE MIGRATING — e.g., old schema to new schema, MySQL to PostgreSQL, adding columns].

1. **Migration plan**:
   - What data is moving where
   - Estimated volume and time
   - Zero-downtime vs maintenance window approach
2. **Backup strategy**: full backup before starting, point-in-time recovery test
3. **Migration script**: idempotent, can be re-run safely
4. **Validation**: verify row counts, checksums, sample records
5. **Dual-write period**: write to old and new schema simultaneously
6. **Cutover**: atomic switch, rollback plan if issues
7. **Cleanup**: remove old schema after validation period
8. **Testing**: run migration on production data copy first

Output: complete migration SQL + validation queries.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
