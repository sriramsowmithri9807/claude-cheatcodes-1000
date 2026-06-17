---
title: "Debug Cross-Browser Compatibility Issues"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [browser, compatibility, css, javascript]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Debug cross-browser compatibility issues with my code.

Issue: [DESCRIBE: looks broken in Safari / IE / Firefox / Mobile Chrome]
Code causing the issue:
```css/html/js
[PASTE CODE]
```

1. Identify the browser-specific API or CSS property causing the issue
2. Check caniuse.com compatibility for the feature
3. Provide a cross-browser fix:
   - CSS: fallback values, -webkit- prefixes, feature queries (@supports)
   - JS: polyfills, alternative APIs
4. Test in: Chrome, Firefox, Safari, Edge, iOS Safari, Android Chrome
5. Postcss/Autoprefixer: automate prefix addition
6. Browserslist config: define browser targets for build tools
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
