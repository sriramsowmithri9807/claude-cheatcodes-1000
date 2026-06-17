---
title: "Define Internal API Standards"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [api, standards, team, documentation]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Create internal API standards for my engineering team.

Team size: [N engineers], building [N microservices]

Standards document covering:
1. **URL conventions**: naming, nesting, parameter formats
2. **HTTP method semantics**: team agreement on GET/POST/PUT/PATCH/DELETE
3. **Status codes**: company-wide lookup table
4. **Error format**: mandatory fields, optional fields
5. **Auth method**: which auth per use case
6. **Pagination**: single standard (cursor-based)
7. **Date format**: ISO 8601 everywhere, always UTC
8. **Naming**: camelCase JSON fields, English only
9. **Versioning**: when and how to version
10. **Documentation**: what must be documented before shipping

Output: API Standards v1.0 document for team adoption.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
