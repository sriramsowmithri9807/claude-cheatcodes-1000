---
title: "Design a Database Backup Strategy"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [backup, postgresql, disaster-recovery, devops]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Design a comprehensive database backup and recovery strategy.

Database: PostgreSQL on [AWS RDS / self-hosted / Supabase]
Data size: [CURRENT SIZE AND GROWTH RATE]
RTO (recovery time objective): [e.g., < 4 hours]
RPO (recovery point objective): [e.g., < 1 hour data loss max]

Implement:
1. **Full backup**: daily, retained 30 days
2. **WAL archiving**: continuous, enables point-in-time recovery
3. **Snapshot backup**: hourly for recent windows
4. **Offsite copies**: 3-2-1 rule (3 copies, 2 media types, 1 offsite)
5. **Encryption**: encrypt backups at rest
6. **Restoration testing**: restore to staging weekly, document steps
7. **Disaster recovery drill**: quarterly full DR exercise
8. **Monitoring**: alert if backup fails

Tool: pgBackRest (better than pg_dump for large databases).
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
