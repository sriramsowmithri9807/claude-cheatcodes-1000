---
title: "Optimize React Native Performance"
category: mobile-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react-native, performance, optimization, mobile]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Optimize my React Native app's performance.

Current issues: [DESCRIBE: slow list, janky animations, slow startup, large bundle]

1. **FlatList optimization**:
   - `getItemLayout` for uniform item heights
   - `keyExtractor` stability
   - `windowSize` tuning
   - `maxToRenderPerBatch`
2. **Memo**: `React.memo`, `useMemo`, `useCallback`
3. **Hermes engine**: enable Hermes for faster JS startup
4. **New Architecture**: enable React Native's new architecture (JSI)
5. **Image optimization**: FastImage, resize before upload, placeholder
6. **Bundle size**: analyze with `react-native-bundle-visualizer`
7. **Animation**: only use Reanimated (runs on UI thread)
8. **FlashList**: replace FlatList for large lists
9. **Startup time**: defer non-critical initialization
10. **Memory**: avoid memory leaks in navigation and event listeners

Profile first with Flipper or Xcode Instruments.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
