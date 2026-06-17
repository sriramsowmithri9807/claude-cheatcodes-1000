---
title: "Add Maps to React Native App"
category: mobile-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react-native, maps, mapbox, location]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Add maps and location features to my React Native app.

Features: [DESCRIBE: show user location, display markers, route, geofencing]

Using: react-native-maps (Google Maps / Apple Maps) or Mapbox

1. **Location permission**: request in foreground and background
2. **User location**: show blue dot, center on user
3. **Map markers**: custom markers with callouts
4. **Polylines**: draw route on map
5. **Clustering**: cluster nearby markers at low zoom
6. **Offline maps**: cache map tiles
7. **Geofencing**: alert when user enters/exits area
8. **Address search**: autocomplete address input
9. **Reverse geocode**: coords → human readable address
10. **Directions**: turn-by-turn (integrate with Google Maps / Apple Maps app)

Performance: limit re-renders when location updates frequently.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
