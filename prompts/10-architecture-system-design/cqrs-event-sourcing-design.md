---
title: "Design CQRS and Event Sourcing Architecture"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [cqrs, event-sourcing, ddd, architecture]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a CQRS/Event Sourcing architecture for: [YOUR DOMAIN].

Why CQRS/ES fits this problem: [DESCRIBE]

Design:
1. **Commands**: operations that change state
   - Define all commands with their payloads
   - Validation rules per command
   - Command handlers
2. **Events**: facts that happened
   - Define all domain events (past tense)
   - Event schema + versioning strategy
   - Event store: append-only table design
3. **Aggregates**: enforce business invariants
   - Reconstruct from events
   - Snapshot strategy
4. **Read models / Projections**: optimized for query
   - Which projections do you need?
   - How to build and rebuild them
5. **Sagas / Process managers**: multi-aggregate workflows
6. **Technology stack**: EventStoreDB / PostgreSQL / Kafka

Fulldomain model with examples.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
