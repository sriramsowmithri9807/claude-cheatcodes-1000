---
title: "Master TypeScript Generics for React"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [typescript, generics, react, types]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Master TypeScript generics in the context of React development.

Build these generic utilities and components:

1. **Generic API hook**: `useApi<TData, TError>(url)` → `{data, error, loading}`
2. **Generic form**: `<Form<TValues>` with typed fields and typed submit handler
3. **Generic table**: `<DataTable<TRow>` with typed columns
4. **Generic select**: `<Select<TOption>` with typed options and onChange
5. **Generic context**: `createContext<TState>()` with typed provider
6. **Conditional types**: `DeepPartial<T>`, `DeepReadonly<T>`, `Nullable<T>`
7. **Mapped types**: transform any model for API vs UI vs form
8. **Template literal types**: typed route params

Each with TypeScript playground-ready examples.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
