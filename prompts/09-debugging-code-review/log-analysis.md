---
title: "Analyze Logs to Find Root Cause"
category: debugging-code-review
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [logs, debugging, monitoring, analysis]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Analyze these logs to find the root cause of the issue.

Logs:
```
[PASTE LOG OUTPUT]
```

Symptoms reported: [DESCRIBE WHAT USERS EXPERIENCED]
Time of incident: [TIMESTAMP]

1. Identify the first error in the timeline
2. Trace the error propagation through the system
3. Find correlated events before the error (what triggered it?)
4. Identify the root cause vs symptoms
5. Check: is this a known pattern? (OOM, connection exhaustion, timeout cascade)
6. Estimate blast radius: how many users/requests affected?
7. Immediate fix recommendation
8. Long-term fix to prevent recurrence
9. Monitoring: what alert would have caught this earlier?

Formatted as a mini incident report.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
