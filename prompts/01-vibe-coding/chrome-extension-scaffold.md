---
title: "Scaffold a Chrome Extension"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [chrome-extension, javascript, browser, web]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a complete Chrome Extension that: [DESCRIBE WHAT IT DOES].

Include all required files:
- `manifest.json` (Manifest V3)
- `popup.html` + `popup.js` (extension popup UI)
- `background.js` (service worker)
- `content.js` (page injection script if needed)
- `options.html` (settings page)
- CSS styles

Features:
- Storage sync for settings
- Message passing between popup ↔ background ↔ content
- Context menu integration
- Keyboard shortcut

Also include: instructions for loading in Chrome developer mode.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
