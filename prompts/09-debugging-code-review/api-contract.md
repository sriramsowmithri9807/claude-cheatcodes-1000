---
title: "Debug API Contract Mismatches"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [api, contract, debugging, types]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Debug the mismatch between my API response and my frontend/client expectations.

API response (actual):
```json
[PASTE ACTUAL API RESPONSE]
```

Expected by client:
```typescript
[PASTE YOUR TYPESCRIPT INTERFACE OR EXPECTED SHAPE]
```

1. List every mismatch (field name, type, nesting, missing field, extra field)
2. Which side is wrong — API or client?
3. Fix both sides to match
4. Add Zod validation to catch this at runtime
5. Add TypeScript types that match the actual API
6. How to prevent this drift: OpenAPI spec + codegen
7. Write a test that would have caught this mismatch
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
