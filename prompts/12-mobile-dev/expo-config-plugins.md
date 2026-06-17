---
title: "Create Expo Config Plugins"
category: mobile-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [expo, config-plugins, native, advanced]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Create an Expo config plugin to add native functionality to my managed Expo app.

Native functionality needed: [DESCRIBE: permission, entitlement, plist entry, Gradle config, native module]

What config plugins are:
- Modify native iOS/Android project WITHOUT ejecting
- Applied during `expo prebuild` (or EAS Build)
- Written in JavaScript/TypeScript

Plugin anatomy:
1. `withAndroidManifest`: add permissions, activities
2. `withInfoPlist`: add iOS permission descriptions
3. `withEntitlements`: add iOS capabilities
4. `withGradleProperties`: modify gradle.properties
5. `withPodfile`: modify Podfile
6. `withXcodeProject`: advanced Xcode modifications

Implement for my use case:
7. Write the plugin function
8. Register in app.json: `"plugins": ["./my-plugin"]`
9. Test: `expo prebuild --clean`
10. Publish: share as npm package

Output: complete config plugin for my native requirement.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
