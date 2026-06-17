---
title: "Create Docker Compose for Development"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [docker, docker-compose, local-dev, containers]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Create a complete Docker Compose setup for local development of my app.

Services:
- App: [Node.js / Python / Go]
- Database: PostgreSQL 16
- Cache: Redis 7
- [OTHER SERVICES: Elasticsearch, MinIO, Mailhog, etc.]

`docker-compose.yml`:
1. Each service with health checks
2. Volume mounts for hot reload (don't copy code into container)
3. Named volumes for persistent data (DB data survives container restart)
4. Environment variables from `.env` file
5. Networking (internal DNS between services)
6. `depends_on` with health check conditions
7. Resource limits (prevent one service from hogging all RAM)

Also:
- `docker-compose.override.yml` for dev-specific overrides
- `docker-compose.prod.yml` for production-like settings
- Makefile with: `make up`, `make down`, `make logs`, `make shell`
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
