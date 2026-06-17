---
title: "Design Error States and Empty States"
category: ui-ux-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [errors, empty-states, ux, design]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Design informative, helpful error states and empty states.

My app: [DESCRIBE]

**Error states**:
1. **404 Page**: friendly + helpful navigation back
2. **500 Error**: apologetic + retry button + status page link
3. **No internet**: offline icon + retry + what still works
4. **API error**: specific message + what user can do
5. **Permission denied**: explain why + request permission
6. **Session expired**: auto-save user's work + re-login prompt

**Empty states** (first-time user or no results):
7. **First visit**: illustrative empty state + primary CTA (don't show empty table)
8. **No search results**: show what was searched + suggestions
9. **Filtered to nothing**: show active filters + clear filter CTA
10. **No notifications**: reassuring (not broken) message

For each: copy + illustration description + CTA button copy.
Illustrations: use SVG blob or emoji-based illustrations.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
