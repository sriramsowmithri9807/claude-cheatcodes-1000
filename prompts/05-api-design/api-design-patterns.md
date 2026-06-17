---
title: "API Design Patterns Masterclass"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [api, patterns, design, best-practices]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Apply these API design patterns to my API: [DESCRIBE YOUR API].

1. **Resource Singleton**: `/me` instead of `/users/{id}` for current user
2. **Sub-resources**: `/posts/{id}/comments` for owned resources
3. **Custom methods**: `/orders/{id}:cancel` (Google API style) for actions
4. **Long-running operations**: return operation ID → poll for status
5. **Batch operations**: `POST /batch` to reduce round trips
6. **Partial updates**: PATCH with RFC 7396 JSON Merge Patch
7. **Field selection**: `?fields=id,name,email` to reduce payload
8. **Sorting**: `?sort=-createdAt,+name`
9. **Includes/expansion**: `?include=author,comments` to embed related
10. **Search endpoint**: POST /search with complex query body

For each: when to use + implementation.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
