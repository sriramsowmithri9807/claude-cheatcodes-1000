---
title: "Implement Production Health Checks"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [health-check, monitoring, backend, devops]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement comprehensive health checks for my Node.js application.

Endpoints:
- `GET /health` — quick liveness probe (always returns 200 if process is alive)
- `GET /health/ready` — readiness probe (checks all dependencies)
- `GET /health/startup` — startup probe (for Kubernetes)

Readiness checks:
1. PostgreSQL: test query
2. Redis: PING
3. External APIs: your critical third-party services
4. Storage: check S3 accessibility
5. Memory: flag if heap > 80%
6. Disk: flag if disk > 90%

Response format (standardized health check API):
```json
{"status": "ok|degraded|critical", "checks": {...}, "version": "...", "uptime": 123}
```

Kubernetes liveness/readiness probe config included.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
