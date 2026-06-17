---
title: "Organize a Large Test Suite"
category: testing-qa
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [testing, organization, structure, maintenance]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Organize my growing test suite for maintainability.

Current state: [DESCRIBE: N test files, what's messy, what's slow]

Organization principles:
1. **Mirror source structure**: test file next to source file
2. **Group by feature**: tests for the same feature together
3. **Setup/teardown**: `beforeAll`, `afterAll`, `beforeEach` correctly
4. **Shared utilities**: test helpers in a shared folder
5. **Test categories**: unit | integration | e2e — run separately

Speed optimization:
6. **Parallel execution**: run test files in parallel (Vitest default)
7. **Selective running**: `--testPathPattern` for fast iteration
8. **Skip slow tests in watch mode**
9. **Mocking**: mock all I/O in unit tests (keep them fast)
10. **Order**: fast tests first (fail fast in CI)

CI strategy: unit tests always, integration on push, e2e nightly.
Output: recommended folder structure + vitest.config.ts.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
