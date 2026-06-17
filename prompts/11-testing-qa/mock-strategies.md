---
title: "Master Mocking Strategies"
category: testing-qa
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [mocking, testing, jest, msw]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Master mocking strategies for comprehensive testing.

Code to test: [PASTE CODE WITH EXTERNAL DEPENDENCIES]

Mocking approaches:
1. **Manual mocks**: custom mock implementations
2. **Jest spies**: `jest.spyOn(obj, 'method')`
3. **Module mocks**: `jest.mock('./module')`
4. **Mock Service Worker (MSW)**: intercept HTTP at network level
5. **Test doubles taxonomy**: stub, spy, mock, fake, dummy — when to use each

What to mock:
6. **Always mock**: external APIs, email, payment, time
7. **Usually mock**: database (use test DB instead)
8. **Never mock**: the code under test itself

Bad mocking patterns:
9. Over-mocking: testing implementation not behavior
10. Brittle mocks: break when implementation changes

For my code: complete mocking setup for each dependency.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
