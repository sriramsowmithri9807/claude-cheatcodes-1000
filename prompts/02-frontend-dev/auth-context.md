---
title: "Build a Complete Auth Context in React"
category: frontend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react, auth, context, typescript]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a complete authentication context for a React SPA.

Backend: [REST API / GraphQL / Supabase / Firebase]

Implement:
1. `AuthContext` with: user, isAuthenticated, isLoading, error
2. `useAuth()` hook
3. `AuthProvider` that persists session (localStorage + refresh token)
4. Protected Route component
5. `login()`, `logout()`, `register()`, `refreshToken()` functions
6. Auto-refresh tokens before expiry
7. Handle 401 errors globally → redirect to login
8. Role checking: `usePermission('admin')` hook
9. Redirect to original URL after login

TypeScript throughout with proper typing of user object.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex component logic
- Specify your exact framework version for best results
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [02-frontend-dev README](README.md)
