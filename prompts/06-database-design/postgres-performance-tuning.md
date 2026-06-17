---
title: "Tune PostgreSQL for Production"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [postgresql, performance, configuration, devops]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Tune PostgreSQL configuration for production performance.

Server specs: [CPU cores, RAM, disk type (SSD/NVMe), workload type (OLTP/OLAP/mixed)]

Configure postgresql.conf:
1. **Memory**: shared_buffers (25% RAM), effective_cache_size (75% RAM), work_mem, maintenance_work_mem
2. **WAL**: wal_buffers, checkpoint_completion_target, max_wal_size
3. **Connections**: max_connections, connection pooler recommendation
4. **Planner**: random_page_cost (1.1 for SSD vs 4 for HDD), effective_io_concurrency
5. **Autovacuum**: tuning for high-write tables
6. **Logging**: log_min_duration_statement = 1000 (log slow queries)
7. **Parallelism**: max_parallel_workers_per_gather

Output: complete postgresql.conf with explanations for each setting.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
