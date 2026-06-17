---
title: "REST API Design from Scratch"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [rest, api-design, best-practices]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Design a REST API for [YOUR DOMAIN] from scratch applying every best practice:
1. Resource naming (nouns, plural, nested where appropriate)
2. HTTP methods (GET safe+idempotent, POST create, PUT replace, PATCH partial, DELETE)
3. Status codes (cheat sheet for every case)
4. Request/response shapes
5. Error format (RFC 7807 Problem Details)
6. Pagination, filtering, sorting query params
7. Versioning strategy
8. Authentication (Bearer JWT)
9. Rate limiting headers
10. HATEOAS links

Output: complete OpenAPI 3.1 YAML + sample cURL commands for every endpoint.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
