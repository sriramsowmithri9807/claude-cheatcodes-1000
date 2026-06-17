---
title: "Design an Event-Driven API"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [events, api, kafka, event-sourcing]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design an event-driven API architecture.

My domain: [DESCRIBE]

Event catalog (define all events):
1. Event naming convention: `[domain].[entity].[past-tense-verb]`
2. Event schema with: id, type, source, time, data, correlationId
3. Schema registry: version events, prevent breaking changes
4. Event taxonomy: Domain Events vs Integration Events vs Commands

API patterns:
5. **Event sourcing**: store events, derive state → audit log for free
6. **CQRS**: separate read model (optimized query) from write model (events)
7. **Choreography**: services react to events (no central orchestrator)
8. **Orchestration**: saga pattern for multi-step business processes

Implementation: Kafka or RabbitMQ + Node.js/Python consumers.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
