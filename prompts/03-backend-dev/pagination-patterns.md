---
title: "Implement Pagination Patterns"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [pagination, api, rest, backend]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement pagination for my API and explain the tradeoffs.

My data: [DESCRIBE YOUR DATA: ordered by what, expected size, query patterns]

Implement all three patterns:

**1. Offset pagination** (simple but slow for large datasets):
- `GET /items?page=2&limit=20`
- SQL: OFFSET + LIMIT

**2. Cursor pagination** (fast, consistent, recommended):
- `GET /items?cursor=eyJ...&limit=20`
- SQL: `WHERE id > cursor_id`
- Base64-encoded cursor encoding/decoding

**3. Keyset pagination** (for sorted by multiple fields):
- Complex multi-column keyset

For each: SQL query, API response shape, frontend usage, and when to use it.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
