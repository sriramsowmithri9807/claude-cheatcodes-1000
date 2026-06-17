---
title: "Configure Database Connection Pooling"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [postgresql, connection-pool, pg, backend]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Configure optimal database connection pooling for my Node.js app.

Database: PostgreSQL
ORM/Query builder: [Prisma / Drizzle / node-postgres / Knex]

Implement:
1. Pool size calculation formula (connections = core_count * 2 + 1)
2. `pg` pool configuration: min, max, idleTimeoutMillis, connectionTimeoutMillis
3. PgBouncer in transaction mode (for serverless environments)
4. Connection leak detection
5. Health check: periodic test query to keep connections warm
6. Graceful pool shutdown on SIGTERM
7. Pool metrics: total, idle, waiting connections
8. Error handling: connection refused, timeout, pool exhausted
9. Read/write splitting: write pool → primary, read pool → replica

Benchmark: show connection count under load without vs with pooling.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
