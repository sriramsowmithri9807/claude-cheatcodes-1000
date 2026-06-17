---
title: "Set Up Micro-Frontend Architecture"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [micro-frontend, module-federation, webpack, architecture]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Set up a Micro-Frontend architecture for [MY APP].

Using: Webpack Module Federation (or Vite equivalent)

Teams/domains:
- Host app (shell): [DESCRIPTION]
- Remote 1 ([TEAM NAME]): [DESCRIPTION]
- Remote 2 ([TEAM NAME]): [DESCRIPTION]

Implement:
1. Host app that dynamically loads remote modules
2. Shared dependencies configuration (React, ReactDOM)
3. Typed remote module loading with TypeScript
4. Error boundary for failed remote loads
5. Versioning strategy
6. Local development setup (all remotes running locally)
7. Deployment: each remote deployed independently

Show: how to share auth state between microfrontends.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
