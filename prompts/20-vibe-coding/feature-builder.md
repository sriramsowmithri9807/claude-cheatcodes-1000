---
title: "Build a Feature Fast"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [feature, vibe-coding, productivity, coding]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Help me build this feature quickly.

Existing app: [DESCRIBE YOUR CURRENT APP AND STACK]
Feature to add: [DESCRIBE THE FEATURE]
Priority: [HOW CRITICAL IS THIS]

Fast feature development approach:

1. **Clarify requirements** (15 min):
   - What is the minimum version of this feature?
   - What are the edge cases I can defer?
   - What existing code can I reuse?

2. **Plan the changes** (15 min):
   - Files to create
   - Files to modify
   - API changes needed
   - Database changes (if any)

3. **Build** (focus mode):
   - Database/schema first
   - API/backend second
   - UI third
   - Tests last (or in parallel)

4. **Ship fast**:
   - Feature flag: hide from users until ready
   - Deploy to staging first
   - Quick smoke test
   - Deploy to production

Output: implementation plan + the code for this specific feature.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
