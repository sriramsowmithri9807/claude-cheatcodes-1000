---
title: "Design Developer Documentation"
category: api-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [docs, api, developer-experience, dx]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Design world-class developer documentation for my API.

API: [DESCRIBE]
Target developers: [SKILL LEVEL AND BACKGROUND]

Documentation structure:
1. **Getting Started**: auth → first API call → see result (< 5 minutes)
2. **Guides**: common use cases as step-by-step tutorials
3. **Reference**: every endpoint, parameter, response (auto-generated from OpenAPI)
4. **Changelog**: what changed in each version
5. **Migration guides**: how to upgrade from v1 to v2
6. **SDKs**: code examples in 5 languages for every endpoint
7. **Playground**: try API calls in the browser
8. **Status page**: link to uptime page
9. **Error reference**: every error code with solution
10. **Community**: Discord/forum link

Tool: Mintlify, Readme.io, or Docusaurus.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
