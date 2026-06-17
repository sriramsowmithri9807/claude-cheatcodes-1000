---
title: "Write a User Guide"
category: documentation
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [user-guide, documentation, end-users, help]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Write a comprehensive user guide for my product.

Product: [DESCRIBE WHAT YOUR PRODUCT DOES]
Users: [DESCRIBE YOUR TYPICAL USER'S TECHNICAL LEVEL]

User guide structure:
1. **Introduction**: what this product does and who it's for
2. **Getting started**: set up + first action in 5 steps
3. **Core concepts**: key terms and concepts explained
4. **Feature guides**: one section per major feature
   - What it does
   - When to use it
   - Step-by-step instructions with screenshots
   - Common questions
5. **Troubleshooting**: top 10 issues + solutions
6. **FAQ**: answers to frequently asked questions
7. **Glossary**: define product-specific terms
8. **Index**: searchable list of topics

Writing style:
- Second person ('you')
- Numbered steps for procedures
- Screenshots for complex UI steps
- Warning boxes for destructive actions

Output: complete user guide.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
