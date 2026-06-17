---
title: "API Testing Patterns"
category: testing-qa
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [api, testing, rest, patterns]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement comprehensive API testing patterns for my REST API.

API: [DESCRIBE]
Testing tool: Vitest + Supertest OR Postman Collections

Test patterns:
1. **Happy path**: successful requests with valid data
2. **Validation errors**: test every required field and format
3. **Auth tests**:
   - No token → 401
   - Expired token → 401
   - Wrong role → 403
   - Correct auth → 200
4. **Not found**: request non-existent resources → 404
5. **Conflict**: create duplicate → 409
6. **Rate limit**: exceed limit → 429
7. **Pagination**: first page, last page, out-of-bounds page
8. **Sorting**: ascending and descending
9. **Filtering**: test all filter combinations
10. **Large payloads**: test max request body size

Organize tests by: resource → operation → scenario.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
