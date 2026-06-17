---
title: "Build a Cron Job Scheduler"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [cron, nodejs, scheduler, backend]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Build a reliable cron job scheduler system.

Jobs to schedule: [LIST YOUR RECURRING TASKS]

Using: node-cron or BullMQ repeatable jobs

Implement:
1. Job registration system (define jobs with cron expressions)
2. Distributed lock (only one instance runs each job in a cluster)
3. Job history: track last run, duration, success/failure
4. Alerting: notify on job failure
5. Manual trigger: run a job on demand via API
6. Cron expression validator and human-readable description
7. Graceful shutdown: finish running job before stopping
8. Job timeout: kill jobs that run too long
9. Dashboard API to view job status
10. Retry on failure with backoff
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
