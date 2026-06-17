---
title: "Scaffold a NestJS Application"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [nestjs, nodejs, typescript, backend]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Scaffold a production NestJS application for: [DESCRIPTION].

Modules to generate:
- AuthModule: JWT, refresh tokens, guards
- UsersModule: CRUD, roles
- [YOUR DOMAIN MODULE]: core business logic

For each module include:
- Controller with all routes
- Service with business logic
- DTOs with class-validator decorators
- Entity (TypeORM or Prisma)
- Guard and Decorator examples
- Unit tests for service

Also: global exception filter, logging interceptor, configuration service, Swagger setup.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
