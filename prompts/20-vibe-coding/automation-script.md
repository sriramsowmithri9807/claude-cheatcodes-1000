---
title: "Write an Automation Script"
category: vibe-coding
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [automation, scripting, productivity, python]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Write an automation script to save me time.

Task to automate: [DESCRIBE WHAT YOU DO MANUALLY]
Current time cost: [HOW LONG IT TAKES MANUALLY]
Frequency: [HOW OFTEN YOU DO IT]

Automation approach:
1. Break down the manual steps
2. Identify the technical approach for each step
3. Write the script
4. Test with a small example first
5. Add error handling
6. Schedule it (cron, GitHub Actions, etc.)

Common automation categories:
- **File processing**: rename, move, convert files
- **Web scraping**: extract data from websites
- **API integration**: connect two services
- **Email/Slack**: send notifications or reports
- **Data transformation**: CSV → database, API → spreadsheet
- **Deployment**: automate repetitive dev tasks

Preferred language: Python (most automation libraries, readable)

Output: complete script that I can run immediately + cron expression if it should be scheduled.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
