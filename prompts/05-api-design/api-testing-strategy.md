---
title: "Design API Testing Strategy"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [testing, api, contract, postman]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Design a comprehensive testing strategy for my API.

API type: [REST / GraphQL] with [N] endpoints

Layers:
1. **Unit tests**: test each service/business logic function in isolation
2. **Integration tests**: test route → controller → service → real DB
3. **Contract tests**: verify API matches OpenAPI spec (Dredd or Spectral)
4. **E2E tests**: test complete user flows via API (Postman collections)
5. **Performance tests**: k6 load test for critical endpoints (target: 1000 RPS)
6. **Security tests**: OWASP ZAP scan, auth bypass attempts
7. **Fuzzing**: send random/malformed inputs to all endpoints

Coverage targets per layer.
CI pipeline: run all layers on each PR.
Output: test strategy document + example tests for each layer.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
