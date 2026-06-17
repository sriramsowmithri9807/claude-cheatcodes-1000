---
title: "Fix TypeScript Type Errors"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [typescript, types, debugging, errors]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Fix these TypeScript type errors:

```typescript
[PASTE YOUR CODE WITH TYPE ERRORS]
```

Errors:
```
[PASTE THE TSC ERROR OUTPUT]
```

For each error:
1. What the error means in plain English
2. Why TypeScript is complaining
3. The correct fix (not just `as any`)
4. If the fix reveals a logic bug, fix that too

Afterward:
- Are there any remaining `any` types I should address?
- Are there TypeScript strict mode settings I should enable?
- How to configure `tsconfig.json` for maximum type safety?
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
