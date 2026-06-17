---
title: "Automate Your Side Project's Boring Parts"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [automation, scripts, productivity, devops]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
I'm building [PROJECT] and I keep doing these repetitive tasks manually: [LIST TASKS].

Automate everything with:
1. **Shell scripts** for each task
2. **npm scripts** in package.json
3. **GitHub Actions** for any CI/CD tasks
4. **Makefile** with a help target listing all commands
5. A **pre-commit hook** that runs relevant checks

For each automation:
- The script code
- How to invoke it
- What it does and why it saves time
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
