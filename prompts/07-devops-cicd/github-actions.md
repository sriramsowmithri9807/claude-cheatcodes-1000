---
title: "Write a Complete GitHub Actions CI/CD Pipeline"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [github-actions, ci-cd, devops, automation]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Write a complete GitHub Actions CI/CD pipeline for my [Node.js / Python / Go] project.

Workflows to create:

**CI workflow** (on every PR):
1. Checkout code
2. Setup Node/Python/Go with version caching
3. Install dependencies (with cache)
4. Lint (ESLint, Ruff, golint)
5. Type check (TypeScript tsc, mypy)
6. Unit tests (with coverage report)
7. Integration tests (spin up Docker services)
8. Build (verify it compiles)
9. Security scan (CodeQL or Snyk)
10. Post results as PR comment

**CD workflow** (on merge to main):
11. Build Docker image
12. Push to registry (GHCR)
13. Deploy to staging (Fly.io / Railway / AWS ECS)
14. Run smoke tests
15. Deploy to production (manual approval gate)

Output: complete YAML workflow files.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
