---
title: "Document Your Database Schema"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [documentation, schema, postgresql, data-dictionary]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Generate comprehensive documentation for my database schema.

Schema: [PASTE YOUR SCHEMA]

Document:
1. **Data dictionary**: every table and column with:
   - Purpose of the table
   - Each column: data type, constraints, description, example value
   - Relationships to other tables
2. **ER diagram** (Mermaid)
3. **Query patterns**: common queries and how to run them
4. **Access patterns**: which queries run most frequently
5. **Index documentation**: what each index is for
6. **Stored procedures/triggers**: what they do and when
7. **Naming conventions**: document the conventions used
8. **Change log**: schema change history

Output in Markdown format, suitable for a team wiki.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
