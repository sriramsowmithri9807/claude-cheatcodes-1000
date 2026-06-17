---
title: "Choose Between Microservices and Monolith"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [microservices, monolith, architecture, decision]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Help me decide between microservices and a monolith for my project.

Project: [DESCRIBE YOUR PROJECT]
Team size: [N engineers]
Timeline: [LAUNCH DATE]
Expected scale: [USERS, RPS]

Monolith advantages:
- Faster to build and deploy
- Easier to debug and test
- Single codebase
- No distributed system complexity
- Right for small teams and early stage

Microservices advantages:
- Independent deployments
- Technology diversity
- Team autonomy
- Targeted scaling
- Right for large teams and complex domains

For MY project:
1. Which is the right starting point?
2. If monolith: how to structure it to split later ("modular monolith")
3. If microservices: which services and how to define boundaries (DDD)
4. Migration path: start monolith → extract services over time
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
