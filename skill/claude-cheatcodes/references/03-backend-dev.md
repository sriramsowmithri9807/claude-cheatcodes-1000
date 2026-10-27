# 03-backend-dev

Server code: REST backends, auth, queues, caching, background jobs, graceful shutdown, many languages.

46 prompts. Search `## ` headings or ids; see index.md for the one-line list.

## Generate Beautiful API Documentation

**id:** `03-backend-dev/api-documentation` · **Difficulty:** intermediate · **Tags:** swagger, openapi, docs, api

````text
Generate comprehensive, beautiful API documentation.

API framework: [Express / Fastify / NestJS / FastAPI]

Using: Swagger UI / Scalar / Redoc

Implement:
1. OpenAPI 3.1 spec generation (code-first from your framework)
2. Complete request/response schemas with examples
3. Authentication documentation (JWT, API Key, OAuth)
4. Error response catalogue (every possible error code)
5. SDKs: auto-generate TypeScript + Python client SDKs
6. Changelog section
7. Try-it-out with a sandbox environment
8. Postman collection export

Host docs at: `/docs` in development, separate docs site in production.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build an API Gateway

**id:** `03-backend-dev/api-gateway` · **Difficulty:** advanced · **Tags:** api-gateway, nginx, nodejs, architecture

**Placeholders:** [LIST SERVICES AND THEIR PORTS]

````text
Build an API Gateway for my microservices.

Services behind the gateway: [LIST SERVICES AND THEIR PORTS]

Using: Express.js gateway (or recommend nginx/Kong if more appropriate)

Implement:
1. Route proxying to upstream services
2. JWT authentication (verify at gateway, forward user info)
3. Rate limiting per user/IP
4. Request/response transformation
5. Aggregation endpoint (combine multiple service calls)
6. Circuit breaker for each upstream
7. Request timeout handling
8. Access logging (structured JSON)
9. Health aggregation endpoint
10. Graceful degradation (serve cached response when upstream is down)
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Implement the Backend-for-Frontend Pattern

**id:** `03-backend-dev/api-gateway-pattern` · **Difficulty:** advanced · **Tags:** bff, api-gateway, architecture, fullstack

````text
Implement the Backend-for-Frontend (BFF) pattern.

My frontends:
- Web app (Next.js)
- Mobile app (React Native)
- Third-party API consumers

Problem: Each frontend needs different data shapes and auth methods.

Design BFF for each:
1. **Web BFF**: session-based auth, server-side rendering optimized responses
2. **Mobile BFF**: JWT auth, mobile-optimized payloads (smaller, compressed)
3. **Public API**: API key auth, rate-limited, versioned

Each BFF:
- Aggregates calls to microservices
- Transforms responses
- Handles auth for its client type
- Caches aggressively for its usage pattern
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Implement Idempotent APIs

**id:** `03-backend-dev/api-idempotency` · **Difficulty:** advanced · **Tags:** idempotency, api, payments, backend

````text
Implement idempotent API endpoints (critical for payments and financial operations).

Why: if a client retries a request (network timeout), the operation must not execute twice.

Implement:
1. `Idempotency-Key` header (UUID, client-provided)
2. Store keys in Redis with 24h TTL
3. On first request: process and cache response
4. On duplicate request (same key): return cached response immediately
5. In-flight protection: lock key while processing (prevent concurrent duplicates)
6. Database: store idempotency key with request fingerprint + response
7. Test: simulate retry scenarios

Apply to: POST /payments, POST /orders, POST /subscriptions
Show the complete middleware implementation.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Advanced API Rate Limiting

**id:** `03-backend-dev/api-rate-limiting` · **Difficulty:** advanced · **Tags:** rate-limiting, redis, api, security

````text
Implement sophisticated API rate limiting for a production API.

Requirements:
- Free tier: 100 req/hour
- Pro tier: 10,000 req/hour
- Enterprise: 1,000,000 req/hour

Implement:
1. Token bucket algorithm (smooth bursting)
2. Sliding window log (most accurate)
3. Redis-based distributed limiting (works across multiple API servers)
4. Per-endpoint limits (stricter for expensive operations)
5. Cost-based limiting (read=1 point, write=5 points, AI=100 points)
6. Response headers: X-RateLimit-Limit, Remaining, Reset, Retry-After
7. Graceful limit exceeded: 429 with retry timing
8. Admin API to adjust limits per user
9. Bypass for internal service calls
10. Dashboard showing rate limit usage per API key
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Set Security Headers on Every API Response

**id:** `03-backend-dev/api-security-headers` · **Difficulty:** beginner · **Tags:** security, headers, express, backend

````text
Set proper HTTP security headers on every API response.

Using: Helmet.js for Express.js

Explain and configure:
1. `Content-Security-Policy`: prevent XSS (show the directives)
2. `X-Content-Type-Options: nosniff`: prevent MIME sniffing
3. `X-Frame-Options: DENY`: prevent clickjacking
4. `Strict-Transport-Security`: enforce HTTPS
5. `Referrer-Policy: strict-origin`: control referer
6. `Permissions-Policy`: disable unused browser features
7. `X-XSS-Protection: 0`: (paradoxically, disable the old filter)
8. `Cache-Control`: prevent caching of sensitive data
9. CORS headers: restrict origins, methods, headers
10. Remove: `X-Powered-By: Express` (stop advertising your stack)

Show the Helmet.js config and test with securityheaders.com.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Write Comprehensive API Tests

**id:** `03-backend-dev/api-testing` · **Difficulty:** intermediate · **Tags:** testing, supertest, jest, api

**Placeholders:** [DESCRIBE YOUR API ROUTES]

````text
Write comprehensive tests for my REST API.

API to test: [DESCRIBE YOUR API ROUTES]
Framework: Express.js or Fastify

Using: Vitest + Supertest + MSW

Test patterns:
1. Happy path: successful responses
2. Validation errors: missing fields, wrong types
3. Authentication: missing token, expired token, wrong role
4. Authorization: user can't access other user's data
5. Edge cases: empty arrays, max length strings, special characters
6. Database errors: simulate DB failure
7. Rate limiting: test limit is enforced

Test setup:
- In-memory SQLite for tests (or test DB with transactions)
- Factory functions for test data
- Shared test server setup
- Coverage: target 80%+
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Implement JWT Authentication from Scratch

**id:** `03-backend-dev/auth-jwt` · **Difficulty:** intermediate · **Tags:** jwt, auth, security, nodejs

````text
Implement JWT authentication from scratch in Node.js (to deeply understand it).

Don't use passport.js — implement manually.

Implement:
1. User registration (bcrypt password hashing, salt rounds = 12)
2. User login (compare hash, issue access + refresh tokens)
3. Access token: 15 min expiry, sign with RS256 (asymmetric)
4. Refresh token: 7 day expiry, store hash in DB
5. Token refresh endpoint
6. Logout (invalidate refresh token in DB)
7. Auth middleware (verify JWT signature, check expiry)
8. Token rotation (new refresh token on each refresh)
9. Token revocation list (Redis set for logged-out users)
10. Security: httpOnly cookie storage vs Authorization header — show both

Explain every security decision.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Implement Background Tasks in Node.js

**id:** `03-backend-dev/background-tasks` · **Difficulty:** intermediate · **Tags:** background-tasks, workers, nodejs, performance

**Placeholders:** [LIST: email sending / image processing / report generation / etc.]

````text
Implement efficient background task processing in Node.js.

Tasks to offload: [LIST: email sending / image processing / report generation / etc.]

Without a queue (for simple cases):
1. `setImmediate()` for CPU tasks
2. `process.nextTick()` — when and when NOT to use
3. Worker threads for CPU-intensive work
4. `child_process.fork()` for isolation

With a queue (BullMQ for production):
1. Queue definition and job types
2. Worker implementation with concurrency
3. Job priorities
4. Error handling + retry
5. Job events (progress, completed, failed)
6. Clean up completed jobs

When to use queue vs worker thread vs async — decision matrix.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Implement Advanced Caching Strategies

**id:** `03-backend-dev/caching-strategies` · **Difficulty:** advanced · **Tags:** redis, caching, backend, performance

**Placeholders:** [LIST YOUR HEAVY QUERIES]

````text
Implement a comprehensive caching strategy for my Node.js API.

Endpoints/data to cache: [LIST YOUR HEAVY QUERIES]

Implement:
1. **Redis setup**: connection pooling, cluster mode support
2. **Cache-aside pattern**: check cache → miss → query DB → populate cache
3. **Write-through**: update cache on every DB write
4. **TTL strategy**: different expiry per data type
5. **Cache invalidation**: tag-based invalidation
6. **Distributed lock**: prevent cache stampede (Redis SETNX)
7. **Local + distributed cache**: L1 (in-memory) + L2 (Redis)
8. **Cache warming**: pre-populate on startup
9. **Cache key naming convention**
10. **Monitoring**: cache hit rate, eviction rate metrics
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Configure Database Connection Pooling

**id:** `03-backend-dev/connection-pooling` · **Difficulty:** intermediate · **Tags:** postgresql, connection-pool, pg, backend

````text
Configure optimal database connection pooling for my Node.js app.

Database: PostgreSQL
ORM/Query builder: [Prisma / Drizzle / node-postgres / Knex]

Implement:
1. Pool size calculation formula (connections = core_count * 2 + 1)
2. `pg` pool configuration: min, max, idleTimeoutMillis, connectionTimeoutMillis
3. PgBouncer in transaction mode (for serverless environments)
4. Connection leak detection
5. Health check: periodic test query to keep connections warm
6. Graceful pool shutdown on SIGTERM
7. Pool metrics: total, idle, waiting connections
8. Error handling: connection refused, timeout, pool exhausted
9. Read/write splitting: write pool → primary, read pool → replica

Benchmark: show connection count under load without vs with pooling.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Cron Job Scheduler

**id:** `03-backend-dev/cron-scheduler` · **Difficulty:** intermediate · **Tags:** cron, nodejs, scheduler, backend

**Placeholders:** [LIST YOUR RECURRING TASKS]

````text
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
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Master Data Validation with Zod

**id:** `03-backend-dev/data-validation` · **Difficulty:** intermediate · **Tags:** zod, validation, typescript, backend

**Placeholders:** [DESCRIBE YOUR DATA TYPES]

````text
Master Zod for data validation across your entire Node.js stack.

Schemas to build: [DESCRIBE YOUR DATA TYPES]

Implement:
1. Basic schemas: string, number, boolean, date with constraints
2. Object schemas with strict mode
3. Array and tuple schemas
4. Union and discriminated union schemas
5. Recursive schemas (nested tree structures)
6. Custom validators with `.refine()` and `.superRefine()`
7. Async validation (check DB for uniqueness)
8. Schema composition: `.merge()`, `.extend()`, `.pick()`, `.omit()`
9. Type inference: `z.infer<typeof schema>`
10. Parse vs safeParse — when to use each
11. Error formatting: turn Zod errors into user-friendly messages
12. OpenAPI schema generation from Zod schemas
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Master Database Migrations

**id:** `03-backend-dev/database-migrations` · **Difficulty:** intermediate · **Tags:** migrations, postgresql, nodejs, devops

**Placeholders:** [DESCRIBE CURRENT STATE], [DESCRIBE TARGET STATE]

````text
Master database migrations for my [Node.js/Python] app.

Current schema: [DESCRIBE CURRENT STATE]
Desired schema: [DESCRIBE TARGET STATE]

Implement using [Flyway / Liquibase / node-pg-migrate / Prisma Migrate]:
1. Migration file naming convention
2. The migration SQL/code for each change
3. Rollback scripts for each migration
4. Data migrations (migrate existing data)
5. Running migrations in CI/CD pipeline
6. Zero-downtime migrations for:
   - Adding a column (always safe)
   - Removing a column (dangerous — show safe approach)
   - Renaming a column (the expand-contract pattern)
   - Adding a NOT NULL constraint to existing column
7. Migration testing in staging before production
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Optimize Database Performance

**id:** `03-backend-dev/database-optimization` · **Difficulty:** advanced · **Tags:** postgresql, optimization, indexes, sql

**Placeholders:** [DESCRIBE: slow queries, high CPU, connection exhaustion, etc.]

````text
Optimize my PostgreSQL database for production performance.

Current issues: [DESCRIBE: slow queries, high CPU, connection exhaustion, etc.]

Implement:
1. **Index analysis**: EXPLAIN ANALYZE on slow queries, add missing indexes
2. **Index types**: B-tree vs GIN vs GiST — when to use each
3. **Query optimization**: rewrite N+1 queries, use CTEs
4. **Connection pooling**: PgBouncer configuration
5. **Partitioning**: partition large tables by date or category
6. **Vacuuming**: configure autovacuum for high-write tables
7. **Read replicas**: route read queries to replica
8. **pg_stat_statements**: identify top slow queries
9. **Caching at application layer**: reduce DB load
10. **Schema changes**: zero-downtime approaches for large tables
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Dockerize a Node.js Application

**id:** `03-backend-dev/docker-setup` · **Difficulty:** intermediate · **Tags:** docker, containers, nodejs, devops

**Placeholders:** [DESCRIBE YOUR APP AND ITS DEPENDENCIES]

````text
Dockerize my Node.js application for production.

Current app: [DESCRIBE YOUR APP AND ITS DEPENDENCIES]

Create:
1. **Dockerfile** (multi-stage build):
   - Stage 1: deps only (layer caching)
   - Stage 2: build TypeScript
   - Stage 3: production image (distroless or alpine)
   - Non-root user for security
   - Health check instruction
2. **docker-compose.yml** for local dev:
   - App + PostgreSQL + Redis
   - Volume mounts for hot reload
   - Environment file
3. **.dockerignore** (exclude node_modules, .env, .git)
4. Optimizations: final image < 200MB, layer caching tricks
5. Production considerations: secrets management, logging to stdout
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Master Drizzle ORM

**id:** `03-backend-dev/drizzle-orm` · **Difficulty:** intermediate · **Tags:** drizzle, orm, typescript, postgresql

**Placeholders:** [DESCRIBE YOUR DATA MODEL]

````text
Master Drizzle ORM — the TypeScript-first, lightweight ORM.

Schema: [DESCRIBE YOUR DATA MODEL]

Implement:
1. Schema definition (table, columns, relations)
2. Drizzle Kit migration generation
3. CRUD operations with full TypeScript inference
4. Joins and relations
5. Transactions
6. Aggregate queries
7. JSON column operations
8. Full-text search with PostgreSQL
9. Drizzle Studio for database browsing
10. Drizzle with Cloudflare D1 (edge SQLite)

Compare with Prisma: when to choose Drizzle (performance-critical, edge compatibility).
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Transactional Email Service

**id:** `03-backend-dev/email-service` · **Difficulty:** intermediate · **Tags:** email, sendgrid, nodejs, backend

**Placeholders:** [LIST: welcome, password reset, invoice, notification, etc.]

````text
Build a robust transactional email service.

Using: Resend (modern) or SendGrid

Emails to send: [LIST: welcome, password reset, invoice, notification, etc.]

Implement:
1. Email template system using React Email (beautiful HTML emails)
2. Template per email type with dynamic variables
3. Queue emails via BullMQ (don't send synchronously in API)
4. Retry logic for failed sends
5. Unsubscribe handling (one-click, per-category)
6. Email logging (track sent, delivered, bounced, opened)
7. Bounce handling webhook
8. Preview endpoint in development
9. Test mode (log to console instead of sending)
10. Rate limiting per recipient
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build an Event-Driven System

**id:** `03-backend-dev/event-driven-system` · **Difficulty:** advanced · **Tags:** event-driven, rabbitmq, kafka, nodejs

**Placeholders:** [DESCRIPTION]

````text
Build an event-driven system using message queues for: [DESCRIPTION].

Using: RabbitMQ (or Kafka for higher throughput)

Implement:
1. Publisher: emit events with schema validation
2. Consumer: subscribe with retry logic (dead letter queue)
3. Event schema registry (Avro or JSON Schema)
4. At-least-once delivery guarantee
5. Idempotency keys to handle duplicate messages
6. Saga pattern for distributed transactions
7. Event sourcing: store all events, derive state
8. Node.js implementation with amqplib or kafkajs
9. Docker compose for local development
10. Monitoring: queue depth, consumer lag metrics
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Production Express.js REST API

**id:** `03-backend-dev/express-rest-api` · **Difficulty:** intermediate · **Tags:** express, nodejs, typescript, rest

**Placeholders:** [APP DESCRIPTION]

````text
Build a production-ready REST API with Express.js + TypeScript for: [APP DESCRIPTION].

Include:
- Folder structure: routes/, controllers/, services/, middleware/, models/
- JWT authentication middleware
- Request validation with Zod
- Error handling middleware (centralized)
- Rate limiting (express-rate-limit)
- Helmet.js security headers
- Morgan request logging
- CORS configuration
- Health check endpoint: GET /health
- Environment config with dotenv-safe
- Swagger/OpenAPI docs with swagger-ui-express
- Graceful shutdown handling
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a FastAPI Python Backend

**id:** `03-backend-dev/fastapi-backend` · **Difficulty:** intermediate · **Tags:** fastapi, python, rest, postgresql

**Placeholders:** [APP DESCRIPTION]

````text
Build a production FastAPI backend for: [APP DESCRIPTION].

Include:
- Pydantic v2 models for request/response validation
- SQLAlchemy 2.0 async ORM with PostgreSQL
- Alembic migrations
- JWT auth (python-jose)
- Background tasks with Celery + Redis
- Dependency injection pattern
- API versioning (/api/v1/)
- OpenAPI docs (FastAPI auto-generates)
- Pytest test suite with fixtures
- Docker + docker-compose setup
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a File Storage Service

**id:** `03-backend-dev/file-storage-service` · **Difficulty:** intermediate · **Tags:** s3, storage, uploads, backend

````text
Build a file storage service supporting uploads, downloads, and transformations.

Storage backend: AWS S3 (or Cloudflare R2 — S3-compatible, free egress)

API endpoints:
- POST /upload → presigned URL (client uploads directly)
- GET /download/:fileId → presigned download URL
- DELETE /files/:fileId → delete from S3 + database
- GET /files → list user's files with pagination

Features:
1. Virus scan integration (ClamAV or CloudScan)
2. File type validation (magic bytes, not just extension)
3. Image resizing on upload (Sharp)
4. Quota management per user
5. Signed URLs with expiry
6. CDN delivery
7. Resumable uploads for large files (S3 multipart)
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a REST API in Go

**id:** `03-backend-dev/go-rest-api` · **Difficulty:** advanced · **Tags:** go, golang, rest, gin

**Placeholders:** [DESCRIPTION]

````text
Build a production REST API in Go for: [DESCRIPTION].

Using: Gin framework + sqlx + PostgreSQL

Include:
- Project structure following Go conventions
- Middleware: auth (JWT), logging (zerolog), recovery, CORS
- Database: sqlx with prepared statements (prevent SQL injection)
- Repository pattern with interfaces (for testability)
- Config management with env vars (godotenv)
- Graceful shutdown
- Makefile for common tasks
- Docker multi-stage build
- Unit tests using testify and mock generation
- OpenAPI spec from Go comments (swaggo)
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Graceful shutdown and error handling in Go

**id:** `03-backend-dev/graceful-shutdown-and-error-handling-in-go` · **Difficulty:** advanced · **Tags:** backend, database, api

````text
Configure graceful shutdown, error handling, and system signal monitoring in Go for a payment gateway webhook handler with OAuth2 login integration.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions


## Build a GraphQL Server with Apollo

**id:** `03-backend-dev/graphql-server` · **Difficulty:** advanced · **Tags:** graphql, apollo, nodejs, typescript

**Placeholders:** [DESCRIBE YOUR DATA DOMAIN]

````text
Build a production GraphQL server with Apollo Server 4 + TypeScript.

Domain: [DESCRIBE YOUR DATA DOMAIN]

Schema: write complete SDL for all types, queries, mutations, subscriptions

Implement:
- Code-first approach using TypeGraphQL OR schema-first with graphql-codegen
- Resolvers with proper separation (resolver → service → repository)
- DataLoader for N+1 prevention
- Cursor-based pagination
- Subscription with Redis pub/sub
- Authentication via context
- Authorization with field-level permissions
- Error handling: custom error classes → GraphQL errors
- Rate limiting per field
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a gRPC Service

**id:** `03-backend-dev/grpc-service` · **Difficulty:** advanced · **Tags:** grpc, protobuf, nodejs, backend

**Placeholders:** [DESCRIPTION]

````text
Build a gRPC service for: [DESCRIPTION].

Define the proto file:
- Service definition with all RPCs
- Message types with proper field numbers
- Use: unary, server streaming, client streaming, bidirectional streaming where appropriate

Implement in Node.js (@grpc/grpc-js):
1. Server implementation
2. Client SDK (reusable wrapper)
3. Authentication via metadata
4. Interceptors for logging and error handling
5. Health checking (grpc-health-probe)
6. Reflection (for grpcui/grpcurl debugging)
7. Load balancing client-side
8. Proto-generated TypeScript types
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Implement Production Health Checks

**id:** `03-backend-dev/health-check` · **Difficulty:** intermediate · **Tags:** health-check, monitoring, backend, devops

````text
Implement comprehensive health checks for my Node.js application.

Endpoints:
- `GET /health` — quick liveness probe (always returns 200 if process is alive)
- `GET /health/ready` — readiness probe (checks all dependencies)
- `GET /health/startup` — startup probe (for Kubernetes)

Readiness checks:
1. PostgreSQL: test query
2. Redis: PING
3. External APIs: your critical third-party services
4. Storage: check S3 accessibility
5. Memory: flag if heap > 80%
6. Disk: flag if disk > 90%

Response format (standardized health check API):
```json
{"status": "ok|degraded|critical", "checks": {...}, "version": "...", "uptime": 123}
```

Kubernetes liveness/readiness probe config included.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Implement Prometheus metrics in a Rust (Axum) backend

**id:** `03-backend-dev/implement-prometheus-metrics-in-a-rust-axum-backend` · **Difficulty:** intermediate · **Tags:** rust, backend, database, api

````text
Implement Prometheus metrics in a Rust (Axum) backend server handling a payment gateway webhook handler. Follow clean architecture and document endpoints.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions


## Set Up Production Logging and Monitoring

**id:** `03-backend-dev/logging-monitoring` · **Difficulty:** advanced · **Tags:** logging, monitoring, opentelemetry, devops

````text
Set up production-grade logging and monitoring for my Node.js app.

**Logging** (using pino — fastest Node.js logger):
1. Structured JSON logs with correlation IDs
2. Log levels: error, warn, info, debug
3. Redact sensitive fields (passwords, tokens, PII)
4. Request/response logging middleware
5. Error logging with stack traces
6. Log shipping to [ELK / Datadog / Grafana Loki]

**Metrics** (using OpenTelemetry):
1. HTTP request duration histogram
2. Custom business metrics (signups, payments)
3. Node.js runtime metrics (heap, CPU)
4. Prometheus endpoint for scraping

**Tracing**: distributed trace IDs across services

**Alerts**: define 5 critical alerts and their thresholds.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Design a Microservices Architecture

**id:** `03-backend-dev/microservices-architecture` · **Difficulty:** advanced · **Tags:** microservices, docker, kubernetes, architecture

**Placeholders:** [MONOLITH TO DECOMPOSE / NEW SYSTEM]

````text
Design a microservices architecture for: [MONOLITH TO DECOMPOSE / NEW SYSTEM].

Services to create:
- [Service 1]: responsibility
- [Service 2]: responsibility
- [Service 3]: responsibility

For each service:
1. Technology choice and justification
2. API contract (REST or gRPC proto definition)
3. Data store (each service owns its data)
4. Docker container setup
5. Health check endpoint

Cross-cutting concerns:
- API Gateway (Kong or Nginx)
- Service discovery
- Distributed tracing (OpenTelemetry)
- Centralized logging (ELK stack)
- Circuit breaker (Resilience4j or polly)
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Scaffold a NestJS Application

**id:** `03-backend-dev/nestjs-app` · **Difficulty:** advanced · **Tags:** nestjs, nodejs, typescript, backend

**Placeholders:** [DESCRIPTION], [YOUR DOMAIN MODULE]

````text
Scaffold a production NestJS application for: [DESCRIPTION].

Modules to generate:
- AuthModule: JWT, refresh tokens, guards
- UsersModule: CRUD, roles
- [YOUR DOMAIN MODULE]: core business logic

For each module include:
- Controller with all routes
- Service with business logic
- DTOs with class-validator decorators
- Entity (TypeORM or Prisma)
- Guard and Decorator examples
- Unit tests for service

Also: global exception filter, logging interceptor, configuration service, Swagger setup.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Secure a Node.js Application

**id:** `03-backend-dev/node-security` · **Difficulty:** advanced · **Tags:** security, nodejs, express, owasp

**Placeholders:** [DESCRIBE YOUR APP]

````text
Perform a security audit and harden my Node.js/Express application.

Current codebase: [DESCRIBE YOUR APP]

Fix these OWASP Top 10 issues:
1. **Injection**: parameterized queries, input sanitization
2. **Broken Auth**: JWT best practices, secure session management
3. **Sensitive Data**: encrypt PII, HTTPS everywhere, no secrets in logs
4. **XXE**: disable XML entity expansion
5. **Broken Access Control**: check authorization on every route
6. **Security Misconfiguration**: Helmet.js, remove X-Powered-By, CSP
7. **XSS**: output encoding, CSP headers
8. **Insecure Deserialization**: validate all deserialized data
9. **Known Vulnerabilities**: npm audit fix
10. **Insufficient Logging**: structured logging of security events

Output: security-hardened version of each vulnerable code section.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Implement OAuth 2.0 and OIDC

**id:** `03-backend-dev/oauth-implementation` · **Difficulty:** advanced · **Tags:** oauth, oidc, auth, security

````text
Implement OAuth 2.0 / OpenID Connect from scratch (to understand it deeply).

Implement both sides:
**Authorization Server** (simplified, for learning):
1. Authorization endpoint (redirect with code)
2. Token endpoint (exchange code for access + refresh + ID token)
3. PKCE support (prevent interception attacks)
4. UserInfo endpoint
5. JWKS endpoint (public keys for JWT verification)

**Resource Server**:
1. JWT validation middleware (verify signature, claims, expiry)
2. Scope checking

**Client** (your app):
1. Full OAuth flow implementation
2. Token refresh logic
3. Secure token storage

Show: complete request/response flow with actual HTTP examples.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Implement Pagination Patterns

**id:** `03-backend-dev/pagination-patterns` · **Difficulty:** intermediate · **Tags:** pagination, api, rest, backend

**Placeholders:** [DESCRIBE YOUR DATA: ordered by what, expected size, query patterns]

````text
Implement pagination for my API and explain the tradeoffs.

My data: [DESCRIBE YOUR DATA: ordered by what, expected size, query patterns]

Implement all three patterns:

**1. Offset pagination** (simple but slow for large datasets):
- `GET /items?page=2&limit=20`
- SQL: OFFSET + LIMIT

**2. Cursor pagination** (fast, consistent, recommended):
- `GET /items?cursor=eyJ...&limit=20`
- SQL: `WHERE id > cursor_id`
- Base64-encoded cursor encoding/decoding

**3. Keyset pagination** (for sorted by multiple fields):
- Complex multi-column keyset

For each: SQL query, API response shape, frontend usage, and when to use it.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Master Prisma ORM

**id:** `03-backend-dev/prisma-orm` · **Difficulty:** intermediate · **Tags:** prisma, orm, postgresql, typescript

**Placeholders:** [DESCRIBE YOUR DATA MODEL]

````text
Master Prisma ORM for my Node.js app.

My database models: [DESCRIBE YOUR DATA MODEL]

Generate:
1. Complete `schema.prisma` with all models, relations, indexes
2. Initial migration SQL
3. Seed file with realistic data
4. TypeScript CRUD repository class for each model
5. Optimized queries: pagination, filtering, sorting, full-text search
6. Transactions for complex operations
7. Soft deletes pattern
8. Relation loading strategies: include vs select vs separate queries
9. Prisma Client extension for custom methods
10. Connection pooling config for production (PgBouncer)
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Master Redis Patterns for Backend

**id:** `03-backend-dev/redis-patterns` · **Difficulty:** advanced · **Tags:** redis, caching, patterns, backend

````text
Implement these Redis patterns in my Node.js application:

1. **Session storage**: store and retrieve user sessions
2. **Distributed lock**: prevent race conditions across instances
3. **Rate limiting**: sliding window counter per user/IP
4. **Pub/Sub**: broadcast events to WebSocket servers
5. **Job queue**: simple queue without BullMQ
6. **Leaderboard**: sorted sets for real-time rankings
7. **Autocomplete**: sorted sets for prefix search
8. **Geospatial**: store locations, query nearby
9. **Bloom filter**: check membership without storing all data
10. **Cache with automatic refresh**: lazy loading pattern

Each pattern: Node.js code (ioredis), key naming, TTL strategy, when to use.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Implement REST API Versioning

**id:** `03-backend-dev/rest-api-versioning` · **Difficulty:** intermediate · **Tags:** rest, versioning, api, backend

**Placeholders:** [DESCRIBE], [LIST WHAT'S CHANGING]

````text
Implement API versioning strategy for my REST API.

Current API: [DESCRIBE]
Breaking changes needed: [LIST WHAT'S CHANGING]

Implement URL versioning (/api/v1/, /api/v2/):
1. Router setup for multiple versions
2. Shared code between versions (don't duplicate business logic)
3. Request coercion: V1 request → V2 handler → V1 response
4. Version deprecation headers
5. Sunset date announcement
6. Migration guide documentation
7. Maintaining tests for all active versions

Also explain: URL vs header vs query param versioning — why URL wins for most APIs.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## REST API Design Best Practices

**id:** `03-backend-dev/rest-best-practices` · **Difficulty:** beginner · **Tags:** rest, api-design, best-practices, backend

**Placeholders:** [DESCRIBE CURRENT ROUTES]

````text
Apply REST API best practices to my API.

My current API: [DESCRIBE CURRENT ROUTES]

Best practices to implement:
1. **Naming**: nouns not verbs, plural resources, lowercase kebab-case
2. **HTTP methods**: GET (safe+idempotent), POST, PUT (full replace), PATCH (partial), DELETE
3. **Status codes**: the right code for every situation (cheat sheet)
4. **Filtering**: `?filter[status]=active&filter[type]=post`
5. **Sorting**: `?sort=-createdAt,name`
6. **Pagination**: cursor-based with metadata
7. **Versioning**: `/api/v1/`
8. **Error format**: consistent JSON error body
9. **HATEOAS**: optional but show when useful
10. **Content negotiation**: Accept header

Rewrite my current routes applying all best practices.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a Full-Text Search Engine

**id:** `03-backend-dev/search-engine` · **Difficulty:** advanced · **Tags:** search, elasticsearch, postgresql, backend

**Placeholders:** [DESCRIBE YOUR DATA]

````text
Add full-text search to my app.

Data to index: [DESCRIBE YOUR DATA]

Option A — PostgreSQL Full-Text Search (no external service):
1. tsvector columns + GIN index
2. to_tsquery with multiple languages
3. Ranking results by relevance (ts_rank)
4. Highlighting matching terms
5. Trigram similarity for fuzzy search

Option B — Elasticsearch:
1. Index mapping design
2. Bulk indexing pipeline
3. Query DSL for: exact match, fuzzy, phrase, wildcard
4. Aggregations for faceted filtering
5. Highlighting
6. Keep ES in sync with DB (CDC or dual-write)

Include: search result pagination, typo tolerance, synonym support.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Implement Server-Sent Events (SSE)

**id:** `03-backend-dev/server-sent-events` · **Difficulty:** intermediate · **Tags:** sse, streaming, real-time, backend

**Placeholders:** [DESCRIBE: live notifications / log streaming / AI response streaming / dashboard updates]

````text
Implement Server-Sent Events (SSE) for real-time one-way streaming.

Use case: [DESCRIBE: live notifications / log streaming / AI response streaming / dashboard updates]

Backend (Express.js):
1. SSE endpoint with proper headers (Content-Type: text/event-stream)
2. Event types: named events, data, id, retry
3. Heartbeat to keep connection alive (comment every 30s)
4. Authentication (validate token before streaming)
5. Client disconnect detection and cleanup
6. Broadcasting to multiple clients

Frontend (React):
1. `useEventSource` hook with reconnection
2. Handle multiple event types
3. Connection status indicator

Compare with WebSockets: when SSE is the better choice.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Design a Serverless Architecture

**id:** `03-backend-dev/serverless-architecture` · **Difficulty:** advanced · **Tags:** serverless, aws-lambda, api-gateway, architecture

**Placeholders:** [APP DESCRIPTION]

````text
Design a complete serverless architecture on AWS for: [APP DESCRIPTION].

Using: AWS Lambda + API Gateway + DynamoDB + S3 + SQS

Design:
1. Lambda functions (one per API endpoint — thin handlers)
2. API Gateway routes and auth (JWT or API Key)
3. DynamoDB table design (single-table design)
4. S3 buckets and access policies
5. SQS queues for async processing
6. EventBridge for scheduled tasks
7. CloudWatch alarms and dashboards
8. IAM roles (principle of least privilege)
9. Infrastructure as Code (AWS CDK in TypeScript)
10. Local development with SAM CLI
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Set Up tRPC for Type-Safe APIs

**id:** `03-backend-dev/trpc-setup` · **Difficulty:** intermediate · **Tags:** trpc, typescript, nextjs, fullstack

**Placeholders:** [LIST YOUR DATA ENTITIES AND OPERATIONS]

````text
Set up tRPC for end-to-end type-safe APIs between my Next.js frontend and backend.

Routers needed: [LIST YOUR DATA ENTITIES AND OPERATIONS]

Implement:
1. tRPC router with procedures for each operation
2. Input validation with Zod
3. Authentication middleware (protected procedures)
4. Context: user session + database client
5. Next.js App Router integration (both server and client usage)
6. React Query integration (useQuery, useMutation)
7. Error handling with TRPCError
8. Subscription for real-time (WebSocket transport)
9. Type inference: `RouterInputs`, `RouterOutputs` types
10. Testing tRPC procedures with `createCaller`
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Master TypeORM Patterns

**id:** `03-backend-dev/typeorm-patterns` · **Difficulty:** intermediate · **Tags:** typeorm, orm, typescript, postgresql

**Placeholders:** [DESCRIBE YOUR DATA MODEL]

````text
Master TypeORM for my TypeScript + PostgreSQL application.

Entities: [DESCRIBE YOUR DATA MODEL]

Implement:
1. Entity definitions with all decorators
2. Relations: OneToOne, ManyToOne, ManyToMany
3. Cascade operations
4. Repository pattern with custom repositories
5. QueryBuilder for complex queries
6. Transactions (with proper isolation levels)
7. Migrations: generate, run, revert
8. Subscribers (entity lifecycle hooks)
9. Soft delete
10. Pagination utility
11. Optimistic locking for concurrent updates
12. TypeORM with NestJS integration
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a WebSocket Server

**id:** `03-backend-dev/websocket-server` · **Difficulty:** intermediate · **Tags:** websockets, nodejs, real-time, backend

````text
Build a production WebSocket server for: [USE CASE — chat / notifications / live data].

Using: Node.js + ws library (or uWebSockets.js for max performance)

Implement:
- Connection management (track all connected clients)
- Authentication (validate JWT on upgrade request)
- Rooms/channels (subscribe to specific topics)
- Message protocol: define JSON message types
- Heartbeat (ping/pong to detect dead connections)
- Reconnection handling (client-side)
- Horizontal scaling with Redis pub/sub (sticky sessions or stateless)
- Rate limiting per connection
- Message history (last N messages on join)
- Graceful shutdown (drain connections)
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Implement Background Job Queues

**id:** `03-backend-dev/worker-queues` · **Difficulty:** intermediate · **Tags:** bullmq, redis, queues, nodejs

**Placeholders:** [LIST YOUR BACKGROUND TASKS]

````text
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
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case


## Build a production-ready [STACK] backend for [SYSTEM]

**id:** `03-backend-dev/build-a-production-ready-stack-backend-for-system` · **Difficulty:** beginner/intermediate/advanced · **Tags:** backend, database, api, node.js, python, rust

**Variant group** (5 generated prompts collapsed). Pick one value per placeholder:
- `[STACK]`: Go | Node.js (Fastify) | Python (Django) | Rust (Axum)
- `[SYSTEM]`: a collaborative document editor backend | a multi-tenant SaaS backend | a video processing microservice
- `[FEATURE]`: PostgreSQL database integration | Prometheus metrics | Redis caching

````text
Build a production-ready REST API with [STACK] for [SYSTEM]. Include [FEATURE], centralized error handling, and robust logging.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** build-a-production-ready-go-backend-for-a-video-processing-microservice, build-a-production-ready-nodejs-fastify-backend-for-a-multi-tenant-saas-backend, build-a-production-ready-nodejs-fastify-backend-for-a-video-processing-microservice, build-a-production-ready-python-django-backend-for-a-collaborative-document-editor-backend, build-a-production-ready-rust-axum-backend-for-a-video-processing-microservice

