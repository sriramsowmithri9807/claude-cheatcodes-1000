---
title: "Build a Point of Sale System"
category: fullstack-projects
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [pos, retail, stripe, fullstack]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a Point of Sale (POS) system for a retail store.

Stack: React + Node.js + PostgreSQL + Stripe Terminal

Features:
1. Product lookup: barcode scan or search by name
2. Cart: add items, quantity, discounts, remove
3. Payment: card via Stripe Terminal, cash, split payment
4. Receipt: print (ESC/POS) or email
5. Refunds: partial or full, back to payment method
6. Customer: create/find customer account, loyalty points
7. End-of-day report: sales summary, by payment method
8. Inventory sync: sales auto-decrement stock
9. Offline mode: queue sales when internet drops, sync when reconnected
10. Multi-register: multiple terminals in same store
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
