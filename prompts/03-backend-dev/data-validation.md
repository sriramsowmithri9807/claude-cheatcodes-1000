---
title: "Master Data Validation with Zod"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [zod, validation, typescript, backend]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Master Zod for data validation across your entire Node.js stack.

Schemas to build: [DESCRIBE YOUR DATA TYPES]

Implement:
1. Basic schemas: string, number, boolean, date with constraints
2. Object schemas with strict mode
3. Array and tuple schemas
4. Union and discriminated union schemas
5. Recursive schemas (nested tree structures)
6. Custom validators with `.refine()` and `.superRefine()`
7. Async validation (check DB for uniqueness)
8. Schema composition: `.merge()`, `.extend()`, `.pick()`, `.omit()`
9. Type inference: `z.infer<typeof schema>`
10. Parse vs safeParse — when to use each
11. Error formatting: turn Zod errors into user-friendly messages
12. OpenAPI schema generation from Zod schemas
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
