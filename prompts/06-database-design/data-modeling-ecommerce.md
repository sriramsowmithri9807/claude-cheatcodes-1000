---
title: "Data Model an E-Commerce System"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [ecommerce, data-modeling, postgresql, schema]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Design the complete data model for an e-commerce system.

Requirements:
- Products with variants (size, color, material combinations)
- Inventory tracking per variant per warehouse
- Orders with line items, taxes, discounts, shipping
- Customer management with addresses
- Pricing: MSRP, sale price, customer-tier pricing
- Reviews and ratings
- Category hierarchy (unlimited depth)

Output:
1. Complete ER diagram (Mermaid)
2. CREATE TABLE SQL (PostgreSQL)
3. Key indexes
4. Sample queries for: product listing with price, order total, inventory check
5. The 3 hardest modeling decisions and why you chose as you did
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
