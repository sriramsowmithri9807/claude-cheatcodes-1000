# 15-data-science

Pandas, scikit-learn, PyTorch, forecasting, churn/fraud models, EDA, dashboards with Streamlit/Plotly.

25 prompts. Search `## ` headings or ids; see index.md for the one-line list.

## Design and Analyze A/B Tests

**id:** `15-data-science/a-b-testing` · **Difficulty:** advanced · **Tags:** ab-testing, statistics, experiments, data-science

**Placeholders:** [DESCRIBE WHAT YOU'RE TESTING]

````text
Design and analyze A/B tests rigorously.

Feature to test: [DESCRIBE WHAT YOU'RE TESTING]
Metric: [PRIMARY METRIC + GUARDRAIL METRICS]

**Experiment design**:
1. **Hypothesis**: null hypothesis + alternative hypothesis
2. **Sample size**: power analysis (80% power, α=0.05)
   - `scipy.stats.t`: compute minimum sample size
3. **Randomization unit**: user, session, device
4. **Duration**: run for minimum N weeks (capture weekly seasonality)
5. **Segments**: check if effect varies by user segment

**Analysis**:
6. **SRM check**: sample ratio mismatch (control/treatment equal?)
7. **Statistical test**: t-test, Mann-Whitney, z-test for proportions
8. **p-value and CI**: report both (CI is more informative)
9. **Effect size**: Cohen's d or relative lift
10. **Multiple testing**: Bonferroni correction for multiple metrics

**Decision**:
11. Did it win? Statistical + practical significance
12. Ship, iterate, or stop?
13. Post-ship monitoring: sustain the lift?

Output: Python analysis notebook.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build an Anomaly Detection System

**id:** `15-data-science/anomaly-detection` · **Difficulty:** advanced · **Tags:** anomaly-detection, machine-learning, monitoring, python

**Placeholders:** [DESCRIBE ANOMALIES: fraud, system failures, unusual behavior], [DESCRIBE: time series metrics / transaction data / sensor data]

````text
Build an anomaly detection system.

Data: [DESCRIBE: time series metrics / transaction data / sensor data]
What to detect: [DESCRIBE ANOMALIES: fraud, system failures, unusual behavior]

Methods:
1. **Statistical**: z-score, IQR for simple cases
2. **Isolation Forest**: tree-based, good for high-dimensional
3. **Autoencoder**: neural network, high reconstruction error = anomaly
4. **LSTM**: for sequential/time-series anomalies
5. **LOF (Local Outlier Factor)**: density-based
6. **Prophet**: anomalies vs seasonal forecast
7. **DBSCAN**: clustering-based outlier detection

For time series specifically:
8. Changepoint detection (ruptures library)
9. Seasonal decomposition → residual anomaly
10. Alert thresholds: dynamic vs static
11. Alert fatigue: tune to minimize false positives

Evaluation:
12. Label known anomalies, measure precision/recall
13. Tune threshold: precision-recall trade-off

Output: production anomaly detection pipeline.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Clean Messy Datasets

**id:** `15-data-science/data-cleaning` · **Difficulty:** beginner · **Tags:** data-cleaning, pandas, etl, python

**Placeholders:** [DESCRIBE THE MESS: missing values, duplicates, inconsistent formats, outliers]

````text
Clean this messy dataset.

Dataset: [DESCRIBE THE MESS: missing values, duplicates, inconsistent formats, outliers]

Data cleaning steps:
1. **Duplicates**: find and remove (or flag) duplicate rows
2. **Missing values**:
   - Structural missingness: MCAR, MAR, MNAR analysis
   - Strategy: drop, fill with mean/median/mode, interpolate, or flag
3. **Inconsistent formats**:
   - Dates: standardize to ISO 8601
   - Categories: 'NY', 'New York', 'new york' → 'New York'
   - Phone numbers, addresses: standardize
4. **Outliers**: IQR method, isolation forest, visual inspection
5. **Type corrections**: strings that should be numbers, dates as strings
6. **Invalid values**: negative ages, future dates, impossible values
7. **Case normalization**: all lowercase for text comparisons
8. **Whitespace**: strip leading/trailing spaces
9. **Unicode**: normalize unicode characters
10. **Schema validation**: check all columns after cleaning

Output: cleaning script + before/after statistics.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Apply Data Engineering Patterns

**id:** `15-data-science/data-engineering-patterns` · **Difficulty:** advanced · **Tags:** data-engineering, patterns, etl, architecture

**Placeholders:** [DESCRIBE YOUR DATA INFRASTRUCTURE]

````text
Apply data engineering patterns to my data platform.

Current situation: [DESCRIBE YOUR DATA INFRASTRUCTURE]

1. **Lambda Architecture**: batch (accurate) + speed (real-time) layers
2. **Kappa Architecture**: everything as stream (simpler)
3. **Data Lakehouse**: structured data in data lake (Delta Lake, Apache Iceberg)
4. **Medallion Architecture**: Bronze (raw) → Silver (clean) → Gold (aggregated)
5. **CDC (Change Data Capture)**: Debezium → Kafka → warehouse
6. **Slowly Changing Dimensions**: SCD Type 2 for historical accuracy
7. **Idempotent pipelines**: safe to rerun without side effects
8. **Data contracts**: schema agreements between producers and consumers
9. **Backfill strategy**: re-process historical data when logic changes
10. **Data catalog**: document all datasets with lineage

For my platform: which patterns to adopt in which order.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build an ETL Data Pipeline

**id:** `15-data-science/data-pipeline` · **Difficulty:** advanced · **Tags:** etl, data-pipeline, airflow, python

**Placeholders:** [DATA WAREHOUSE / LAKE / DATABASE], [DESCRIBE YOUR DATA SOURCES], [HOURLY / DAILY / REAL-TIME]

````text
Build a production ETL data pipeline.

Sources: [DESCRIBE YOUR DATA SOURCES]
Destination: [DATA WAREHOUSE / LAKE / DATABASE]
Schedule: [HOURLY / DAILY / REAL-TIME]

Pipeline design:
1. **Extract**: connect to sources, handle authentication, pagination
2. **Transform**:
   - Schema normalization
   - Data type coercion
   - Business rules application
   - Deduplication
   - Validation
3. **Load**: upsert to destination, handle conflicts

Reliability:
4. **Idempotency**: safe to run multiple times
5. **Incremental loading**: only process new/changed records
6. **Checkpointing**: resume from failure point
7. **Alerting**: fail loudly with clear error messages

Orchestration (Apache Airflow):
8. DAG structure and dependencies
9. Retry policy
10. SLA monitoring
11. Backfill strategy

Output: Airflow DAG + Python transform functions.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement Data Quality Monitoring

**id:** `15-data-science/data-quality` · **Difficulty:** advanced · **Tags:** data-quality, great-expectations, monitoring, validation

**Placeholders:** [DESCRIBE YOUR DATA AND PIPELINE]

````text
Implement data quality monitoring for my data pipeline.

Data: [DESCRIBE YOUR DATA AND PIPELINE]

Using: Great Expectations

1. **Expectation suites**: define what 'good data' looks like
2. **Column expectations**:
   - not null: critical columns always have values
   - unique: primary keys are unique
   - between: numeric values in valid range
   - in set: categorical values are valid options
   - regex: strings match expected format
3. **Distribution expectations**: mean within ±2σ of baseline
4. **Completeness**: row count within N% of yesterday
5. **Freshness**: latest timestamp within N hours

Pipeline integration:
6. Validate at ingestion (fail fast before processing)
7. Validate before loading to warehouse
8. Data docs: auto-generated HTML report
9. Alerting: Slack when expectations fail
10. Quarantine: move bad records aside, don't fail entire pipeline

Output: Great Expectations suite for my data.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Create Data Visualizations

**id:** `15-data-science/data-visualization` · **Difficulty:** intermediate · **Tags:** visualization, matplotlib, plotly, python

**Placeholders:** [DESCRIBE YOUR DATA], [TECHNICAL / BUSINESS STAKEHOLDERS], [WHAT STORY DO YOU WANT TO TELL]

````text
Create professional data visualizations.

Data to visualize: [DESCRIBE YOUR DATA]
Audience: [TECHNICAL / BUSINESS STAKEHOLDERS]
Visualization goals: [WHAT STORY DO YOU WANT TO TELL]

Visualization types with code:
1. **Line chart**: trends over time
2. **Bar chart**: compare categories (horizontal for long labels)
3. **Scatter plot**: correlation between two variables
4. **Histogram**: distribution of one variable
5. **Box plot**: distribution with outliers
6. **Heatmap**: correlation matrix, confusion matrix
7. **Sankey diagram**: flow between states
8. **Geospatial**: choropleth map with plotly
9. **Dashboard**: Plotly Dash or Streamlit interactive dashboard
10. **Animation**: animated chart showing change over time

Design principles:
11. Less is more: remove chart junk
12. Color: meaningful, accessible palette
13. Annotations: highlight key insights
14. Titles: answer the question, not just label the axes

Using: Plotly Express + Matplotlib.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Write Data Warehouse Queries

**id:** `15-data-science/data-warehouse-query` · **Difficulty:** intermediate · **Tags:** sql, data-warehouse, analytics, bigquery

**Placeholders:** [LIST THE QUESTIONS TO ANSWER], [PASTE YOUR TABLE SCHEMAS]

````text
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
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build dbt Data Models

**id:** `15-data-science/dbt-models` · **Difficulty:** advanced · **Tags:** dbt, analytics, sql, data-warehouse

**Placeholders:** [DESCRIBE WHAT STAKEHOLDERS NEED], [DESCRIBE YOUR RAW TABLES]

````text
Build dbt data models for my analytics.

Raw sources: [DESCRIBE YOUR RAW TABLES]
Analytics questions: [DESCRIBE WHAT STAKEHOLDERS NEED]

dbt project structure:
```
models/
  staging/        # 1:1 with source, light cleaning
    stg_users.sql
    stg_orders.sql
  intermediate/   # Business logic
    int_user_orders.sql
  marts/          # Final tables for BI
    dim_users.sql
    fct_orders.sql
```

Best practices:
1. Staging models: rename columns, cast types, no joins
2. Intermediate: join, filter, basic aggregations
3. Mart models: wide tables ready for BI (metrics pre-computed)
4. `ref()`: always reference other models with ref()
5. `source()`: reference raw tables with source()
6. Tests: not_null, unique, accepted_values, relationships
7. Documentation: description for every model and column
8. Macros: reusable SQL snippets

Output: complete dbt project for my use case.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build Deep Learning Models with PyTorch

**id:** `15-data-science/deep-learning-pytorch` · **Difficulty:** advanced · **Tags:** pytorch, deep-learning, neural-networks, python

**Placeholders:** [DESCRIBE: image classification, NLP, tabular, custom architecture], [DESCRIBE]

````text
Build a deep learning model with PyTorch.

Task: [DESCRIBE: image classification, NLP, tabular, custom architecture]
Dataset: [DESCRIBE]

Implementation:
1. **Dataset class**: `torch.utils.data.Dataset` for your data
2. **DataLoader**: batching, shuffling, num_workers
3. **Model architecture**: `nn.Module` subclass
4. **Loss function**: CrossEntropyLoss, MSELoss, etc.
5. **Optimizer**: Adam with weight decay, learning rate scheduler
6. **Training loop**:
   - Forward pass
   - Loss computation
   - Backward pass
   - Optimizer step
   - Gradient clipping
7. **Validation loop**: no_grad, eval mode
8. **Checkpointing**: save/load best model
9. **Metrics**: accuracy, AUC, etc. per epoch
10. **TensorBoard**: log loss and metrics
11. **GPU**: `.to(device)`, CUDA availability check
12. **Mixed precision**: `torch.autocast` for speed

Output: complete training script for my task.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Perform Exploratory Data Analysis

**id:** `15-data-science/exploratory-analysis` · **Difficulty:** intermediate · **Tags:** eda, pandas, data-science, python

**Placeholders:** [DESCRIBE YOUR DATA OR PASTE FIRST FEW ROWS], [WHAT BUSINESS QUESTION ARE YOU TRYING TO ANSWER]

````text
Perform exploratory data analysis on my dataset.

Dataset: [DESCRIBE YOUR DATA OR PASTE FIRST FEW ROWS]
Goal: [WHAT BUSINESS QUESTION ARE YOU TRYING TO ANSWER]

EDA steps:
1. **Shape**: rows, columns, memory usage
2. **Data types**: check dtypes, fix miscasts
3. **Missing values**: count per column, visualize with heatmap
4. **Distributions**: histograms for numeric, bar charts for categorical
5. **Outliers**: boxplots, IQR method, z-score detection
6. **Correlations**: correlation matrix heatmap
7. **Target analysis**: distribution of target variable
8. **Feature relationships**: scatter plots, grouped statistics
9. **Time trends**: if time-series, plot over time
10. **Summary statistics**: mean, median, std, min/max per column

Output: complete Jupyter notebook with all plots and insights.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Master Feature Engineering

**id:** `15-data-science/feature-engineering` · **Difficulty:** advanced · **Tags:** feature-engineering, machine-learning, pandas, python

**Placeholders:** [DESCRIBE WHAT YOU'RE PREDICTING], [DESCRIBE YOUR COLUMNS], [SPECIFIC TO YOUR DOMAIN]

````text
Apply advanced feature engineering to my dataset.

Raw features: [DESCRIBE YOUR COLUMNS]
Target: [DESCRIBE WHAT YOU'RE PREDICTING]
Domain: [e.g., e-commerce, healthcare, finance]

Feature engineering techniques:
1. **Interaction features**: multiply/divide two features
2. **Polynomial features**: x^2, x^3 for non-linear relationships
3. **Binning**: convert continuous to bins (age groups)
4. **Log transform**: handle skewed distributions
5. **Ratios**: relative metrics (conversion rate, revenue per user)
6. **Lag features**: previous N timesteps (time-series)
7. **Rolling statistics**: 7-day rolling mean, max, std
8. **Target encoding**: encode categorical with target mean (careful of leakage)
9. **Embeddings**: text → dense vector features
10. **Clustering features**: cluster assignment as feature
11. **Domain features**: [SPECIFIC TO YOUR DOMAIN]

For each feature: why it might help + implementation + how to validate it improves model.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Write Better Jupyter Notebooks

**id:** `15-data-science/jupyter-best-practices` · **Difficulty:** beginner · **Tags:** jupyter, notebooks, data-science, best-practices

**Placeholders:** [DESCRIBE WHAT YOUR NOTEBOOK DOES]

````text
Apply best practices to my Jupyter notebooks.

Current notebook: [DESCRIBE WHAT YOUR NOTEBOOK DOES]

Notebook quality improvements:
1. **Structure**: introduction → data → analysis → conclusions
2. **Markdown**: rich text cells explaining the story (not just code)
3. **Cell size**: one logical step per cell
4. **Reproducibility**: set random seeds, specify package versions
5. **Dependencies**: requirements.txt or conda environment.yml
6. **Data paths**: use relative paths, document where data comes from
7. **Function extraction**: move reusable code to .py files
8. **Output management**: clear outputs before committing to git
9. **nbstripout**: git hook to strip outputs automatically
10. **Parameterization**: Papermill for parameterized notebook runs

Conversion to production:
11. Extract core logic to Python module
12. Keep notebook as documentation/analysis only
13. Schedule with Airflow using PapermillOperator

Output: refactored notebook following all best practices.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build a Machine Learning Pipeline

**id:** `15-data-science/ml-pipeline` · **Difficulty:** advanced · **Tags:** machine-learning, scikit-learn, pipeline, python

**Placeholders:** [CLASSIFICATION / REGRESSION / CLUSTERING], [DESCRIBE: size, features, target]

````text
Build a production-ready machine learning pipeline.

Problem type: [CLASSIFICATION / REGRESSION / CLUSTERING]
Dataset: [DESCRIBE: size, features, target]
Success metric: [ACCURACY / AUC / RMSE / etc.]

Pipeline steps:
1. **Data loading**: from CSV/database/API
2. **Feature engineering**: create new features from raw data
3. **Preprocessing**:
   - Numeric: StandardScaler or MinMaxScaler
   - Categorical: OneHotEncoder or OrdinalEncoder
   - Missing values: SimpleImputer or IterativeImputer
4. **Model selection**: try 3-5 algorithms
5. **Cross-validation**: 5-fold CV for model evaluation
6. **Hyperparameter tuning**: RandomizedSearchCV or Optuna
7. **Model interpretation**: feature importance, SHAP values
8. **Evaluation**: confusion matrix, classification report
9. **Serialization**: joblib save/load
10. **Inference**: predict on new data

Using: scikit-learn Pipeline for reproducibility.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Track ML Experiments with MLflow

**id:** `15-data-science/mlflow-experiment-tracking` · **Difficulty:** intermediate · **Tags:** mlflow, experiment-tracking, mlops, python

**Placeholders:** [DESCRIBE YOUR MODEL TRAINING PROCESS]

````text
Set up ML experiment tracking with MLflow.

ML workflow: [DESCRIBE YOUR MODEL TRAINING PROCESS]

1. **MLflow setup**: local tracking server or Databricks
2. **Experiment**: group of runs with the same goal
3. **Run**: single training run with params + metrics
4. **Log parameters**: hyperparameters for this run
5. **Log metrics**: training + validation metrics each epoch
6. **Log artifacts**: model file, plots, feature importance
7. **Log model**: versioned model with schema
8. **Tags**: run metadata (git commit, dataset version)

Best practices:
9. **Autologging**: `mlflow.sklearn.autolog()` for auto-tracking
10. **Model registry**: promote best model to staging → production
11. **Comparison**: compare metrics across runs in UI
12. **Reproducibility**: log data version, random seed, environment

Integrate with:
13. scikit-learn: autolog
14. PyTorch: log epoch metrics
15. Optuna: log hyperparameter search

Output: complete MLflow-instrumented training script.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Evaluate and Compare ML Models

**id:** `15-data-science/model-evaluation` · **Difficulty:** advanced · **Tags:** evaluation, machine-learning, metrics, python

**Placeholders:** [BINARY CLASSIFICATION / MULTI-CLASS / REGRESSION], [LIST YOUR CANDIDATE MODELS]

````text
Evaluate and compare machine learning models rigorously.

Models to compare: [LIST YOUR CANDIDATE MODELS]
Problem type: [BINARY CLASSIFICATION / MULTI-CLASS / REGRESSION]

**For classification**:
1. **Accuracy**: misleading for imbalanced classes
2. **Precision, Recall, F1**: trade-off based on business need
3. **AUC-ROC**: discriminative ability (threshold-independent)
4. **PR-AUC**: better for imbalanced datasets
5. **Confusion matrix**: understand error types
6. **Calibration**: predicted probabilities vs actual (Platt scaling)

**For regression**:
7. **MAE**: robust to outliers
8. **RMSE**: penalizes large errors more
9. **MAPE**: relative error (interpretable as %)
10. **R²**: variance explained

**Statistical comparison**:
11. McNemar's test: are two classifiers significantly different?
12. Cross-validation variance: is one model more stable?
13. Learning curves: is model underfitting or overfitting?

Output: model comparison table + visualization.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Process and Analyze Text Data

**id:** `15-data-science/nlp-text-processing` · **Difficulty:** intermediate · **Tags:** nlp, text-processing, spacy, python

**Placeholders:** [DESCRIBE YOUR TEXT: customer reviews, news articles, tweets, documents], [DESCRIBE: sentiment, topic, classification, entity extraction]

````text
Process and analyze text data with NLP techniques.

Text data: [DESCRIBE YOUR TEXT: customer reviews, news articles, tweets, documents]
Goal: [DESCRIBE: sentiment, topic, classification, entity extraction]

Processing pipeline:
1. **Cleaning**: lowercase, remove HTML, special chars
2. **Tokenization**: split into words/sentences
3. **Stop word removal**: remove common uninformative words
4. **Stemming/Lemmatization**: reduce to base form

Analysis:
5. **TF-IDF**: term frequency - inverse document frequency
6. **Topic modeling**: LDA for discovering topics
7. **Named Entity Recognition**: extract people, orgs, places
8. **Sentiment analysis**: VADER for lexicon, transformers for ML
9. **Text classification**: train classifier on labeled examples
10. **Word embeddings**: Word2Vec, GloVe, or sentence transformers
11. **Text similarity**: cosine similarity between documents
12. **Summarization**: extractive vs abstractive

Using: spaCy + HuggingFace transformers.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Master Pandas Data Manipulation

**id:** `15-data-science/pandas-mastery` · **Difficulty:** intermediate · **Tags:** pandas, data-manipulation, python, data-science

**Placeholders:** [DESCRIBE WHAT YOU NEED TO DO WITH THE DATA], [DESCRIBE YOUR DATAFRAME]

````text
Master pandas for data manipulation and analysis.

Dataset: [DESCRIBE YOUR DATAFRAME]
Task: [DESCRIBE WHAT YOU NEED TO DO WITH THE DATA]

Pandas techniques to apply:
1. **Filtering**: boolean indexing, query(), isin()
2. **Groupby**: groupby + agg with multiple functions
3. **Pivot tables**: pivot_table() for cross-tabulation
4. **Merge/Join**: merge() types (inner, left, outer)
5. **String operations**: .str accessor, regex extraction
6. **DateTime**: parse dates, resample, rolling windows
7. **Apply**: apply() vs vectorized operations (performance)
8. **Stack/Unstack**: reshaping wide to long and back
9. **Missing data**: fillna(), interpolate(), dropna()
10. **Window functions**: rolling(), expanding(), ewm()
11. **Categorical**: convert to Categorical for memory + performance
12. **Performance**: use numpy where possible, avoid iterrows

For each: show the correct pandas pattern + common mistakes.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build a Recommender System

**id:** `15-data-science/recommender-system` · **Difficulty:** advanced · **Tags:** recommendations, collaborative-filtering, machine-learning, python

**Placeholders:** [DESCRIBE: user-item interactions, ratings, purchase history, content features], [MOVIES / PRODUCTS / CONTENT / USERS TO FOLLOW]

````text
Build a recommender system.

Data available: [DESCRIBE: user-item interactions, ratings, purchase history, content features]
Recommendation goal: [MOVIES / PRODUCTS / CONTENT / USERS TO FOLLOW]

Approaches:
1. **Collaborative filtering**: users who liked X also liked Y
   - Memory-based: user-user, item-item similarity
   - Model-based: matrix factorization (SVD, ALS)
2. **Content-based**: recommend similar items to what user liked
3. **Hybrid**: combine collaborative + content
4. **Neural**: two-tower model (embedding user + item)

Implement:
5. Surprise or implicit library for collaborative filtering
6. Cosine similarity for item-to-item
7. Evaluation: NDCG@K, Recall@K, Precision@K
8. Cold start: handle new users and new items
9. Diversity: don't just recommend safe choices
10. A/B test: measure click-through improvement

Output: working recommender + evaluation pipeline.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build Scikit-Learn Pipelines

**id:** `15-data-science/scikit-learn-pipeline` · **Difficulty:** intermediate · **Tags:** scikit-learn, pipeline, machine-learning, python

**Placeholders:** [DESCRIBE YOUR ML TASK], [LIST YOUR FEATURE TYPES: numeric, categorical, text, dates]

````text
Build scikit-learn Pipelines for reproducible ML workflows.

Problem: [DESCRIBE YOUR ML TASK]
Features: [LIST YOUR FEATURE TYPES: numeric, categorical, text, dates]

Pipeline construction:
1. **ColumnTransformer**: different processing per feature type
2. **Numeric**: StandardScaler or RobustScaler
3. **Categorical**: OneHotEncoder or OrdinalEncoder
4. **Text**: TfidfVectorizer
5. **Missing**: SimpleImputer before transformers
6. **Estimator**: your chosen model at the end

Benefits:
7. **No data leakage**: fit only on training data
8. **Cross-validation**: Pipeline + cross_val_score
9. **Hyperparameter tuning**: GridSearchCV with pipeline params
10. **Serialization**: `joblib.dump(pipeline, 'model.pkl')`
11. **Inference**: `pipeline.predict(new_data)` handles all transforms

Output: complete Pipeline for my ML task.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Process Big Data with PySpark

**id:** `15-data-science/spark-big-data` · **Difficulty:** advanced · **Tags:** spark, big-data, python, distributed

**Placeholders:** [DESCRIBE: ETL, ML, aggregation, stream processing], [DESCRIBE: TB/PB scale]

````text
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
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Perform Statistical Analysis

**id:** `15-data-science/statistical-analysis` · **Difficulty:** advanced · **Tags:** statistics, scipy, hypothesis-testing, python

**Placeholders:** [DESCRIBE YOUR DATA], [WHAT STATISTICAL QUESTION ARE YOU ASKING]

````text
Perform rigorous statistical analysis.

Data: [DESCRIBE YOUR DATA]
Question: [WHAT STATISTICAL QUESTION ARE YOU ASKING]

**Descriptive statistics**:
1. Central tendency: mean, median, mode
2. Spread: variance, std, IQR, range
3. Shape: skewness, kurtosis
4. Confidence intervals for each statistic

**Hypothesis testing**:
5. Choose the right test:
   - t-test: compare two means
   - ANOVA: compare multiple means
   - Chi-squared: categorical association
   - Wilcoxon: non-parametric alternative
6. Check assumptions before running test
7. Interpret p-value correctly (not binary threshold)
8. Report effect size (not just p-value)
9. Statistical power: did you have enough data?

**Common analyses**:
10. A/B test analysis with confidence intervals
11. Correlation analysis with significance testing
12. Regression analysis with diagnostics

Output: analysis notebook with interpretation.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build a Time Series Forecasting Model

**id:** `15-data-science/time-series-ml` · **Difficulty:** advanced · **Tags:** time-series, forecasting, prophet, python

**Placeholders:** [DESCRIBE YOUR TIME SERIES: what you're measuring, frequency, history length], [HOW FAR AHEAD TO PREDICT], [MAPE / MAE / RMSE]

````text
Build a time series forecasting model.

Data: [DESCRIBE YOUR TIME SERIES: what you're measuring, frequency, history length]
Forecast horizon: [HOW FAR AHEAD TO PREDICT]
Metric: [MAPE / MAE / RMSE]

Approaches:
1. **Baseline**: seasonal naive, simple average
2. **Statistical**: ARIMA, SARIMA (statsmodels)
3. **Machine Learning**: LightGBM with lag features
4. **Deep Learning**: LSTM / Temporal Fusion Transformer
5. **Meta-learning**: Prophet (Facebook, good for business metrics with seasonality)

For Prophet:
6. Trend, seasonality (weekly, yearly)
7. Holiday effects
8. Changepoints
9. Forecasting and uncertainty intervals
10. Cross-validation with time-series split (no data leakage)

Evaluate:
11. Time-series cross-validation
12. Plot forecast vs actual
13. Error analysis: where does the model fail?
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build a [ML_TASK] pipeline with [LIBRARY]

**id:** `15-data-science/build-a-ml-task-pipeline-with-library` · **Difficulty:** beginner/advanced · **Tags:** machine-learning, data-analysis, streamlit, python, data-science, customer, plotly, fraud, pytorch, image, pandas, text, tensorflow, user, scikit-learn, weekly

**Variant group** (12 generated prompts collapsed). Pick one value per placeholder:
- `[LIBRARY]`: Pandas | Plotly Express | PyTorch | Scikit-Learn | Streamlit dashboarding | TensorFlow
- `[ML_TASK]`: customer churn predictions | fraud anomaly detection | image objects classification | text sentiments reviews analysis | user demographics clustering | weekly demand time series forecasting
- `[ML_FEATURE]`: automated feature engineering pipelines | hyperparameters tuning steps | k-fold cross-validation runs | metrics evaluation charts | model checkpointing mechanisms

````text
Build a python data science script to execute [ML_TASK] utilizing [LIBRARY]. Make sure to include [ML_FEATURE] for accuracy.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** build-a-customer-churn-predictions-pipeline-with-streamlit-dashboarding, build-a-fraud-anomaly-detection-pipeline-with-plotly-express, build-a-fraud-anomaly-detection-pipeline-with-pytorch, build-a-fraud-anomaly-detection-pipeline-with-streamlit-dashboarding, build-a-image-objects-classification-pipeline-with-pandas, build-a-image-objects-classification-pipeline-with-plotly-express, build-a-image-objects-classification-pipeline-with-pytorch, build-a-image-objects-classification-pipeline-with-streamlit-dashboarding, build-a-text-sentiments-reviews-analysis-pipeline-with-pytorch, build-a-text-sentiments-reviews-analysis-pipeline-with-tensorflow, build-a-user-demographics-clustering-pipeline-with-plotly-express, build-a-weekly-demand-time-series-forecasting-pipeline-with-scikit-learn


## Create a data visualization dashboard for [ML_TASK] with [LIBRARY]

**id:** `15-data-science/create-a-data-visualization-dashboard-for-ml-task-with-library` · **Difficulty:** beginner/intermediate/advanced · **Tags:** machine-learning, data-analysis, python, pandas, data-science, customer, plotly, tensorflow, fraud, image, user, pytorch, scikit-learn, weekly, streamlit

**Variant group** (15 generated prompts collapsed). Pick one value per placeholder:
- `[LIBRARY]`: Pandas | Plotly Express | PyTorch | Scikit-Learn | Streamlit dashboarding | TensorFlow
- `[ML_TASK]`: customer churn predictions | fraud anomaly detection | image objects classification | user demographics clustering | weekly demand time series forecasting
- `[ML_FEATURE]`: automated feature engineering pipelines | hyperparameters tuning steps | k-fold cross-validation runs | metrics evaluation charts | model checkpointing mechanisms

````text
Build an interactive analytics dashboard for [ML_TASK] using [LIBRARY] with [ML_FEATURE] to represent business insights.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** create-a-data-visualization-dashboard-for-customer-churn-predictions-with-pandas, create-a-data-visualization-dashboard-for-customer-churn-predictions-with-plotly-express, create-a-data-visualization-dashboard-for-customer-churn-predictions-with-tensorflow, create-a-data-visualization-dashboard-for-fraud-anomaly-detection-with-tensorflow, create-a-data-visualization-dashboard-for-image-objects-classification-with-pandas, create-a-data-visualization-dashboard-for-image-objects-classification-with-plotly-express, create-a-data-visualization-dashboard-for-image-objects-classification-with-tensorflow, create-a-data-visualization-dashboard-for-user-demographics-clustering-with-pandas, create-a-data-visualization-dashboard-for-user-demographics-clustering-with-pytorch, create-a-data-visualization-dashboard-for-user-demographics-clustering-with-scikit-learn, create-a-data-visualization-dashboard-for-user-demographics-clustering-with-tensorflow, create-a-data-visualization-dashboard-for-weekly-demand-time-series-forecasting-with-plotly-express, create-a-data-visualization-dashboard-for-weekly-demand-time-series-forecasting-with-pytorch, create-a-data-visualization-dashboard-for-weekly-demand-time-series-forecasting-with-scikit-learn, create-a-data-visualization-dashboard-for-weekly-demand-time-series-forecasting-with-streamlit-dashboarding

