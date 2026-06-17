---
title: "Write End-to-End Tests with Playwright"
category: testing-qa
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [e2e, playwright, testing, automation]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Write end-to-end tests for my web application using Playwright.

App: [DESCRIBE YOUR APP]
Key user flows to test:
1. [USER FLOW 1: e.g., Sign up → complete onboarding → first core action]
2. [USER FLOW 2: e.g., Search → add to cart → checkout]
3. [USER FLOW 3: e.g., Admin creates → user sees it]

Playwright best practices:
- Page Object Model: one class per page
- Stable locators: data-testid attributes
- Parallel test execution
- CI-ready: headless, record videos on failure
- No sleeps: use Playwright's auto-waiting
- Isolated tests: each test starts fresh
- API mocking for tests that don't need real data

Output: page objects + test specs + Playwright config.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
