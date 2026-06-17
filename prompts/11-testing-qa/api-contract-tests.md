---
title: "Write API Contract Tests"
category: testing-qa
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [contract-testing, pact, api, testing]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Write consumer-driven contract tests using Pact.

Consumer: [YOUR FRONTEND / SERVICE]
Provider: [YOUR API / MICROSERVICE]

Consumer side:
1. Define interactions: request + expected response shape
2. Pact test: real HTTP calls against Pact mock server
3. Pact file generated: the contract
4. Publish contract to Pact Broker

Provider side:
5. Pull contracts from Pact Broker
6. Run provider verification against real provider
7. Provider test: does the provider fulfill the contract?
8. Publish verification results

**Can I deploy check**:
9. Before deploying consumer: can it talk to this provider version?
10. Before deploying provider: does it satisfy all consumer contracts?

CI integration: GitHub Actions workflow for both sides.
Output: consumer test + provider test + GitHub Actions config.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
