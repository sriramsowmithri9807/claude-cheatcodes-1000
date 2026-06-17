---
title: "Design API Pagination"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [pagination, api, rest, design]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Design comprehensive pagination for my API.

Resources to paginate: [LIST]
Expected scale: [e.g., millions of records]

Implement all patterns:
1. **Offset pagination**: ?page=2&per_page=20 → simple, has limitations
2. **Cursor pagination**: ?cursor=xxx&limit=20 → scalable, consistent
3. **Keyset pagination**: ?after_id=xxx&after_created_at=xxx → for sorted multi-col
4. **Seek pagination**: combining cursor + filters

For each:
- SQL/query implementation
- Response envelope shape (data, meta, links)
- Total count: when to include, when to skip (expensive)
- Frontend integration example
- Performance characteristics

Recommendation for my specific use case.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
