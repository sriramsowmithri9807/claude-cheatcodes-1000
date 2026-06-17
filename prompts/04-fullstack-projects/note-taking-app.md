---
title: "Build a Note-Taking App"
category: fullstack-projects
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [notes, editor, react, fullstack]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a Notion-lite note-taking app.

Stack: Next.js + PostgreSQL + Tiptap editor

Features:
1. Block-based editor: text, heading, bullet list, numbered list, code, image, divider
2. Slash command: / to insert blocks
3. Drag to reorder blocks
4. Nested pages (tree structure in sidebar)
5. Full-text search across all notes
6. Tags and favorites
7. Share note: public read-only URL
8. Real-time autosave (debounced, no manual save needed)
9. Markdown import/export
10. Dark mode

Optional: real-time collaboration with Yjs
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
