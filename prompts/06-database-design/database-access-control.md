---
title: "Implement Database Access Control"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [security, postgresql, rbac, access-control]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement principle-of-least-privilege access control for my PostgreSQL database.

Roles needed: [e.g., API service, analytics, admin, migration runner]

Implement:
1. **Roles hierarchy**: base roles inherited by specific roles
2. **GRANT syntax**: table-level, column-level, row-level
3. **Row Level Security (RLS)**: policies per role per table
4. **Schema permissions**: USAGE, CREATE
5. **Function SECURITY DEFINER**: run elevated for specific operations
6. **Connection limits per role**
7. **Audit logging**: log every query from admin role
8. **Network restriction**: pg_hba.conf IP allowlist per role
9. **Password rotation**: procedure without downtime
10. **Application user**: never connect as postgres superuser

Output: complete role setup SQL + documentation.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
