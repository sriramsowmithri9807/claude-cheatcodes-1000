---
title: "Generate PDFs from React Components"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [pdf, react, react-pdf, documents]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Generate professional PDFs from React components.

Document to generate: [DESCRIBE: invoice / report / certificate / contract]

Using: @react-pdf/renderer

Implement:
1. PDF document with pages, header, footer
2. Tables with borders and alternating row colors
3. Images and logos
4. Typography with custom fonts (load from URL)
5. Page numbers and total pages
6. Dynamic content from data
7. Download button that triggers PDF generation
8. Preview the PDF in a modal before downloading

Also: email delivery option using the PDF as a Buffer attachment.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
