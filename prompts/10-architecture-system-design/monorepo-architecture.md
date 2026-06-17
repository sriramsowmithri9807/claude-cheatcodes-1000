---
title: "Design Monorepo Architecture"
category: architecture-system-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [monorepo, turborepo, architecture, packages]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a monorepo architecture for my project.

Apps to include: [LIST]
Shared code: [DESCRIBE WHAT TO SHARE]

Using: Turborepo + pnpm workspaces

```
apps/
  web/          Next.js frontend
  api/          Node.js backend
  mobile/       React Native
  admin/        Admin dashboard
packages/
  ui/           Shared React components
  types/        Shared TypeScript types
  utils/        Shared utilities
  config/
    eslint/
    tsconfig/
    tailwind/
```

Design decisions:
1. Package boundaries and ownership
2. Versioning: fixed (all same version) vs independent
3. Publishing: private registry or not
4. Build pipeline: turbo.json task dependencies
5. Change detection: which apps to rebuild on change
6. CI: affected packages only
7. Code sharing rules: what can depend on what
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
