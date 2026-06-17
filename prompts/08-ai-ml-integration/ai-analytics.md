---
title: "Add AI-Powered Analytics"
category: ai-ml-integration
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [analytics, ai, claude, insights]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Add AI-powered analytics and insights to my business application.

Data available: [DESCRIBE YOUR METRICS AND DATABASES]
Business questions to answer: [LIST 5-10 KEY BUSINESS QUESTIONS]

1. **Natural language to SQL**: Claude converts business questions to SQL queries
2. **Query execution**: run the SQL safely (read-only role)
3. **Result interpretation**: Claude explains what the numbers mean
4. **Anomaly detection**: flag unusual patterns in metrics
5. **Trend analysis**: identify and explain trends over time
6. **Prediction**: simple forecasting (Claude + statistical method)
7. **Automated insights**: weekly AI-generated insights report
8. **Comparative analysis**: compare periods, segments, cohorts
9. **Root cause analysis**: why did metric X drop this week?
10. **Chart recommendations**: which visualization best shows this data?

Safety: read-only database access, query validation.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
