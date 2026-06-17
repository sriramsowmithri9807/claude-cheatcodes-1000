---
title: "Mock External APIs for Development and Testing"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [mocking, msw, testing, api]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Set up comprehensive API mocking for development and testing.

External APIs I use: [LIST THIRD-PARTY APIS]

Using: Mock Service Worker (MSW)

1. Handler setup: intercept matching requests
2. Realistic mock data using Faker.js
3. Simulated network delay and errors
4. Conditional responses: different responses based on request body
5. Stateful mocks: cart that accumulates items
6. Passthrough: let some requests hit real API
7. Browser vs Node.js setup
8. Integration with React Testing Library
9. Integration with Vitest
10. Toggle mocks with environment variable

Also: WireMock for Java, nock for Node.js, VCR for Ruby — comparison.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
