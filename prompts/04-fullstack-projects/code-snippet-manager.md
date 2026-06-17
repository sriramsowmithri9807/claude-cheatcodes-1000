---
title: "Build a Code Snippet Manager"
category: fullstack-projects
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [snippets, developer-tools, fullstack, search]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a developer code snippet manager (like Carbon or Ray.so but with search and sharing).

Stack: Next.js + PostgreSQL + Prism.js (syntax highlighting)

Features:
1. Create snippets: title, description, code, language, tags
2. Syntax highlighting for 50+ languages
3. Collections / folders
4. Full-text search (content + title + tags)
5. Public snippets: shareable URL with beautiful code rendering
6. Private snippets: only visible to owner
7. Embed code: `<iframe>` embed for blogs/docs
8. VS Code extension: save snippet from editor, search from command palette
9. Copy to clipboard with one click
10. Import from GitHub Gist
11. AI: explain snippet, generate similar snippet (Claude API)
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
