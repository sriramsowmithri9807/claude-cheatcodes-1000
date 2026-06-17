---
title: "Advanced Git Hooks"
category: devex-tooling
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [git, hooks, automation, quality]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Set up advanced Git hooks for automation and quality.

Hooks to implement:

**pre-commit** (< 10 seconds):
1. Lint staged files
2. Format staged files
3. Check for secrets (detect-secrets)
4. Type check changed files

**commit-msg**:
5. Enforce Conventional Commits format
6. Link to Jira ticket if team policy

**pre-push**:
7. Run unit tests
8. Check for TODO/FIXME without ticket
9. Verify no debug statements left

**post-merge** (informational):
10. Remind to run `pnpm install` if package.json changed
11. Remind to run migrations if schema changed

**prepare-commit-msg**:
12. Pre-populate commit message with branch name

Implementation:
13. Husky for hook management
14. lint-staged for staged files
15. Parallel execution for speed
16. Skip in CI: `CI=true` bypasses hooks

Output: complete hook setup.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
