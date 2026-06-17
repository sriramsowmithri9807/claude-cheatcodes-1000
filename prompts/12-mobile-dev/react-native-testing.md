---
title: "Test React Native Apps"
category: mobile-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react-native, testing, jest, detox]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Write tests for my React Native app.

App: [DESCRIBE]

**Unit + Component tests** (Jest + RNTL):
1. Setup: jest-expo preset
2. Component rendering tests
3. User interaction: `fireEvent.press`, `fireEvent.changeText`
4. Navigation testing: mock navigation
5. Async tests: API calls, loading states

**E2E tests** (Detox):
6. Detox setup for iOS + Android
7. First test: launch → navigate → interact → assert
8. Text matchers: `by.id()`, `by.text()`, `by.type()`
9. Actions: tap, longPress, typeText, scroll
10. Assertions: `expect(el).toBeVisible()`, `toHaveText()`
11. Network mocking in E2E
12. CI: run E2E on iOS simulator in GitHub Actions

Output: unit test suite + Detox E2E for critical flows.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
