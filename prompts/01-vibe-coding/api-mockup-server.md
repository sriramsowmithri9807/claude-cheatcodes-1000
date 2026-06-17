---
title: "Build an Instant Mock API Server"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [api, mock, testing, json-server]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Build me an instant mock API server for my frontend that simulates:

[DESCRIBE YOUR API NEEDS / PASTE OPENAPI SPEC]

Use Express.js + TypeScript. Include:
- All CRUD endpoints with realistic fake data
- Simulated network delay (100–500ms random)
- Error simulation (5% chance of 500 error)
- CORS configured for localhost
- Authentication simulation (any Bearer token accepted)
- Pagination support on list endpoints
- Request/response logging middleware

Also include a `db.json` with 20 realistic seed records per entity.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
