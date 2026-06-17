---
title: "Design a Multi-Tenant Database"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [multi-tenant, saas, postgresql, architecture]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a multi-tenant database architecture for my SaaS application.

Tenants: [EXPECTED NUMBER — dozens? thousands?]

Three approaches:

**Option A — Row-level (shared schema)**:
- Add `tenant_id` to every table
- Row Level Security (RLS) to isolate
- Pros: simple, cheap. Cons: noisy neighbor, harder to export tenant data

**Option B — Schema-per-tenant**:
- Each tenant gets own PostgreSQL schema
- Up to ~1000 tenants per DB
- Pros: easy isolation. Cons: complex migrations

**Option C — Database-per-tenant**:
- Ultimate isolation
- Pros: compliance, custom backups. Cons: expensive, complex infra

For MY tenant count and compliance needs: which approach?
Implementation for the recommended approach including migration strategy.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
