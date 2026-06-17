---
title: "Build a CRM System"
category: fullstack-projects
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [crm, nextjs, fullstack, business]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a lightweight CRM for a small sales team.

Stack: Next.js + PostgreSQL + Prisma

Features:
1. **Contacts**: name, company, email, phone, custom fields, tags
2. **Companies**: associated contacts, deals
3. **Deals/Pipeline**: kanban view by stage (Lead → Qualified → Proposal → Won/Lost)
4. **Activities**: log calls, emails, meetings against a contact/deal
5. **Tasks**: follow-up reminders with due dates
6. **Notes**: rich text notes on any record
7. **Email integration**: log emails from Gmail/Outlook
8. **Reports**: win rate, pipeline value, activity by rep
9. **Import**: bulk import from CSV
10. **Team**: assign contacts/deals to sales reps

DB schema + complete API + key UI components.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
