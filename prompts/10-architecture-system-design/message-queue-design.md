---
title: "Design a Message Queue Architecture"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [message-queue, kafka, rabbitmq, architecture]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a message queue architecture for my distributed system.

Messages/events to handle: [DESCRIBE YOUR MESSAGE TYPES]
Volume: [MESSAGES PER SECOND]
Consumers: [LIST SERVICES THAT CONSUME MESSAGES]

Broker selection:
- RabbitMQ: complex routing, acknowledgment, smaller scale
- Kafka: high throughput, replay, stream processing
- SQS: AWS-native, simple, at-least-once
- Redis Streams: low latency, simple, no replay

For my use case: which broker?

Design:
1. Queue/topic structure and naming
2. Message schema (Avro/Protobuf/JSON)
3. Routing rules
4. Consumer group setup
5. Error handling: DLQ, retry policy
6. Ordering guarantees (where needed)
7. Scalability: partition count, consumer instances
8. Monitoring: queue depth, consumer lag
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
