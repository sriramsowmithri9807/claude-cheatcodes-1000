---
title: "Apply Domain-Driven Design"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [ddd, architecture, domain, patterns]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Apply Domain-Driven Design (DDD) to my project.

Business domain: [DESCRIBE YOUR BUSINESS DOMAIN]

1. **Ubiquitous language**: define key terms that business and tech agree on
2. **Domain model**: identify entities, value objects, aggregates
3. **Bounded contexts**: where does one model's language apply?
4. **Context map**: how bounded contexts relate (shared kernel, anti-corruption layer, etc.)
5. **Aggregate boundaries**: what belongs together? What consistency boundary?
6. **Domain services**: logic that doesn't fit in an entity
7. **Repositories**: abstract storage, return aggregates
8. **Domain events**: things that happen in the domain
9. **Application layer**: orchestrates domain objects
10. **Infrastructure layer**: implements repository interfaces

Diagram the context map and one fully designed aggregate.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
