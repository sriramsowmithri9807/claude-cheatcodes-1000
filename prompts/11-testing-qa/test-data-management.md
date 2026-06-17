---
title: "Manage Test Data Effectively"
category: testing-qa
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [test-data, testing, factories, seeding]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Set up effective test data management.

Stack: [NODE.JS / PYTHON] + [DATABASE]

1. **Factory pattern**: create test objects with sensible defaults
2. **Override specific fields**: `createUser({ email: 'custom@test.com' })
3. **Traits**: `createUser('admin')`, `createUser('verified')`
4. **Sequence numbers**: unique IDs, emails, usernames
5. **Relationships**: `createPost({ author: createUser() })`

Database strategy:
6. **Test database**: separate DB for tests
7. **Transactions**: wrap each test in a transaction, rollback
8. **Reset between tests**: DELETE all rows (faster than recreate)
9. **Seed**: minimal seed data that all tests can rely on

Test fixtures:
10. JSON files for complex nested structures
11. Shared fixtures for common scenarios
12. Parameterized tests with multiple data sets

Implement using: fishery (TypeScript) or factory_boy (Python).
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
