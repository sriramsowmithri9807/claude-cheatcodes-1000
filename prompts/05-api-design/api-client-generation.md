---
title: "Auto-Generate API Clients from OpenAPI"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [openapi, codegen, sdk, typescript]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Auto-generate typed API clients from my OpenAPI specification.

My OpenAPI spec: [PATH OR PASTE]
Target languages: TypeScript, Python, Kotlin (Android)

Using: openapi-generator-cli or openapi-typescript

1. TypeScript client: openapi-typescript + openapi-fetch
   - Zero-runtime-overhead types
   - Fetch-based, works everywhere
   - Tree-shakeable
2. Python client: openapi-generator
   - Pydantic models for responses
   - Async (httpx) version
3. React Query integration: tanstack-query-openapi
   - Auto-generated hooks per endpoint

Output: generator config + GitHub Actions to regenerate on spec change.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
