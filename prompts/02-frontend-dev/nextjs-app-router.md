---
title: "Master Next.js App Router Patterns"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [nextjs, app-router, react, typescript]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement these Next.js 14+ App Router patterns for [MY APP]:

1. **Layouts**: Root layout, nested layouts, parallel routes
2. **Loading UI**: `loading.tsx` with Suspense boundaries
3. **Error handling**: `error.tsx` with reset functionality
4. **Server Components**: data fetching without `useEffect`
5. **Client Components**: minimal client JS, proper `'use client'` usage
6. **Server Actions**: form handling without API routes
7. **Route Handlers**: API endpoints in `app/api/`
8. **Metadata API**: dynamic SEO metadata per page
9. **Streaming**: `<Suspense>` for progressive loading
10. **Caching**: `fetch` with revalidation, `unstable_cache`

Show before/after for each pattern migrating from Pages Router.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
