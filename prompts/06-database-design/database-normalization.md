---
title: "Normalize a Database Schema"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [normalization, sql, schema, design]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Normalize this database schema to 3NF (Third Normal Form):

[PASTE YOUR CURRENT SCHEMA — especially if it has JSON columns, repeated data, or one giant table]

Process:
1. **1NF**: eliminate repeating groups, ensure atomic values
2. **2NF**: eliminate partial dependencies (all non-key fields depend on full PK)
3. **3NF**: eliminate transitive dependencies
4. **BCNF**: Boyce-Codd Normal Form if needed

For each step:
- Identify the violation
- The SQL to fix it
- The tradeoffs (normalization vs performance)

Then: **controlled denormalization** — add back specific denormalized columns with justification for query performance.

Output: complete normalized schema + migration from current to normalized.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
