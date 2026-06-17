---
title: "Write Effective Stored Procedures"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [stored-procedures, postgresql, plpgsql, backend]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Write stored procedures and functions for these complex operations: [DESCRIBE YOUR OPERATIONS].

Using: PostgreSQL PL/pgSQL

1. **Functions vs procedures**: when to use each
2. **SECURITY DEFINER**: run as function owner (for RLS bypass where needed)
3. **Transaction control**: COMMIT/ROLLBACK within procedure
4. **Exception handling**: EXCEPTION block, SQLSTATE codes
5. **Dynamic SQL**: EXECUTE for dynamic queries
6. **Loops and cursors**: FOR loops, cursor fetch
7. **Returning data**: SETOF, TABLE, record types
8. **Triggers**: BEFORE/AFTER, ROW/STATEMENT level
9. **Performance**: inlining optimization, search_path
10. **Testing**: pgTAP for PL/pgSQL unit tests

Alternative: should this logic be in the application layer?
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
