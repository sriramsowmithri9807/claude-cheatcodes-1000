---
title: "Write Tests for React Components"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [testing, react-testing-library, jest, vitest]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Write comprehensive tests for my React components.

Components to test: [LIST YOUR COMPONENTS]

Testing patterns:
1. **Rendering**: does it render without crashing
2. **Props**: test all prop variations
3. **User interactions**: click, type, select using `userEvent`
4. **Async behavior**: loading states, data fetching (msw mocking)
5. **Accessibility**: axe-core integration
6. **Snapshots**: when they're useful vs harmful
7. **Custom hooks**: `renderHook` from RTL
8. **Context providers**: wrapping with providers in tests

Test organization: describe blocks, arrange-act-assert pattern.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
