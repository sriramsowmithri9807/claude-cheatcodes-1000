---
title: "Implement Authentication in React Native"
category: mobile-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react-native, auth, expo, security]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement authentication in my React Native app.

Auth methods: [EMAIL+PASSWORD / SOCIAL LOGIN / BIOMETRIC]
Backend: [DESCRIBE OR Firebase/Supabase]

1. **Token storage**: expo-secure-store for access + refresh tokens
2. **Auto-login**: check stored token on app start
3. **Token refresh**: transparently refresh expired tokens
4. **Logout**: clear all stored data
5. **Social login**:
   - Google: `@react-native-google-signin/google-signin`
   - Apple: `expo-apple-authentication` (required on iOS)
6. **Biometric**: Face ID / Fingerprint (expo-local-authentication)
7. **Deep link callback**: OAuth redirect back to app
8. **Logged-in check**: protected routes in Expo Router
9. **Session persistence**: stay logged in after app restart
10. **Multi-account**: switch between accounts

Output: auth context + login screen + protected navigation.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
