---
title: "Transform API Data Shapes"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [transformation, api, typescript, mapping]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Design a data transformation layer for my API.

Problem: my database models don't match what my API consumers need.

DB model: [DESCRIBE]
API response needed: [DESCRIBE DIFFERENCES]

Implement:
1. Serializer pattern: db_model → api_response
2. Deserializer: api_request → db_model
3. Field renaming: snake_case → camelCase
4. Field filtering: hide internal fields
5. Field addition: compute derived fields
6. Nested objects: embed related models
7. Type coercion: convert timestamps, enums, nulls
8. TypeScript types: end-to-end type safety
9. Versioned serializers: v1 and v2 output from same DB
10. Partial responses: honor `?fields=` param
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
