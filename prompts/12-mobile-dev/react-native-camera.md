---
title: "Add Camera and Media Features"
category: mobile-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react-native, camera, expo, media]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Add camera and media features to my React Native app.

Features needed: [DESCRIBE: photo capture, video, QR scan, face detection]

Using: expo-camera + expo-image-picker + expo-media-library

1. **Camera permissions**: request with usage description
2. **Photo capture**: take photo, display preview, save
3. **Video recording**: start/stop recording
4. **Gallery picker**: select existing photos/videos
5. **Image manipulation**: resize, crop, compress (expo-image-manipulator)
6. **Upload**: multipart upload to backend or S3 presigned URL
7. **QR code scanner**: expo-barcode-scanner
8. **Face detection**: camera + face bounding box
9. **File storage**: save to device gallery (expo-media-library)
10. **Permission flow**: graceful handling when denied

Output: camera screen component + upload integration.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
