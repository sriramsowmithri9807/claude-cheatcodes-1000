---
title: "Create Wireframes for a New Feature"
category: ui-ux-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [wireframing, design, planning, ux]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Create wireframes for a new feature in my application.

Feature to design: [DESCRIBE THE FEATURE]
Existing app context: [DESCRIBE YOUR APP AND ITS PATTERNS]

Outputin ASCII wireframe format:

```
┌─────────────────────────────────┐
│  Header / Navigation            │
├─────────────────────────────────┤
│  [Wireframe content here]       │
│                                 │
└─────────────────────────────────┘
```

Wireframes needed:
1. Main view (desktop + mobile)
2. Empty state (no data)
3. Loading state
4. Error state
5. Key interaction states (expanded, selected, etc.)

For each wireframe:
- What the user sees
- Interactive elements
- What happens on each action
- Edge cases addressed

Also: user flow diagram showing navigation between screens.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
