# 06-database-design

Schemas, indexing, migrations, sharding, replication for Postgres, MySQL, MongoDB, Redis, DynamoDB, etc.

38 prompts. Search `## ` headings or ids; see index.md for the one-line list.

## Write Complex Analytical SQL

**id:** `06-database-design/analytical-queries` · **Difficulty:** advanced · **Tags:** sql, analytics, postgresql, reporting

**Placeholders:** [BUSINESS QUESTION 1], [BUSINESS QUESTION 2], [BUSINESS QUESTION 3], [PASTE YOUR SCHEMA]

````text
Write complex analytical SQL queries for my business intelligence needs.

Schema: [PASTE YOUR SCHEMA]
Questions to answer:
1. [BUSINESS QUESTION 1]
2. [BUSINESS QUESTION 2]
3. [BUSINESS QUESTION 3]

For each query:
1. SQL with full explanation of each clause
2. EXPLAIN ANALYZE analysis
3. Index recommendations to optimize it
4. Alternative approaches compared

Concepts to use where appropriate:
- CTEs and recursive CTEs
- Window functions
- ROLLUP and CUBE for multi-dimensional aggregation
- LATERAL joins
- JSON aggregation
- Conditional aggregation (SUM CASE WHEN)
- Materialized views for frequently-run queries
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design a Database Backup Strategy

**id:** `06-database-design/backup-strategy` · **Difficulty:** intermediate · **Tags:** backup, postgresql, disaster-recovery, devops

**Placeholders:** [CURRENT SIZE AND GROWTH RATE]

````text
Design a comprehensive database backup and recovery strategy.

Database: PostgreSQL on [AWS RDS / self-hosted / Supabase]
Data size: [CURRENT SIZE AND GROWTH RATE]
RTO (recovery time objective): [e.g., < 4 hours]
RPO (recovery point objective): [e.g., < 1 hour data loss max]

Implement:
1. **Full backup**: daily, retained 30 days
2. **WAL archiving**: continuous, enables point-in-time recovery
3. **Snapshot backup**: hourly for recent windows
4. **Offsite copies**: 3-2-1 rule (3 copies, 2 media types, 1 offsite)
5. **Encryption**: encrypt backups at rest
6. **Restoration testing**: restore to staging weekly, document steps
7. **Disaster recovery drill**: quarterly full DR exercise
8. **Monitoring**: alert if backup fails

Tool: pgBackRest (better than pg_dump for large databases).
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement CQRS and Event Sourcing

**id:** `06-database-design/cqrs-event-sourcing` · **Difficulty:** advanced · **Tags:** cqrs, event-sourcing, architecture, postgresql

**Placeholders:** [YOUR DOMAIN]

````text
Implement CQRS and Event Sourcing for: [YOUR DOMAIN].

**Event Sourcing**:
1. Events table: id, aggregate_type, aggregate_id, event_type, data, created_at
2. Append-only: never update events
3. Reconstruct state: replay all events for an aggregate
4. Snapshot: save state at N events to speed up reconstruction
5. Event versioning: how to handle schema changes in old events

**CQRS**:
6. Command side: validate → apply → persist events
7. Query side: materialized read models (denormalized for query speed)
8. Projections: event handlers that build read models
9. Eventual consistency: read side may lag behind write side
10. Sagas: multi-step processes with compensation

Node.js + PostgreSQL implementation.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Plan and Execute Data Migration

**id:** `06-database-design/data-migration` · **Difficulty:** advanced · **Tags:** migration, postgresql, etl, data

````text
Plan and execute a data migration for: [DESCRIBE WHAT YOU'RE MIGRATING — e.g., old schema to new schema, MySQL to PostgreSQL, adding columns].

1. **Migration plan**:
   - What data is moving where
   - Estimated volume and time
   - Zero-downtime vs maintenance window approach
2. **Backup strategy**: full backup before starting, point-in-time recovery test
3. **Migration script**: idempotent, can be re-run safely
4. **Validation**: verify row counts, checksums, sample records
5. **Dual-write period**: write to old and new schema simultaneously
6. **Cutover**: atomic switch, rollback plan if issues
7. **Cleanup**: remove old schema after validation period
8. **Testing**: run migration on production data copy first

Output: complete migration SQL + validation queries.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Data Model an E-Commerce System

**id:** `06-database-design/data-modeling-ecommerce` · **Difficulty:** intermediate · **Tags:** ecommerce, data-modeling, postgresql, schema

````text
Design the complete data model for an e-commerce system.

Requirements:
- Products with variants (size, color, material combinations)
- Inventory tracking per variant per warehouse
- Orders with line items, taxes, discounts, shipping
- Customer management with addresses
- Pricing: MSRP, sale price, customer-tier pricing
- Reviews and ratings
- Category hierarchy (unlimited depth)

Output:
1. Complete ER diagram (Mermaid)
2. CREATE TABLE SQL (PostgreSQL)
3. Key indexes
4. Sample queries for: product listing with price, order total, inventory check
5. The 3 hardest modeling decisions and why you chose as you did
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design a Data Warehouse

**id:** `06-database-design/data-warehouse` · **Difficulty:** advanced · **Tags:** data-warehouse, analytics, dimensional, bigquery

**Placeholders:** [LIST YOUR KEY METRICS], [LIST YOUR OPERATIONAL DATABASES]

````text
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
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement Database Access Control

**id:** `06-database-design/database-access-control` · **Difficulty:** advanced · **Tags:** security, postgresql, rbac, access-control

````text
Implement principle-of-least-privilege access control for my PostgreSQL database.

Roles needed: [e.g., API service, analytics, admin, migration runner]

Implement:
1. **Roles hierarchy**: base roles inherited by specific roles
2. **GRANT syntax**: table-level, column-level, row-level
3. **Row Level Security (RLS)**: policies per role per table
4. **Schema permissions**: USAGE, CREATE
5. **Function SECURITY DEFINER**: run elevated for specific operations
6. **Connection limits per role**
7. **Audit logging**: log every query from admin role
8. **Network restriction**: pg_hba.conf IP allowlist per role
9. **Password rotation**: procedure without downtime
10. **Application user**: never connect as postgres superuser

Output: complete role setup SQL + documentation.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Manage Database Connections in Production

**id:** `06-database-design/database-connection-management` · **Difficulty:** advanced · **Tags:** connections, postgresql, pooling, performance

**Placeholders:** [EXPECTED RPS AND CONCURRENCY]

````text
Optimize database connection management for production.

Stack: Node.js + PostgreSQL
Load: [EXPECTED RPS AND CONCURRENCY]

1. **Connection pool sizing**: (CPU cores × 2) + 1 per server
2. **pg pool config**: max, min, idleTimeoutMillis, connectionTimeoutMillis
3. **PgBouncer**: transaction pooling for serverless/high concurrency
4. **Connection leaks**: detect and fix (log long-held connections)
5. **Serverless problem**: functions create new connections per invocation
6. **RDS Proxy**: managed connection pooler for AWS
7. **Monitoring**: pg_stat_activity, wait events, max_connections
8. **Connection limits per role**: `ALTER ROLE myuser CONNECTION LIMIT 100`
9. **Graceful shutdown**: drain connections before restart
10. **Circuit breaker**: stop making new connections if DB is overwhelmed
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Database Design Patterns

**id:** `06-database-design/database-design-patterns` · **Difficulty:** advanced · **Tags:** patterns, postgresql, design, modeling

**Placeholders:** [DESCRIBE YOUR DOMAIN]

````text
Apply these database design patterns to my schema: [DESCRIBE YOUR DOMAIN].

1. **Polymorphic associations**: entity belongs to multiple parent types
2. **EAV (Entity-Attribute-Value)**: flexible attributes (use sparingly)
3. **Adjacency list**: self-referential (parent_id) for trees
4. **Nested sets**: faster tree traversal, harder updates
5. **Closure table**: best tree reads + writes
6. **Soft delete**: deleted_at timestamp (and how to index correctly)
7. **Audit log**: who changed what and when (shadow table pattern)
8. **Optimistic locking**: version column for concurrent update detection
9. **UUID vs integer primary keys**: tradeoffs
10. **Composite primary keys**: when to use, when to avoid
11. **Bridge table**: many-to-many with extra attributes
12. **Materialized path**: store full path as string for hierarchy
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Review a Database Schema

**id:** `06-database-design/database-design-review` · **Difficulty:** intermediate · **Tags:** schema, review, postgresql, design

**Placeholders:** [PASTE YOUR SCHEMA]

````text
Review this database schema and identify all issues:

[PASTE YOUR SCHEMA]

Analyze:
1. **Normalization**: identify violations and how to fix them
2. **Data types**: wrong types (e.g., storing numbers as VARCHAR)
3. **Missing constraints**: NOT NULL, UNIQUE, CHECK, FK
4. **Missing indexes**: obvious lookup columns without index
5. **Naming**: inconsistent conventions
6. **Performance**: potential N+1, missing composite indexes
7. **Security**: sensitive data without encryption markers
8. **Scalability**: design issues that won't scale to 10x data
9. **Redundancy**: data stored in multiple places
10. **Audit trail**: missing created_at/updated_at

For each issue: severity + explanation + SQL to fix.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Document Your Database Schema

**id:** `06-database-design/database-documentation` · **Difficulty:** beginner · **Tags:** documentation, schema, postgresql, data-dictionary

**Placeholders:** [PASTE YOUR SCHEMA]

````text
Generate comprehensive documentation for my database schema.

Schema: [PASTE YOUR SCHEMA]

Document:
1. **Data dictionary**: every table and column with:
   - Purpose of the table
   - Each column: data type, constraints, description, example value
   - Relationships to other tables
2. **ER diagram** (Mermaid)
3. **Query patterns**: common queries and how to run them
4. **Access patterns**: which queries run most frequently
5. **Index documentation**: what each index is for
6. **Stored procedures/triggers**: what they do and when
7. **Naming conventions**: document the conventions used
8. **Change log**: schema change history

Output in Markdown format, suitable for a team wiki.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement Database Encryption

**id:** `06-database-design/database-encryption` · **Difficulty:** advanced · **Tags:** encryption, security, postgresql, compliance

**Placeholders:** [HIPAA / PCI-DSS / GDPR], [LIST: SSN, credit cards, health data, etc.]

````text
Implement encryption for sensitive data in my database.

Sensitive fields: [LIST: SSN, credit cards, health data, etc.]
Compliance: [HIPAA / PCI-DSS / GDPR]

Layers:
1. **Encryption at rest**: disk-level (transparent, OS/DB handles)
2. **Encryption in transit**: SSL/TLS for DB connections (verify, don't just encrypt)
3. **Column-level encryption**: pgcrypto for specific sensitive fields
4. **Application-level encryption**: encrypt before insert, decrypt on read
5. **Key management**: AWS KMS / HashiCorp Vault (don't store keys in DB)
6. **Searchable encryption**: how to search encrypted fields
7. **Tokenization**: replace sensitive data with non-sensitive token
8. **Data masking**: return masked value to non-privileged users

For each compliance framework: what is required vs nice-to-have.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Master Database Indexing

**id:** `06-database-design/database-indexing` · **Difficulty:** advanced · **Tags:** indexes, postgresql, performance, sql

**Placeholders:** [DESCRIBE OR PASTE YOUR TOP 10 QUERIES], [PASTE YOUR TABLES]

````text
Design the optimal index strategy for my database.

Schema: [PASTE YOUR TABLES]
Frequent queries: [DESCRIBE OR PASTE YOUR TOP 10 QUERIES]

1. **When to index**: high cardinality, frequent WHERE, JOIN, ORDER BY
2. **When NOT to index**: write-heavy tables, low cardinality, small tables
3. **B-tree indexes**: default, range queries, equality
4. **Composite indexes**: column order matters — explain how
5. **Partial indexes**: index WHERE condition (only index what you query)
6. **Covering indexes**: INCLUDE extra columns to avoid table lookup
7. **GIN indexes**: for arrays, JSONB, full-text search
8. **Index bloat**: REINDEX, VACUUM impact
9. **Unused indexes**: find and drop them (pg_stat_user_indexes)
10. **Index-only scans**: when possible

Output: exact CREATE INDEX statements for my queries.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Monitor Your Database

**id:** `06-database-design/database-monitoring` · **Difficulty:** advanced · **Tags:** monitoring, postgresql, metrics, alerting

````text
Set up comprehensive database monitoring.

Database: PostgreSQL (self-hosted or AWS RDS)

Key metrics:
1. **Connection count**: vs max_connections (alert at 80%)
2. **Query latency**: p95, p99 per query type
3. **Cache hit rate**: buffer cache hit should be > 99%
4. **Vacuum status**: tables needing vacuum, bloat
5. **Replication lag**: streaming + logical replication lag
6. **Lock waits**: long-running locks blocking queries
7. **Deadlocks**: frequency and which queries cause them
8. **Index usage**: unused indexes wasting space + write overhead
9. **Table/index bloat**: dead rows percentage
10. **Disk I/O**: read vs write, iops, wait time

Tools: pg_stat_statements, pg_activity, pgBadger log analyzer, Prometheus pg_exporter.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Normalize a Database Schema

**id:** `06-database-design/database-normalization` · **Difficulty:** intermediate · **Tags:** normalization, sql, schema, design

````text
Normalize this database schema to 3NF (Third Normal Form):

[PASTE YOUR CURRENT SCHEMA — especially if it has JSON columns, repeated data, or one giant table]

Process:
1. **1NF**: eliminate repeating groups, ensure atomic values
2. **2NF**: eliminate partial dependencies (all non-key fields depend on full PK)
3. **3NF**: eliminate transitive dependencies
4. **BCNF**: Boyce-Codd Normal Form if needed

For each step:
- Identify the violation
- The SQL to fix it
- The tradeoffs (normalization vs performance)

Then: **controlled denormalization** — add back specific denormalized columns with justification for query performance.

Output: complete normalized schema + migration from current to normalized.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Set Up Database Replication

**id:** `06-database-design/database-replication` · **Difficulty:** advanced · **Tags:** replication, postgresql, high-availability, devops

````text
Set up database replication for high availability and read scaling.

Stack: PostgreSQL 15+

1. **Streaming replication** (hot standby):
   - Primary config: wal_level, max_wal_senders
   - Replica config: primary_conninfo, hot_standby
   - Replication slots: don't lose WAL even if replica lags
   - Monitoring: replication lag
2. **Read replicas**:
   - Route read queries to replica
   - Application-level routing vs PgBouncer vs pgpool
3. **Failover**:
   - Detect primary failure (Patroni / pg_auto_failover)
   - Promote replica to primary
   - Update connection string (DNS / load balancer)
   - Recovery time objective: < 30 seconds
4. **Multi-region**: logical replication across regions
5. **Testing**: simulate primary failure in staging monthly
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Scale Your Database

**id:** `06-database-design/database-scaling` · **Difficulty:** advanced · **Tags:** scaling, postgresql, read-replicas, sharding

**Placeholders:** [SINGLE DB, SIZE, QUERIES/SEC]

````text
Create a database scaling plan for my application.

Current: [SINGLE DB, SIZE, QUERIES/SEC]
Projected: [10x / 100x GROWTH over N months]

Scaling ladder (do these in order):
1. **Optimize queries and indexes** (free, do first)
2. **Vertical scaling**: bigger instance (quick fix, but has ceiling)
3. **Connection pooling**: PgBouncer (handle more concurrent connections)
4. **Read replicas**: route reads to replica (helps 80% of workloads)
5. **Caching layer**: Redis for hot data (reduce DB load 50-90%)
6. **Partitioning**: split large tables (time-based or range)
7. **Horizontal sharding**: Citus or app-level sharding (last resort)
8. **CQRS**: separate read and write models

For each step: when to do it (trigger metric) + implementation time.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Generate a Database Schema from Requirements

**id:** `06-database-design/database-schema-generation` · **Difficulty:** intermediate · **Tags:** schema, postgresql, requirements, design

**Placeholders:** [PASTE YOUR BUSINESS REQUIREMENTS DOCUMENT]

````text
Generate a database schema from these business requirements:

[PASTE YOUR BUSINESS REQUIREMENTS DOCUMENT]

Process:
1. **Noun extraction**: identify entities from requirements
2. **Relationship identification**: one-to-many, many-to-many
3. **Attribute mapping**: business terms → database columns + types
4. **Business rules → constraints**: required fields, valid values, uniqueness
5. **Decisions log**: document every non-obvious choice

Output:
- Mermaid ER diagram
- PostgreSQL CREATE TABLE statements (production-quality)
- Indexes
- Sample seed data
- List of assumptions made (for stakeholder review)
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Generate Realistic Database Seed Data

**id:** `06-database-design/database-seeds` · **Difficulty:** beginner · **Tags:** seed, testing, faker, postgresql

**Placeholders:** [N], [PASTE YOUR SCHEMA]

````text
Generate realistic seed data for my database.

Schema: [PASTE YOUR SCHEMA]

Requirements:
- [N] users with diverse realistic names (international)
- [N] records for each main entity
- Realistic relationships (users have 1-5 posts, etc.)
- Edge cases: empty strings where nullable, max length strings, special characters
- Different status distributions: 80% active, 15% inactive, 5% suspended

Output:
1. SQL INSERT statements for base seed data
2. Node.js script using Faker.js for generating larger datasets
3. Python script alternative
4. Specific edge case records to always include in seeds
5. Instructions for: fresh seed (delete + reseed) vs additive seed
6. CI seed: fast minimal seed for test suite
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design Database Sharding

**id:** `06-database-design/database-sharding` · **Difficulty:** advanced · **Tags:** sharding, postgresql, scalability, architecture

**Placeholders:** [DESCRIBE: single PostgreSQL, projected 100M+ rows, growth rate]

````text
Design a database sharding strategy for my application at scale.

Current situation: [DESCRIBE: single PostgreSQL, projected 100M+ rows, growth rate]

Sharding key selection:
1. User ID sharding: route all user data to same shard
2. Tenant ID: for multi-tenant SaaS
3. Date range: for time-series data
4. Hash-based: even distribution

Implement:
5. Consistent hashing for shard routing
6. Application-level sharding (vs Citus)
7. Cross-shard queries: how to handle joins
8. Shard rebalancing when adding shards
9. Hot spots: how to detect and fix
10. Citus (PostgreSQL extension): managed sharding

Alternative: vertical scaling + read replicas first (defer sharding as long as possible).
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Master Database Transactions

**id:** `06-database-design/database-transactions` · **Difficulty:** advanced · **Tags:** transactions, postgresql, acid, concurrency

**Placeholders:** [DESCRIBE CONCURRENT OPERATIONS]

````text
Master transactions and concurrency control in PostgreSQL.

My use case: [DESCRIBE CONCURRENT OPERATIONS]

1. **ACID properties**: what each means in practice with examples
2. **Isolation levels**:
   - READ COMMITTED (default): what can go wrong
   - REPEATABLE READ: solves phantom reads
   - SERIALIZABLE: highest isolation, performance cost
3. **Phenomena**: dirty read, non-repeatable read, phantom read, serialization anomaly
4. **Optimistic locking**: version column + WHERE version = N
5. **Pessimistic locking**: SELECT FOR UPDATE, SKIP LOCKED
6. **SKIP LOCKED**: job queue pattern
7. **Deadlocks**: how to detect, how to prevent (consistent lock ordering)
8. **Long transactions**: why they're dangerous, how to avoid
9. **Advisory locks**: application-level locks in PostgreSQL
10. **Two-phase commit**: distributed transactions
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design a Database Schema

**id:** `06-database-design/er-diagram` · **Difficulty:** intermediate · **Tags:** postgresql, schema, erd, modeling

**Placeholders:** [YOUR APPLICATION]

````text
Design a complete database schema for: [YOUR APPLICATION].

Output:
1. Entity-Relationship Diagram (ASCII art or Mermaid)
2. CREATE TABLE SQL for each entity with:
   - Correct data types (prefer specific: UUID, TEXT, TIMESTAMPTZ, NUMERIC, BOOLEAN)
   - NOT NULL constraints where appropriate
   - DEFAULT values
   - CHECK constraints
   - UNIQUE constraints
   - Foreign keys with ON DELETE behavior
3. Indexes (beyond primary key)
4. Rationale for each major design decision
5. Alternative designs considered and why rejected

Normalization target: 3NF unless denormalization is justified.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design a Graph Database Schema

**id:** `06-database-design/graph-database` · **Difficulty:** advanced · **Tags:** neo4j, graph, database, relationships

````text
Design a graph database schema using Neo4j for: [DESCRIBE YOUR DOMAIN — social network, recommendation engine, dependency graph, fraud detection].

1. **Nodes**: define all node labels and their properties
2. **Relationships**: define all relationship types and directions
3. **Properties on relationships**: when to put data on the edge
4. **Indexes**: node property indexes for lookup
5. **Constraints**: unique constraints on node properties

Cypher queries for your key use cases:
6. Find all connections within N degrees
7. Shortest path between two nodes
8. Recommend based on similar users (collaborative filtering)
9. Detect cycles (fraud rings)
10. Pattern matching queries

When to use Neo4j vs relational DB — decision matrix.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design a MongoDB Schema

**id:** `06-database-design/mongodb-schema` · **Difficulty:** intermediate · **Tags:** mongodb, nosql, schema, document

**Placeholders:** [YOUR APPLICATION]

````text
Design an optimal MongoDB schema for: [YOUR APPLICATION].

Decisions to make:
1. **Embed vs Reference**: when to embed documents vs use references (show examples)
2. **One-to-one**: how to model (embed in most cases)
3. **One-to-many**: embed array vs separate collection — decide based on cardinality
4. **Many-to-many**: junction document pattern vs array of IDs
5. **Polymorphism**: different document shapes in one collection
6. **Bucket pattern**: time-series data optimization
7. **Outlier pattern**: handle exceptional large documents
8. **Indexes**: compound, text, geo, sparse, partial
9. **Aggregation pipeline**: for your main queries
10. **Transactions**: when MongoDB transactions are needed

SQL vs MongoDB decision: justify the choice for this use case.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design a Multi-Tenant Database

**id:** `06-database-design/multi-tenant-database` · **Difficulty:** advanced · **Tags:** multi-tenant, saas, postgresql, architecture

````text
Design a multi-tenant database architecture for my SaaS application.

Tenants: [EXPECTED NUMBER — dozens? thousands?]

Three approaches:

**Option A — Row-level (shared schema)**:
- Add `tenant_id` to every table
- Row Level Security (RLS) to isolate
- Pros: simple, cheap. Cons: noisy neighbor, harder to export tenant data

**Option B — Schema-per-tenant**:
- Each tenant gets own PostgreSQL schema
- Up to ~1000 tenants per DB
- Pros: easy isolation. Cons: complex migrations

**Option C — Database-per-tenant**:
- Ultimate isolation
- Pros: compliance, custom backups. Cons: expensive, complex infra

For MY tenant count and compliance needs: which approach?
Implementation for the recommended approach including migration strategy.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Choose the Right NoSQL Database

**id:** `06-database-design/nosql-selection` · **Difficulty:** advanced · **Tags:** nosql, dynamodb, mongodb, cassandra

**Placeholders:** [DESCRIBE YOUR USE CASE, ACCESS PATTERNS, SCALE]

````text
Help me choose the right NoSQL database for: [DESCRIBE YOUR USE CASE, ACCESS PATTERNS, SCALE].

Evaluate:
1. **MongoDB**: document store, flexible schema, good for catalogs, CMS
2. **DynamoDB**: AWS managed, single-digit ms at any scale, limited query patterns
3. **Cassandra**: write-heavy, time-series, geographic distribution
4. **Redis**: in-memory, caching, real-time, pub/sub
5. **Elasticsearch**: full-text search, log analytics
6. **InfluxDB**: time-series metrics
7. **Neo4j**: graph relationships
8. **CockroachDB**: distributed SQL (PostgreSQL compatible)

For my specific access patterns and scale:
- Winner and justification
- Data model for the winning DB
- Failure modes to plan for
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## ORM vs Raw SQL Decision Guide

**id:** `06-database-design/orm-vs-raw-sql` · **Difficulty:** intermediate · **Tags:** orm, sql, prisma, postgresql

**Placeholders:** [DESCRIBE], [LOW / MEDIUM / HIGH]

````text
Advise on whether to use an ORM or raw SQL for my project.

Project: [DESCRIBE]
Team SQL experience: [LOW / MEDIUM / HIGH]

Argumentsfor ORM (Prisma, Drizzle, TypeORM):
1. Type safety — TypeScript types from schema
2. Migration management
3. Relationship loading
4. Simpler CRUD operations
5. Less SQL knowledge required

Arguments for raw SQL:
6. Full SQL power (window functions, CTEs, complex queries)
7. No abstraction overhead
8. Easier optimization
9. Better for existing complex schemas

For MY project specifically:
- Recommendation with justification
- If ORM: which one and why
- Hybrid: ORM for CRUD + raw SQL for complex queries
- Implementation pattern for the hybrid approach
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Tune PostgreSQL for Production

**id:** `06-database-design/postgres-performance-tuning` · **Difficulty:** advanced · **Tags:** postgresql, performance, configuration, devops

````text
Tune PostgreSQL configuration for production performance.

Server specs: [CPU cores, RAM, disk type (SSD/NVMe), workload type (OLTP/OLAP/mixed)]

Configure postgresql.conf:
1. **Memory**: shared_buffers (25% RAM), effective_cache_size (75% RAM), work_mem, maintenance_work_mem
2. **WAL**: wal_buffers, checkpoint_completion_target, max_wal_size
3. **Connections**: max_connections, connection pooler recommendation
4. **Planner**: random_page_cost (1.1 for SSD vs 4 for HDD), effective_io_concurrency
5. **Autovacuum**: tuning for high-write tables
6. **Logging**: log_min_duration_statement = 1000 (log slow queries)
7. **Parallelism**: max_parallel_workers_per_gather

Output: complete postgresql.conf with explanations for each setting.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Advanced PostgreSQL Features

**id:** `06-database-design/postgresql-advanced` · **Difficulty:** advanced · **Tags:** postgresql, advanced, sql, database

**Placeholders:** [DESCRIBE YOUR DATA AND QUERIES]

````text
Implement these advanced PostgreSQL features in my database:

Use case: [DESCRIBE YOUR DATA AND QUERIES]

1. **JSONB**: store and query semi-structured data, GIN index, jsonb_path operators
2. **Full-text search**: tsvector, tsquery, GIN index, ts_rank, tsheadline
3. **Partitioning**: range/list/hash partitioning, partition pruning
4. **CTEs**: WITH clause, recursive CTEs for tree structures
5. **Window functions**: ROW_NUMBER, RANK, LEAD/LAG, running totals
6. **Materialized views**: refresh strategy, incremental refresh
7. **Foreign Data Wrappers**: query external PostgreSQL or CSV
8. **Triggers and rules**: computed columns, audit log
9. **Extensions**: pg_stat_statements, pgcrypto, postgis
10. **EXPLAIN ANALYZE**: read and optimize query plans
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Master PostgreSQL JSONB

**id:** `06-database-design/postgresql-jsonb` · **Difficulty:** advanced · **Tags:** postgresql, jsonb, nosql, querying

**Placeholders:** [DESCRIBE WHAT YOU'RE STORING AS JSON]

````text
Master JSONB in PostgreSQL for flexible schema storage.

My use case: [DESCRIBE WHAT YOU'RE STORING AS JSON]

1. **JSONB vs JSON**: always use JSONB (binary, indexed)
2. **Operators**: `->`, `->>`, `#>`, `#>>`, `@>`, `<@`, `?`, `?|`, `?&`
3. **Indexing**: GIN index (full doc), jsonb_path_ops for `@>`, expression index for specific keys
4. **Functions**: jsonb_set, jsonb_insert, jsonb_strip_nulls, jsonb_object_keys
5. **Path operations**: jsonb_path_query (JSONPath)
6. **Aggregation**: jsonb_agg, jsonb_object_agg
7. **Schema validation**: CHECK constraint with custom function
8. **Updating nested keys**: jsonb_set deep update
9. **Performance**: when JSONB is fast and when it slows you down
10. **Migration pattern**: relational → JSONB → relational again

For each: working SQL examples with my use case.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Model Data in Redis

**id:** `06-database-design/redis-data-modeling` · **Difficulty:** advanced · **Tags:** redis, data-modeling, nosql, caching

**Placeholders:** [DESCRIBE HOW YOU QUERY IT], [DESCRIBE YOUR DATA]

````text
Model and store this data efficiently in Redis:

Data: [DESCRIBE YOUR DATA]
Access patterns: [DESCRIBE HOW YOU QUERY IT]

Redis data structures:
1. **String**: simple key-value, counters, cached JSON
2. **Hash**: user objects, settings (field-level access)
3. **List**: queues, recent items, activity feeds
4. **Set**: unique values, tags, set operations (union/intersect/diff)
5. **Sorted Set**: leaderboards, scheduled tasks, range queries
6. **Stream**: append-only log, event sourcing, message queue
7. **HyperLogLog**: approximate unique count (< 1% error, constant memory)
8. **Bloom Filter**: membership test without false negatives
9. **Geo**: store and query locations, find nearby
10. **JSON** (RedisJSON): store/query JSON documents

Key naming conventions + TTL strategy for each.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement Soft Delete

**id:** `06-database-design/soft-delete-pattern` · **Difficulty:** beginner · **Tags:** soft-delete, postgresql, patterns, data

**Placeholders:** [LIST]

````text
Implement soft delete for my application.

Tables to soft-delete: [LIST]

Implement:
1. Add `deleted_at TIMESTAMPTZ NULL` to each table
2. PostgreSQL views: `active_users` that filters `WHERE deleted_at IS NULL`
3. RLS policy: automatically filter deleted rows for the API user role
4. Cascade soft deletes: when user is deleted, soft-delete their posts/comments too
5. Restore: undelete functionality (admin only)
6. Hard delete schedule: permanently delete soft-deleted records after 90 days (GDPR)
7. Indexes: partial index `WHERE deleted_at IS NULL` for performance
8. Application layer: always query through the view (prevent bugs)
9. Audit trail: who deleted what and when
10. Find deleted records: admin query to see deleted items
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Optimize Slow SQL Queries

**id:** `06-database-design/sql-query-optimization` · **Difficulty:** advanced · **Tags:** sql, optimization, indexes, postgresql

**Placeholders:** [PASTE YOUR SLOW QUERIES AND THEIR EXPLAIN ANALYZE OUTPUT]

````text
Optimize these slow SQL queries:

[PASTE YOUR SLOW QUERIES AND THEIR EXPLAIN ANALYZE OUTPUT]

Optimization techniques:
1. **Read EXPLAIN ANALYZE**: identify seq scan, hash join, sort spills
2. **Index creation**: B-tree, GIN, GiST, partial, covering indexes
3. **Query rewriting**: EXISTS vs IN, CTEs vs subqueries, avoiding DISTINCT
4. **JOIN optimization**: order, type (hash/nested loop/merge), conditions
5. **Filter pushdown**: move WHERE conditions to reduce rows early
6. **N+1 elimination**: single JOIN vs multiple queries
7. **Pagination**: cursor-based vs OFFSET
8. **Materialized views**: precompute expensive aggregations
9. **Statistics**: ANALYZE, pg_stats for planner accuracy
10. **Partitioning**: for very large tables

Before/after EXPLAIN ANALYZE comparison.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Master SQL Window Functions

**id:** `06-database-design/sql-window-functions` · **Difficulty:** intermediate · **Tags:** sql, window-functions, postgresql, analytics

**Placeholders:** [DESCRIBE YOUR TABLES], [WHAT DO YOU NEED TO CALCULATE]

````text
Master SQL window functions for analytics queries.

My data: [DESCRIBE YOUR TABLES]
Analytics questions: [WHAT DO YOU NEED TO CALCULATE]

Teach me with my data:
1. **ROW_NUMBER()**: assign unique row numbers within partition
2. **RANK() / DENSE_RANK()**: rankings with ties
3. **NTILE(n)**: divide rows into N buckets
4. **LAG() / LEAD()**: access previous/next row value
5. **FIRST_VALUE() / LAST_VALUE()**: first/last value in window
6. **SUM() / AVG() / COUNT()**: running totals and rolling averages
7. **PARTITION BY**: reset window per group
8. **ROWS BETWEEN**: define frame: current row, N preceding, unbounded

For each: SQL query against my data + result explanation.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Write Effective Stored Procedures

**id:** `06-database-design/stored-procedures` · **Difficulty:** advanced · **Tags:** stored-procedures, postgresql, plpgsql, backend

**Placeholders:** [DESCRIBE YOUR OPERATIONS]

````text
Write stored procedures and functions for these complex operations: [DESCRIBE YOUR OPERATIONS].

Using: PostgreSQL PL/pgSQL

1. **Functions vs procedures**: when to use each
2. **SECURITY DEFINER**: run as function owner (for RLS bypass where needed)
3. **Transaction control**: COMMIT/ROLLBACK within procedure
4. **Exception handling**: EXCEPTION block, SQLSTATE codes
5. **Dynamic SQL**: EXECUTE for dynamic queries
6. **Loops and cursors**: FOR loops, cursor fetch
7. **Returning data**: SETOF, TABLE, record types
8. **Triggers**: BEFORE/AFTER, ROW/STATEMENT level
9. **Performance**: inlining optimization, search_path
10. **Testing**: pgTAP for PL/pgSQL unit tests

Alternative: should this logic be in the application layer?
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design a Time-Series Database

**id:** `06-database-design/time-series-data` · **Difficulty:** advanced · **Tags:** time-series, timescaledb, influxdb, iot

**Placeholders:** [DESCRIBE YOUR DATA: IoT sensors / metrics / financial ticks / events]

````text
Design a time-series data storage solution for: [DESCRIBE YOUR DATA: IoT sensors / metrics / financial ticks / events].

Option A — TimescaleDB (PostgreSQL extension):
1. Hypertable setup (auto-partition by time)
2. Chunk interval (1 hour vs 1 day vs 1 week)
3. Retention policy (drop data older than N months)
4. Compression (50-90% storage reduction)
5. Continuous aggregates (pre-compute hourly/daily summaries)
6. Time-series queries: time_bucket, lag, interpolation

Option B — InfluxDB:
7. Measurement, tags, fields design
8. Flux query language examples
9. Retention policies

For my use case: which is better and why?
Benchmark: expected query latency for 1B rows.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Configure [CONCERN] for [DATABASE] on [WORKLOAD]

**id:** `06-database-design/configure-concern-for-database-on-workload` · **Difficulty:** beginner/intermediate/advanced · **Tags:** postgresql, database, mysql, sql, schema, mongodb, redis

**Variant group** (6 generated prompts collapsed). Pick one value per placeholder:
- `[DATABASE]`: MongoDB | MySQL | Redis
- `[WORKLOAD]`: a geographic location coordinates tracking service | a social network relations graph | a user session cache store | an e-commerce warehouse index
- `[CONCERN]`: data types definitions | database replica setups | idempotent migration scripts | optimal indexing strategies

````text
Write the data definition language (DDL) and setup guides for [CONCERN] in [DATABASE] for [WORKLOAD] to ensure maximum query throughput.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** configure-data-types-definitions-for-mysql-on-a-social-network-relations-graph, configure-database-replica-setups-for-mongodb-on-a-geographic-location-coordinates-tracking-service, configure-idempotent-migration-scripts-for-redis-on-an-e-commerce-warehouse-index, configure-optimal-indexing-strategies-for-mongodb-on-a-geographic-location-coordinates-tracking-service, configure-optimal-indexing-strategies-for-mongodb-on-a-social-network-relations-graph, configure-optimal-indexing-strategies-for-mysql-on-a-user-session-cache-store


## Design [DATABASE] schema for [WORKLOAD]

**id:** `06-database-design/design-database-schema-for-workload` · **Difficulty:** beginner/intermediate/advanced · **Tags:** postgresql, database, sql, cassandra, schema, mysql, neo4j, redis

**Variant group** (8 generated prompts collapsed). Pick one value per placeholder:
- `[DATABASE]`: Cassandra | MySQL | Neo4j | Redis
- `[WORKLOAD]`: a massive application log aggregator | a microservice messaging history | a social network relations graph | an e-commerce warehouse index

````text
Design a production-ready [DATABASE] schema for [WORKLOAD]. Define tables/collections, column data types, foreign keys, and indexes.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** design-cassandra-schema-for-an-e-commerce-warehouse-index, design-mysql-schema-for-a-massive-application-log-aggregator, design-mysql-schema-for-a-microservice-messaging-history, design-mysql-schema-for-an-e-commerce-warehouse-index, design-neo4j-schema-for-a-microservice-messaging-history, design-neo4j-schema-for-an-e-commerce-warehouse-index, design-redis-schema-for-a-social-network-relations-graph, design-redis-schema-for-an-e-commerce-warehouse-index

