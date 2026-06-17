---
title: "Build a Recipe Sharing Platform"
category: fullstack-projects
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [recipe, community, nextjs, fullstack]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a recipe sharing platform (like AllRecipes).

Stack: Next.js + PostgreSQL + Cloudinary

Features:
1. Recipe: title, description, ingredients (with amounts), instructions (steps)
2. Media: multiple photos, optional video
3. Tags: cuisine, diet (vegan/gluten-free), meal type, difficulty
4. Servings scaling: user changes servings → amounts scale automatically
5. Save / bookmark recipes
6. Rating and reviews
7. User profiles with collection of recipes
8. Search: full-text + filter by dietary restrictions
9. Meal planner: drag recipes to weekly calendar
10. Shopping list: combine ingredients from planned meals (deduplicate)
11. AI ingredient substitutions (Claude API)
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
