---
title: "Debug CSS Layout Problems"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [css, layout, debugging, flexbox]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Debug my CSS layout problem.

Problem: [DESCRIBE: element is overlapping, not centering, not full-width, disappearing, wrong on mobile]
HTML:
```html
[PASTE HTML]
```
CSS:
```css
[PASTE CSS]
```
Browser/device where it breaks: [DESCRIBE]

1. Inspect in DevTools: check computed styles, box model, margins
2. Identify the specific property causing the issue
3. Common causes check:
   - Collapsing margins
   - Float clearing
   - Position context (relative parent for absolute child)
   - Flexbox vs Grid confusion
   - z-index without position
   - Missing `box-sizing: border-box`
   - Viewport units on mobile (100vh issue)
4. Fix with minimum CSS change
5. Make it responsive if not already
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
