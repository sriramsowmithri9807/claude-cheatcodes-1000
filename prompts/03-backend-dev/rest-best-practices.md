---
title: "REST API Design Best Practices"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [rest, api-design, best-practices, backend]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Apply REST API best practices to my API.

My current API: [DESCRIBE CURRENT ROUTES]

Best practices to implement:
1. **Naming**: nouns not verbs, plural resources, lowercase kebab-case
2. **HTTP methods**: GET (safe+idempotent), POST, PUT (full replace), PATCH (partial), DELETE
3. **Status codes**: the right code for every situation (cheat sheet)
4. **Filtering**: `?filter[status]=active&filter[type]=post`
5. **Sorting**: `?sort=-createdAt,name`
6. **Pagination**: cursor-based with metadata
7. **Versioning**: `/api/v1/`
8. **Error format**: consistent JSON error body
9. **HATEOAS**: optional but show when useful
10. **Content negotiation**: Accept header

Rewrite my current routes applying all best practices.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
