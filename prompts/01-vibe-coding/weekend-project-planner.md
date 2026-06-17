---
title: "Plan a Weekend Coding Project"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [planning, project-management, mvp]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
I have this weekend (Sat + Sun, ~12 hours total) to build: [PROJECT IDEA].

Create a detailed hour-by-hour plan:
- Saturday morning (3h): [Foundation]
- Saturday afternoon (3h): [Core features]  
- Sunday morning (3h): [Polish & edge cases]
- Sunday afternoon (3h): [Deploy & share]

For each block:
- Specific tasks with checkboxes
- Files to create/edit
- Potential blockers and how to avoid them

Also: What to cut if I'm running behind, and what's the absolute minimum I need for a deployable v1.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
