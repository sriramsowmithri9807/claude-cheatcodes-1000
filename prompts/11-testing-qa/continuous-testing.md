---
title: "Set Up Continuous Testing"
category: testing-qa
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [ci-cd, testing, automation, pipeline]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Set up continuous testing integrated with my development workflow.

Stack: [DESCRIBE]
CI: GitHub Actions

Testing gates:
1. **Pre-commit hook** (local, < 30s):
   - Lint (ESLint)
   - Type check (TypeScript)
   - Unit tests for changed files only
2. **PR opened** (< 5 min):
   - Full unit test suite
   - Integration tests
   - Coverage check (fail if drops below threshold)
3. **Merge to main** (< 15 min):
   - Full test suite
   - E2E smoke tests
   - Performance regression test
4. **Nightly** (unlimited time):
   - Extended E2E suite
   - Load tests
   - Security scan
5. **Post-deploy**:
   - Smoke tests against production

Output: complete GitHub Actions workflows for each gate.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
