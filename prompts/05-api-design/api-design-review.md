---
title: "Conduct an API Design Review"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [api, design-review, best-practices, team]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Conduct a thorough API design review for this proposed API:

[PASTE YOUR PROPOSED API DESIGN]

Review checklist:
□ Resource naming follows conventions
□ HTTP methods are semantically correct
□ Status codes are appropriate
□ Error responses are consistent
□ Pagination is implemented correctly
□ Auth is secure and consistent
□ Rate limiting is planned
□ Versioning strategy is defined
□ Breaking changes are identified
□ Documentation is planned
□ Security: no sensitive data in URLs
□ CORS is properly configured
□ Backwards compatibility is maintained
□ Performance: no N+1 in response shapes
□ Idempotency on critical operations

For each failing item: why it fails and how to fix it.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
