---
title: "Set Up GraphQL Federation"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [graphql, federation, microservices, apollo]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Set up Apollo GraphQL Federation for my microservices.

Services:
- [Service 1]: owns [ENTITIES]
- [Service 2]: owns [ENTITIES]
- [Service 3]: owns [ENTITIES]

Implement:
1. Gateway: Apollo Router or Apollo Server Gateway
2. Subgraph setup for each service
3. Entity definition: @key directive on shared types
4. Reference resolver: resolve entities from other subgraphs
5. Extend types across subgraphs
6. Federated subscriptions
7. Auth: propagate token from gateway to subgraphs
8. Performance: query planning and batching
9. Supergraph schema composition
10. Schema checks: validate before deploying

With Docker Compose for local development.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
