---
title: "Generate Realistic Fake Data for Your App"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [testing, mock-data, faker, seed]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Generate realistic seed data for my app. Here's the data schema:

[PASTE YOUR DATABASE SCHEMA OR TYPESCRIPT TYPES]

Produce:
1. 20 realistic, diverse sample records (not just "John Doe" and "test@test.com")
2. A JavaScript/TypeScript seed file using this data
3. A Faker.js script that can generate unlimited records following these patterns
4. Edge cases to test: empty fields, long strings, special characters, international names/addresses

Make the fake data feel real — realistic names from diverse cultures, real-looking addresses, plausible dates.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
