---
title: "Design API Error Handling"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [error-handling, api, rfc7807, rest]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Design a consistent error handling strategy for my REST API.

Following RFC 7807 Problem Details:
```json
{
  "type": "https://api.example.com/errors/validation-error",
  "title": "Validation Failed",
  "status": 422,
  "detail": "The request body contains invalid data.",
  "instance": "/users/register",
  "errors": [{"field": "email", "message": "Must be a valid email"}]
}
```

Design:
1. Error type registry (all possible error types with URLs)
2. HTTP status code decision tree
3. Validation errors: list all field errors
4. Business logic errors: meaningful codes (INSUFFICIENT_FUNDS, USER_SUSPENDED)
5. Internal errors: never leak stack traces
6. Rate limit errors: include retry timing
7. Client SDK: parse errors into typed exceptions
8. Monitoring: every 5xx triggers an alert
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
