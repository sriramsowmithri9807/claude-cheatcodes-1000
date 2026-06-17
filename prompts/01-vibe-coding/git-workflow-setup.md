---
title: "Set Up a Professional Git Workflow"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [git, workflow, branching, ci]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Set up a professional Git workflow for my team working on [PROJECT TYPE].

Provide:
1. Branching strategy (GitFlow vs trunk-based, with justification for my team size)
2. Commit message convention (Conventional Commits) with examples
3. Pre-commit hooks (`.husky/` + `lint-staged` config)
4. PR/MR template (`.github/pull_request_template.md`)
5. Branch protection rules to configure on GitHub
6. `commitlint.config.js` configuration
7. `CHANGELOG.md` automation with `standard-version`
8. Git aliases cheat sheet for the team
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
