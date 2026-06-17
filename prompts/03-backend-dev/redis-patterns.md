---
title: "Master Redis Patterns for Backend"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [redis, caching, patterns, backend]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement these Redis patterns in my Node.js application:

1. **Session storage**: store and retrieve user sessions
2. **Distributed lock**: prevent race conditions across instances
3. **Rate limiting**: sliding window counter per user/IP
4. **Pub/Sub**: broadcast events to WebSocket servers
5. **Job queue**: simple queue without BullMQ
6. **Leaderboard**: sorted sets for real-time rankings
7. **Autocomplete**: sorted sets for prefix search
8. **Geospatial**: store locations, query nearby
9. **Bloom filter**: check membership without storing all data
10. **Cache with automatic refresh**: lazy loading pattern

Each pattern: Node.js code (ioredis), key naming, TTL strategy, when to use.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
