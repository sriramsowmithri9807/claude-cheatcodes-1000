---
title: "Convert User Stories to Working Code"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [agile, user-stories, tdd, features]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Convert these user stories into working code using TDD:

[PASTE USER STORIES IN GIVEN/WHEN/THEN FORMAT]

For each user story:
1. Write the failing test first (Jest)
2. Implement the minimum code to pass the test
3. Refactor for clarity

Tech stack: [YOUR STACK]

Output the complete test file and implementation file. Group tests by user story with `describe` blocks.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
