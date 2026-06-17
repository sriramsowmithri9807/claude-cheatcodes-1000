---
title: "Design an Event-Driven Architecture"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [event-driven, kafka, architecture, messaging]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design an event-driven architecture for my system.

System: [DESCRIBE YOUR CURRENT/DESIRED SYSTEM]
Problems to solve: [DESCRIBE: tight coupling, synchronous chains, real-time features]

1. **Event catalog**: all domain events with schemas
2. **Message broker**: Kafka vs RabbitMQ vs SQS — which and why
3. **Producer**: how services publish events
4. **Consumer**: how services subscribe and process
5. **Consumer groups**: parallel processing, partition assignment
6. **At-least-once delivery**: handle duplicate messages
7. **Dead letter queue**: failed messages, retry policy
8. **Schema registry**: versioned Avro/Protobuf schemas
9. **Saga pattern**: distributed transactions via events
10. **Observability**: distributed tracing across events
11. **Ordering**: when you need ordered processing
12. **Replay**: reprocess historical events

Diagram the event flow.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
