---
title: "Learn System Design"
category: student-learning
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [system-design, learning, architecture, fundamentals]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Teach me system design concepts.

My level: [BEGINNER / INTERMEDIATE]
Learning goal: [DESCRIBE: interview prep, actual system to design, general knowledge]

Core concepts to learn:

**Scalability**:
1. Horizontal vs vertical scaling
2. Load balancing: algorithms and types
3. CDN: what it does and when to use it
4. Caching: layers, strategies, invalidation

**Databases**:
5. SQL vs NoSQL: when to use each
6. Sharding and replication
7. CAP theorem: consistency, availability, partition tolerance

**Communication**:
8. Synchronous vs asynchronous
9. REST vs message queues
10. WebSockets vs polling

**Reliability**:
11. Single point of failure
12. Circuit breaker pattern
13. Rate limiting

For each concept:
- Simple explanation with analogy
- When it's used in real systems
- Trade-offs

Then: walk me through designing [SIMPLE SYSTEM].
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
