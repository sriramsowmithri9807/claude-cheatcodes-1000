---
title: "Monitor Your Database"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [monitoring, postgresql, metrics, alerting]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Set up comprehensive database monitoring.

Database: PostgreSQL (self-hosted or AWS RDS)

Key metrics:
1. **Connection count**: vs max_connections (alert at 80%)
2. **Query latency**: p95, p99 per query type
3. **Cache hit rate**: buffer cache hit should be > 99%
4. **Vacuum status**: tables needing vacuum, bloat
5. **Replication lag**: streaming + logical replication lag
6. **Lock waits**: long-running locks blocking queries
7. **Deadlocks**: frequency and which queries cause them
8. **Index usage**: unused indexes wasting space + write overhead
9. **Table/index bloat**: dead rows percentage
10. **Disk I/O**: read vs write, iops, wait time

Tools: pg_stat_statements, pg_activity, pgBadger log analyzer, Prometheus pg_exporter.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
