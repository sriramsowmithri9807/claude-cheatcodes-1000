---
title: "Audit Color Accessibility"
category: ui-ux-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [accessibility, color, wcag, design]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Audit and fix color accessibility in my design.

Current color palette: [PASTE HEX VALUES]
UI elements using these colors: [DESCRIBE]

WCAG 2.1 requirements:
- **AA**: normal text 4.5:1, large text 3:1, UI components 3:1
- **AAA**: normal text 7:1, large text 4.5:1

Audit:
1. Calculate contrast ratio for every text/background combination
2. Flag all failures with their current ratio
3. Suggest adjusted colors that pass while staying on-brand
4. Check: colored icons on colored backgrounds
5. Check: focus indicators (3:1 against adjacent colors)
6. Check: placeholder text (often too light)
7. Check: disabled state (often too light)
8. Color blindness: can everything be understood without color alone?

Fix:
9. Adjusted color values for all failures
10. Add pattern/icon to supplement color-only information

Output: audit table + fixed color values.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
