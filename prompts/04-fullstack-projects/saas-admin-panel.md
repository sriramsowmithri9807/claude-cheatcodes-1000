---
title: "Build a SaaS Admin Panel"
category: fullstack-projects
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [admin, saas, fullstack, dashboard]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a complete admin panel for a SaaS application.

Stack: React + Node.js + PostgreSQL

Sections:
1. **Dashboard**: total users, MRR, churn, signups this month, active now
2. **Users**: search, filter by plan, view profile, impersonate, ban, delete
3. **Subscriptions**: all subs, by plan, revenue per plan, churned subs
4. **Feature flags**: enable/disable features per user or globally
5. **Announcements**: send in-app banner to all users
6. **Email campaigns**: send one-off email to user segments
7. **Audit log**: all admin actions logged
8. **Database explorer**: safe read-only SQL queries
9. **API keys**: view all API keys, revoke
10. **System health**: uptime, queue depth, error rate

Secure: admin-only routes with 2FA requirement.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
