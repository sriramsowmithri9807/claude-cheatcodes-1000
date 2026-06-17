---
title: "Write Integration Tests"
category: testing-qa
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [testing, integration, supertest, database]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Write integration tests for my API.

API routes to test: [LIST YOUR ENDPOINTS]
Stack: Express.js + PostgreSQL + Redis

Setup:
1. Test database: isolated test DB, reset between test suites
2. Test server: start Express app with test config
3. Supertest: HTTP requests in tests
4. Mock external services: email, payment, third-party APIs

Test patterns:
5. **Auth flows**: register → login → access protected route
6. **CRUD flows**: create → read → update → delete
7. **Error flows**: invalid input, unauthorized, not found
8. **Business rules**: ensure business rules are enforced
9. **Pagination**: test page boundaries
10. **Concurrent requests**: test race condition protection

Database strategy: transactions that rollback after each test (or Docker Postgres per test run).
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
