---
title: "Intelligently Split a Large File"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [refactor, architecture, clean-code, modules]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
This file has grown too large: [PASTE FILE OR DESCRIBE IT].

Refactor it by:
1. Identifying all distinct concerns/responsibilities in this file
2. Proposing a new folder structure with one file per concern
3. Writing each split file with proper imports/exports
4. Updating the original file to import from the new modules
5. Identifying any circular dependencies to watch for

Follow: Single Responsibility Principle. Each file should have exactly one reason to change.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
