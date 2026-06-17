---
title: "Debug Feature Flag Problems"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [feature-flags, debugging, configuration]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Debug issues with my feature flag implementation.

Feature flag system: [DESCRIBE HOW FLAGS ARE STORED AND CHECKED]
Problem: [DESCRIBE: flag not applying, wrong users seeing feature, flag causing errors]
Code: [PASTE RELEVANT CODE]

1. Verify flag value: log the raw flag value before the check
2. Check the evaluation logic: is the condition correct?
3. Cache: is an old cached value being used?
4. User targeting: is the user ID/segment correctly identified?
5. Rollout percentage: is the hash function deterministic and correct?
6. Race condition: is the flag checked before it's loaded?
7. Default value: what happens if flag service is down?
8. Testing: how to test a feature behind a flag
9. Rollback: how to immediately disable the flag

Fix my specific feature flag issue.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
