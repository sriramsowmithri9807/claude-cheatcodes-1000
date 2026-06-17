---
title: "Build a Production Error Boundary System"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [react, error-handling, reliability, monitoring]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a comprehensive error boundary system for a React app.

Implement:
1. Generic `ErrorBoundary` component with fallback UI
2. Route-level error boundaries (one per major section)
3. Component-level granular error boundaries
4. Error reporting to Sentry (or a generic reporter interface)
5. Error recovery (retry button)
6. Different fallback UIs: page-level (full page) vs component-level (inline)
7. Development mode: detailed error info + stack trace
8. Production mode: user-friendly message only
9. Error ID for user to report to support

TypeScript, works with React 18+ (concurrent mode safe).
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for code-heavy tasks
- For extended reasoning on architecture decisions, use Fable 5 with extended thinking
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [01-vibe-coding README](README.md)
