---
title: "Build an AI Code Review Tool"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [code-review, claude, ai, development]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build an AI-powered code review tool using Claude.

Review focus: [SECURITY / PERFORMANCE / STYLE / ALL]
Languages: [LIST]

1. **GitHub PR integration**: webhook → fetch diff → analyze → comment
2. **Review prompt**: analyze for bugs, security issues, performance, style
3. **Structured output**: list of issues with: file, line, severity, description, suggestion
4. **Severity levels**: critical (must fix), major (should fix), minor (nice to fix)
5. **Context loading**: load related files for better analysis
6. **Auto-fix suggestions**: generate corrected code for simple issues
7. **False positive reduction**: learn from reviewer dismissals
8. **GitHub PR comments**: post inline comments on specific lines
9. **Summary comment**: overall assessment at top of PR
10. **Rate limiting**: respect both Claude and GitHub API limits

GitHub App implementation.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
