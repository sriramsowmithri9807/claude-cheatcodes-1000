---
title: "Build a GraphQL Server with Apollo"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [graphql, apollo, nodejs, typescript]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a production GraphQL server with Apollo Server 4 + TypeScript.

Domain: [DESCRIBE YOUR DATA DOMAIN]

Schema: write complete SDL for all types, queries, mutations, subscriptions

Implement:
- Code-first approach using TypeGraphQL OR schema-first with graphql-codegen
- Resolvers with proper separation (resolver → service → repository)
- DataLoader for N+1 prevention
- Cursor-based pagination
- Subscription with Redis pub/sub
- Authentication via context
- Authorization with field-level permissions
- Error handling: custom error classes → GraphQL errors
- Rate limiting per field
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
