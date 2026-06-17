---
title: "Implement API Contract Testing"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [contract-testing, pact, testing, api]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement consumer-driven contract testing for my API ecosystem.

Provider: [YOUR API SERVICE]
Consumers: [FRONTEND APP, MOBILE APP, THIRD-PARTY SERVICE]

Using: Pact (consumer-driven contract testing)

1. Consumer writes a contract: "I expect this request to return this response shape"
2. Contract published to Pact Broker
3. Provider verifies against the contract in CI
4. If contract breaks, CI fails — immediate feedback

Implement:
- Consumer contract test (JavaScript/TypeScript)
- Provider verification (Node.js)
- Pact Broker setup (Docker)
- CI integration (GitHub Actions)
- Versioning contracts with semantic versioning
- "Can I Deploy" check before production deploy
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
