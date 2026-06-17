---
title: "Create a Data Dictionary"
category: documentation
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [data-dictionary, documentation, database, data]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Create a comprehensive data dictionary.

Database/System: [DESCRIBE]
Audience: [DATA ANALYSTS / ENGINEERS / PRODUCT MANAGERS]

Data dictionary format:

**Table/Collection: [NAME]**
| Column | Type | Nullable | Description | Example | Notes |
|---|---|---|---|---|---|
| id | UUID | No | Unique identifier | `550e8400-...` | Auto-generated |
| created_at | TIMESTAMPTZ | No | When record was created | `2024-01-15T10:30:00Z` | UTC always |
| status | VARCHAR(20) | No | Current status | `active` | Enum: active, inactive, deleted |

**Relationships**: what this table connects to
**Business rules**: constraints beyond the schema
**Common queries**: typical access patterns
**Owner**: team that owns this data

Create data dictionary for all tables in my system.
Format as Markdown suitable for a team wiki.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
