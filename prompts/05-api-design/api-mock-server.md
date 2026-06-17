---
title: "Build a Production-Like Mock Server"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [mock, api, prism, testing]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a comprehensive mock API server for my frontend team.

My API spec: [OPENAPI YAML or description]

Using: Prism (from Stoplight) — generate mock from OpenAPI automatically

1. Serve mock from OpenAPI spec: `prism mock api.yaml`
2. Dynamic examples: not just static examples from spec
3. Validation: validate requests against spec (reject invalid requests)
4. Proxy mode: real requests with recording for future mocks
5. Scenarios: different responses based on request params
6. Stateful mocking: maintain state between requests
7. Docker: run mock server in CI
8. Delay simulation: add realistic latency
9. Error scenarios: force specific error codes
10. Team sharing: host mock server for entire frontend team
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
