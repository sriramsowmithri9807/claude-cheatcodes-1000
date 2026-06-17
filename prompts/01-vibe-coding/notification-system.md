---
title: "Build an In-App Notification System"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [notifications, react, backend, real-time]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a complete in-app notification system.

Backend (Node.js):
- Notification model with: type, title, body, read status, userId, createdAt
- Polymorphic target (comment notification vs system alert vs mention)
- Bulk create API for fan-out to many users
- Mark read/unread, mark all read
- Real-time delivery via WebSocket

Frontend (React):
- Bell icon with unread count badge
- Dropdown panel with notification list
- Notification item with icon, text, time ago, read indicator
- Infinite scroll for history
- Sound + browser push notifications (with permission)
- Toast for new notifications while browsing

Include database migration and the complete API + UI code.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
