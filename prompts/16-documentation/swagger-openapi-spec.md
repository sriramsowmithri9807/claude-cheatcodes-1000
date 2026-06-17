---
title: "Write a Complete OpenAPI Specification"
category: documentation
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [openapi, swagger, api, documentation]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Write a complete OpenAPI 3.1 specification.

API to document: [DESCRIBE YOUR API]

Complete OpenAPI structure:
```yaml
openapi: 3.1.0
info:
  title: My API
  version: 2.0.0
  description: |
    [DETAILED DESCRIPTION]
  contact:
    email: api@example.com
  license:
    name: MIT

servers:
  - url: https://api.example.com/v2
    description: Production
  - url: https://sandbox.api.example.com/v2
    description: Sandbox

security:
  - BearerAuth: []

components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
  schemas:
    [REUSABLE SCHEMAS]
  responses:
    [REUSABLE RESPONSES]

paths:
  /[EACH ENDPOINT]:
    [OPERATIONS]
```

Include:
- All endpoints with full schemas
- 3+ examples per endpoint
- All error responses
- Authentication documentation
- Webhook definitions
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
