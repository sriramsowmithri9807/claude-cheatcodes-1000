---
title: "Master Database Transactions"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [transactions, postgresql, acid, concurrency]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Master transactions and concurrency control in PostgreSQL.

My use case: [DESCRIBE CONCURRENT OPERATIONS]

1. **ACID properties**: what each means in practice with examples
2. **Isolation levels**:
   - READ COMMITTED (default): what can go wrong
   - REPEATABLE READ: solves phantom reads
   - SERIALIZABLE: highest isolation, performance cost
3. **Phenomena**: dirty read, non-repeatable read, phantom read, serialization anomaly
4. **Optimistic locking**: version column + WHERE version = N
5. **Pessimistic locking**: SELECT FOR UPDATE, SKIP LOCKED
6. **SKIP LOCKED**: job queue pattern
7. **Deadlocks**: how to detect, how to prevent (consistent lock ordering)
8. **Long transactions**: why they're dangerous, how to avoid
9. **Advisory locks**: application-level locks in PostgreSQL
10. **Two-phase commit**: distributed transactions
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
