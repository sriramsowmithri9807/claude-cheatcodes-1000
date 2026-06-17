---
title: "Apply Animation Principles to UI"
category: ui-ux-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [animation, ux, motion, design]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Apply the 12 principles of animation to my UI.

App: [DESCRIBE]

**Disney's 12 principles applied to UI**:
1. **Squash and stretch**: buttons compress on press (scale 0.95)
2. **Anticipation**: loading indicator before action starts
3. **Staging**: most important element animates first
4. **Straight ahead vs pose to pose**: CSS transitions vs keyframes
5. **Follow through**: elements overshoot then settle (spring)
6. **Slow in, slow out**: ease-in-out (never linear for UI)
7. **Arcs**: natural curved motion paths (not straight lines)
8. **Secondary action**: smaller elements react to main animation
9. **Timing**: duration = perceived weight (heavy = slower)
10. **Exaggeration**: slightly overdo for delightful feel
11. **Solid drawing**: 3D-aware scale and perspective
12. **Appeal**: animations should feel alive

**UI-specific additions**:
- Duration: 100ms (micro), 200-300ms (standard), 400-600ms (large)
- Easing: spring for physical, ease-out for entrances

Apply to my app's key interactions.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
