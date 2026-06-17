---
title: "Dockerize a Node.js Application"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [docker, containers, nodejs, devops]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Dockerize my Node.js application for production.

Current app: [DESCRIBE YOUR APP AND ITS DEPENDENCIES]

Create:
1. **Dockerfile** (multi-stage build):
   - Stage 1: deps only (layer caching)
   - Stage 2: build TypeScript
   - Stage 3: production image (distroless or alpine)
   - Non-root user for security
   - Health check instruction
2. **docker-compose.yml** for local dev:
   - App + PostgreSQL + Redis
   - Volume mounts for hot reload
   - Environment file
3. **.dockerignore** (exclude node_modules, .env, .git)
4. Optimizations: final image < 200MB, layer caching tricks
5. Production considerations: secrets management, logging to stdout
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
