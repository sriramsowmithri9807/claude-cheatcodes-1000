---
title: "Build a FastAPI Python Backend"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [fastapi, python, rest, postgresql]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a production FastAPI backend for: [APP DESCRIPTION].

Include:
- Pydantic v2 models for request/response validation
- SQLAlchemy 2.0 async ORM with PostgreSQL
- Alembic migrations
- JWT auth (python-jose)
- Background tasks with Celery + Redis
- Dependency injection pattern
- API versioning (/api/v1/)
- OpenAPI docs (FastAPI auto-generates)
- Pytest test suite with fixtures
- Docker + docker-compose setup
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
