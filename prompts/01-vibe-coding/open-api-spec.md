---
title: "Generate an OpenAPI 3.1 Spec for Your API"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [openapi, swagger, api-docs, rest]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Generate a complete OpenAPI 3.1 specification for my API:

[DESCRIBE YOUR API: endpoints, auth method, main entities]

Include:
- All paths with GET/POST/PUT/PATCH/DELETE where appropriate
- Request bodies with JSON Schema validation
- Response schemas for 200, 400, 401, 403, 404, 500
- Security schemes (Bearer JWT or API Key)
- Tags for grouping
- Examples for every endpoint
- Reusable components ($ref schemas)

Output as valid YAML that can be imported into Swagger UI or Postman.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
