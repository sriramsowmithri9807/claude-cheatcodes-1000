---
title: "Master PostgreSQL JSONB"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [postgresql, jsonb, nosql, querying]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Master JSONB in PostgreSQL for flexible schema storage.

My use case: [DESCRIBE WHAT YOU'RE STORING AS JSON]

1. **JSONB vs JSON**: always use JSONB (binary, indexed)
2. **Operators**: `->`, `->>`, `#>`, `#>>`, `@>`, `<@`, `?`, `?|`, `?&`
3. **Indexing**: GIN index (full doc), jsonb_path_ops for `@>`, expression index for specific keys
4. **Functions**: jsonb_set, jsonb_insert, jsonb_strip_nulls, jsonb_object_keys
5. **Path operations**: jsonb_path_query (JSONPath)
6. **Aggregation**: jsonb_agg, jsonb_object_agg
7. **Schema validation**: CHECK constraint with custom function
8. **Updating nested keys**: jsonb_set deep update
9. **Performance**: when JSONB is fast and when it slows you down
10. **Migration pattern**: relational → JSONB → relational again

For each: working SQL examples with my use case.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
