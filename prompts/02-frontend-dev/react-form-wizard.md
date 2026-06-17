---
title: "Build a Multi-Step Form Wizard"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react, forms, validation, typescript]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a production-ready multi-step form wizard in React + TypeScript.

Steps: [DESCRIBE YOUR FORM STEPS AND FIELDS]

Features:
- Progress indicator (step dots or bar)
- Validation per step before advancing (react-hook-form + Zod)
- Back button with state preservation
- Data persists in localStorage (survive page refresh)
- Review step showing all inputs before submit
- Loading state during submission
- Success/error states
- Accessible (ARIA live regions for step changes)
- Smooth step transition animations

No UI library — pure React + CSS Modules.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
