---
title: "Run CI Locally"
category: devex-tooling
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [ci, local-development, act, tooling]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Run CI pipeline locally before pushing.

CI system: GitHub Actions

Using: `act` (run GitHub Actions locally via Docker)

1. **Installation**: `brew install act`
2. **First run**: `act` runs `on: push` workflow
3. **Specific job**: `act -j test`
4. **Specific event**: `act pull_request`
5. **Secrets**: `act --secret-file .secrets`
6. **Container size**: `act --container-options '--memory 4g'`

Alternatives:
7. **Run steps manually**: document each CI step as npm script
8. **Docker**: reproduce CI environment locally
9. **Nx affected**: only test changed packages

Common CI issues to catch locally:
10. Missing environment variables
11. Wrong Node.js version
12. Test database not configured
13. Permissions issues
14. Missing secrets

`.actrc` file:
15. Default platform, secrets, environment settings

Output: act configuration + local CI guide.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
