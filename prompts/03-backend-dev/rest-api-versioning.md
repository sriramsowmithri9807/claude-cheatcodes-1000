---
title: "Implement REST API Versioning"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [rest, versioning, api, backend]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement API versioning strategy for my REST API.

Current API: [DESCRIBE]
Breaking changes needed: [LIST WHAT'S CHANGING]

Implement URL versioning (/api/v1/, /api/v2/):
1. Router setup for multiple versions
2. Shared code between versions (don't duplicate business logic)
3. Request coercion: V1 request → V2 handler → V1 response
4. Version deprecation headers
5. Sunset date announcement
6. Migration guide documentation
7. Maintaining tests for all active versions

Also explain: URL vs header vs query param versioning — why URL wins for most APIs.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
