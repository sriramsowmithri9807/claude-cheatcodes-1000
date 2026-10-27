# 10-architecture-system-design

System design: scaling, microservices, event-driven, caching, replication, classic design interviews.

33 prompts. Search `## ` headings or ids; see index.md for the one-line list.

## Design API Composition Layer

**id:** `10-architecture-system-design/api-composition` · **Difficulty:** advanced · **Tags:** api, composition, bff, graphql

**Placeholders:** [LIST YOUR MICROSERVICES AND WHAT THEY PROVIDE], [WEB APP, MOBILE APP, PARTNER API]

````text
Design an API composition layer for my distributed system.

Downstream services: [LIST YOUR MICROSERVICES AND WHAT THEY PROVIDE]
Clients: [WEB APP, MOBILE APP, PARTNER API]

Composition strategies:
1. **BFF (Backend for Frontend)**: dedicated API per client type
2. **GraphQL**: unified graph over multiple services
3. **API Gateway + aggregation**: gateway composes multiple upstream calls

For my system:
4. Which composition strategy (or hybrid)?
5. How to aggregate data from Service A + Service B into one response
6. How to handle failures (partial response when one service fails)
7. Distributed transactions across services
8. Auth token propagation
9. Response caching at composition layer
10. Observability: trace composition calls end-to-end
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design API Before Implementation

**id:** `10-architecture-system-design/api-design-first` · **Difficulty:** intermediate · **Tags:** api-first, openapi, design, planning

**Placeholders:** [DESCRIBE FEATURE], [FRONTEND / MOBILE / THIRD-PARTY]

````text
Design my API before writing any implementation code.

Feature to design: [DESCRIBE FEATURE]
Consumers: [FRONTEND / MOBILE / THIRD-PARTY]

Step 1: Resource modeling
- What are the main resources?
- What are the relationships?
- What operations are needed per resource?

Step 2: OpenAPI spec
- Write the complete spec in OpenAPI 3.1
- Include request/response schemas
- Include error responses
- Include auth requirements

Step 3: Review questions
- Is this API easy to use?
- Does it follow REST conventions?
- Is it consistent with existing API?
- What might change in v2?

Output: complete OpenAPI 3.1 YAML + design decisions document.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design an API-First Architecture

**id:** `10-architecture-system-design/api-first-design` · **Difficulty:** advanced · **Tags:** api-first, architecture, design, openapi

**Placeholders:** [DESCRIBE]

````text
Design an API-first architecture for my product.

Product: [DESCRIBE]
Consumers: [Web app, Mobile, Third-party developers]

API-first means:
- API spec is written BEFORE implementation
- Frontend and backend develop in parallel against the mock
- API is the product — consumers are first-class citizens

Process:
1. **Domain modeling**: identify resources from business domain
2. **OpenAPI spec**: write complete spec before writing code
3. **Mock server**: generate mock from spec (Prism)
4. **Contract testing**: consumer tests run against spec
5. **Code generation**: generate server stubs from spec
6. **Developer portal**: documentation from spec
7. **SDK generation**: client SDKs from spec
8. **Versioning**: embed versioning strategy in the spec from day 1

Output: starter OpenAPI spec for my domain.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design a Multi-Layer Cache Architecture

**id:** `10-architecture-system-design/cache-architecture` · **Difficulty:** advanced · **Tags:** caching, architecture, redis, cdn

**Placeholders:** [LATENCY TARGET, AVAILABILITY TARGET], [READ-HEAVY / WRITE-HEAVY / MIXED]

````text
Design a multi-layer cache architecture for my application.

Application type: [READ-HEAVY / WRITE-HEAVY / MIXED]
SLA: [LATENCY TARGET, AVAILABILITY TARGET]

Cache layers:
1. **Browser cache**: Cache-Control headers, service worker
2. **CDN**: Cloudflare/CloudFront for static and semi-static
3. **API gateway**: cache common API responses at gateway
4. **Application L1**: in-process memory cache (LRU, small, fast)
5. **Application L2**: Redis (larger, shared across instances)
6. **Query cache**: database query result cache
7. **DB buffer**: PostgreSQL shared_buffers

Design decisions:
8. Cache-aside vs write-through vs write-behind per layer
9. TTL strategy per data type
10. Cache invalidation: event-driven vs TTL-based
11. Cache warming on deploy
12. Consistency: eventual vs strong for each layer

Draw the cache hierarchy with hit rates.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design Comprehensive Caching Strategy

**id:** `10-architecture-system-design/caching-strategy` · **Difficulty:** advanced · **Tags:** caching, strategy, architecture, redis

**Placeholders:** [CACHING DECISION], [DESCRIBE: slow queries, high DB load, expensive computations], [DESCRIBE], [YOUR DATA TYPE 1], [YOUR DATA TYPE 2], [YOUR DATA TYPE 3]

````text
Design a comprehensive caching strategy for my application.

Application: [DESCRIBE]
Problem: [DESCRIBE: slow queries, high DB load, expensive computations]

For each type of data, define:
1. **Cache location**: browser / CDN / Redis / in-memory
2. **Cache key**: what uniquely identifies this cached item
3. **TTL**: how long before it expires
4. **Invalidation trigger**: what event makes this cache stale
5. **Cache miss behavior**: compute it, return stale, return default
6. **Consistency requirements**: eventual or strong

Specific data types in my app:
- [YOUR DATA TYPE 1]: [CACHING DECISION]
- [YOUR DATA TYPE 2]: [CACHING DECISION]
- [YOUR DATA TYPE 3]: [CACHING DECISION]

Cache warming: how to pre-populate on deploy.
Monitoring: hit rate, eviction rate, memory usage.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design CDN and Edge Architecture

**id:** `10-architecture-system-design/cdn-architecture` · **Difficulty:** advanced · **Tags:** cdn, edge, cloudflare, architecture

**Placeholders:** [DESCRIBE: global users, content types, real-time requirements]

````text
Design a CDN and edge architecture for my application.

Application: [DESCRIBE: global users, content types, real-time requirements]

1. **Static asset delivery**: JS, CSS, images at edge (long TTL)
2. **Dynamic content caching**: API responses at edge (short TTL or bypass)
3. **Edge compute**: Cloudflare Workers or Lambda@Edge for logic
4. **Geo-routing**: serve from nearest POP
5. **Cache keys**: vary by: URL, cookie segment, accept-language
6. **Purging**: instant cache invalidation on content update
7. **Origin shielding**: protect origin from traffic spikes
8. **WAF**: block malicious traffic at edge
9. **DDoS protection**: absorb attacks at edge
10. **Analytics**: real user monitoring at edge

Cost optimization: what NOT to cache at CDN (saves money).
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement Clean Architecture

**id:** `10-architecture-system-design/clean-architecture` · **Difficulty:** advanced · **Tags:** clean-architecture, solid, architecture, layers

**Placeholders:** [DESCRIBE]

````text
Implement Clean Architecture for my application.

Application type: [DESCRIBE]

Layers (inner → outer, dependencies point inward):

1. **Entities**: business objects, no framework deps
2. **Use Cases**: application-specific business rules
3. **Interface Adapters**: controllers, presenters, gateways
4. **Frameworks & Drivers**: web, DB, UI

Implement:
- Folder structure with layer separation
- Dependency rule: nothing in inner circle knows about outer
- Dependency injection at the edges
- Repository pattern for data access
- Use case per feature
- Controller → Use Case → Entity → Repository

Example: implement user registration end-to-end
- Entity: User with validation
- Use Case: RegisterUser
- Repository interface + PostgreSQL implementation
- HTTP Controller
- Dependency injection wiring
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design CQRS and Event Sourcing Architecture

**id:** `10-architecture-system-design/cqrs-event-sourcing-design` · **Difficulty:** advanced · **Tags:** cqrs, event-sourcing, ddd, architecture

**Placeholders:** [DESCRIBE], [YOUR DOMAIN]

````text
Design a CQRS/Event Sourcing architecture for: [YOUR DOMAIN].

Why CQRS/ES fits this problem: [DESCRIBE]

Design:
1. **Commands**: operations that change state
   - Define all commands with their payloads
   - Validation rules per command
   - Command handlers
2. **Events**: facts that happened
   - Define all domain events (past tense)
   - Event schema + versioning strategy
   - Event store: append-only table design
3. **Aggregates**: enforce business invariants
   - Reconstruct from events
   - Snapshot strategy
4. **Read models / Projections**: optimized for query
   - Which projections do you need?
   - How to build and rebuild them
5. **Sagas / Process managers**: multi-aggregate workflows
6. **Technology stack**: EventStoreDB / PostgreSQL / Kafka

Fulldomain model with examples.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design Data Flow Architecture

**id:** `10-architecture-system-design/data-flow-architecture` · **Difficulty:** advanced · **Tags:** data-flow, pipelines, architecture, etl

**Placeholders:** [LIST: user actions, external APIs, IoT devices, etc.]

````text
Design the data flow architecture for my system.

Data sources: [LIST: user actions, external APIs, IoT devices, etc.]
Destinations: [OLTP database, analytics, ML training, CDN, search index]

Design:
1. **Ingestion**: how data enters the system (REST API, webhooks, batch upload, streaming)
2. **Validation**: schema check, business rules, deduplication
3. **Transformation**: normalize, enrich, join with reference data
4. **Storage routing**: which data goes where
5. **Stream processing**: real-time with Kafka Streams or Flink
6. **Batch processing**: nightly with Airflow or dbt
7. **CDC**: Change Data Capture (Debezium) for DB replication
8. **Backfilling**: re-process historical data
9. **Lineage**: track where each piece of data came from
10. **Monitoring**: data quality, freshness, volume anomalies

Diagram the full data flow.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design a Privacy-First Architecture

**id:** `10-architecture-system-design/data-privacy-architecture` · **Difficulty:** advanced · **Tags:** privacy, gdpr, architecture, security

**Placeholders:** [DESCRIBE YOUR APP AND DATA], [N]

````text
Design a privacy-first architecture compliant with GDPR and CCPA.

Application: [DESCRIBE YOUR APP AND DATA]

1. **Data inventory**: catalog all personal data collected
2. **Data minimization**: collect only what's needed
3. **Consent management**: granular consent, stored and auditable
4. **Data access layer**: all PII access goes through one service (log it)
5. **Encryption**: PII encrypted at rest (column-level with key rotation)
6. **Anonymization**: aggregate reporting uses anonymized data
7. **Right to erasure**: delete user → cascade delete all personal data
8. **Right to access**: export all user data as JSON/CSV
9. **Data retention**: auto-delete data after [N] months
10. **Breach detection**: alert on unusual bulk data access
11. **Third parties**: data sharing agreements, limited to necessary
12. **DPO tools**: privacy impact assessment, audit logs

Output: architecture diagram + data flow with privacy controls.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design Database Architecture for Scale

**id:** `10-architecture-system-design/database-architecture` · **Difficulty:** advanced · **Tags:** database, architecture, postgresql, scalability

**Placeholders:** [DESCRIBE CURRENT SETUP], [SCALE TARGET], [SIZE, GROWTH RATE, READ/WRITE RATIO]

````text
Design a database architecture that can scale to [SCALE TARGET].

Current: [DESCRIBE CURRENT SETUP]
Data characteristics: [SIZE, GROWTH RATE, READ/WRITE RATIO]

Architecture layers:
1. **Write path**: primary PostgreSQL with auto-failover (Patroni)
2. **Read path**: read replicas with connection routing
3. **Caching layer**: Redis for hot data (> 99% cache hit target)
4. **Search**: Elasticsearch for full-text
5. **Analytics**: ClickHouse or Redshift for OLAP
6. **Time-series**: TimescaleDB for metrics
7. **Queueing**: PostgreSQL as queue (SKIP LOCKED) vs Redis vs Kafka
8. **Archive**: move old data to S3 (Parquet format)

Draw the data flow for the 5 most common operations in my system.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Apply Domain-Driven Design

**id:** `10-architecture-system-design/ddd-design` · **Difficulty:** advanced · **Tags:** ddd, architecture, domain, patterns

**Placeholders:** [DESCRIBE YOUR BUSINESS DOMAIN]

````text
Apply Domain-Driven Design (DDD) to my project.

Business domain: [DESCRIBE YOUR BUSINESS DOMAIN]

1. **Ubiquitous language**: define key terms that business and tech agree on
2. **Domain model**: identify entities, value objects, aggregates
3. **Bounded contexts**: where does one model's language apply?
4. **Context map**: how bounded contexts relate (shared kernel, anti-corruption layer, etc.)
5. **Aggregate boundaries**: what belongs together? What consistency boundary?
6. **Domain services**: logic that doesn't fit in an entity
7. **Repositories**: abstract storage, return aggregates
8. **Domain events**: things that happen in the domain
9. **Application layer**: orchestrates domain objects
10. **Infrastructure layer**: implements repository interfaces

Diagram the context map and one fully designed aggregate.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Apply Gang of Four Design Patterns

**id:** `10-architecture-system-design/design-patterns` · **Difficulty:** advanced · **Tags:** design-patterns, gof, architecture, oop

**Placeholders:** [DESCRIBE WHAT'S AWKWARD OR HARD TO EXTEND], [DESCRIBE]

````text
Apply relevant design patterns to my codebase.

Code/System: [DESCRIBE]
Problems to solve: [DESCRIBE WHAT'S AWKWARD OR HARD TO EXTEND]

Suggest and implement the right patterns:

**Creational**: Factory, Abstract Factory, Builder, Singleton, Prototype
**Structural**: Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy
**Behavioral**: Chain of Responsibility, Command, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor

For each suggested pattern:
1. Which pattern to use here
2. Why it solves the problem
3. TypeScript/Python implementation
4. Before and after code comparison
5. When NOT to use this pattern (overengineering warning)
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design Distributed Tracing System

**id:** `10-architecture-system-design/distributed-tracing` · **Difficulty:** advanced · **Tags:** tracing, opentelemetry, observability, architecture

**Placeholders:** [LIST YOUR SERVICES], [NODE.JS / PYTHON / GO]

````text
Design a distributed tracing system for my microservices.

Services: [LIST YOUR SERVICES]
Languages: [NODE.JS / PYTHON / GO]

Design:
1. **Trace propagation**: W3C TraceContext headers across all services
2. **Instrumentation strategy**:
   - Auto-instrumentation: HTTP, DB, Redis, message queues
   - Manual spans: business-critical operations
3. **Sampling**: 100% dev, 10% prod, 100% for errors
4. **Span attributes**: tenant_id, user_id, feature_flag versions
5. **Context propagation**: through queues (special headers)
6. **Backend**: Jaeger (self-hosted) or Tempo (Grafana) or DataDog
7. **Correlation**: link trace_id to log lines and metrics
8. **SLO tracking**: trace-based SLI calculation
9. **Alerting**: trace-based anomaly detection
10. **Cost**: sampling to manage backend storage cost

OpenTelemetry SDK setup for Node.js.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design an Event-Driven Architecture

**id:** `10-architecture-system-design/event-driven-architecture` · **Difficulty:** advanced · **Tags:** event-driven, kafka, architecture, messaging

**Placeholders:** [DESCRIBE YOUR CURRENT/DESIRED SYSTEM], [DESCRIBE: tight coupling, synchronous chains, real-time features]

````text
Design an event-driven architecture for my system.

System: [DESCRIBE YOUR CURRENT/DESIRED SYSTEM]
Problems to solve: [DESCRIBE: tight coupling, synchronous chains, real-time features]

1. **Event catalog**: all domain events with schemas
2. **Message broker**: Kafka vs RabbitMQ vs SQS — which and why
3. **Producer**: how services publish events
4. **Consumer**: how services subscribe and process
5. **Consumer groups**: parallel processing, partition assignment
6. **At-least-once delivery**: handle duplicate messages
7. **Dead letter queue**: failed messages, retry policy
8. **Schema registry**: versioned Avro/Protobuf schemas
9. **Saga pattern**: distributed transactions via events
10. **Observability**: distributed tracing across events
11. **Ordering**: when you need ordered processing
12. **Replay**: reprocess historical events

Diagram the event flow.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design Feature Flag System Architecture

**id:** `10-architecture-system-design/feature-flags-architecture` · **Difficulty:** advanced · **Tags:** feature-flags, architecture, gradual-rollout, experimentation

**Placeholders:** [N]

````text
Design a feature flag system for my engineering team.

Team size: [N], services: [N]

Requirements:
- Toggle features without deployment
- Gradual rollout (1% → 10% → 100%)
- User/segment targeting
- A/B testing experiments
- Kill switch for emergencies

Architecture:
1. **Flag store**: database schema for flags + rules
2. **Evaluation engine**: rules engine (user in segment? rollout %?)
3. **SDK**: client library (JavaScript + Python) with local caching
4. **Admin UI**: create/edit flags, set rollout %
5. **Streaming updates**: SSE/WebSocket to push flag changes
6. **Analytics**: track exposure and conversion per variant
7. **Audit log**: who changed what flag and when
8. **Emergency mode**: fast disable all flags if eval service fails

Build vs buy: LaunchDarkly vs Unleash vs custom.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement Hexagonal Architecture

**id:** `10-architecture-system-design/hexagonal-architecture` · **Difficulty:** advanced · **Tags:** hexagonal, ports-adapters, architecture, clean

**Placeholders:** [DESCRIBE]

````text
Implement Hexagonal Architecture (Ports and Adapters) for my application.

Application: [DESCRIBE]

Structure:
```
src/
  core/              # Pure domain logic, no framework deps
    domain/
      entities/
      value-objects/
      services/
    ports/
      in/              # Driving ports (use cases)
      out/             # Driven ports (interfaces)
  adapters/
    in/
      http/            # REST API controllers
      graphql/         # GraphQL resolvers
      cli/             # CLI commands
    out/
      persistence/     # Database implementations
      messaging/       # Event bus
      external-api/    # Third-party services
```

Implement:
1. A complete use case end-to-end
2. Dependency injection setup
3. Testing without infrastructure (mock ports)
4. Adding a new adapter without changing core
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design Load Balancing Architecture

**id:** `10-architecture-system-design/load-balancing-architecture` · **Difficulty:** advanced · **Tags:** load-balancing, architecture, nginx, aws

**Placeholders:** [DESCRIBE], [EXPECTED PEAK RPS]

````text
Design a comprehensive load balancing architecture.

Application: [DESCRIBE]
Scale: [EXPECTED PEAK RPS]

Layers:
1. **DNS level**: Route 53 weighted routing / GeoDNS
2. **Global CDN**: CloudFront / Cloudflare (static assets + API caching)
3. **Layer 4 (TCP)**: AWS NLB for raw TCP throughput
4. **Layer 7 (HTTP)**: AWS ALB or Nginx (path routing, SSL termination)
5. **Application cluster**: stateless app servers (scale horizontally)
6. **Service mesh**: Istio for service-to-service load balancing
7. **Database**: PgBouncer + read replica routing
8. **Cache**: Redis Cluster for distributed caching

Health check strategy at each layer.
Failover behavior at each layer.
Draw the full request path.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design a Logging Architecture

**id:** `10-architecture-system-design/logging-architecture` · **Difficulty:** advanced · **Tags:** logging, architecture, elk, loki

**Placeholders:** [COMPLIANCE REQUIREMENTS], [ESTIMATED GB/DAY], [LIST]

````text
Design a centralized logging architecture for my distributed system.

Services: [LIST]
Log volume: [ESTIMATED GB/DAY]
Retention: [COMPLIANCE REQUIREMENTS]

Design:
1. **Log format**: structured JSON with standard fields (timestamp, level, service, trace_id, user_id)
2. **Log levels**: define what goes in each level across all services
3. **Shipping**: Fluentd or Vector (pull logs from stdout → ship to backend)
4. **Backend option A (ELK)**:
   - Elasticsearch: store and index (expensive)
   - Kibana: search and visualize
5. **Backend option B (Loki + Grafana)**:
   - Label-based (not full-text indexed → cheaper)
   - LogQL for queries
6. **Retention tiers**: hot (7d fast) → warm (30d medium) → cold (1y S3)
7. **Search**: full-text search vs label filter
8. **Alerting**: pattern-based alerts on error spikes
9. **Cost**: estimate $/GB for each option
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design a Message Queue Architecture

**id:** `10-architecture-system-design/message-queue-design` · **Difficulty:** advanced · **Tags:** message-queue, kafka, rabbitmq, architecture

**Placeholders:** [DESCRIBE YOUR MESSAGE TYPES], [LIST SERVICES THAT CONSUME MESSAGES], [MESSAGES PER SECOND]

````text
Design a message queue architecture for my distributed system.

Messages/events to handle: [DESCRIBE YOUR MESSAGE TYPES]
Volume: [MESSAGES PER SECOND]
Consumers: [LIST SERVICES THAT CONSUME MESSAGES]

Broker selection:
- RabbitMQ: complex routing, acknowledgment, smaller scale
- Kafka: high throughput, replay, stream processing
- SQS: AWS-native, simple, at-least-once
- Redis Streams: low latency, simple, no replay

For my use case: which broker?

Design:
1. Queue/topic structure and naming
2. Message schema (Avro/Protobuf/JSON)
3. Routing rules
4. Consumer group setup
5. Error handling: DLQ, retry policy
6. Ordering guarantees (where needed)
7. Scalability: partition count, consumer instances
8. Monitoring: queue depth, consumer lag
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Choose Between Microservices and Monolith

**id:** `10-architecture-system-design/microservices-vs-monolith` · **Difficulty:** advanced · **Tags:** microservices, monolith, architecture, decision

**Placeholders:** [DESCRIBE YOUR PROJECT], [LAUNCH DATE], [USERS, RPS]

````text
Help me decide between microservices and a monolith for my project.

Project: [DESCRIBE YOUR PROJECT]
Team size: [N engineers]
Timeline: [LAUNCH DATE]
Expected scale: [USERS, RPS]

Monolith advantages:
- Faster to build and deploy
- Easier to debug and test
- Single codebase
- No distributed system complexity
- Right for small teams and early stage

Microservices advantages:
- Independent deployments
- Technology diversity
- Team autonomy
- Targeted scaling
- Right for large teams and complex domains

For MY project:
1. Which is the right starting point?
2. If monolith: how to structure it to split later ("modular monolith")
3. If microservices: which services and how to define boundaries (DDD)
4. Migration path: start monolith → extract services over time
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design Monorepo Architecture

**id:** `10-architecture-system-design/monorepo-architecture` · **Difficulty:** advanced · **Tags:** monorepo, turborepo, architecture, packages

**Placeholders:** [DESCRIBE WHAT TO SHARE], [LIST]

````text
Design a monorepo architecture for my project.

Apps to include: [LIST]
Shared code: [DESCRIBE WHAT TO SHARE]

Using: Turborepo + pnpm workspaces

```
apps/
  web/          Next.js frontend
  api/          Node.js backend
  mobile/       React Native
  admin/        Admin dashboard
packages/
  ui/           Shared React components
  types/        Shared TypeScript types
  utils/        Shared utilities
  config/
    eslint/
    tsconfig/
    tailwind/
```

Design decisions:
1. Package boundaries and ownership
2. Versioning: fixed (all same version) vs independent
3. Publishing: private registry or not
4. Build pipeline: turbo.json task dependencies
5. Change detection: which apps to rebuild on change
6. CI: affected packages only
7. Code sharing rules: what can depend on what
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design a Multi-Tenant SaaS Architecture

**id:** `10-architecture-system-design/multi-tenant-architecture` · **Difficulty:** advanced · **Tags:** multi-tenant, saas, architecture, isolation

**Placeholders:** [GDPR / HIPAA / SOC2], [SCALE: 10 / 100 / 10,000], [SMALL SMB / LARGE ENTERPRISE]

````text
Design the architecture for a multi-tenant SaaS platform.

Expected tenants: [SCALE: 10 / 100 / 10,000]
Compliance needs: [GDPR / HIPAA / SOC2]
Tenant size range: [SMALL SMB / LARGE ENTERPRISE]

Isolation model selection:
1. **Shared everything**: all tenants in one DB, filtered by tenant_id
2. **Schema per tenant**: own PostgreSQL schema
3. **Database per tenant**: ultimate isolation (enterprise)
4. **Hybrid**: small tenants shared, large tenants isolated

For my scale and compliance: which model?

Implement:
5. Tenant resolution (subdomain, header, path)
6. Data isolation (RLS policies or separate DBs)
7. Configuration per tenant (feature flags, limits)
8. Billing per tenant (usage-based pricing)
9. Data export per tenant (GDPR right to data)
10. Tenant onboarding automation
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design Observability Architecture

**id:** `10-architecture-system-design/observability-architecture` · **Difficulty:** advanced · **Tags:** observability, monitoring, architecture, telemetry

**Placeholders:** [DESCRIBE YOUR SERVICES AND INFRASTRUCTURE]

````text
Design a comprehensive observability architecture for my system.

System: [DESCRIBE YOUR SERVICES AND INFRASTRUCTURE]

Three pillars:

**Metrics** (Prometheus + Grafana):
1. Infrastructure: CPU, memory, disk, network
2. Application: request rate, error rate, latency
3. Business: signups, revenue, active users
4. SLIs and SLOs: define and track service levels

**Logs** (Loki or ELK):
5. Structured JSON logging from all services
6. Correlation IDs linking related log entries
7. Log-based alerting for error patterns

**Traces** (Tempo or Jaeger):
8. End-to-end request tracing
9. Service dependency map
10. Latency breakdown per component

Platform: Grafana LGTM stack (all open source)
Alerts: define on-call playbook for each alert
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement Resilience Patterns

**id:** `10-architecture-system-design/resilience-patterns` · **Difficulty:** advanced · **Tags:** resilience, circuit-breaker, retry, architecture

**Placeholders:** [LIST EXTERNAL DEPENDENCIES]

````text
Implement resilience patterns to make my services fault-tolerant.

Services that can fail: [LIST EXTERNAL DEPENDENCIES]

1. **Circuit Breaker**: open circuit when error rate > 50% for 60s
   - States: Closed → Open → Half-Open
   - Node.js: opossum library
2. **Retry with backoff**: retry transient failures
   - Exponential backoff: 1s, 2s, 4s, 8s
   - Jitter: add random ±20% to prevent thundering herd
   - Don't retry: 4xx responses (except 429)
3. **Bulkhead**: isolate failures (separate thread pools / queues)
4. **Timeout**: fail fast, don't wait indefinitely
5. **Fallback**: return cached data when primary fails
6. **Health check**: monitor dependency health
7. **Chaos engineering**: randomly fail dependencies in staging

Implement all patterns in Node.js with Axios and opossum.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Apply Scalability Patterns

**id:** `10-architecture-system-design/scalability-patterns` · **Difficulty:** advanced · **Tags:** scalability, patterns, architecture, high-availability

**Placeholders:** [DESCRIBE]

````text
Apply scalability patterns to my application architecture.

Current architecture: [DESCRIBE]
Scale target: [e.g., 10M users, 100K RPS, 1PB data]

Horizontal scaling patterns:
1. **Load balancing**: distribute across multiple instances
2. **Stateless services**: sessions in Redis, not server memory
3. **Read replicas**: distribute read queries
4. **Database sharding**: partition data
5. **Caching**: L1 (process), L2 (Redis), L3 (CDN)

Vertical scaling patterns:
6. **Connection pooling**: handle more connections
7. **Async processing**: queue slow work
8. **CDN**: offload static content
9. **Microservices**: scale hot components independently
10. **Data tiering**: hot data in Redis, warm in RDS, cold in S3

For my system: which to apply first (biggest impact for least work).
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design a Security Architecture

**id:** `10-architecture-system-design/security-architecture` · **Difficulty:** advanced · **Tags:** security, architecture, zero-trust, defense-in-depth

**Placeholders:** [DESCRIBE], [PUBLIC / SENSITIVE / HIGHLY CONFIDENTIAL]

````text
Design a comprehensive security architecture for my application.

Application type: [DESCRIBE]
Data sensitivity: [PUBLIC / SENSITIVE / HIGHLY CONFIDENTIAL]

Defense in depth layers:
1. **Network**: VPC, private subnets, security groups, WAF
2. **Edge**: Cloudflare WAF, DDoS protection, bot detection
3. **Authentication**: MFA, SSO, session management
4. **Authorization**: RBAC + ABAC, least privilege
5. **Application**: OWASP Top 10 mitigations, input validation
6. **Data**: encryption at rest, in transit, key management
7. **Secrets**: Vault or AWS Secrets Manager, rotation
8. **Audit logging**: immutable audit trail for sensitive operations
9. **Vulnerability management**: dependency scanning, SAST, DAST
10. **Incident response**: detection, containment, recovery playbook
11. **Compliance**: SOC2, ISO 27001, GDPR controls mapping

Threat model: identify top 5 threats and how each is mitigated.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design a Serverless Architecture

**id:** `10-architecture-system-design/serverless-architecture-design` · **Difficulty:** advanced · **Tags:** serverless, aws, lambda, architecture

**Placeholders:** [DESCRIBE]

````text
Design a complete serverless architecture for my application.

Application: [DESCRIBE]

AWS Serverless components:
1. **Lambda**: one function per API endpoint (thin handlers)
2. **API Gateway**: HTTP API (cheaper, faster than REST API)
3. **DynamoDB**: single-table design for data storage
4. **S3**: file storage + static website hosting
5. **SQS**: async processing queue
6. **EventBridge**: event bus, cron jobs
7. **Cognito**: user auth (or Auth0)
8. **CloudFront**: CDN in front of everything
9. **Secrets Manager**: environment secrets
10. **CDK**: infrastructure as code

Design decisions:
- When to use Lambda vs container (ECS Fargate)
- DynamoDB access patterns and key design
- Cold start mitigation strategy
- Local development setup (SAM CLI)

Draw complete architecture diagram.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design a Real-Time Streaming Architecture

**id:** `10-architecture-system-design/streaming-architecture` · **Difficulty:** advanced · **Tags:** streaming, kafka, flink, architecture

**Placeholders:** [DESCRIBE: live dashboard, fraud detection, IoT, recommendation], [DESCRIBE]

````text
Design a real-time data streaming architecture.

Data types and volume: [DESCRIBE]
Latency requirement: [e.g., < 1 second end-to-end]
Use case: [DESCRIBE: live dashboard, fraud detection, IoT, recommendation]

Architecture:
1. **Ingestion**: Kafka (partitioned by key for ordering + parallelism)
2. **Stream processing**: Kafka Streams or Apache Flink
   - Filtering, transformation, aggregation
   - Windowing: tumbling, sliding, session windows
   - State management (count, sum, average)
3. **Serving layer**: Redis for materialized views (sub-ms reads)
4. **Batch reconciliation**: nightly batch corrects any streaming errors
5. **Replay**: reprocess stream from beginning
6. **Schema evolution**: Avro + schema registry
7. **Exactly-once**: Kafka transactions for strong consistency

Latency budget: where does the time go in the pipeline?
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Solve System Design Interview Questions

**id:** `10-architecture-system-design/system-design-interview` · **Difficulty:** advanced · **Tags:** system-design, interviews, architecture, scalability

````text
Walk me through the system design for: [SYSTEM — e.g., design Twitter, design a URL shortener, design a rate limiter].

Approach this like a system design interview:

1. **Clarify requirements**:
   - Functional: what should the system do?
   - Non-functional: scale, latency, availability, consistency
   - Constraints: read-heavy or write-heavy? Geography? Budget?
2. **Capacity estimation**: users, storage, bandwidth, QPS
3. **High-level design**: draw the components and data flow
4. **API design**: key APIs the system exposes
5. **Data model**: schema for the main entities
6. **Deep dive**: one component in detail (the interesting part)
7. **Bottlenecks**: what breaks at scale? How to fix?
8. **Tradeoffs**: what did you sacrifice for what?

Drawn as ASCII architecture diagram.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design Zero-Downtime Architecture

**id:** `10-architecture-system-design/zero-downtime-architecture` · **Difficulty:** advanced · **Tags:** zero-downtime, high-availability, deployment, architecture

**Placeholders:** [DESCRIBE CURRENT DEPLOY PROCESS AND DOWNTIME]

````text
Design an architecture for zero-downtime deployments and operations.

Current situation: [DESCRIBE CURRENT DEPLOY PROCESS AND DOWNTIME]

Components:
1. **Load balancer health checks**: remove unhealthy instances immediately
2. **Rolling deployment**: update N instances at a time
3. **Blue/green deployment**: full parallel environment switch
4. **Canary deployment**: route 1% → 10% → 100% gradually
5. **Database migrations**: backward-compatible schema changes only
6. **Feature flags**: deploy code before enabling it
7. **Connection draining**: finish in-flight requests before shutdown
8. **Graceful shutdown**: SIGTERM → drain → exit
9. **Readiness probe**: don't send traffic until app is ready
10. **Rollback**: immediate automated rollback on error rate spike

Make every production deployment invisible to users.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design architecture for a [SYSTEM]

**id:** `10-architecture-system-design/design-architecture-for-a-system` · **Difficulty:** beginner/intermediate/advanced · **Tags:** millions, analytics, scaling, architecture, system-design, distributed, high, extreme, high-traffic, notification, video, web

**Variant group** (6 generated prompts collapsed). Pick one value per placeholder:
- `[SYSTEM]`: analytics ingestion pipeline | distributed URL shortener | high-traffic chat server | notification microservice cluster | video delivery CDN network | web crawler cluster
- `[SCALE_REQUIREMENT]`: extreme write-heavy traffic spikes | high partition tolerance requirements | millions of monthly active users

````text
Design a distributed system architecture for a [SYSTEM] to support [SCALE_REQUIREMENT]. Document the data flow, database choices, caching strategy, and failover design.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** design-architecture-for-a-analytics-ingestion-pipeline, design-architecture-for-a-distributed-url-shortener, design-architecture-for-a-high-traffic-chat-server, design-architecture-for-a-notification-microservice-cluster, design-architecture-for-a-video-delivery-cdn-network, design-architecture-for-a-web-crawler-cluster


## Scale a [SYSTEM] to handle [SCALE_REQUIREMENT]

**id:** `10-architecture-system-design/scale-a-system-to-handle-scale-requirement` · **Difficulty:** beginner/intermediate/advanced · **Tags:** analytics, high, scaling, architecture, system-design, low-latency, distributed, millions, high-traffic, extreme, notification, video, web

**Variant group** (13 generated prompts collapsed). Pick one value per placeholder:
- `[SYSTEM]`: analytics ingestion pipeline | distributed URL shortener | high-traffic chat server | notification microservice cluster | video delivery CDN network | web crawler cluster
- `[SCALE_REQUIREMENT]`: extreme write-heavy traffic spikes | high partition tolerance requirements | low-latency reads globally | millions of monthly active users
- `[INFRA_COMPONENT]`: DNS load balancing policies | Kafka queues integration | Redis caching clusters | multi-region master-slave replication

````text
Create a system design specification detailing how to scale a [SYSTEM] to support [SCALE_REQUIREMENT] with [INFRA_COMPONENT].
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** scale-a-analytics-ingestion-pipeline-to-handle-high-partition-tolerance-requirements, scale-a-analytics-ingestion-pipeline-to-handle-low-latency-reads-globally, scale-a-distributed-url-shortener-to-handle-high-partition-tolerance-requirements, scale-a-distributed-url-shortener-to-handle-millions-of-monthly-active-users, scale-a-high-traffic-chat-server-to-handle-high-partition-tolerance-requirements, scale-a-high-traffic-chat-server-to-handle-millions-of-monthly-active-users, scale-a-notification-microservice-cluster-to-handle-extreme-write-heavy-traffic-spikes, scale-a-notification-microservice-cluster-to-handle-low-latency-reads-globally, scale-a-notification-microservice-cluster-to-handle-millions-of-monthly-active-users, scale-a-video-delivery-cdn-network-to-handle-millions-of-monthly-active-users, scale-a-web-crawler-cluster-to-handle-extreme-write-heavy-traffic-spikes, scale-a-web-crawler-cluster-to-handle-low-latency-reads-globally, scale-a-web-crawler-cluster-to-handle-millions-of-monthly-active-users

