---
title: "Document TypeScript Code with JSDoc"
category: documentation
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [jsdoc, typescript, documentation, api]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Add comprehensive JSDoc documentation to my TypeScript code.

Code to document: [PASTE YOUR TYPESCRIPT CODE]

JSDoc patterns for TypeScript:
1. **Function documentation**:
```typescript
/**
 * Brief description of what the function does.
 *
 * @param userId - The unique identifier of the user
 * @param options - Configuration options
 * @returns The created user object
 * @throws {ValidationError} When userId is invalid
 * @example
 * ```typescript
 * const user = await getUser('user_123', { includeProfile: true });
 * ```
 */
```

2. **Interface documentation**: document each property
3. **Class documentation**: describe the class, constructor, public methods
4. **Type aliases**: document complex types
5. **Deprecated**: `@deprecated Use newFunction() instead`
6. **Internal**: `@internal` for non-public API

Generate docs:
7. TypeDoc: `typedoc --entryPoints src/index.ts`
8. Output: static HTML documentation site

Document all exported symbols in my code.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
