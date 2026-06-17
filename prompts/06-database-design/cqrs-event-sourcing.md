---
title: "Implement CQRS and Event Sourcing"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [cqrs, event-sourcing, architecture, postgresql]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement CQRS and Event Sourcing for: [YOUR DOMAIN].

**Event Sourcing**:
1. Events table: id, aggregate_type, aggregate_id, event_type, data, created_at
2. Append-only: never update events
3. Reconstruct state: replay all events for an aggregate
4. Snapshot: save state at N events to speed up reconstruction
5. Event versioning: how to handle schema changes in old events

**CQRS**:
6. Command side: validate → apply → persist events
7. Query side: materialized read models (denormalized for query speed)
8. Projections: event handlers that build read models
9. Eventual consistency: read side may lag behind write side
10. Sagas: multi-step processes with compensation

Node.js + PostgreSQL implementation.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
