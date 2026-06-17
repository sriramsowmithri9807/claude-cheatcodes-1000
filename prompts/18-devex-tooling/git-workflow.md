---
title: "Set Up Git Workflow for Teams"
category: devex-tooling
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [git, workflow, branching, team]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Set up a Git workflow for my engineering team.

Team size: [N engineers]
Deployment frequency: [DAILY / MULTIPLE TIMES A DAY]

Branching strategy:
**GitHub Flow** (simple, for continuous deployment):
1. `main` → always deployable
2. Feature branches → PR → merge
3. Deploy from main automatically

**Git Flow** (for scheduled releases):
4. `main` → production
5. `develop` → integration
6. `feature/` → develop
7. `release/` → main
8. `hotfix/` → main

Branch naming: `type/short-description` where type = feat/fix/docs/chore

Commit conventions:
9. Conventional Commits: `feat: add user avatar upload`
10. Commitlint: enforce in pre-commit hook

PR process:
11. PR template: description, test plan, screenshots
12. Minimum 1 review required
13. CI must pass before merge
14. Squash merge to keep history clean

Output: Git workflow documentation + hook configs.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
