---
title: "Generate Beautiful API Documentation"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [swagger, openapi, docs, api]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Generate comprehensive, beautiful API documentation.

API framework: [Express / Fastify / NestJS / FastAPI]

Using: Swagger UI / Scalar / Redoc

Implement:
1. OpenAPI 3.1 spec generation (code-first from your framework)
2. Complete request/response schemas with examples
3. Authentication documentation (JWT, API Key, OAuth)
4. Error response catalogue (every possible error code)
5. SDKs: auto-generate TypeScript + Python client SDKs
6. Changelog section
7. Try-it-out with a sandbox environment
8. Postman collection export

Host docs at: `/docs` in development, separate docs site in production.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
