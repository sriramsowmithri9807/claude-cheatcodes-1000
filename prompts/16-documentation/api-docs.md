---
title: "Write API Documentation"
category: documentation
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [api, documentation, openapi, developer-experience]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Write comprehensive API documentation.

API: [DESCRIBE YOUR API]
Audience: [THIRD-PARTY DEVELOPERS]

1. **Overview**: what the API does in 2 sentences
2. **Authentication**: how to get and use API keys/tokens
3. **Base URL**: production and sandbox
4. **Request format**: content-type, encoding
5. **Response format**: envelope structure, status codes
6. **Rate limits**: limits + how to handle 429
7. **Errors**: complete error code reference with solutions
8. **Versioning**: current version, how to upgrade

For each endpoint:
9. Method + path
10. Description of what it does
11. Request parameters (path, query, body) with types and required/optional
12. Request body example (JSON)
13. Response body example
14. Error responses specific to this endpoint
15. Code examples in 3 languages (curl, JavaScript, Python)

Output: complete API documentation in Markdown.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
