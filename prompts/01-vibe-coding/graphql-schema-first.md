---
title: "Design a GraphQL API Schema-First"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [graphql, api, schema, typescript]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
You are a GraphQL expert. Design a GraphQL API for: [YOUR APP].

Schema-first approach:
1. Complete GraphQL SDL schema (all types, queries, mutations, subscriptions)
2. TypeScript codegen config (using GraphQL Code Generator)
3. Resolvers implementation (Node.js + Apollo Server)
4. DataLoader setup for N+1 prevention
5. Authentication/authorization in resolvers
6. Error handling with custom error types
7. Example queries in GraphQL Playground format
8. Performance considerations for each resolver
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
