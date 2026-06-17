---
title: "Process Big Data with PySpark"
category: data-science
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [spark, big-data, python, distributed]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Process big data with PySpark.

Data size: [DESCRIBE: TB/PB scale]
Processing goal: [DESCRIBE: ETL, ML, aggregation, stream processing]

PySpark fundamentals:
1. **SparkContext vs SparkSession**: use SparkSession
2. **DataFrames**: preferred over RDDs for structured data
3. **Schema definition**: explicit schema for reliability
4. **Reading data**: parquet, CSV, JSON from S3/HDFS
5. **Transformations**: select, filter, groupBy, agg, join
6. **Actions**: collect, show, count, write
7. **Partitioning**: repartition vs coalesce
8. **Caching**: .cache() and .persist() strategy
9. **Broadcast join**: when one table is small
10. **UDFs**: user-defined functions (prefer built-in over UDF)

Performance:
11. Avoid shuffles (group by, join) when possible
12. EXPLAIN plan: read the query execution plan
13. Adaptive Query Execution (Spark 3+)

Output: PySpark script for my processing job.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
