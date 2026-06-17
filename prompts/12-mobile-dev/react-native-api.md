---
title: "Connect React Native to Backend API"
category: mobile-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react-native, api, tanstack-query, axios]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Connect my React Native app to a backend API.

API: [DESCRIBE YOUR BACKEND API]
Auth: [JWT / OAuth]

1. **HTTP client**: Axios with base URL + interceptors
2. **Auth interceptor**: attach token to every request
3. **Refresh interceptor**: auto-refresh expired token
4. **Error interceptor**: handle 401 (logout), 5xx (show error)
5. **TanStack Query**: data fetching, caching, background refetch
6. **Optimistic updates**: update UI before server confirms
7. **Infinite queries**: paginated lists with infinite scroll
8. **Mutations**: POST/PUT/DELETE with loading/error states
9. **Offline**: cache results, show stale data when offline
10. **Retry**: automatic retry on network failure
11. **Environment**: .env for API URL per environment
12. **TypeScript**: typed API responses with Zod validation

Output: API client + TanStack Query hooks for my endpoints.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
