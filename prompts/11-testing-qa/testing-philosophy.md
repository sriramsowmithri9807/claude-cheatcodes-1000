---
title: "Develop a Testing Philosophy"
category: testing-qa
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [testing, philosophy, strategy, best-practices]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Help me develop a testing philosophy and practical guidelines for my team.

Team: [DESCRIBE TEAM SIZE AND EXPERIENCE LEVEL]
Current state: [DESCRIBE: no tests / some tests / comprehensive tests but slow]

Philosophy principles:
1. **Tests are documentation**: tests show what the code should do
2. **Test behavior, not implementation**: don't test internal private methods
3. **Fast feedback**: unit tests in < 30s, full suite in < 10min
4. **Trust**: if you don't trust a test, fix or delete it
5. **TDD where appropriate**: TDD for complex logic, not boilerplate

Practical rules:
6. Bug → test → fix (always write regression test)
7. New feature → test coverage > 80%
8. Refactoring → tests protect you
9. Code review: check test quality not just code quality
10. Flaky tests → fix immediately, they erode trust

Output: a one-page Testing Guidelines document for my team.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
