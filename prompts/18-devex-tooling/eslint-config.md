---
title: "Configure ESLint for Your Project"
category: devex-tooling
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [eslint, linting, code-quality, javascript]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Configure ESLint for maximum code quality.

Project type: [React / Next.js / Node.js / TypeScript]

ESLint flat config (`eslint.config.js`):
1. **Parser**: @typescript-eslint/parser for TypeScript
2. **Plugin bundles**:
   - `@typescript-eslint/eslint-plugin`: TypeScript rules
   - `eslint-plugin-react`: React best practices
   - `eslint-plugin-react-hooks`: Hooks rules
   - `eslint-plugin-import`: import ordering
   - `eslint-plugin-unicorn`: modern JS best practices
3. **Rules to enable**:
   - No any: `@typescript-eslint/no-explicit-any`
   - No unused vars (with destructuring exception)
   - Consistent returns
   - No floating promises
   - Import organization
4. **Rules to disable** (with reason)
5. **Override**: different rules for test files
6. **Prettier integration**: `eslint-config-prettier`
7. **Pre-commit hook**: run ESLint via lint-staged
8. **CI**: fail if ESLint errors

Output: complete `eslint.config.js` for my project.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
