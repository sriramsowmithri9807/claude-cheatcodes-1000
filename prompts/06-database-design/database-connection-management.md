---
title: "Manage Database Connections in Production"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [connections, postgresql, pooling, performance]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Optimize database connection management for production.

Stack: Node.js + PostgreSQL
Load: [EXPECTED RPS AND CONCURRENCY]

1. **Connection pool sizing**: (CPU cores × 2) + 1 per server
2. **pg pool config**: max, min, idleTimeoutMillis, connectionTimeoutMillis
3. **PgBouncer**: transaction pooling for serverless/high concurrency
4. **Connection leaks**: detect and fix (log long-held connections)
5. **Serverless problem**: functions create new connections per invocation
6. **RDS Proxy**: managed connection pooler for AWS
7. **Monitoring**: pg_stat_activity, wait events, max_connections
8. **Connection limits per role**: `ALTER ROLE myuser CONNECTION LIMIT 100`
9. **Graceful shutdown**: drain connections before restart
10. **Circuit breaker**: stop making new connections if DB is overwhelmed
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
