---
title: "Handle Audio and Video in React Native"
category: mobile-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react-native, audio, video, expo]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Add audio and video capabilities to my React Native app.

Features: [DESCRIBE: music player, video streaming, voice recording, podcast player]

Using: expo-av (or expo-audio + expo-video for newer Expo)

**Audio**:
1. Playback: load, play, pause, seek, speed control
2. Background audio: play while app is backgrounded
3. Lock screen controls: media controls on lock screen
4. Recording: record audio, save to file
5. Streaming: play audio from URL

**Video**:
6. Fullscreen player
7. Custom controls overlay
8. Picture-in-picture (iOS)
9. Video thumbnail generation

**Optimizations**:
10. Buffer management for smooth streaming
11. Quality switching for adaptive bitrate
12. Offline download for later playback

Output: MediaPlayer component with all controls.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
