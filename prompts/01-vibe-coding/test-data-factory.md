---
title: "Build a Test Data Factory"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [testing, factories, typescript, jest]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a test data factory system for my TypeScript project.

Models to build factories for:
[PASTE YOUR TYPESCRIPT INTERFACES/TYPES]

Implement:
1. Factory function for each model with sensible defaults
2. Override capability: `createUser({ email: 'test@test.com' })`
3. Trait support: `createUser('admin')`, `createUser('suspended')`
4. Relationship factories: `createPost({ author: createUser() })`
5. Sequence numbers for unique fields
6. Faker.js integration for realistic data
7. Database factory that actually creates records (Prisma/Drizzle)

Pattern: inspired by factory_bot (Ruby) or fishery (TypeScript).
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
