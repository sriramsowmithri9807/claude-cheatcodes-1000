---
title: "Master Package Management"
category: devex-tooling
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [npm, pnpm, packages, dependencies]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Master package management for my Node.js project.

**pnpm (recommended)**:
1. Why pnpm: 2-3x faster than npm, disk efficient
2. `pnpm install`, `pnpm add`, `pnpm remove`
3. Lock file: `pnpm-lock.yaml`
4. Workspace: manage monorepos

**Dependency management**:
5. `dependencies` vs `devDependencies` vs `peerDependencies`
6. Pinning: `^` (compatible) vs `~` (patch only) vs exact
7. `npm outdated`: see what can be updated
8. `npx npm-check-updates -u`: update all deps
9. Renovate bot: automate dependency updates

**Security**:
10. `pnpm audit`: check for vulnerabilities
11. `pnpm audit --fix`: fix automatically

**Troubleshooting**:
12. Peer dependency conflicts: resolution field
13. Duplicate packages: `pnpm dedupe`
14. Clear cache: `pnpm store prune`

**Publishing**:
15. `pnpm pack`: preview what's published
16. `pnpm publish --access public`

Output: package.json best practices + scripts.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
