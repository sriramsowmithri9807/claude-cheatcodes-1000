---
title: "Generate a Database Schema from Requirements"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [schema, postgresql, requirements, design]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Generate a database schema from these business requirements:

[PASTE YOUR BUSINESS REQUIREMENTS DOCUMENT]

Process:
1. **Noun extraction**: identify entities from requirements
2. **Relationship identification**: one-to-many, many-to-many
3. **Attribute mapping**: business terms → database columns + types
4. **Business rules → constraints**: required fields, valid values, uniqueness
5. **Decisions log**: document every non-obvious choice

Output:
- Mermaid ER diagram
- PostgreSQL CREATE TABLE statements (production-quality)
- Indexes
- Sample seed data
- List of assumptions made (for stakeholder review)
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
