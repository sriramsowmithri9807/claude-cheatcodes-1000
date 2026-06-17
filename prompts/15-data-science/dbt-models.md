---
title: "Build dbt Data Models"
category: data-science
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [dbt, analytics, sql, data-warehouse]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build dbt data models for my analytics.

Raw sources: [DESCRIBE YOUR RAW TABLES]
Analytics questions: [DESCRIBE WHAT STAKEHOLDERS NEED]

dbt project structure:
```
models/
  staging/        # 1:1 with source, light cleaning
    stg_users.sql
    stg_orders.sql
  intermediate/   # Business logic
    int_user_orders.sql
  marts/          # Final tables for BI
    dim_users.sql
    fct_orders.sql
```

Best practices:
1. Staging models: rename columns, cast types, no joins
2. Intermediate: join, filter, basic aggregations
3. Mart models: wide tables ready for BI (metrics pre-computed)
4. `ref()`: always reference other models with ref()
5. `source()`: reference raw tables with source()
6. Tests: not_null, unique, accepted_values, relationships
7. Documentation: description for every model and column
8. Macros: reusable SQL snippets

Output: complete dbt project for my use case.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
