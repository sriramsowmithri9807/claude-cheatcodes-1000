---
title: "Build a Crowdfunding Platform"
category: fullstack-projects
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [crowdfunding, stripe, fullstack, community]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a Kickstarter-style crowdfunding platform.

Stack: Next.js + PostgreSQL + Stripe + Cloudinary

Features:
1. Project creation: title, story (rich text), goal, deadline, rewards
2. Rewards: backer tiers with perks and quantity limits
3. Funding: pledge (Stripe Payment Intent, charged only if goal met)
4. Progress: funding bar, % funded, backers count, days left
5. Comments and updates from creator
6. Backer dashboard: all pledges, downloadable rewards
7. Creator dashboard: funding stats, backer export, send updates
8. Refund: auto-refund if goal not reached by deadline
9. Discovery: categories, trending, ending soon
10. Social: share buttons, embed widget

Stripe hold → capture on success / cancel on failure is the key flow.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
