---
title: "Database Design Patterns"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [patterns, postgresql, design, modeling]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Apply these database design patterns to my schema: [DESCRIBE YOUR DOMAIN].

1. **Polymorphic associations**: entity belongs to multiple parent types
2. **EAV (Entity-Attribute-Value)**: flexible attributes (use sparingly)
3. **Adjacency list**: self-referential (parent_id) for trees
4. **Nested sets**: faster tree traversal, harder updates
5. **Closure table**: best tree reads + writes
6. **Soft delete**: deleted_at timestamp (and how to index correctly)
7. **Audit log**: who changed what and when (shadow table pattern)
8. **Optimistic locking**: version column for concurrent update detection
9. **UUID vs integer primary keys**: tradeoffs
10. **Composite primary keys**: when to use, when to avoid
11. **Bridge table**: many-to-many with extra attributes
12. **Materialized path**: store full path as string for hierarchy
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
