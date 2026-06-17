---
title: "Build a Rich Markdown Editor"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [editor, markdown, react, ui]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a rich Markdown editor like Notion or Hashnode's editor.

Using: Tiptap (or ProseMirror directly for maximum control)

Features:
1. Toolbar: bold, italic, code, headings, lists, blockquote, link, image
2. Keyboard shortcuts: ⌘B for bold, ⌘K for link, etc.
3. Slash commands: type `/` to insert blocks
4. Drag and drop blocks to reorder
5. Auto-link: paste URL → detect and convert
6. Code blocks with syntax highlighting
7. Real-time Markdown preview (split view)
8. Export to HTML and raw Markdown
9. Mention system: @username autocomplete
10. Auto-save with debounce
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
