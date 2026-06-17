---
title: "Build a Documentation Site with Docusaurus"
category: documentation
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [docusaurus, documentation, react, website]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a documentation website with Docusaurus.

Documentation to host: [DESCRIBE YOUR DOCS]

1. **Setup**: `npx create-docusaurus@latest my-docs classic --typescript`
2. **Configuration**: `docusaurus.config.ts` — navbar, footer, themes
3. **Content**: Markdown/MDX files in `docs/` folder
4. **Sidebar**: auto-generated or custom `sidebars.ts`
5. **Components**: MDX lets you embed React components in docs
6. **Versioning**: multiple doc versions for different releases
7. **Search**: Algolia DocSearch (free for open source)
8. **Blog**: built-in blog for release notes
9. **Custom theme**: extend Docusaurus theme for your brand
10. **Deployment**: GitHub Pages, Vercel, Netlify (one command)

Features to configure:
11. Dark mode toggle
12. i18n for multiple languages
13. OpenAPI plugin for API reference
14. Analytics: Plausible or Google Analytics

Output: complete Docusaurus site for my docs.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
