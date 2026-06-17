---
title: "Design an n8n Automation Workflow"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [automation, n8n, no-code, workflow]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Design a complete n8n automation workflow for: [DESCRIBE YOUR AUTOMATION].

Provide:
1. The complete workflow as a JSON export (importable into n8n)
2. Step-by-step explanation of each node
3. Error handling nodes and what they do
4. Webhook triggers and their configuration
5. Environment variables to configure
6. Testing instructions

If n8n can't do part of it, suggest a custom Code node solution.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
