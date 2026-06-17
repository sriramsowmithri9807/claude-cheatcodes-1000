---
title: "Solve Git Problems"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [git, debugging, version-control, recovery]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Help me solve this Git problem:

[DESCRIBE YOUR GIT SITUATION AND WHAT WENT WRONG]

My git log: [PASTE: git log --oneline -10]
Current status: [PASTE: git status]
Error message: [PASTE IF ANY]

Scenarios I need help with (check which apply):
□ Accidentally committed to wrong branch
□ Need to undo a commit (already pushed)
□ Merge conflict I can't resolve
□ Lost uncommitted work
□ Detached HEAD state
□ Rebased and things went wrong
□ Want to combine multiple commits
□ Need to cherry-pick a commit

Provide: step-by-step commands with explanation of what each one does. Warn me about any destructive operations.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
