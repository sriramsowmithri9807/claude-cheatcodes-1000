#!/usr/bin/env python3
"""Seed prompts for categories 03-10."""
from pathlib import Path

ROOT = Path(__file__).parent.parent
PROMPTS = ROOT / "prompts"

def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n")
    print(f"  ✍️  {path.relative_to(ROOT)}")

def make_prompt(category, title, tags, difficulty, prompt_text, models=None):
    if models is None:
        models = ["claude-haiku-3-5", "claude-sonnet-4", "claude-opus-4", "claude-fable-5"]
    return f"""---
title: "{title}"
category: {category}
models: [{', '.join(models)}]
tags: [{', '.join(tags)}]
difficulty: {difficulty}
author: community
tested: true
---

## 🎯 Prompt

```
{prompt_text.strip()}
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
"""

# ─── CATEGORY 03: BACKEND DEV ─────────────────────────────────────────────────
cat = PROMPTS / "03-backend-dev"
backend = [
  ("express-rest-api.md","Build a Production Express.js REST API",["express","nodejs","typescript","rest"],"intermediate","""Build a production-ready REST API with Express.js + TypeScript for: [APP DESCRIPTION].

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
- Graceful shutdown handling"""),
  ("fastapi-backend.md","Build a FastAPI Python Backend",["fastapi","python","rest","postgresql"],"intermediate","""Build a production FastAPI backend for: [APP DESCRIPTION].

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
- Docker + docker-compose setup"""),
  ("nestjs-app.md","Scaffold a NestJS Application",["nestjs","nodejs","typescript","backend"],"advanced","""Scaffold a production NestJS application for: [DESCRIPTION].

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

Also: global exception filter, logging interceptor, configuration service, Swagger setup."""),
  ("prisma-orm.md","Master Prisma ORM",["prisma","orm","postgresql","typescript"],"intermediate","""Master Prisma ORM for my Node.js app.

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
10. Connection pooling config for production (PgBouncer)"""),
  ("graphql-server.md","Build a GraphQL Server with Apollo",["graphql","apollo","nodejs","typescript"],"advanced","""Build a production GraphQL server with Apollo Server 4 + TypeScript.

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
- Rate limiting per field"""),
  ("go-rest-api.md","Build a REST API in Go",["go","golang","rest","gin"],"advanced","""Build a production REST API in Go for: [DESCRIPTION].

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
- OpenAPI spec from Go comments (swaggo)"""),
  ("websocket-server.md","Build a WebSocket Server",["websockets","nodejs","real-time","backend"],"intermediate","""Build a production WebSocket server for: [USE CASE — chat / notifications / live data].

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
- Graceful shutdown (drain connections)"""),
  ("microservices-architecture.md","Design a Microservices Architecture",["microservices","docker","kubernetes","architecture"],"advanced","""Design a microservices architecture for: [MONOLITH TO DECOMPOSE / NEW SYSTEM].

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
- Circuit breaker (Resilience4j or polly)"""),
  ("event-driven-system.md","Build an Event-Driven System",["event-driven","rabbitmq","kafka","nodejs"],"advanced","""Build an event-driven system using message queues for: [DESCRIPTION].

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
10. Monitoring: queue depth, consumer lag metrics"""),
  ("worker-queues.md","Implement Background Job Queues",["bullmq","redis","queues","nodejs"],"intermediate","""Implement a background job processing system using BullMQ + Redis.

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
10. Dead letter queue for failed jobs"""),
  ("caching-strategies.md","Implement Advanced Caching Strategies",["redis","caching","backend","performance"],"advanced","""Implement a comprehensive caching strategy for my Node.js API.

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
10. **Monitoring**: cache hit rate, eviction rate metrics"""),
  ("database-migrations.md","Master Database Migrations",["migrations","postgresql","nodejs","devops"],"intermediate","""Master database migrations for my [Node.js/Python] app.

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
7. Migration testing in staging before production"""),
  ("rest-api-versioning.md","Implement REST API Versioning",["rest","versioning","api","backend"],"intermediate","""Implement API versioning strategy for my REST API.

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

Also explain: URL vs header vs query param versioning — why URL wins for most APIs."""),
  ("grpc-service.md","Build a gRPC Service",["grpc","protobuf","nodejs","backend"],"advanced","""Build a gRPC service for: [DESCRIPTION].

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
8. Proto-generated TypeScript types"""),
  ("api-gateway.md","Build an API Gateway",["api-gateway","nginx","nodejs","architecture"],"advanced","""Build an API Gateway for my microservices.

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
10. Graceful degradation (serve cached response when upstream is down)"""),
  ("serverless-architecture.md","Design a Serverless Architecture",["serverless","aws-lambda","api-gateway","architecture"],"advanced","""Design a complete serverless architecture on AWS for: [APP DESCRIPTION].

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
10. Local development with SAM CLI"""),
  ("oauth-implementation.md","Implement OAuth 2.0 and OIDC",["oauth","oidc","auth","security"],"advanced","""Implement OAuth 2.0 / OpenID Connect from scratch (to understand it deeply).

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

Show: complete request/response flow with actual HTTP examples."""),
  ("search-engine.md","Build a Full-Text Search Engine",["search","elasticsearch","postgresql","backend"],"advanced","""Add full-text search to my app.

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

Include: search result pagination, typo tolerance, synonym support."""),
  ("file-storage-service.md","Build a File Storage Service",["s3","storage","uploads","backend"],"intermediate","""Build a file storage service supporting uploads, downloads, and transformations.

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
7. Resumable uploads for large files (S3 multipart)"""),
  ("email-service.md","Build a Transactional Email Service",["email","sendgrid","nodejs","backend"],"intermediate","""Build a robust transactional email service.

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
10. Rate limiting per recipient"""),
  ("node-security.md","Secure a Node.js Application",["security","nodejs","express","owasp"],"advanced","""Perform a security audit and harden my Node.js/Express application.

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

Output: security-hardened version of each vulnerable code section."""),
  ("redis-patterns.md","Master Redis Patterns for Backend",["redis","caching","patterns","backend"],"advanced","""Implement these Redis patterns in my Node.js application:

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

Each pattern: Node.js code (ioredis), key naming, TTL strategy, when to use."""),
  ("logging-monitoring.md","Set Up Production Logging and Monitoring",["logging","monitoring","opentelemetry","devops"],"advanced","""Set up production-grade logging and monitoring for my Node.js app.

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

**Alerts**: define 5 critical alerts and their thresholds."""),
  ("database-optimization.md","Optimize Database Performance",["postgresql","optimization","indexes","sql"],"advanced","""Optimize my PostgreSQL database for production performance.

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
10. **Schema changes**: zero-downtime approaches for large tables"""),
  ("api-testing.md","Write Comprehensive API Tests",["testing","supertest","jest","api"],"intermediate","""Write comprehensive tests for my REST API.

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
- Coverage: target 80%+"""),
  ("health-check.md","Implement Production Health Checks",["health-check","monitoring","backend","devops"],"intermediate","""Implement comprehensive health checks for my Node.js application.

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

Kubernetes liveness/readiness probe config included."""),
  ("pagination-patterns.md","Implement Pagination Patterns",["pagination","api","rest","backend"],"intermediate","""Implement pagination for my API and explain the tradeoffs.

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

For each: SQL query, API response shape, frontend usage, and when to use it."""),
  ("auth-jwt.md","Implement JWT Authentication from Scratch",["jwt","auth","security","nodejs"],"intermediate","""Implement JWT authentication from scratch in Node.js (to deeply understand it).

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

Explain every security decision."""),
  ("docker-setup.md","Dockerize a Node.js Application",["docker","containers","nodejs","devops"],"intermediate","""Dockerize my Node.js application for production.

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
5. Production considerations: secrets management, logging to stdout"""),
  ("trpc-setup.md","Set Up tRPC for Type-Safe APIs",["trpc","typescript","nextjs","fullstack"],"intermediate","""Set up tRPC for end-to-end type-safe APIs between my Next.js frontend and backend.

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
10. Testing tRPC procedures with `createCaller`"""),
  ("api-rate-limiting.md","Advanced API Rate Limiting",["rate-limiting","redis","api","security"],"advanced","""Implement sophisticated API rate limiting for a production API.

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
10. Dashboard showing rate limit usage per API key"""),
  ("cron-scheduler.md","Build a Cron Job Scheduler",["cron","nodejs","scheduler","backend"],"intermediate","""Build a reliable cron job scheduler system.

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
10. Retry on failure with backoff"""),
  ("data-validation.md","Master Data Validation with Zod",["zod","validation","typescript","backend"],"intermediate","""Master Zod for data validation across your entire Node.js stack.

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
12. OpenAPI schema generation from Zod schemas"""),
  ("api-documentation.md","Generate Beautiful API Documentation",["swagger","openapi","docs","api"],"intermediate","""Generate comprehensive, beautiful API documentation.

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

Host docs at: `/docs` in development, separate docs site in production."""),
  ("connection-pooling.md","Configure Database Connection Pooling",["postgresql","connection-pool","pg","backend"],"intermediate","""Configure optimal database connection pooling for my Node.js app.

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

Benchmark: show connection count under load without vs with pooling."""),
  ("api-idempotency.md","Implement Idempotent APIs",["idempotency","api","payments","backend"],"advanced","""Implement idempotent API endpoints (critical for payments and financial operations).

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
Show the complete middleware implementation."""),
  ("background-tasks.md","Implement Background Tasks in Node.js",["background-tasks","workers","nodejs","performance"],"intermediate","""Implement efficient background task processing in Node.js.

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

When to use queue vs worker thread vs async — decision matrix."""),
  ("rest-best-practices.md","REST API Design Best Practices",["rest","api-design","best-practices","backend"],"beginner","""Apply REST API best practices to my API.

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

Rewrite my current routes applying all best practices."""),
  ("typeorm-patterns.md","Master TypeORM Patterns",["typeorm","orm","typescript","postgresql"],"intermediate","""Master TypeORM for my TypeScript + PostgreSQL application.

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
12. TypeORM with NestJS integration"""),
  ("api-security-headers.md","Set Security Headers on Every API Response",["security","headers","express","backend"],"beginner","""Set proper HTTP security headers on every API response.

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

Show the Helmet.js config and test with securityheaders.com."""),
  ("drizzle-orm.md","Master Drizzle ORM",["drizzle","orm","typescript","postgresql"],"intermediate","""Master Drizzle ORM — the TypeScript-first, lightweight ORM.

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

Compare with Prisma: when to choose Drizzle (performance-critical, edge compatibility)."""),
  ("server-sent-events.md","Implement Server-Sent Events (SSE)",["sse","streaming","real-time","backend"],"intermediate","""Implement Server-Sent Events (SSE) for real-time one-way streaming.

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

Compare with WebSockets: when SSE is the better choice."""),
  ("api-gateway-pattern.md","Implement the Backend-for-Frontend Pattern",["bff","api-gateway","architecture","fullstack"],"advanced","""Implement the Backend-for-Frontend (BFF) pattern.

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
- Caches aggressively for its usage pattern"""),
]

for filename, title, tags, difficulty, prompt_text in backend:
    write(cat / filename, make_prompt("backend-dev", title, tags, difficulty, prompt_text))

# ─── CATEGORY 04: FULLSTACK PROJECTS ───────────────────────────────────────────
cat = PROMPTS / "04-fullstack-projects"
fullstack = [
  ("saas-starter.md","Build a Complete SaaS Starter Kit",["saas","nextjs","stripe","auth"],"advanced","""Build a complete, production-ready SaaS starter kit.

Tech stack:
- Frontend: Next.js 14 App Router + TypeScript
- Auth: Auth.js v5
- Database: PostgreSQL + Prisma ORM
- Payments: Stripe subscriptions
- Email: Resend
- UI: shadcn/ui
- Deployment: Vercel + Supabase

Features to include:
1. Auth: signup, login, OAuth (Google/GitHub), email verify, password reset
2. Stripe: checkout, webhooks, customer portal, subscription status
3. Dashboard: overview, settings, billing page
4. Team/org support: invite members, roles (owner/admin/member)
5. API: public API with API key generation
6. Admin: user management panel

Output: complete folder structure + all core files."""),
  ("ecommerce-platform.md","Build an E-Commerce Platform",["ecommerce","nextjs","stripe","fullstack"],"advanced","""Build a full e-commerce platform from scratch.

Stack: Next.js 14 + TypeScript + PostgreSQL + Stripe + Cloudinary

Features:
1. **Product catalog**: list, search, filter, categories
2. **Product page**: images, description, variants (size/color), stock
3. **Cart**: add/remove, quantity, persist in localStorage or session
4. **Checkout**: Stripe Payment Element, address, shipping options
5. **Orders**: order history, order detail, status tracking
6. **Auth**: customer accounts, guest checkout
7. **Admin**: add/edit products, manage orders, inventory
8. **Email**: order confirmation, shipping notification

Database schema + all API routes + key UI components included."""),
  ("social-media-app.md","Build a Social Media App",["social","nextjs","fullstack","real-time"],"advanced","""Build a Twitter/X-style social media app.

Stack: Next.js + TypeScript + Prisma + PostgreSQL + Socket.io

Core features:
1. Posts: create, like, repost, quote, delete
2. Media: attach images/videos to posts
3. Feed: following timeline + explore tab
4. Follow/unfollow users
5. Notifications: likes, follows, mentions (real-time)
6. Search: users and posts
7. DMs: real-time direct messages
8. User profile: bio, avatar, follower/following counts
9. Hashtags: trending, click to explore
10. Auth: signup with username selection

Full database schema + API routes + React components."""),
  ("project-management-app.md","Build a Project Management App",["project-management","react","fullstack","kanban"],"advanced","""Build a Linear/Jira-style project management app.

Stack: React + Node.js + PostgreSQL + Socket.io

Features:
1. Projects and workspaces
2. Issues: create, assign, priority, status, labels
3. Kanban board with drag-and-drop
4. List view with sorting/filtering
5. Roadmap/timeline view
6. Comments on issues (with mentions)
7. Activity feed per issue
8. Team members and permissions
9. Real-time updates (collaborator sees your changes instantly)
10. Keyboard shortcuts (Linear-style)

Full schema, API design, and component architecture."""),
  ("blog-platform.md","Build a Modern Blog Platform",["blog","nextjs","mdx","cms"],"intermediate","""Build a developer blog platform like Hashnode or Dev.to.

Stack: Next.js 14 + MDX + PostgreSQL + Prisma + Cloudinary

Features:
1. Write posts in MDX (Markdown + React components)
2. Syntax highlighted code blocks
3. Tag system with exploration
4. Reactions (like, unicorn, bookmark)
5. Comments with nested replies
6. Reading progress bar
7. Related posts
8. Author profiles
9. RSS feed
10. Newsletter integration (subscribe to author)
11. SEO: OG images, sitemap, structured data
12. Admin: unpublished drafts, scheduled publishing"""),
  ("job-board.md","Build a Job Board",["job-board","nextjs","fullstack","search"],"intermediate","""Build a job board like Hacker News: Who is hiring.

Stack: Next.js + TypeScript + PostgreSQL + Stripe

Features:
1. Job listings: title, company, location, salary range, tags, description
2. Search: full-text + filter by category/location/remote/salary
3. Job detail page with apply button
4. Employer dashboard: post jobs, view applications
5. Job seeker: save jobs, apply, track applications
6. Email alerts for new matching jobs
7. Company profiles
8. Pricing: free (1 listing) vs paid (featured, unlimited)
9. Admin: approve/reject listings
10. SEO: each listing is a public indexed page

Full implementation with DB schema and key routes."""),
  ("chat-application.md","Build a Real-Time Chat App",["chat","websockets","react","fullstack"],"advanced","""Build a Slack-style real-time chat application.

Stack: React + Node.js + Socket.io + PostgreSQL + Redis

Features:
1. Workspaces and channels
2. Direct messages (1:1 and group DMs)
3. Real-time messaging with delivery receipts
4. Typing indicators
5. Message reactions (emoji)
6. Thread replies
7. File attachments (images auto-preview)
8. User presence (online/offline/away)
9. Message search
10. Notifications: desktop push, unread counts, mention alerts
11. Mobile responsive

Architecture: Socket.io rooms for channels, Redis adapter for scaling."""),
  ("learning-management.md","Build a Learning Management System",["lms","education","video","fullstack"],"advanced","""Build a Udemy-style Learning Management System (LMS).

Stack: Next.js + PostgreSQL + S3 + Stripe

Features:
1. **Course catalog**: browse, search, filter by category/price/rating
2. **Course detail**: description, curriculum, instructor, reviews, preview video
3. **Video player**: custom player with progress tracking
4. **Enrollment**: Stripe one-time payment or subscription
5. **Course player**: lesson navigation, completion tracking, notes
6. **Quiz/Assessment**: at the end of sections
7. **Certificate**: auto-generate PDF on course completion
8. **Instructor dashboard**: create courses, upload videos, view analytics
9. **Student dashboard**: enrolled courses, progress
10. **Reviews and ratings system**

Key technical challenge: video streaming with resume from where left off."""),
  ("booking-system.md","Build a Booking/Scheduling System",["booking","calendar","fullstack","stripe"],"advanced","""Build a Calendly-style booking and scheduling system.

Stack: Next.js + PostgreSQL + Stripe + SendGrid

Features:
1. User creates event types (30 min meeting, 1 hour call, etc.)
2. User sets availability windows per day of week
3. Buffer time between bookings
4. Booking page: calendar picker showing available slots
5. Booking confirmation: form (name, email, reason)
6. Invitee gets confirmation email + calendar invite (.ics)
7. Host gets notification + can reschedule/cancel
8. Time zone handling (IANA tz, no ambiguity)
9. Google Calendar integration (check conflicts, add events)
10. Stripe: charge for premium event types
11. Reminders: email 24h and 1h before"""),
  ("inventory-system.md","Build an Inventory Management System",["inventory","react","fullstack","business"],"intermediate","""Build a small business inventory management system.

Stack: React + Node.js + PostgreSQL

Features:
1. Product catalog with variants (SKU, price, cost, barcode)
2. Stock levels with low-stock alerts
3. Receive stock: purchase orders, supplier management
4. Sales: record sales, update stock automatically
5. Multi-location: manage stock across multiple stores/warehouses
6. Transfers between locations
7. Reports: inventory value, top sellers, stock history
8. Barcode scanner support (camera or USB scanner)
9. CSV import/export
10. Role-based access: manager vs staff

DB schema + API + key UI screens."""),
  ("forum-platform.md","Build a Forum Platform",["forum","community","nextjs","fullstack"],"intermediate","""Build a Reddit-style forum platform.

Stack: Next.js + PostgreSQL + Redis

Features:
1. Communities (subreddits) with moderation
2. Posts: link, text, image, video
3. Voting: upvote/downvote, Reddit-style karma
4. Comments: nested, collapsible, sorted by best/new/top
5. User profiles: karma, post/comment history
6. Moderation: remove posts, ban users, mod queue
7. Trending: hot algorithm (score + time decay)
8. Search: across posts and communities
9. Flair: user and post flair
10. Cross-posting
11. Markdown in posts and comments
12. Email digest of top posts"""),
  ("analytics-dashboard.md","Build an Analytics Dashboard",["analytics","charts","react","fullstack"],"advanced","""Build a web analytics dashboard (like a lightweight Plausible or Fathom).

Stack: Next.js + ClickHouse (time-series DB) + React

Metrics to track:
1. Pageviews, unique visitors, sessions
2. Traffic sources (direct, search, social, referral)
3. Top pages by views
4. Countries and cities
5. Devices (desktop/mobile/tablet), browsers, OS
6. Bounce rate, session duration
7. Goal conversions

Dashboard features:
- Date range picker (today, 7d, 30d, custom)
- Real-time visitors (WebSocket)
- Comparison to previous period
- Charts: line, bar, donut

Data collection: lightweight JS snippet (< 1KB, no cookies, GDPR-friendly)"""),
  ("crm-system.md","Build a CRM System",["crm","nextjs","fullstack","business"],"advanced","""Build a lightweight CRM for a small sales team.

Stack: Next.js + PostgreSQL + Prisma

Features:
1. **Contacts**: name, company, email, phone, custom fields, tags
2. **Companies**: associated contacts, deals
3. **Deals/Pipeline**: kanban view by stage (Lead → Qualified → Proposal → Won/Lost)
4. **Activities**: log calls, emails, meetings against a contact/deal
5. **Tasks**: follow-up reminders with due dates
6. **Notes**: rich text notes on any record
7. **Email integration**: log emails from Gmail/Outlook
8. **Reports**: win rate, pipeline value, activity by rep
9. **Import**: bulk import from CSV
10. **Team**: assign contacts/deals to sales reps

DB schema + complete API + key UI components."""),
  ("marketplace.md","Build a Two-Sided Marketplace",["marketplace","stripe-connect","fullstack","payments"],"advanced","""Build a two-sided marketplace (like Airbnb, Etsy, Fiverr).

Stack: Next.js + PostgreSQL + Stripe Connect

Core features:
1. **Sellers**: create listings, manage inventory, view orders, payouts
2. **Buyers**: browse, search, filter, buy, review
3. **Payments**: Stripe Connect (marketplace payments with platform fee)
4. **Escrow**: hold payment until buyer confirms delivery
5. **Reviews**: two-way reviews (buyer reviews seller and vice versa)
6. **Disputes**: flag orders, admin resolution
7. **Messaging**: buyer ↔ seller chat
8. **Categories and SEO**: each listing indexed by Google
9. **Search**: full-text + faceted filters
10. **Admin panel**: approve listings, manage disputes, see revenue

Stripe Connect onboarding flow is the most complex part — show fully."""),
  ("expense-tracker.md","Build a Personal Finance Tracker",["finance","fullstack","charts","react"],"intermediate","""Build a personal finance and expense tracker app.

Stack: Next.js + PostgreSQL + Plaid API

Features:
1. Manual transaction entry: amount, category, date, note
2. Bank account connection via Plaid (automatic import)
3. Category management: custom categories with budgets
4. Budget tracking: progress bars, overspend alerts
5. Monthly summary: income vs expenses, savings rate
6. Charts: spending by category (donut), trend over time (line)
7. Recurring transactions: detect and label subscriptions
8. Net worth tracker: assets vs liabilities
9. Export to CSV for taxes
10. Multi-currency support

Full implementation with Plaid integration or CSV import fallback."""),
  ("video-platform.md","Build a Video Streaming Platform",["video","streaming","fullstack","s3"],"advanced","""Build a YouTube-style video platform.

Stack: Next.js + Node.js + PostgreSQL + AWS S3 + CloudFront + FFmpeg

Features:
1. **Upload**: multipart upload to S3, show progress
2. **Processing**: FFmpeg transcoding (1080p, 720p, 480p HLS)
3. **Player**: HLS.js player with quality selector, playback speed, captions
4. **Thumbnails**: auto-generate at 25%, 50%, 75% + user-set custom thumbnail
5. **Metadata**: title, description, tags, category, visibility
6. **Engagement**: likes, comments, subscribe
7. **Recommendations**: related videos
8. **Search**: title + description full-text
9. **Analytics**: views, watch time, traffic sources (for creators)
10. **Monetization**: tip button or membership (Stripe)"""),
  ("recipe-platform.md","Build a Recipe Sharing Platform",["recipe","community","nextjs","fullstack"],"intermediate","""Build a recipe sharing platform (like AllRecipes).

Stack: Next.js + PostgreSQL + Cloudinary

Features:
1. Recipe: title, description, ingredients (with amounts), instructions (steps)
2. Media: multiple photos, optional video
3. Tags: cuisine, diet (vegan/gluten-free), meal type, difficulty
4. Servings scaling: user changes servings → amounts scale automatically
5. Save / bookmark recipes
6. Rating and reviews
7. User profiles with collection of recipes
8. Search: full-text + filter by dietary restrictions
9. Meal planner: drag recipes to weekly calendar
10. Shopping list: combine ingredients from planned meals (deduplicate)
11. AI ingredient substitutions (Claude API)"""),
  ("event-platform.md","Build an Event Management Platform",["events","ticketing","stripe","fullstack"],"advanced","""Build an Eventbrite-style event management platform.

Stack: Next.js + PostgreSQL + Stripe + SendGrid + MapBox

Features:
1. Create events: title, description, date/time, location (map), category
2. Ticket types: free, paid, donation; quantity limits; early bird pricing
3. Registration flow: select tickets → Stripe checkout → confirmation email
4. QR code tickets: generate per attendee, scan at door
5. Event dashboard: attendee list, revenue, check-in stats
6. Discovery: map view of nearby events, category browse
7. Calendar: add to Google/Apple Calendar
8. Virtual events: embed Zoom/Meet link (shown only to registered)
9. Recurring events
10. Waitlist: when sold out, notify on cancellations"""),
  ("code-snippet-manager.md","Build a Code Snippet Manager",["snippets","developer-tools","fullstack","search"],"intermediate","""Build a developer code snippet manager (like Carbon or Ray.so but with search and sharing).

Stack: Next.js + PostgreSQL + Prism.js (syntax highlighting)

Features:
1. Create snippets: title, description, code, language, tags
2. Syntax highlighting for 50+ languages
3. Collections / folders
4. Full-text search (content + title + tags)
5. Public snippets: shareable URL with beautiful code rendering
6. Private snippets: only visible to owner
7. Embed code: `<iframe>` embed for blogs/docs
8. VS Code extension: save snippet from editor, search from command palette
9. Copy to clipboard with one click
10. Import from GitHub Gist
11. AI: explain snippet, generate similar snippet (Claude API)"""),
  ("habit-tracker.md","Build a Habit Tracker App",["habits","react","fullstack","gamification"],"intermediate","""Build a habit tracking app with gamification.

Stack: React Native (Expo) or Next.js PWA + PostgreSQL

Features:
1. Create habits: name, icon, target frequency (daily/weekly/specific days)
2. Log completion: mark habit as done for today
3. Streak tracking: current streak and longest streak
4. Visualizations: GitHub-style contribution heatmap, weekly bar chart
5. Statistics: completion rate, best streak, total completions
6. Reminders: push notifications at set time
7. Gamification: XP, level up, badges for milestones
8. Categories: health, fitness, learning, creativity
9. Notes: add context when logging
10. Social: share progress (opt-in), follow friends' habits

Full DB schema + API + UI with beautiful animations."""),
  ("resume-builder.md","Build a Resume Builder",["resume","pdf","react","fullstack"],"intermediate","""Build an online resume builder that generates beautiful PDFs.

Stack: Next.js + PostgreSQL + react-pdf

Features:
1. Sections: contact, summary, experience, education, skills, projects, certifications
2. Multiple templates: modern, classic, minimal, creative
3. Live preview: see changes in real-time
4. Export: PDF + ATS-friendly plain text
5. AI enhancement: improve bullet points (Claude API)
6. ATS score: analyze against a job description
7. Shareable URL: public resume page
8. Version history: save multiple versions
9. Import from LinkedIn
10. Cover letter generator (AI)

React PDF renders the exact same layout in both preview and export."""),
  ("note-taking-app.md","Build a Note-Taking App",["notes","editor","react","fullstack"],"intermediate","""Build a Notion-lite note-taking app.

Stack: Next.js + PostgreSQL + Tiptap editor

Features:
1. Block-based editor: text, heading, bullet list, numbered list, code, image, divider
2. Slash command: / to insert blocks
3. Drag to reorder blocks
4. Nested pages (tree structure in sidebar)
5. Full-text search across all notes
6. Tags and favorites
7. Share note: public read-only URL
8. Real-time autosave (debounced, no manual save needed)
9. Markdown import/export
10. Dark mode

Optional: real-time collaboration with Yjs"""),
  ("newsletter-platform.md","Build a Newsletter Platform",["newsletter","email","fullstack","stripe"],"advanced","""Build a Substack-style newsletter platform.

Stack: Next.js + PostgreSQL + Resend + Stripe

Features:
1. Writer: create newsletter, publish posts (markdown editor)
2. Subscribers: free and paid tiers
3. Subscription management: Stripe for paid subscriptions
4. Send: trigger email delivery to all subscribers on publish
5. Archive: public archive of all posts
6. Subscribe widget: embeddable `<iframe>` for other websites
7. Unsubscribe: one-click, respect immediately
8. Analytics per post: opens, clicks, unsubscribes
9. Comments on posts
10. Writer dashboard: subscriber count, revenue, post performance

Email delivery must handle thousands of recipients (queue-based)."""),
  ("url-shortener.md","Build a URL Shortener Service",["url-shortener","redis","analytics","fullstack"],"intermediate","""Build a URL shortener with analytics (like Bit.ly).

Stack: Node.js + Redis + PostgreSQL + Next.js

Features:
1. Shorten any URL: generate 6-char base62 code
2. Custom aliases: user picks their own slug
3. QR code generation
4. Redirect: GET /:code → 301 redirect (cache in Redis, 1ms response)
5. Analytics per link: clicks, unique visitors, countries, referrers, devices
6. Click tracking: async (don't slow the redirect)
7. Link expiry: optional TTL
8. Password-protected links
9. API: programmatic shortening with API key
10. Dashboard: all links, stats, delete, edit

Performance target: redirect in < 5ms (Redis-first lookup)."""),
  ("appointment-booking.md","Build a Medical Appointment Booking System",["appointments","healthcare","fullstack","calendar"],"advanced","""Build a medical appointment booking system.

Stack: Next.js + PostgreSQL + Twilio (SMS) + Stripe

Roles: Admin, Doctor, Patient

Features:
1. Doctors: set weekly availability, blocked dates, appointment types
2. Patients: find doctor, view calendar, book appointment
3. Appointment types: consultation (30min), follow-up (15min), procedure (60min)
4. Confirmation: email + SMS to patient and doctor
5. Reminders: 24h and 2h before (SMS + email)
6. Telemedicine: virtual appointments with video link
7. Medical records: doctor adds notes after appointment (patient can view)
8. Insurance: collect insurance info at booking
9. Cancellation: with configurable advance notice requirement
10. Waitlist: patient joins if slot becomes available"""),
  ("crowdfunding-platform.md","Build a Crowdfunding Platform",["crowdfunding","stripe","fullstack","community"],"advanced","""Build a Kickstarter-style crowdfunding platform.

Stack: Next.js + PostgreSQL + Stripe + Cloudinary

Features:
1. Project creation: title, story (rich text), goal, deadline, rewards
2. Rewards: backer tiers with perks and quantity limits
3. Funding: pledge (Stripe Payment Intent, charged only if goal met)
4. Progress: funding bar, % funded, backers count, days left
5. Comments and updates from creator
6. Backer dashboard: all pledges, downloadable rewards
7. Creator dashboard: funding stats, backer export, send updates
8. Refund: auto-refund if goal not reached by deadline
9. Discovery: categories, trending, ending soon
10. Social: share buttons, embed widget

Stripe hold → capture on success / cancel on failure is the key flow."""),
  ("fitness-tracker.md","Build a Fitness Tracking App",["fitness","health","react-native","fullstack"],"intermediate","""Build a fitness tracking app.

Stack: React Native (Expo) + Node.js + PostgreSQL

Features:
1. Workout templates: create routines with exercises, sets, reps, weight
2. Workout logging: log today's workout, track personal bests
3. Exercise library: 200+ exercises with instructions and muscle groups
4. Progress charts: weight lifted over time, volume per muscle group
5. Body measurements: weight, body fat %, measurements log
6. Calendar: view past workouts, streaks
7. Rest timer: countdown between sets
8. HealthKit / Google Fit integration: import steps, heart rate
9. Share workout: generate image summary
10. AI coach: suggest next workout based on history (Claude API)"""),
  ("dating-app.md","Build a Matching/Dating App",["matching","swipe","fullstack","real-time"],"advanced","""Build a dating/matching app (Tinder-style).

Stack: React Native (Expo) + Node.js + PostgreSQL + Redis + Socket.io

Core features:
1. Profile: photos, bio, age, location, preferences
2. Discovery: swipe right (like), left (pass), super-like
3. Matching algorithm: only match if both swipe right
4. Chat: real-time messages with Socket.io
5. Photo upload: multiple photos, drag to reorder
6. Geolocation: show profiles within X km
7. Filters: age range, distance, interests
8. Push notifications: new match, new message
9. Boost: increase visibility temporarily
10. Report/block: safety features

Privacy: hide last active time, control who sees your profile."""),
  ("podcast-platform.md","Build a Podcast Hosting Platform",["podcast","audio","streaming","fullstack"],"advanced","""Build a podcast hosting and discovery platform.

Stack: Next.js + Node.js + S3 + PostgreSQL

Features:
1. Upload episodes: MP3/M4A, title, description, show notes, episode number
2. RSS feed generation (valid podcast RSS with all required tags)
3. Web player: custom HTML5 audio player with chapters support
4. Auto-submit to Apple Podcasts, Spotify (show RSS URL)
5. Transcription: auto-transcribe with Whisper API
6. Show notes: rich text editor with timestamps
7. Analytics: downloads per episode, listener geography (private feed tokens)
8. Embeddable player widget
9. Subscription: email list of listeners
10. Monetization: supporter donations (Stripe)"""),
  ("real-estate-platform.md","Build a Real Estate Listing Platform",["real-estate","maps","search","fullstack"],"advanced","""Build a real estate listing platform (like Zillow).

Stack: Next.js + PostgreSQL + MapBox + Cloudinary

Features:
1. Listings: address, price, beds, baths, sqft, photos, description
2. Map view: cluster pins by area, click to see listing
3. List view: grid of cards with key details
4. Search: by address/city/zip, filter by price/beds/type
5. Saved searches: alert on new matching listings
6. Favorite properties
7. Property detail: full gallery, map, neighborhood stats, similar homes
8. Mortgage calculator
9. Request viewing: contact agent form
10. Agent profiles: their listings, contact info

SEO: each listing is a public page indexed by Google."""),
  ("task-automation.md","Build a No-Code Task Automation Platform",["automation","workflows","fullstack","no-code"],"advanced","""Build a simple Zapier-style automation platform.

Stack: Next.js + Node.js + BullMQ + PostgreSQL

Concepts:
- **Triggers**: events that start a workflow (webhook, schedule, form submission)
- **Actions**: things that happen (send email, HTTP request, DB insert, Slack message)
- **Workflows**: chain of trigger + multiple actions

Implement:
1. Workflow builder UI (visual flow editor)
2. Trigger types: Webhook, Schedule (cron), Manual
3. Action types: HTTP Request, Send Email, Slack Webhook, Database Insert
4. Data mapping: pass data between trigger and actions
5. Workflow runs history: success/failure/payload
6. Error handling: retry failed actions
7. Webhook URL generation per workflow"""),
  ("travel-planner.md","Build an AI Travel Planner",["travel","ai","fullstack","maps"],"intermediate","""Build an AI-powered travel itinerary planner.

Stack: Next.js + Claude API + PostgreSQL + MapBox

Features:
1. Input: destination, dates, number of travelers, budget, interests
2. AI generation: Claude generates day-by-day itinerary
3. Itinerary display: timeline view with activities, restaurants, hotels
4. Map integration: plot all locations on interactive map
5. Save itinerary to account
6. Edit: add/remove/reorder activities
7. Collaboration: share with travel companions (they can suggest edits)
8. Export: PDF itinerary + calendar events (.ics)
9. Packing list: AI-generated based on destination + activities
10. Budget breakdown: estimated costs per day

Claude prompt engineering: get structured JSON itinerary."""),
  ("document-editor.md","Build a Collaborative Document Editor",["editor","collaboration","yjs","fullstack"],"advanced","""Build a Google Docs-style collaborative document editor.

Stack: Next.js + Node.js + Yjs + y-websocket + Tiptap + PostgreSQL

Features:
1. Rich text editor: headings, bold/italic, lists, tables, images, code blocks
2. Real-time collaboration: multiple users edit simultaneously (CRDT-powered)
3. Cursor presence: see other users' cursors with name labels
4. Comments: highlight text → add comment → reply thread
5. Version history: restore to any past version
6. Share: private, view-only link, public
7. Export: PDF, Word (.docx), Markdown
8. Templates: start from pre-made document templates
9. Table of contents: auto-generated from headings
10. Word count, reading time stats"""),
  ("customer-support.md","Build a Customer Support Ticketing System",["support","helpdesk","fullstack","email"],"advanced","""Build a Zendesk-style customer support system.

Stack: Next.js + Node.js + PostgreSQL + SendGrid

Roles: Customer, Agent, Admin

Features:
1. Customers: submit ticket via web form or email
2. Email ingestion: support@company.com → creates ticket automatically
3. Ticket lifecycle: Open → In Progress → Resolved → Closed
4. Assignment: route to agent by category/round-robin
5. Internal notes: agents communicate privately
6. SLA: first response < 4h, resolution < 24h — track and alert
7. CSAT: post-resolution survey
8. Knowledge base: articles that auto-suggest when customer types ticket
9. AI first response: Claude drafts suggested reply for agent review
10. Reporting: ticket volume, response times, CSAT scores"""),
  ("subscription-box.md","Build a Subscription Box Business Platform",["subscription","ecommerce","stripe","fullstack"],"advanced","""Build a complete platform for a subscription box business.

Stack: Next.js + PostgreSQL + Stripe + Shippo

Features:
1. **Landing page**: product imagery, what's in the box, testimonials, subscribe CTA
2. **Subscribe flow**: choose plan (monthly/quarterly/annual), Stripe, shipping address
3. **Subscriber portal**: manage subscription, skip month, cancel, change address
4. **Box management**: admin creates box contents per cycle
5. **Fulfillment**: generate packing slips, create shipments via Shippo API
6. **Tracking**: send tracking emails, customers track in portal
7. **Referral program**: unique referral link, credit for successful referrals
8. **Churn prevention**: cancel flow with pause option + discount offer
9. **Analytics**: MRR, churn rate, active subscribers
10. **Inventory**: track stock per item, alert when low"""),
  ("iot-dashboard.md","Build an IoT Data Dashboard",["iot","mqtt","websockets","fullstack"],"advanced","""Build an IoT data collection and visualization dashboard.

Stack: Node.js + MQTT + InfluxDB (time-series) + React + WebSocket

Architecture:
1. **MQTT broker**: receive telemetry from IoT devices
2. **Ingestion service**: subscribe to MQTT, validate, write to InfluxDB
3. **REST API**: query historical data, manage devices
4. **WebSocket**: push live sensor data to dashboard
5. **Dashboard**: real-time gauges, time-series charts, device map
6. **Alerting**: threshold alerts (temperature > 80°C → notify)
7. **Device management**: register devices, see status, last seen
8. **Data retention**: auto-delete data older than 90 days

Example devices: temperature sensors, energy monitors, GPS trackers."""),
  ("quiz-platform.md","Build an Online Quiz Platform",["quiz","education","fullstack","gamification"],"intermediate","""Build an online quiz and assessment platform.

Stack: Next.js + PostgreSQL + Socket.io

Features:
1. Question types: multiple choice, true/false, short answer, code challenge
2. Quiz builder: add questions, set time limit, configure scoring
3. Taking a quiz: countdown timer, progress indicator
4. Live quiz mode: host shares code → participants join → play in real-time
5. Leaderboard: live standings during quiz
6. Results: score, correct answers, explanations
7. Analytics: per-question performance, average score
8. Import questions from CSV
9. Public quiz library: share your quizzes
10. Certificates on completion (PDF)
11. AI question generator: paste topic → generate 10 questions (Claude API)"""),
  ("inventory-pos.md","Build a Point of Sale System",["pos","retail","stripe","fullstack"],"advanced","""Build a Point of Sale (POS) system for a retail store.

Stack: React + Node.js + PostgreSQL + Stripe Terminal

Features:
1. Product lookup: barcode scan or search by name
2. Cart: add items, quantity, discounts, remove
3. Payment: card via Stripe Terminal, cash, split payment
4. Receipt: print (ESC/POS) or email
5. Refunds: partial or full, back to payment method
6. Customer: create/find customer account, loyalty points
7. End-of-day report: sales summary, by payment method
8. Inventory sync: sales auto-decrement stock
9. Offline mode: queue sales when internet drops, sync when reconnected
10. Multi-register: multiple terminals in same store"""),
  ("review-platform.md","Build a Review and Rating Platform",["reviews","ratings","fullstack","community"],"intermediate","""Build a product/business review platform (like Trustpilot or G2).

Stack: Next.js + PostgreSQL + Algolia (search)

Features:
1. Businesses claim their profile
2. Customers write reviews: rating (1-5 stars), text, pros/cons, verified purchase badge
3. Business response to reviews
4. Helpful votes on reviews
5. Fake review detection: velocity checks, account age requirements
6. Review widgets: embeddable badge for business websites
7. Search: find businesses by name or category
8. Compare: side-by-side comparison of 2-3 businesses
9. Featured reviews: AI summary of sentiment (Claude API)
10. Report inappropriate reviews"""),
  ("saas-admin-panel.md","Build a SaaS Admin Panel",["admin","saas","fullstack","dashboard"],"intermediate","""Build a complete admin panel for a SaaS application.

Stack: React + Node.js + PostgreSQL

Sections:
1. **Dashboard**: total users, MRR, churn, signups this month, active now
2. **Users**: search, filter by plan, view profile, impersonate, ban, delete
3. **Subscriptions**: all subs, by plan, revenue per plan, churned subs
4. **Feature flags**: enable/disable features per user or globally
5. **Announcements**: send in-app banner to all users
6. **Email campaigns**: send one-off email to user segments
7. **Audit log**: all admin actions logged
8. **Database explorer**: safe read-only SQL queries
9. **API keys**: view all API keys, revoke
10. **System health**: uptime, queue depth, error rate

Secure: admin-only routes with 2FA requirement."""),
  ("waitlist-system.md","Build a Pre-Launch Waitlist System",["waitlist","viral","marketing","fullstack"],"intermediate","""Build a viral pre-launch waitlist system.

Stack: Next.js + PostgreSQL + Resend

Features:
1. Landing page with email capture
2. Thank you page: shows referral link immediately
3. Referral tracking: get N spots higher for each referral
4. Leaderboard: top referrers (public)
5. Email confirmation with referral link
6. Progress email: "You've moved up X spots!"
7. Social share buttons: Twitter, WhatsApp, copy link
8. Admin: view all signups, approve in batches
9. Launch email: notify approved users
10. Analytics: conversion rate, referral source, viral coefficient

Make the referral mechanic feel gamified and exciting."""),
]

for filename, title, tags, difficulty, prompt_text in fullstack:
    write(cat / filename, make_prompt("fullstack-projects", title, tags, difficulty, prompt_text))

print(f"\n✅ Categories 03 and 04 complete!")
