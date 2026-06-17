---
title: "Set Up Testing Tools"
category: devex-tooling
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [testing, vitest, playwright, setup]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Set up comprehensive testing tools for my project.

Project: [DESCRIBE]

**Vitest** (unit + component tests):
1. Install: `npm install --save-dev vitest @vitest/ui`
2. `vitest.config.ts`: configure jsdom, coverage, aliases
3. React setup: `@testing-library/react` + `@testing-library/user-event`
4. Global: `describe`, `it`, `expect`, `vi` available without imports
5. Coverage: `@vitest/coverage-v8`, HTML report
6. UI: `vitest --ui` — browser interface for tests

**Playwright** (E2E tests):
7. Install: `npx playwright install`
8. `playwright.config.ts`: browsers, base URL, workers
9. Page Object Model: one class per page
10. Fixtures: extend test with reusable setup
11. API testing: `request` fixture for API calls
12. Visual testing: `expect(page).toHaveScreenshot()`

**MSW** (API mocking):
13. Define handlers for your API
14. Browser: ServiceWorker mode
15. Node.js: setupServer() for unit tests

Output: complete testing setup with example tests.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
