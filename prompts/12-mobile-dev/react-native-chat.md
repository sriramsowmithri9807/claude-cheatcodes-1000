---
title: "Build a Real-Time Chat in React Native"
category: mobile-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react-native, chat, websockets, mobile]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build real-time chat in my React Native app.

Using: Socket.io + React Native GiftedChat

1. **Socket connection**: connect on login, disconnect on logout
2. **Authentication**: send token on WebSocket handshake
3. **GiftedChat setup**: renderItem, renderBubble, renderInput
4. **Message types**: text, image, voice, emoji
5. **Delivery receipts**: sent → delivered → read
6. **Typing indicator**: show when other user is typing
7. **Pagination**: load older messages on scroll up
8. **Push notifications**: receive messages when app is background
9. **Image messages**: pick from gallery, upload, display
10. **Voice messages**: record, visualize waveform, play
11. **Online presence**: show online/offline status
12. **Message actions**: long press → reply, copy, delete

Output: complete chat screen component.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
