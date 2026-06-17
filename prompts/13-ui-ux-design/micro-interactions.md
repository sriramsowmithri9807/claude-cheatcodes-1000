---
title: "Design Micro-Interactions"
category: ui-ux-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [animations, micro-interactions, ux, design]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Design delightful micro-interactions for my application.

App context: [DESCRIBE YOUR APP]

Micro-interactions to design:
1. **Button press**: scale down + color darken (tactile feel)
2. **Toggle switch**: slide + color change with spring physics
3. **Checkbox**: scale in checkmark with bounce
4. **Form validation**: success → green check, error → red shake
5. **Loading states**: skeleton → skeleton fade → content fade in
6. **Navigation**: smooth page transition (slide/fade)
7. **Hover effects**: lift (shadow + translateY), color shift
8. **Toast notifications**: slide up + auto-dismiss with animation
9. **Delete**: swipe or fade out with confirmation
10. **Pull to refresh**: elastic overscroll
11. **Long press**: subtle haptic feedback pattern
12. **Upload progress**: radial or linear with completion burst

For each: CSS/Framer Motion implementation + timing spec.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
