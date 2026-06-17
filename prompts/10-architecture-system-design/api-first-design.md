---
title: "Design an API-First Architecture"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [api-first, architecture, design, openapi]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design an API-first architecture for my product.

Product: [DESCRIBE]
Consumers: [Web app, Mobile, Third-party developers]

API-first means:
- API spec is written BEFORE implementation
- Frontend and backend develop in parallel against the mock
- API is the product — consumers are first-class citizens

Process:
1. **Domain modeling**: identify resources from business domain
2. **OpenAPI spec**: write complete spec before writing code
3. **Mock server**: generate mock from spec (Prism)
4. **Contract testing**: consumer tests run against spec
5. **Code generation**: generate server stubs from spec
6. **Developer portal**: documentation from spec
7. **SDK generation**: client SDKs from spec
8. **Versioning**: embed versioning strategy in the spec from day 1

Output: starter OpenAPI spec for my domain.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
