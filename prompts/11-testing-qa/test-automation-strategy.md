---
title: "Design Test Automation Strategy"
category: testing-qa
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [testing, strategy, automation, qa]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a comprehensive test automation strategy for my project.

Project: [DESCRIBE]
Team: [N developers, Y QA engineers]
Deployment frequency: [DAILY / MULTIPLE TIMES PER DAY]

Test pyramid:
```
           E2E (10%)
         Integration (20%)
       Unit Tests (70%)
```

For each layer:
1. What to test at this layer
2. Tools and frameworks
3. Who writes these tests (dev or QA)
4. When they run (pre-commit, pre-merge, post-deploy)
5. Target coverage and speed

Test pipeline:
6. Pre-commit: lint + fast unit tests (< 30s)
7. PR: unit + integration tests + linting
8. Merge to main: full suite including E2E
9. Nightly: performance, security, extended E2E
10. Monitoring: alert on flaky tests

Output: testing strategy document + recommended tools.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
