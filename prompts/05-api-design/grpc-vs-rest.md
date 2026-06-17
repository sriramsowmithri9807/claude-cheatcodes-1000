---
title: "Choose Between gRPC, REST, and GraphQL"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [grpc, rest, graphql, architecture]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Help me choose the right API style for my use case: [DESCRIBE YOUR SYSTEM: services, clients, requirements].

Provide a rigorous comparison:

| Criteria | REST | GraphQL | gRPC |
|---|---|---|---|
| Performance | | | |
| Type safety | | | |
| Browser support | | | |
| Tooling | | | |
| Learning curve | | | |
| Caching | | | |
| Schema evolution | | | |

For MY use case specifically:
- Recommendation with justification
- Where each would fail
- Hybrid approach (if applicable)
- Implementation starter for the recommended option
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
