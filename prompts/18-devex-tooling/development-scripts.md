---
title: "Write Useful Development Scripts"
category: devex-tooling
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [scripts, automation, bash, tooling]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Write useful automation scripts for my development workflow.

Project: [DESCRIBE]

Scripts to create:

1. **setup.sh**: bootstrap new developer environment
   - Install dependencies
   - Setup local databases
   - Copy .env.example → .env
   - Run migrations
   - Seed data
   - Start services

2. **reset-db.sh**: reset database to clean state
   - Drop and recreate database
   - Run all migrations
   - Run seeds

3. **generate-migration.sh**: create new migration file
   - Ask for migration name
   - Create timestamped file
   - Open in editor

4. **deploy.sh**: deployment script
   - Run tests
   - Build
   - Deploy
   - Health check
   - Notify Slack

5. **clean.sh**: cleanup script
   - Delete build artifacts
   - Clear caches
   - Optional: reset database

Best practices:
6. `set -e`: exit on error
7. Color output: success=green, error=red
8. Dry run mode: `--dry-run` flag

Output: all scripts for my project.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
