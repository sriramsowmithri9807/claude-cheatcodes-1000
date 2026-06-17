---
title: "Build a Matching/Dating App"
category: fullstack-projects
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [matching, swipe, fullstack, real-time]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a dating/matching app (Tinder-style).

Stack: React Native (Expo) + Node.js + PostgreSQL + Redis + Socket.io

Core features:
1. Profile: photos, bio, age, location, preferences
2. Discovery: swipe right (like), left (pass), super-like
3. Matching algorithm: only match if both swipe right
4. Chat: real-time messages with Socket.io
5. Photo upload: multiple photos, drag to reorder
6. Geolocation: show profiles within X km
7. Filters: age range, distance, interests
8. Push notifications: new match, new message
9. Boost: increase visibility temporarily
10. Report/block: safety features

Privacy: hide last active time, control who sees your profile.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
