---
title: "Generate Realistic Database Seed Data"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [seed, testing, faker, postgresql]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Generate realistic seed data for my database.

Schema: [PASTE YOUR SCHEMA]

Requirements:
- [N] users with diverse realistic names (international)
- [N] records for each main entity
- Realistic relationships (users have 1-5 posts, etc.)
- Edge cases: empty strings where nullable, max length strings, special characters
- Different status distributions: 80% active, 15% inactive, 5% suspended

Output:
1. SQL INSERT statements for base seed data
2. Node.js script using Faker.js for generating larger datasets
3. Python script alternative
4. Specific edge case records to always include in seeds
5. Instructions for: fresh seed (delete + reseed) vs additive seed
6. CI seed: fast minimal seed for test suite
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
