---
title: "Design and Build an API SDK"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [sdk, api, typescript, client]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design and build a TypeScript SDK for my API.

API: [DESCRIBE YOUR API]

SDK design principles:
1. **Type safety**: TypeScript types for all requests and responses
2. **Fluent interface**: `client.users.create({...}).then()`
3. **Resource-based**: `client.users`, `client.products`
4. **Consistent error handling**: typed error classes
5. **Retry logic**: built-in retry with backoff
6. **Pagination helpers**: auto-paginate with async iterators
7. **Request/response interceptors**: for logging, auth refresh
8. **Config**: base URL, API key, timeout, retries
9. **Framework-agnostic**: works in Node.js and browser
10. **Zero dependencies**: or minimal deps

Output: complete SDK + README + usage examples.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
