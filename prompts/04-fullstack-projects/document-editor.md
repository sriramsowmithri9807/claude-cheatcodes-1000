---
title: "Build a Collaborative Document Editor"
category: fullstack-projects
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [editor, collaboration, yjs, fullstack]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a Google Docs-style collaborative document editor.

Stack: Next.js + Node.js + Yjs + y-websocket + Tiptap + PostgreSQL

Features:
1. Rich text editor: headings, bold/italic, lists, tables, images, code blocks
2. Real-time collaboration: multiple users edit simultaneously (CRDT-powered)
3. Cursor presence: see other users' cursors with name labels
4. Comments: highlight text → add comment → reply thread
5. Version history: restore to any past version
6. Share: private, view-only link, public
7. Export: PDF, Word (.docx), Markdown
8. Templates: start from pre-made document templates
9. Table of contents: auto-generated from headings
10. Word count, reading time stats
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
