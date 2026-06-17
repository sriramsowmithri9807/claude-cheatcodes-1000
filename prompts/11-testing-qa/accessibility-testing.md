---
title: "Test Accessibility (a11y)"
category: testing-qa
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [accessibility, a11y, testing, wcag]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Test and fix accessibility in my web application.

App: [DESCRIBE]
Compliance target: WCAG 2.1 AA

Automated testing:
1. **axe-core**: integrate with React Testing Library
2. **Lighthouse**: accessibility audit in CI
3. **Playwright**: axe-playwright for E2E a11y tests

Manual testing:
4. **Keyboard navigation**: tab through entire app, no mouse
5. **Screen reader**: VoiceOver (Mac) + NVDA (Windows)
6. **High contrast mode**: Windows high contrast
7. **Zoom to 400%**: no content lost
8. **Color contrast**: check all text/background pairs

Common issues to check:
9. Missing alt text on images
10. No focus indicator
11. Missing form labels
12. Poor color contrast
13. Non-descriptive link text
14. Dynamic content not announced

Output: axe integration + list of found issues + fixes.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
