---
title: "Set Up Code Generation Tools"
category: devex-tooling
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [code-generation, plop, hygen, scaffolding]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Set up code generation tools to scaffold components, modules, and files.

Project: [DESCRIBE]
Common boilerplate: [DESCRIBE: component, service, test, API route]

Using: Plop.js

1. **Installation**: `npm install --save-dev plop`
2. **Plopfile**: define generators
3. **Generator structure**:
   - Name (what you're generating)
   - Prompts (questions to ask user)
   - Actions (what files to create)
4. **Templates**: Handlebars templates for each file

Generators to create:
5. **React component**: component.tsx + styles + test + stories
6. **API route**: handler.ts + types + test
7. **Database model**: schema + migration + seed
8. **Zustand store**: store.ts + types
9. **Service**: service.ts + interface + mock

Usage:
```bash
npx plop component
# ? Component name: UserProfile
# ✓ Created src/components/UserProfile/UserProfile.tsx
# ✓ Created src/components/UserProfile/UserProfile.test.tsx
```

Output: Plopfile + templates for my generators.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
