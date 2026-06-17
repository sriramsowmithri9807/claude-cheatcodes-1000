---
title: "Design API Composition Layer"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [api, composition, bff, graphql]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design an API composition layer for my distributed system.

Downstream services: [LIST YOUR MICROSERVICES AND WHAT THEY PROVIDE]
Clients: [WEB APP, MOBILE APP, PARTNER API]

Composition strategies:
1. **BFF (Backend for Frontend)**: dedicated API per client type
2. **GraphQL**: unified graph over multiple services
3. **API Gateway + aggregation**: gateway composes multiple upstream calls

For my system:
4. Which composition strategy (or hybrid)?
5. How to aggregate data from Service A + Service B into one response
6. How to handle failures (partial response when one service fails)
7. Distributed transactions across services
8. Auth token propagation
9. Response caching at composition layer
10. Observability: trace composition calls end-to-end
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
