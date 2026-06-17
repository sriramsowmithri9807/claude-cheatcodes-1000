---
title: "Design a MongoDB Schema"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [mongodb, nosql, schema, document]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Design an optimal MongoDB schema for: [YOUR APPLICATION].

Decisions to make:
1. **Embed vs Reference**: when to embed documents vs use references (show examples)
2. **One-to-one**: how to model (embed in most cases)
3. **One-to-many**: embed array vs separate collection — decide based on cardinality
4. **Many-to-many**: junction document pattern vs array of IDs
5. **Polymorphism**: different document shapes in one collection
6. **Bucket pattern**: time-series data optimization
7. **Outlier pattern**: handle exceptional large documents
8. **Indexes**: compound, text, geo, sparse, partial
9. **Aggregation pipeline**: for your main queries
10. **Transactions**: when MongoDB transactions are needed

SQL vs MongoDB decision: justify the choice for this use case.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
