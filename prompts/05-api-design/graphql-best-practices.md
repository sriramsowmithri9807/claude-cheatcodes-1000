---
title: "GraphQL API Best Practices"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [graphql, best-practices, api, performance]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Apply GraphQL best practices to my schema: [DESCRIBE YOUR SCHEMA].

1. **Schema design**: self-documenting, expressive types
2. **Naming**: consistent conventions (camelCase fields, PascalCase types)
3. **Nullability**: when to use ! — prefer nullable for forward compatibility
4. **Pagination**: Relay connection spec (avoid arrays for paginated data)
5. **Mutations**: one input type per mutation, return the mutated type
6. **Error handling**: errors as data vs GraphQL errors
7. **N+1 prevention**: DataLoader pattern, every resolver uses DataLoader
8. **Depth limiting**: prevent deeply nested queries (denial of service)
9. **Query complexity analysis**: score queries, reject too-complex ones
10. **Persisted queries**: hash-based for production (security + performance)
11. **Field deprecation**: @deprecated with migration notes
12. **Authorization**: never trust client, check auth in every resolver
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
