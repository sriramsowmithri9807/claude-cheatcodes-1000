---
title: "Set Up Visual Regression Testing"
category: testing-qa
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [visual-regression, storybook, chromatic, testing]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Set up visual regression testing to catch UI changes.

App: [DESCRIBE]
Option A — Chromatic (Storybook hosted):
1. Connect Storybook to Chromatic
2. GitHub Action: run Chromatic on every PR
3. Review visual diffs in Chromatic UI
4. Approve or reject changes
5. Baseline updates on approval

Option B — Playwright screenshot comparison:
6. Navigate to each page
7. Take screenshot
8. Compare to stored baseline (pixel diff)
9. Fail on diff > threshold
10. Update baselines manually

For Chromatic:
- Install and configure
- Per-story vs per-component tests
- Flaky story handling (animations)
- Interaction tests with Storybook

For Playwright:
- Screenshot strategy (full page vs viewport)
- Mask dynamic content (dates, user names)
- Cross-browser visual testing

Output: complete setup for your chosen option.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
