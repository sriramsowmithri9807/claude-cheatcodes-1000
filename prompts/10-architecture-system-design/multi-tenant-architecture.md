---
title: "Design a Multi-Tenant SaaS Architecture"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [multi-tenant, saas, architecture, isolation]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design the architecture for a multi-tenant SaaS platform.

Expected tenants: [SCALE: 10 / 100 / 10,000]
Compliance needs: [GDPR / HIPAA / SOC2]
Tenant size range: [SMALL SMB / LARGE ENTERPRISE]

Isolation model selection:
1. **Shared everything**: all tenants in one DB, filtered by tenant_id
2. **Schema per tenant**: own PostgreSQL schema
3. **Database per tenant**: ultimate isolation (enterprise)
4. **Hybrid**: small tenants shared, large tenants isolated

For my scale and compliance: which model?

Implement:
5. Tenant resolution (subdomain, header, path)
6. Data isolation (RLS policies or separate DBs)
7. Configuration per tenant (feature flags, limits)
8. Billing per tenant (usage-based pricing)
9. Data export per tenant (GDPR right to data)
10. Tenant onboarding automation
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
