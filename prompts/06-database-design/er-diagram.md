---
title: "Design a Database Schema"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [postgresql, schema, erd, modeling]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Design a complete database schema for: [YOUR APPLICATION].

Output:
1. Entity-Relationship Diagram (ASCII art or Mermaid)
2. CREATE TABLE SQL for each entity with:
   - Correct data types (prefer specific: UUID, TEXT, TIMESTAMPTZ, NUMERIC, BOOLEAN)
   - NOT NULL constraints where appropriate
   - DEFAULT values
   - CHECK constraints
   - UNIQUE constraints
   - Foreign keys with ON DELETE behavior
3. Indexes (beyond primary key)
4. Rationale for each major design decision
5. Alternative designs considered and why rejected

Normalization target: 3NF unless denormalization is justified.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
