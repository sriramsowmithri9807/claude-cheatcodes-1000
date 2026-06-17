---
title: "Implement Background Job Queues"
category: backend-dev
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [bullmq, redis, queues, nodejs]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Implement a background job processing system using BullMQ + Redis.

Jobs to process: [LIST YOUR BACKGROUND TASKS]

Implement:
1. Queue setup for each job type
2. Job producers (enqueue jobs from API)
3. Job workers (process jobs with error handling)
4. Retry strategy (exponential backoff, max attempts)
5. Priority queues (some jobs more urgent)
6. Scheduled/cron jobs (repeat on schedule)
7. Progress tracking (update frontend via WebSocket)
8. Bull Board UI for monitoring queues
9. Graceful worker shutdown
10. Dead letter queue for failed jobs
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
