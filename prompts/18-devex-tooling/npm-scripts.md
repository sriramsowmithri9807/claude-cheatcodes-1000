---
title: "Organize npm Scripts"
category: devex-tooling
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [npm, scripts, automation, package-json]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Organize npm scripts for my project.

Project: [DESCRIBE YOUR STACK]

Standard npm scripts every project should have:
```json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "lint:fix": "eslint . --fix",
    "format": "prettier --write .",
    "format:check": "prettier --check .",
    "type-check": "tsc --noEmit",
    "test": "vitest run",
    "test:watch": "vitest",
    "test:coverage": "vitest run --coverage",
    "test:ui": "vitest --ui",
    "e2e": "playwright test",
    "e2e:ui": "playwright test --ui",
    "db:migrate": "prisma migrate dev",
    "db:seed": "ts-node prisma/seed.ts",
    "db:studio": "prisma studio",
    "prepare": "husky",
    "clean": "rm -rf .next node_modules"
  }
}
```

Cross-platform scripts:
- Use `cross-env` for env variables
- Use `rimraf` instead of `rm -rf`
- Use `concurrently` for parallel scripts

Output: complete package.json scripts section.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
