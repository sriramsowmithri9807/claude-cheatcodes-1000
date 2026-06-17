---
title: "Set Up a Professional Monorepo"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [monorepo, turborepo, pnpm, nx, architecture]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Set up a professional monorepo for a project with: [LIST YOUR APPS AND PACKAGES].

Use: pnpm workspaces + Turborepo

Structure:
```
apps/
  web/        (Next.js)
  api/        (Node.js/Express)
  mobile/     (React Native or Expo)
packages/
  ui/         (shared React components)
  utils/      (shared utilities)
  types/      (shared TypeScript types)
  config/     (shared configs: eslint, tsconfig, prettier)
```

Provide:
- Root `package.json` and `turbo.json` config
- Each `package.json` with proper workspace references
- Shared TypeScript config inheritance
- Build and dev pipeline
- CI pipeline that only runs affected packages
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
