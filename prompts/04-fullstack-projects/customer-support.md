---
title: "Build a Customer Support Ticketing System"
category: fullstack-projects
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [support, helpdesk, fullstack, email]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a Zendesk-style customer support system.

Stack: Next.js + Node.js + PostgreSQL + SendGrid

Roles: Customer, Agent, Admin

Features:
1. Customers: submit ticket via web form or email
2. Email ingestion: support@company.com → creates ticket automatically
3. Ticket lifecycle: Open → In Progress → Resolved → Closed
4. Assignment: route to agent by category/round-robin
5. Internal notes: agents communicate privately
6. SLA: first response < 4h, resolution < 24h — track and alert
7. CSAT: post-resolution survey
8. Knowledge base: articles that auto-suggest when customer types ticket
9. AI first response: Claude drafts suggested reply for agent review
10. Reporting: ticket volume, response times, CSAT scores
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
