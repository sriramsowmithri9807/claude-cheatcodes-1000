---
title: "Write Better Changelogs"
category: documentation
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [changelog, documentation, releases, communication]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Write user-facing changelogs for my releases.

Current release notes/changelog: [PASTE OR DESCRIBE]
Changes in this release: [LIST YOUR CHANGES]

Changelog principles (Keep a Changelog):
1. **For humans, not computers**: don't paste git log
2. **Latest first**: newest version at top
3. **Types**: Added, Changed, Deprecated, Removed, Fixed, Security
4. **User perspective**: how does this change affect me?
5. **Link to issues/PRs**: for users who want details

Examples of good vs bad:
- Bad: 'Fix bug in user module'
- Good: 'Fixed an issue where saving your profile photo would fail for images larger than 10MB'

For each change in my release:
6. Categorize it correctly
7. Rewrite it from the user's perspective
8. Note any migration steps needed
9. Link relevant documentation

Output: formatted CHANGELOG.md section for my release.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
