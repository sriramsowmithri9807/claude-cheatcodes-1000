---
title: "Set Up Monorepo Tooling"
category: devex-tooling
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [monorepo, turborepo, pnpm, nx]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Set up tooling for my monorepo.

Apps/packages: [LIST WHAT'S IN YOUR MONOREPO]

**pnpm workspaces** (package manager):
1. `pnpm-workspace.yaml`: define workspace packages
2. Hoist: shared dependencies at root
3. Protocol: `workspace:*` for internal packages

**Turborepo** (build system):
4. `turbo.json`: define pipeline tasks
5. Task caching: skip rebuilding if inputs unchanged
6. Remote cache: share cache across CI and team
7. Filtering: `turbo build --filter=@myorg/web`

Workspace structure:
```
apps/
  web/
  api/
packages/
  ui/
  utils/
  tsconfig/
```

Shared configs:
8. Root `tsconfig.json` extended by all packages
9. Root ESLint config extended by all
10. Root Prettier config

CI optimization:
11. Only build/test affected packages
12. Remote cache for CI speed

Output: complete monorepo setup.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
