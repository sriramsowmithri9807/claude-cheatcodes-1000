---
title: "Choose the Right NoSQL Database"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [nosql, dynamodb, mongodb, cassandra]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Help me choose the right NoSQL database for: [DESCRIBE YOUR USE CASE, ACCESS PATTERNS, SCALE].

Evaluate:
1. **MongoDB**: document store, flexible schema, good for catalogs, CMS
2. **DynamoDB**: AWS managed, single-digit ms at any scale, limited query patterns
3. **Cassandra**: write-heavy, time-series, geographic distribution
4. **Redis**: in-memory, caching, real-time, pub/sub
5. **Elasticsearch**: full-text search, log analytics
6. **InfluxDB**: time-series metrics
7. **Neo4j**: graph relationships
8. **CockroachDB**: distributed SQL (PostgreSQL compatible)

For my specific access patterns and scale:
- Winner and justification
- Data model for the winning DB
- Failure modes to plan for
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
