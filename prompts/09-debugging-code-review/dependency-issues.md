---
title: "Debug Dependency Conflicts"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [dependencies, npm, debugging, node-js]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Debug my dependency conflicts.

Error: [PASTE npm install / yarn / pnpm error]
package.json: [PASTE RELEVANT SECTION]
Node version: [VERSION]
OS: [OS]

1. Explain what the conflict is (peer dependency, incompatible version, etc.)
2. Check `npm ls [package-name]` — which versions are installed?
3. Check if there's a version that satisfies all peer deps
4. Override strategy: use `resolutions` (yarn) or `overrides` (npm v8+)
5. Check if the package has a version that drops the conflicting dep
6. Alternative: is there a replacement package without the conflict?

Output: exact commands to resolve the conflict + updated package.json.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
