---
title: "Master React Query / TanStack Query"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react-query, tanstack, data-fetching, cache]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Master TanStack Query v5 (React Query) for [MY APP].

Implement these patterns:
1. Basic `useQuery` with TypeScript generics
2. `useMutation` with optimistic updates + rollback
3. Infinite queries for pagination/infinite scroll
4. Prefetching: hover prefetch, SSR prefetch (Next.js)
5. Dependent queries (query B runs after query A)
6. Query invalidation strategies
7. Polling: refetch every N seconds
8. Offline support: `networkMode: 'offlineFirst'`
9. Global error handling with `QueryErrorBoundary`
10. DevTools integration

Include: a `queryClient` singleton setup and provider configuration.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
