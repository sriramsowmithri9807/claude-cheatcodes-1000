---
title: "Run an AI-Powered Project Retrospective"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [retrospective, agile, productivity, team]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Act as an experienced engineering manager facilitating a retrospective. Here are notes from our last sprint/project:

[PASTE YOUR SPRINT NOTES, INCIDENTS, METRICS, FEEDBACK]

Facilitate a retrospective:
1. **What went well** (celebrate these)
2. **What didn't go well** (be specific, no blame)
3. **Root cause analysis** for the top 2 problems
4. **Actionable improvements** (with owners and deadlines)
5. **Team health check** based on the data
6. **One process change** to implement immediately

Output as a formatted retrospective report suitable for sharing with the team.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
