---
title: "Design Database Sharding"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [sharding, postgresql, scalability, architecture]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a database sharding strategy for my application at scale.

Current situation: [DESCRIBE: single PostgreSQL, projected 100M+ rows, growth rate]

Sharding key selection:
1. User ID sharding: route all user data to same shard
2. Tenant ID: for multi-tenant SaaS
3. Date range: for time-series data
4. Hash-based: even distribution

Implement:
5. Consistent hashing for shard routing
6. Application-level sharding (vs Citus)
7. Cross-shard queries: how to handle joins
8. Shard rebalancing when adding shards
9. Hot spots: how to detect and fix
10. Citus (PostgreSQL extension): managed sharding

Alternative: vertical scaling + read replicas first (defer sharding as long as possible).
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
