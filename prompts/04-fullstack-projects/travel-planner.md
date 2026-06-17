---
title: "Build an AI Travel Planner"
category: fullstack-projects
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [travel, ai, fullstack, maps]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build an AI-powered travel itinerary planner.

Stack: Next.js + Claude API + PostgreSQL + MapBox

Features:
1. Input: destination, dates, number of travelers, budget, interests
2. AI generation: Claude generates day-by-day itinerary
3. Itinerary display: timeline view with activities, restaurants, hotels
4. Map integration: plot all locations on interactive map
5. Save itinerary to account
6. Edit: add/remove/reorder activities
7. Collaboration: share with travel companions (they can suggest edits)
8. Export: PDF itinerary + calendar events (.ics)
9. Packing list: AI-generated based on destination + activities
10. Budget breakdown: estimated costs per day

Claude prompt engineering: get structured JSON itinerary.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
