---
title: "GraphQL Schema Design Masterclass"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [graphql, schema, api]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a GraphQL schema for [YOUR DOMAIN].

Principles to apply:
1. Think in graphs, not endpoints
2. Nullable vs non-nullable fields — when to use each
3. Input types for mutations
4. Connection pattern for pagination (edges, nodes, pageInfo)
5. Interface and Union types for polymorphism
6. Enum types for fixed values
7. Custom scalars (Date, URL, JSON, Money)
8. Subscription types for real-time
9. Directives: @deprecated, @auth, @cacheControl
10. Schema stitching vs federation for distributed systems

Output: complete SDL schema + example queries for each type.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
