---
title: "Build and Deploy with EAS"
category: mobile-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [expo, eas, deployment, mobile]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build and deploy my Expo app with EAS (Expo Application Services).

App: [DESCRIBE]

**EAS Build**:
1. `eas build:configure` — create eas.json
2. Build profiles: development, preview, production
3. iOS: Apple Developer account setup, certificates, profiles
4. Android: keystore management
5. Build command: `eas build --platform all --profile production`
6. Build cache: speed up builds

**EAS Update (OTA)**:
7. Update JS bundle without App Store review
8. Channels: production, staging, preview
9. Rollback bad update
10. `eas update --channel production --message "Fix login bug"`

**EAS Submit**:
11. `eas submit --platform ios` → App Store Connect
12. `eas submit --platform android` → Play Store

**GitHub Actions**: automate build + submit on push to main.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
