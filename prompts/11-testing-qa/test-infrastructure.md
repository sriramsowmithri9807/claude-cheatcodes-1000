---
title: "Build Test Infrastructure"
category: testing-qa
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [testing, infrastructure, docker, ci-cd]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build robust test infrastructure for my application.

Requirements:
- Tests should be reproducible anywhere
- Fast: parallel execution
- Isolated: tests don't interfere
- Real: use real services where possible, not mocks

Infrastructure:
1. **Docker Compose for tests**: PostgreSQL + Redis + app in containers
2. **Database per test run**: each CI job gets fresh database
3. **Testcontainers**: spin up DB in Docker from test code
4. **Test environment management**: create/destroy on demand
5. **Parallelism**: split tests across multiple CI workers
6. **Caching**: cache Docker images, dependencies
7. **GitHub Actions matrix**: run against multiple versions
8. **Artifact storage**: test results, coverage reports, screenshots
9. **Flaky test retry**: retry up to 3 times before failing CI
10. **Test result reporting**: PR comment with pass/fail + coverage

Output: complete infrastructure setup.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
