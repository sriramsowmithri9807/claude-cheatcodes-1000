---
title: "Build Native Web Components"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [web-components, custom-elements, shadow-dom, javascript]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build production-ready Web Components (framework-agnostic).

Components to build:
1. `<my-button>` — accessible button with variants
2. `<my-modal>` — dialog with focus trap and backdrop
3. `<my-toast>` — notification system
4. `<my-tabs>` — accessible tab interface
5. `<my-accordion>` — expand/collapse sections

Each component must:
- Use Shadow DOM for style encapsulation
- Define a clean attribute/property API
- Fire custom events for parent communication
- Work in React, Vue, Angular, and vanilla HTML
- Be tree-shakeable when used in bundles
- Pass all ARIA requirements

Include TypeScript type declarations (.d.ts) for IDE support.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
