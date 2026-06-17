---
title: "Implement Complete SEO for Next.js"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [seo, nextjs, metadata, structured-data]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement complete SEO for my Next.js 14 app.

App type: [DESCRIBE YOUR APP]
Key pages: [LIST IMPORTANT PAGES]

Implement:
1. Root metadata in `layout.tsx`
2. Dynamic metadata in each `page.tsx` using `generateMetadata`
3. Open Graph tags for social sharing
4. Twitter Card metadata
5. JSON-LD structured data (Organization, Article, Product, BreadcrumbList)
6. Sitemap generation (`app/sitemap.ts`)
7. Robots.txt (`app/robots.ts`)
8. Canonical URLs
9. Dynamic OG images using `next/og`
10. Internationalized SEO with `hreflang` for [LANGUAGES]
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
