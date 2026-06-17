---
title: "Apply Scalability Patterns"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [scalability, patterns, architecture, high-availability]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Apply scalability patterns to my application architecture.

Current architecture: [DESCRIBE]
Scale target: [e.g., 10M users, 100K RPS, 1PB data]

Horizontal scaling patterns:
1. **Load balancing**: distribute across multiple instances
2. **Stateless services**: sessions in Redis, not server memory
3. **Read replicas**: distribute read queries
4. **Database sharding**: partition data
5. **Caching**: L1 (process), L2 (Redis), L3 (CDN)

Vertical scaling patterns:
6. **Connection pooling**: handle more connections
7. **Async processing**: queue slow work
8. **CDN**: offload static content
9. **Microservices**: scale hot components independently
10. **Data tiering**: hot data in Redis, warm in RDS, cold in S3

For my system: which to apply first (biggest impact for least work).
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
