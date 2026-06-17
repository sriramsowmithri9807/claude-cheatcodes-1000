---
title: "Model Data in Redis"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [redis, data-modeling, nosql, caching]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Model and store this data efficiently in Redis:

Data: [DESCRIBE YOUR DATA]
Access patterns: [DESCRIBE HOW YOU QUERY IT]

Redis data structures:
1. **String**: simple key-value, counters, cached JSON
2. **Hash**: user objects, settings (field-level access)
3. **List**: queues, recent items, activity feeds
4. **Set**: unique values, tags, set operations (union/intersect/diff)
5. **Sorted Set**: leaderboards, scheduled tasks, range queries
6. **Stream**: append-only log, event sourcing, message queue
7. **HyperLogLog**: approximate unique count (< 1% error, constant memory)
8. **Bloom Filter**: membership test without false negatives
9. **Geo**: store and query locations, find nearby
10. **JSON** (RedisJSON): store/query JSON documents

Key naming conventions + TTL strategy for each.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
