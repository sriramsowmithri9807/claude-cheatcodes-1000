---
title: "Review a Database Schema"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [schema, review, postgresql, design]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Review this database schema and identify all issues:

[PASTE YOUR SCHEMA]

Analyze:
1. **Normalization**: identify violations and how to fix them
2. **Data types**: wrong types (e.g., storing numbers as VARCHAR)
3. **Missing constraints**: NOT NULL, UNIQUE, CHECK, FK
4. **Missing indexes**: obvious lookup columns without index
5. **Naming**: inconsistent conventions
6. **Performance**: potential N+1, missing composite indexes
7. **Security**: sensitive data without encryption markers
8. **Scalability**: design issues that won't scale to 10x data
9. **Redundancy**: data stored in multiple places
10. **Audit trail**: missing created_at/updated_at

For each issue: severity + explanation + SQL to fix.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
