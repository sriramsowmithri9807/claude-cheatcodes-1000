---
title: "Write Data Warehouse Queries"
category: data-science
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [sql, data-warehouse, analytics, bigquery]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Write efficient data warehouse queries for business analytics.

Warehouse: [BigQuery / Snowflake / Redshift]
Schema: [PASTE YOUR TABLE SCHEMAS]
Business questions: [LIST THE QUESTIONS TO ANSWER]

Query patterns:
1. **Funnel analysis**: % users completing each step
2. **Cohort analysis**: retention by signup week
3. **LTV (Lifetime Value)**: revenue per cohort over time
4. **Conversion rates**: per channel, per campaign, per product
5. **Day-over-day comparison**: today vs same day last week
6. **Rolling 7/30-day metrics**: active users, revenue
7. **Attribution**: first-touch, last-touch, multi-touch
8. **Session analysis**: events within a user session
9. **Percentile distribution**: p50, p90, p99 of metric
10. **Market basket analysis**: frequently bought together

For each: optimized SQL + explanation + index recommendations.
Performance: avoid SELECT *, use partition pruning.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
