---
title: "ORM vs Raw SQL Decision Guide"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [orm, sql, prisma, postgresql]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Advise on whether to use an ORM or raw SQL for my project.

Project: [DESCRIBE]
Team SQL experience: [LOW / MEDIUM / HIGH]

Argumentsfor ORM (Prisma, Drizzle, TypeORM):
1. Type safety — TypeScript types from schema
2. Migration management
3. Relationship loading
4. Simpler CRUD operations
5. Less SQL knowledge required

Arguments for raw SQL:
6. Full SQL power (window functions, CTEs, complex queries)
7. No abstraction overhead
8. Easier optimization
9. Better for existing complex schemas

For MY project specifically:
- Recommendation with justification
- If ORM: which one and why
- Hybrid: ORM for CRUD + raw SQL for complex queries
- Implementation pattern for the hybrid approach
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
