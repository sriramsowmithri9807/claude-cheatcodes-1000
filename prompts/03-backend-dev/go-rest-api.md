---
title: "Build a REST API in Go"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [go, golang, rest, gin]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a production REST API in Go for: [DESCRIPTION].

Using: Gin framework + sqlx + PostgreSQL

Include:
- Project structure following Go conventions
- Middleware: auth (JWT), logging (zerolog), recovery, CORS
- Database: sqlx with prepared statements (prevent SQL injection)
- Repository pattern with interfaces (for testability)
- Config management with env vars (godotenv)
- Graceful shutdown
- Makefile for common tasks
- Docker multi-stage build
- Unit tests using testify and mock generation
- OpenAPI spec from Go comments (swaggo)
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
