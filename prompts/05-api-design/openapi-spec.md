---
title: "Write a Complete OpenAPI 3.1 Spec"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [openapi, swagger, api, documentation]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Write a complete OpenAPI 3.1 specification for my API:

[DESCRIBE YOUR API: purpose, main resources, auth method]

Include:
1. `info` block with description and contact
2. `servers` for development and production
3. `securitySchemes` for your auth method
4. All `paths` with every operation
5. Request bodies with inline examples
6. Response schemas for 200, 400, 401, 403, 404, 422, 500
7. Reusable `components/schemas` (avoid repetition)
8. Reusable `components/responses` for common errors
9. Reusable `components/parameters`
10. Webhook definitions (if applicable)

Output: valid YAML, importable into Postman or Swagger UI.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
