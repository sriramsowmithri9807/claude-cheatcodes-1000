---
title: "Design a Data Warehouse"
category: database-design
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [data-warehouse, analytics, dimensional, bigquery]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Design a data warehouse for analytics on my application data.

Sources: [LIST YOUR OPERATIONAL DATABASES]
Analytical questions to answer: [LIST YOUR KEY METRICS]

1. **Star schema design**:
   - Fact tables: [transactions, events, sessions]
   - Dimension tables: users, products, dates, locations
2. **ETL pipeline**: source → transform → load (dbt or Apache Airflow)
3. **Slowly Changing Dimensions (SCD)**: Type 1 vs Type 2 vs Type 3
4. **Incremental loading**: only process new/changed records
5. **Data quality**: validation, deduplication, outlier detection
6. **Aggregations**: pre-compute summary tables for dashboard
7. **Platform**: BigQuery vs Snowflake vs Redshift — which and why

Example SQL queries for your key metrics.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
