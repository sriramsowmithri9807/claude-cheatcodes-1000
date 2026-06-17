---
title: "Make React Native App Accessible"
category: mobile-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react-native, accessibility, a11y, mobile]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Make my React Native app fully accessible.

Compliance target: WCAG 2.1 AA + Apple HIG + Google Material accessibility

1. **VoiceOver / TalkBack**: test with screen reader
2. **accessibilityLabel**: descriptive labels for all interactive elements
3. **accessibilityRole**: button, link, header, tab, etc.
4. **accessibilityState**: checked, disabled, selected, expanded
5. **accessibilityHint**: additional context for complex actions
6. **Focus management**: after modal opens, focus moves inside
7. **Dynamic type**: support iOS dynamic font sizes
8. **Color contrast**: meet 4.5:1 ratio for all text
9. **Touch targets**: minimum 44x44pt
10. **Motion**: respect `prefers-reduced-motion`
11. **Accessible images**: `accessible + accessibilityLabel` or `accessibilityElementsHidden` for decorative
12. **Forms**: label each input field

Test with: Accessibility Inspector (iOS), TalkBack (Android).
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
