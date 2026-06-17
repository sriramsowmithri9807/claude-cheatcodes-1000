---
title: "Design Information Architecture"
category: ui-ux-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [ia, navigation, ux, structure]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design the information architecture for my application.

App: [DESCRIBE YOUR APP AND ITS MAIN FEATURES]
Users: [DESCRIBE YOUR USER TYPES AND THEIR GOALS]

1. **Card sorting** (mental model):
   - List all features/content in your app
   - Group them as a user would
   - Identify naming conventions users expect
2. **Hierarchy**: organize content into logical tree
3. **Navigation patterns**:
   - Primary: top bar / sidebar / bottom tabs
   - Secondary: breadcrumbs, tabs, sub-navigation
   - Utility: search, profile, settings
4. **Labeling**: names that match user mental models
5. **Progressive disclosure**: hide complexity until needed
6. **Search**: when navigation alone isn't enough
7. **Cross-linking**: related content links between sections
8. **Mobile vs desktop**: different IA for different contexts
9. **Sitemap**: visual map of all pages and relationships
10. **Navigation test**: can users find key items in < 3 clicks?

Output: sitemap + navigation design.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
