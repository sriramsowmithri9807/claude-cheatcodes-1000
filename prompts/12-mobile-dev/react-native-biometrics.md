---
title: "Implement Biometric Authentication"
category: mobile-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react-native, biometrics, security, expo]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Add biometric authentication (Face ID, Touch ID, Fingerprint) to my React Native app.

Using: `expo-local-authentication`

1. **Check availability**: is biometric available and enrolled?
2. **Types**: face recognition, fingerprint, iris
3. **Authentication**: prompt with reason, get result
4. **Fallback**: if biometric fails → fall back to PIN/password
5. **Store credentials**: biometric gates access to stored credentials (expo-secure-store)
6. **First time**: user enables biometric in settings screen
7. **Persist choice**: remember user's biometric preference
8. **Re-auth**: require biometric on app resume (sensitive apps)
9. **Android**: handle API differences between Android versions
10. **Accessibility**: graceful degradation if no biometric hardware

Flow: app launch → check biometric preference → authenticate → show app.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
