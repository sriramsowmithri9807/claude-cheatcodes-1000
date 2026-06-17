---
title: "Implement Deep Links in React Native"
category: mobile-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react-native, deep-links, expo-router, mobile]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement deep links in my React Native app.

Links to handle:
- `myapp://post/123` — open specific post
- `https://myapp.com/post/123` — universal link (opens app if installed)

**With Expo Router**:
1. Configure URL scheme in `app.json`
2. Configure associated domain for universal links
3. File-based routes handle deep links automatically
4. Dynamic routes: `app/post/[id].tsx`
5. Test: `npx uri-scheme open myapp://post/123 --ios`

**Universal links setup**:
6. iOS: `apple-app-site-association` file on your domain
7. Android: `assetlinks.json` file on your domain

**Navigation on deep link**:
8. App closed: open to correct screen
9. App open: navigate without closing current session
10. Auth guard: redirect to login if not authenticated, then to deep link destination after

Output: complete deep link configuration.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
