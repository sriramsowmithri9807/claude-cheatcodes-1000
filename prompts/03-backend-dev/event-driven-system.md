---
title: "Build an Event-Driven System"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [event-driven, rabbitmq, kafka, nodejs]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build an event-driven system using message queues for: [DESCRIPTION].

Using: RabbitMQ (or Kafka for higher throughput)

Implement:
1. Publisher: emit events with schema validation
2. Consumer: subscribe with retry logic (dead letter queue)
3. Event schema registry (Avro or JSON Schema)
4. At-least-once delivery guarantee
5. Idempotency keys to handle duplicate messages
6. Saga pattern for distributed transactions
7. Event sourcing: store all events, derive state
8. Node.js implementation with amqplib or kafkajs
9. Docker compose for local development
10. Monitoring: queue depth, consumer lag metrics
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
