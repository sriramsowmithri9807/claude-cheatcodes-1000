---
title: "Write Comprehensive API Tests"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [testing, supertest, jest, api]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Write comprehensive tests for my REST API.

API to test: [DESCRIBE YOUR API ROUTES]
Framework: Express.js or Fastify

Using: Vitest + Supertest + MSW

Test patterns:
1. Happy path: successful responses
2. Validation errors: missing fields, wrong types
3. Authentication: missing token, expired token, wrong role
4. Authorization: user can't access other user's data
5. Edge cases: empty arrays, max length strings, special characters
6. Database errors: simulate DB failure
7. Rate limiting: test limit is enforced

Test setup:
- In-memory SQLite for tests (or test DB with transactions)
- Factory functions for test data
- Shared test server setup
- Coverage: target 80%+
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
