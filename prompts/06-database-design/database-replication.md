---
title: "Set Up Database Replication"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [replication, postgresql, high-availability, devops]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Set up database replication for high availability and read scaling.

Stack: PostgreSQL 15+

1. **Streaming replication** (hot standby):
   - Primary config: wal_level, max_wal_senders
   - Replica config: primary_conninfo, hot_standby
   - Replication slots: don't lose WAL even if replica lags
   - Monitoring: replication lag
2. **Read replicas**:
   - Route read queries to replica
   - Application-level routing vs PgBouncer vs pgpool
3. **Failover**:
   - Detect primary failure (Patroni / pg_auto_failover)
   - Promote replica to primary
   - Update connection string (DNS / load balancer)
   - Recovery time objective: < 30 seconds
4. **Multi-region**: logical replication across regions
5. **Testing**: simulate primary failure in staging monthly
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
