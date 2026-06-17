---
title: "Implement Push Notifications"
category: mobile-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react-native, notifications, expo, mobile]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement push notifications in my React Native + Expo app.

Notification types: [DESCRIBE: marketing, transactional, real-time events]

1. **Setup**: expo-notifications + EAS configuration
2. **Permission request**: ask for permission with context
3. **Device token**: get Expo push token, send to your backend
4. **Local notifications**: schedule without server
5. **Remote notifications**: send from backend via Expo Push API
6. **Rich notifications**: title, body, image, actions
7. **Notification handling**:
   - App in foreground: show in-app toast
   - App in background: system notification
   - App closed: open to specific screen on tap
8. **Deep linking**: notification tap → specific screen
9. **Badge count**: update app icon badge
10. **Category actions**: quick reply, dismiss buttons

Backend: endpoint to store tokens + send notifications.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
