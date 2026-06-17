---
title: "Secure a React Native App"
category: mobile-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react-native, security, mobile, encryption]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement security best practices for my React Native app.

1. **Certificate pinning**: reject MITM attacks on API calls
   - `react-native-ssl-pinning`
   - Pin certificate SHA256 hash
2. **Secure storage**: never store secrets in AsyncStorage
   - expo-secure-store for sensitive data
   - MMKV with encryption for app data
3. **Root/jailbreak detection**: `react-native-device-info`
4. **Screenshot prevention**: block screenshots on sensitive screens
5. **Obfuscation**: obfuscate JS bundle (ProGuard + Metro config)
6. **Environment variables**: never hardcode API keys
   - EAS Secrets for build-time secrets
   - Backend serves keys, not hardcoded in app
7. **Code protection**: enable Hermes, minimize source maps
8. **Biometric auth**: gate sensitive operations
9. **Session timeout**: logout after inactivity
10. **Clipboard**: clear clipboard after copy of sensitive data
11. **Deep link validation**: validate origin of deep links
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
