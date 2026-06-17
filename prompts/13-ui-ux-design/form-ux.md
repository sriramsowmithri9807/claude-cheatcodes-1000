---
title: "Design High-Converting Forms"
category: ui-ux-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [forms, ux, conversion, design]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Design high-converting, user-friendly forms.

Forms in my app: [DESCRIBE YOUR MAIN FORMS]

Conversion optimization:
1. **Single column**: never use two columns for forms (unless desktop)
2. **Labels above**: not inside (inside labels disappear)
3. **Placeholder**: show example value, not label
4. **Input width**: match expected content width
5. **Keyboard type**: show number pad for phone numbers
6. **Autocomplete**: `autocomplete` attribute for browser assist
7. **Real-time validation**: validate on blur, not on change (less jarring)
8. **Error placement**: below the field, never just red border
9. **Success state**: green checkmark on valid field
10. **Progress indicator**: show step X of Y for multi-step
11. **Smart defaults**: pre-fill what you know
12. **Submit button**: active only when required fields complete

Specific improvements for each of my forms.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
