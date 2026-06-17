---
title: "Design Database Architecture for Scale"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [database, architecture, postgresql, scalability]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a database architecture that can scale to [SCALE TARGET].

Current: [DESCRIBE CURRENT SETUP]
Data characteristics: [SIZE, GROWTH RATE, READ/WRITE RATIO]

Architecture layers:
1. **Write path**: primary PostgreSQL with auto-failover (Patroni)
2. **Read path**: read replicas with connection routing
3. **Caching layer**: Redis for hot data (> 99% cache hit target)
4. **Search**: Elasticsearch for full-text
5. **Analytics**: ClickHouse or Redshift for OLAP
6. **Time-series**: TimescaleDB for metrics
7. **Queueing**: PostgreSQL as queue (SKIP LOCKED) vs Redis vs Kafka
8. **Archive**: move old data to S3 (Parquet format)

Draw the data flow for the 5 most common operations in my system.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
