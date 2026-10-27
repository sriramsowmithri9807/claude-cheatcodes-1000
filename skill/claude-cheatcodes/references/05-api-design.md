# 05-api-design

REST/GraphQL/gRPC/webhook design, OpenAPI specs, versioning, pagination, rate limits, error formats.

45 prompts. Search `## ` headings or ids; see index.md for the one-line list.

## Design API Authentication Systems

**id:** `05-api-design/api-authentication` · **Difficulty:** advanced · **Tags:** auth, api, jwt, oauth

**Placeholders:** [DESCRIBE]

````text
Design the authentication system for my public API:

Consumers: [3rd-party developers / mobile apps / other services]
Security requirements: [DESCRIBE]

Design:
1. API Key authentication: generation, storage (hashed), rotation
2. JWT Bearer: access tokens, refresh, expiry
3. OAuth 2.0: authorization code + PKCE for third-party apps
4. HMAC request signing: for server-to-server (like AWS Signature)
5. Rate limiting per auth method (API keys get higher limits)
6. Scopes: define permission model for your API
7. Token revocation
8. Audit log: who accessed what and when

Output: auth spec document + implementation code for each method.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Maintain API Backwards Compatibility

**id:** `05-api-design/api-backwards-compatibility` · **Difficulty:** advanced · **Tags:** api, compatibility, versioning, design

**Placeholders:** [DESCRIBE]

````text
Define rules for maintaining backwards compatibility in my API.

Current consumers: [DESCRIBE]

Non-breaking changes (safe to ship):
1. Add new optional fields to responses
2. Add new optional request fields
3. Add new endpoints
4. Add new enum values (caution)
5. Increase rate limits

Breaking changes (require versioning or careful migration):
6. Remove/rename fields
7. Change field types
8. Change auth requirements
9. Change response codes
10. Make optional fields required

For each potential breaking change in my API:
- Is it actually breaking?
- If yes: expand-contract migration pattern
- Testing: contract tests to detect regressions

Output: compatibility policy + API change checklist.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design API Caching Strategy

**id:** `05-api-design/api-caching` · **Difficulty:** advanced · **Tags:** caching, api, http, etag

**Placeholders:** [LIST YOUR ENDPOINTS AND HOW OFTEN DATA CHANGES]

````text
Design a comprehensive caching strategy for my API.

Endpoints: [LIST YOUR ENDPOINTS AND HOW OFTEN DATA CHANGES]

HTTP caching:
1. `Cache-Control` headers for each endpoint type
2. `ETag` implementation (conditional GET, 304 responses)
3. `Last-Modified` header
4. `Vary` header for content negotiation
5. CDN caching: which endpoints to cache at edge
6. Cache invalidation on data change

Server-side caching:
7. Redis cache for expensive queries
8. Cache warming strategy
9. Cache aside vs write-through vs write-behind

Client-side:
10. React Query cache coordination with HTTP cache

Output: cache policy per endpoint type + implementation code.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Manage Your API Changelog

**id:** `05-api-design/api-changelog` · **Difficulty:** beginner · **Tags:** changelog, api, versioning, documentation

**Placeholders:** [DESCRIBE], [LIST CHANGES]

````text
Create and maintain a professional API changelog.

My API: [DESCRIBE]
Changes this release: [LIST CHANGES]

Changelog format:
```
## [2.4.0] - 2026-01-15
### Added
- `GET /users/{id}/activity` endpoint
### Changed  
- `created_at` field is now an ISO 8601 string (was Unix timestamp)
### Deprecated
- `GET /users/{id}/feed` (use `GET /feed?user_id={id}` instead, sunset: 2026-07-01)
### Removed
- `POST /auth/token` (was deprecated in 2.0.0)
### Fixed
- Pagination cursor now works correctly with filters applied
### Security
- Fixed IDOR vulnerability in document access control
```

Also: how to:
1. Automate changelog from conventional commits
2. Notify API consumers of changes
3. Maintain breaking change log separately
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Auto-Generate API Clients from OpenAPI

**id:** `05-api-design/api-client-generation` · **Difficulty:** intermediate · **Tags:** openapi, codegen, sdk, typescript

**Placeholders:** [PATH OR PASTE]

````text
Auto-generate typed API clients from my OpenAPI specification.

My OpenAPI spec: [PATH OR PASTE]
Target languages: TypeScript, Python, Kotlin (Android)

Using: openapi-generator-cli or openapi-typescript

1. TypeScript client: openapi-typescript + openapi-fetch
   - Zero-runtime-overhead types
   - Fetch-based, works everywhere
   - Tree-shakeable
2. Python client: openapi-generator
   - Pydantic models for responses
   - Async (httpx) version
3. React Query integration: tanstack-query-openapi
   - Auto-generated hooks per endpoint

Output: generator config + GitHub Actions to regenerate on spec change.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement API Contract Testing

**id:** `05-api-design/api-contract-testing` · **Difficulty:** advanced · **Tags:** contract-testing, pact, testing, api

**Placeholders:** [FRONTEND APP, MOBILE APP, THIRD-PARTY SERVICE], [YOUR API SERVICE]

````text
Implement consumer-driven contract testing for my API ecosystem.

Provider: [YOUR API SERVICE]
Consumers: [FRONTEND APP, MOBILE APP, THIRD-PARTY SERVICE]

Using: Pact (consumer-driven contract testing)

1. Consumer writes a contract: "I expect this request to return this response shape"
2. Contract published to Pact Broker
3. Provider verifies against the contract in CI
4. If contract breaks, CI fails — immediate feedback

Implement:
- Consumer contract test (JavaScript/TypeScript)
- Provider verification (Node.js)
- Pact Broker setup (Docker)
- CI integration (GitHub Actions)
- Versioning contracts with semantic versioning
- "Can I Deploy" check before production deploy
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Transform API Data Shapes

**id:** `05-api-design/api-data-transformation` · **Difficulty:** intermediate · **Tags:** transformation, api, typescript, mapping

**Placeholders:** [DESCRIBE DIFFERENCES], [DESCRIBE]

````text
Design a data transformation layer for my API.

Problem: my database models don't match what my API consumers need.

DB model: [DESCRIBE]
API response needed: [DESCRIBE DIFFERENCES]

Implement:
1. Serializer pattern: db_model → api_response
2. Deserializer: api_request → db_model
3. Field renaming: snake_case → camelCase
4. Field filtering: hide internal fields
5. Field addition: compute derived fields
6. Nested objects: embed related models
7. Type coercion: convert timestamps, enums, nulls
8. TypeScript types: end-to-end type safety
9. Versioned serializers: v1 and v2 output from same DB
10. Partial responses: honor `?fields=` param
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Deprecate API Endpoints Gracefully

**id:** `05-api-design/api-deprecation` · **Difficulty:** intermediate · **Tags:** api, deprecation, versioning, lifecycle

**Placeholders:** [LIST ENDPOINTS TO DEPRECATE AND THEIR REPLACEMENTS]

````text
Plan and execute graceful deprecation of these API endpoints:

[LIST ENDPOINTS TO DEPRECATE AND THEIR REPLACEMENTS]

Deprecation process:
1. Add `Deprecation` and `Sunset` headers (RFC 8594)
2. Update docs with deprecation notice + migration guide
3. Log usage of deprecated endpoints (to track migration progress)
4. Email API consumers who have called the endpoint recently
5. Show deprecation warning in developer dashboard
6. Hard cutoff date announcement (3-6 months notice)
7. Grace period extension process for consumers who need more time
8. Traffic monitoring: graph call volume trending to zero
9. Actual removal + 410 Gone response
10. Post-mortem: how many consumers were impacted
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## API Design Patterns Masterclass

**id:** `05-api-design/api-design-patterns` · **Difficulty:** advanced · **Tags:** api, patterns, design, best-practices

**Placeholders:** [DESCRIBE YOUR API]

````text
Apply these API design patterns to my API: [DESCRIBE YOUR API].

1. **Resource Singleton**: `/me` instead of `/users/{id}` for current user
2. **Sub-resources**: `/posts/{id}/comments` for owned resources
3. **Custom methods**: `/orders/{id}:cancel` (Google API style) for actions
4. **Long-running operations**: return operation ID → poll for status
5. **Batch operations**: `POST /batch` to reduce round trips
6. **Partial updates**: PATCH with RFC 7396 JSON Merge Patch
7. **Field selection**: `?fields=id,name,email` to reduce payload
8. **Sorting**: `?sort=-createdAt,+name`
9. **Includes/expansion**: `?include=author,comments` to embed related
10. **Search endpoint**: POST /search with complex query body

For each: when to use + implementation.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Conduct an API Design Review

**id:** `05-api-design/api-design-review` · **Difficulty:** intermediate · **Tags:** api, design-review, best-practices, team

**Placeholders:** [PASTE YOUR PROPOSED API DESIGN]

````text
Conduct a thorough API design review for this proposed API:

[PASTE YOUR PROPOSED API DESIGN]

Review checklist:
□ Resource naming follows conventions
□ HTTP methods are semantically correct
□ Status codes are appropriate
□ Error responses are consistent
□ Pagination is implemented correctly
□ Auth is secure and consistent
□ Rate limiting is planned
□ Versioning strategy is defined
□ Breaking changes are identified
□ Documentation is planned
□ Security: no sensitive data in URLs
□ CORS is properly configured
□ Backwards compatibility is maintained
□ Performance: no N+1 in response shapes
□ Idempotency on critical operations

For each failing item: why it fails and how to fix it.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design Developer Documentation

**id:** `05-api-design/api-documentation-design` · **Difficulty:** intermediate · **Tags:** docs, api, developer-experience, dx

**Placeholders:** [DESCRIBE], [SKILL LEVEL AND BACKGROUND]

````text
Design world-class developer documentation for my API.

API: [DESCRIBE]
Target developers: [SKILL LEVEL AND BACKGROUND]

Documentation structure:
1. **Getting Started**: auth → first API call → see result (< 5 minutes)
2. **Guides**: common use cases as step-by-step tutorials
3. **Reference**: every endpoint, parameter, response (auto-generated from OpenAPI)
4. **Changelog**: what changed in each version
5. **Migration guides**: how to upgrade from v1 to v2
6. **SDKs**: code examples in 5 languages for every endpoint
7. **Playground**: try API calls in the browser
8. **Status page**: link to uptime page
9. **Error reference**: every error code with solution
10. **Community**: Discord/forum link

Tool: Mintlify, Readme.io, or Docusaurus.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design API Error Handling

**id:** `05-api-design/api-error-handling` · **Difficulty:** intermediate · **Tags:** error-handling, api, rfc7807, rest

````text
Design a consistent error handling strategy for my REST API.

Following RFC 7807 Problem Details:
```json
{
  "type": "https://api.example.com/errors/validation-error",
  "title": "Validation Failed",
  "status": 422,
  "detail": "The request body contains invalid data.",
  "instance": "/users/register",
  "errors": [{"field": "email", "message": "Must be a valid email"}]
}
```

Design:
1. Error type registry (all possible error types with URLs)
2. HTTP status code decision tree
3. Validation errors: list all field errors
4. Business logic errors: meaningful codes (INSUFFICIENT_FUNDS, USER_SUSPENDED)
5. Internal errors: never leak stack traces
6. Rate limit errors: include retry timing
7. Client SDK: parse errors into typed exceptions
8. Monitoring: every 5xx triggers an alert
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design an API Gateway

**id:** `05-api-design/api-gateway-design` · **Difficulty:** advanced · **Tags:** api-gateway, kong, nginx, architecture

**Placeholders:** [LIST YOUR SERVICES]

````text
Design an API gateway for my microservices architecture.

Services: [LIST YOUR SERVICES]
Clients: [Web app, Mobile app, Third-party]

Gateway responsibilities:
1. **Routing**: path-based and header-based routing rules
2. **Auth**: JWT validation, API key management
3. **Rate limiting**: per client, per service, per endpoint
4. **Load balancing**: round-robin, weighted, least-connections
5. **Circuit breaker**: fail fast when upstream is unhealthy
6. **Caching**: cache GET responses at edge
7. **Transformation**: request/response manipulation
8. **Observability**: request tracing, access logs, metrics
9. **TLS termination**: HTTPS → HTTP to services
10. **DDoS protection**: IP blocking, challenge-based

Tool: Kong (open source) or Nginx + Lua, with config files.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement Advanced API Gateway Rate Limiting

**id:** `05-api-design/api-gateway-rate-limiting` · **Difficulty:** advanced · **Tags:** api-gateway, rate-limiting, kong, nginx

````text
Implement sophisticated rate limiting at the API gateway level.

Gateway: [Kong / Nginx / Cloudflare Workers]

Rate limiting tiers:
- Anonymous: 100 req/min per IP
- Free account: 1,000 req/hour
- Pro account: 50,000 req/hour
- Enterprise: custom

Advanced features:
1. Cost-based limiting (not just request count)
2. Endpoint-specific limits (POST /ai-generate = 10x cost)
3. Global vs per-region limits
4. DDoS protection: detect and block attack patterns
5. Whitelisting: internal services bypass limits
6. Rate limit sharing across microservices
7. Graceful degradation: partial service when near limit

Redis cluster configuration for distributed state.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Manage the Full API Lifecycle

**id:** `05-api-design/api-lifecycle` · **Difficulty:** advanced · **Tags:** api, lifecycle, devops, strategy

**Placeholders:** [DESCRIBE]

````text
Manage my API's full lifecycle from design to sunset.

My API: [DESCRIBE]

Phases:
1. **Design**: API-first — spec before code, review with stakeholders
2. **Mock**: generate mock server from spec for parallel dev
3. **Develop**: implement against spec, linting to verify conformance
4. **Test**: contract testing, integration tests, security scan
5. **Document**: auto-generate from spec + hand-written guides
6. **Release**: semantic versioning, changelog, consumer notification
7. **Monitor**: uptime, latency, error rates, usage analytics
8. **Iterate**: gather consumer feedback, add features without breaking
9. **Deprecate**: announce sunset, provide migration path
10. **Sunset**: remove old version, redirect to new

Tool recommendations for each phase.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Load Test Your API

**id:** `05-api-design/api-load-testing` · **Difficulty:** intermediate · **Tags:** load-testing, k6, performance, api

**Placeholders:** [DESCRIBE YOUR API]

````text
Design and run a comprehensive load test for my API.

API to test: [DESCRIBE YOUR API]
Performance targets: [e.g., 1000 RPS, p99 < 200ms, error rate < 0.1%]

Using: k6

1. Baseline test: 1 user, 30s — establish baseline latency
2. Load test: ramp to 1000 VUs over 5min, sustain 10min
3. Spike test: instant jump to 10x normal traffic
4. Stress test: find breaking point (keep increasing until failure)
5. Soak test: moderate load for 24h (find memory leaks)

For each test:
- k6 script with realistic scenarios (not just one endpoint)
- Metrics to capture
- Pass/fail thresholds
- Results interpretation

Output: k6 scripts + Grafana dashboard for results.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build a Production-Like Mock Server

**id:** `05-api-design/api-mock-server` · **Difficulty:** intermediate · **Tags:** mock, api, prism, testing

````text
Build a comprehensive mock API server for my frontend team.

My API spec: [OPENAPI YAML or description]

Using: Prism (from Stoplight) — generate mock from OpenAPI automatically

1. Serve mock from OpenAPI spec: `prism mock api.yaml`
2. Dynamic examples: not just static examples from spec
3. Validation: validate requests against spec (reject invalid requests)
4. Proxy mode: real requests with recording for future mocks
5. Scenarios: different responses based on request params
6. Stateful mocking: maintain state between requests
7. Docker: run mock server in CI
8. Delay simulation: add realistic latency
9. Error scenarios: force specific error codes
10. Team sharing: host mock server for entire frontend team
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Mock External APIs for Development and Testing

**id:** `05-api-design/api-mocking` · **Difficulty:** intermediate · **Tags:** mocking, msw, testing, api

**Placeholders:** [LIST THIRD-PARTY APIS]

````text
Set up comprehensive API mocking for development and testing.

External APIs I use: [LIST THIRD-PARTY APIS]

Using: Mock Service Worker (MSW)

1. Handler setup: intercept matching requests
2. Realistic mock data using Faker.js
3. Simulated network delay and errors
4. Conditional responses: different responses based on request body
5. Stateful mocks: cart that accumulates items
6. Passthrough: let some requests hit real API
7. Browser vs Node.js setup
8. Integration with React Testing Library
9. Integration with Vitest
10. Toggle mocks with environment variable

Also: WireMock for Java, nock for Node.js, VCR for Ruby — comparison.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Monitor Your API in Production

**id:** `05-api-design/api-monitoring` · **Difficulty:** advanced · **Tags:** monitoring, api, apm, observability

**Placeholders:** [DESCRIBE YOUR STACK]

````text
Set up comprehensive monitoring for my production API.

Current setup: [DESCRIBE YOUR STACK]

Metrics to track:
1. **Availability**: uptime percentage (target: 99.9%)
2. **Latency**: p50, p95, p99 response times per endpoint
3. **Error rate**: 4xx and 5xx rates separately
4. **Throughput**: requests per second over time
5. **Saturation**: CPU, memory, DB connections

Alerting:
6. Error rate > 1% for 5 minutes → PagerDuty
7. p95 latency > 500ms → Slack
8. Uptime drops → immediate alert

Tools: Prometheus + Grafana (self-hosted) or DataDog (managed)

Output: dashboard JSON + alerting rules + runbook template.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design API Pagination

**id:** `05-api-design/api-pagination` · **Difficulty:** intermediate · **Tags:** pagination, api, rest, design

**Placeholders:** [LIST]

````text
Design comprehensive pagination for my API.

Resources to paginate: [LIST]
Expected scale: [e.g., millions of records]

Implement all patterns:
1. **Offset pagination**: ?page=2&per_page=20 → simple, has limitations
2. **Cursor pagination**: ?cursor=xxx&limit=20 → scalable, consistent
3. **Keyset pagination**: ?after_id=xxx&after_created_at=xxx → for sorted multi-col
4. **Seek pagination**: combining cursor + filters

For each:
- SQL/query implementation
- Response envelope shape (data, meta, links)
- Total count: when to include, when to skip (expensive)
- Frontend integration example
- Performance characteristics

Recommendation for my specific use case.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build an API Playground

**id:** `05-api-design/api-playground` · **Difficulty:** intermediate · **Tags:** api, playground, developer-experience, ui

**Placeholders:** [DESCRIBE]

````text
Build an interactive API playground for my API (like Stripe's API explorer).

My API: [DESCRIBE]

Features:
1. Request builder: select method, endpoint, fill params/body
2. Auth: enter API key or use OAuth to get a token
3. Environment selector: sandbox vs production
4. Code generation: copy the request as cURL, JavaScript, Python, Ruby
5. Response viewer: formatted JSON, headers, status code
6. Request history: last 50 requests
7. Saved requests: name and save common requests
8. Schema viewer: explore all available endpoints with docs
9. Example responses: pre-loaded realistic examples
10. Dark mode

Stack: React + Monaco Editor (for JSON body) + fetch API.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design API Rate Limiting

**id:** `05-api-design/api-rate-limiting-design` · **Difficulty:** advanced · **Tags:** rate-limiting, api, design, backend

````text
Design a comprehensive rate limiting strategy for my public API.

My API plans:
- Free: 1,000 req/day
- Pro: 100,000 req/day  
- Enterprise: unlimited (with fair-use)

Design:
1. Algorithm: token bucket vs leaky bucket vs sliding window — which and why
2. Granularity: global vs per-endpoint vs per-resource
3. Cost model: assign cost to expensive operations (search=10x, AI=100x)
4. Burst allowance: short bursts above limit without penalty
5. Response headers: standard headers consumers should read
6. 429 response body: clear message with retry timing
7. Abuse prevention: detect and block abusive patterns
8. Override: enterprise customers with custom limits

Output: rate limiting spec + Redis implementation.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design and Build an API SDK

**id:** `05-api-design/api-sdk-design` · **Difficulty:** advanced · **Tags:** sdk, api, typescript, client

**Placeholders:** [DESCRIBE YOUR API]

````text
Design and build a TypeScript SDK for my API.

API: [DESCRIBE YOUR API]

SDK design principles:
1. **Type safety**: TypeScript types for all requests and responses
2. **Fluent interface**: `client.users.create({...}).then()`
3. **Resource-based**: `client.users`, `client.products`
4. **Consistent error handling**: typed error classes
5. **Retry logic**: built-in retry with backoff
6. **Pagination helpers**: auto-paginate with async iterators
7. **Request/response interceptors**: for logging, auth refresh
8. **Config**: base URL, API key, timeout, retries
9. **Framework-agnostic**: works in Node.js and browser
10. **Zero dependencies**: or minimal deps

Output: complete SDK + README + usage examples.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Secure Your API Against Common Attacks

**id:** `05-api-design/api-security` · **Difficulty:** advanced · **Tags:** security, api, owasp, backend

**Placeholders:** [DESCRIBE]

````text
Harden my API against the OWASP API Security Top 10.

My API: [DESCRIBE]

1. **Broken Object Level Auth (BOLA)**: verify ownership on every request
2. **Broken Auth**: JWT best practices, no weak secrets
3. **Broken Object Property Level Auth**: never expose more fields than needed
4. **Unrestricted Resource Consumption**: rate limiting, pagination limits
5. **Broken Function Level Auth**: re-verify role on admin operations
6. **Unrestricted Access to Sensitive Business Flows**: apply stricter limits
7. **Server Side Request Forgery**: validate and allowlist URLs
8. **Security Misconfiguration**: headers, CORS, debug endpoints
9. **Improper Inventory Management**: disable unused endpoints
10. **Unsafe Consumption of APIs**: validate third-party API responses

For each: code example of the vulnerability + the fix.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Define Internal API Standards

**id:** `05-api-design/api-standards` · **Difficulty:** intermediate · **Tags:** api, standards, team, documentation

````text
Create internal API standards for my engineering team.

Team size: [N engineers], building [N microservices]

Standards document covering:
1. **URL conventions**: naming, nesting, parameter formats
2. **HTTP method semantics**: team agreement on GET/POST/PUT/PATCH/DELETE
3. **Status codes**: company-wide lookup table
4. **Error format**: mandatory fields, optional fields
5. **Auth method**: which auth per use case
6. **Pagination**: single standard (cursor-based)
7. **Date format**: ISO 8601 everywhere, always UTC
8. **Naming**: camelCase JSON fields, English only
9. **Versioning**: when and how to version
10. **Documentation**: what must be documented before shipping

Output: API Standards v1.0 document for team adoption.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Add Distributed Tracing to APIs

**id:** `05-api-design/api-telemetry` · **Difficulty:** advanced · **Tags:** tracing, opentelemetry, observability, api

**Placeholders:** [LIST YOUR SERVICES AND THEIR STACK]

````text
Add distributed tracing across my API services using OpenTelemetry.

Services: [LIST YOUR SERVICES AND THEIR STACK]

Implement:
1. OpenTelemetry SDK setup in each service (Node.js + Python examples)
2. Trace context propagation (W3C TraceContext headers)
3. Auto-instrumentation: HTTP, DB, Redis, message queues
4. Manual spans for business-critical operations
5. Trace attributes: user ID, request ID, customer tier
6. Sampling: 100% in dev, 10% in prod (head-based sampling)
7. Export to Jaeger (open source) or DataDog APM
8. Baggage: propagate tenant ID across service boundaries

Visualize: trace waterfall showing where time is spent.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design API Testing Strategy

**id:** `05-api-design/api-testing-strategy` · **Difficulty:** intermediate · **Tags:** testing, api, contract, postman

**Placeholders:** [N]

````text
Design a comprehensive testing strategy for my API.

API type: [REST / GraphQL] with [N] endpoints

Layers:
1. **Unit tests**: test each service/business logic function in isolation
2. **Integration tests**: test route → controller → service → real DB
3. **Contract tests**: verify API matches OpenAPI spec (Dredd or Spectral)
4. **E2E tests**: test complete user flows via API (Postman collections)
5. **Performance tests**: k6 load test for critical endpoints (target: 1000 RPS)
6. **Security tests**: OWASP ZAP scan, auth bypass attempts
7. **Fuzzing**: send random/malformed inputs to all endpoints

Coverage targets per layer.
CI pipeline: run all layers on each PR.
Output: test strategy document + example tests for each layer.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## API Versioning Strategy

**id:** `05-api-design/api-versioning-strategy` · **Difficulty:** intermediate · **Tags:** api, versioning, rest, strategy

**Placeholders:** [DESCRIBE WHAT'S CHANGING], [DESCRIBE YOUR CONSUMERS]

````text
Define a complete API versioning strategy for my product:

Current API users: [DESCRIBE YOUR CONSUMERS]
Breaking change planned: [DESCRIBE WHAT'S CHANGING]

Cover:
1. URL vs header vs query param — evaluate tradeoffs for my case
2. SemVer for APIs: what constitutes major/minor/patch
3. Backward compatibility rules (what is and isn't a breaking change)
4. Deprecation process: sunset headers, docs notice, timeline
5. Migration guide format for consumers
6. Running multiple versions simultaneously
7. Sunset monitoring: detect when old version traffic → 0
8. Client SDK versioning strategy

Output: versioning policy document + implementation code.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design Asynchronous API Operations

**id:** `05-api-design/async-api-design` · **Difficulty:** advanced · **Tags:** async, api, webhooks, polling

**Placeholders:** [LIST]

````text
Design async operation handling for my API.

Operations that are slow (> 5 seconds): [LIST]

Pattern 1 — Polling:
1. POST /export → 202 Accepted + `{job_id, status_url}`
2. GET /jobs/{id} → {status: pending|processing|done|failed, result_url}
3. Client polls with exponential backoff
4. Result available for 24h then deleted

Pattern 2 — Webhooks:
5. Client registers webhook URL
6. On completion: POST to webhook with result

Pattern 3 — WebSocket / SSE:
7. Connect before starting job
8. Receive real-time progress events

For MY specific operations: which pattern to use and why.
Implementation for each.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design an Event-Driven API

**id:** `05-api-design/event-driven-api` · **Difficulty:** advanced · **Tags:** events, api, kafka, event-sourcing

**Placeholders:** [DESCRIBE]

````text
Design an event-driven API architecture.

My domain: [DESCRIBE]

Event catalog (define all events):
1. Event naming convention: `[domain].[entity].[past-tense-verb]`
2. Event schema with: id, type, source, time, data, correlationId
3. Schema registry: version events, prevent breaking changes
4. Event taxonomy: Domain Events vs Integration Events vs Commands

API patterns:
5. **Event sourcing**: store events, derive state → audit log for free
6. **CQRS**: separate read model (optimized query) from write model (events)
7. **Choreography**: services react to events (no central orchestrator)
8. **Orchestration**: saga pattern for multi-step business processes

Implementation: Kafka or RabbitMQ + Node.js/Python consumers.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## GraphQL API Best Practices

**id:** `05-api-design/graphql-best-practices` · **Difficulty:** advanced · **Tags:** graphql, best-practices, api, performance

**Placeholders:** [DESCRIBE YOUR SCHEMA]

````text
Apply GraphQL best practices to my schema: [DESCRIBE YOUR SCHEMA].

1. **Schema design**: self-documenting, expressive types
2. **Naming**: consistent conventions (camelCase fields, PascalCase types)
3. **Nullability**: when to use ! — prefer nullable for forward compatibility
4. **Pagination**: Relay connection spec (avoid arrays for paginated data)
5. **Mutations**: one input type per mutation, return the mutated type
6. **Error handling**: errors as data vs GraphQL errors
7. **N+1 prevention**: DataLoader pattern, every resolver uses DataLoader
8. **Depth limiting**: prevent deeply nested queries (denial of service)
9. **Query complexity analysis**: score queries, reject too-complex ones
10. **Persisted queries**: hash-based for production (security + performance)
11. **Field deprecation**: @deprecated with migration notes
12. **Authorization**: never trust client, check auth in every resolver
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Set Up GraphQL Federation

**id:** `05-api-design/graphql-federation` · **Difficulty:** advanced · **Tags:** graphql, federation, microservices, apollo

**Placeholders:** [ENTITIES]

````text
Set up Apollo GraphQL Federation for my microservices.

Services:
- [Service 1]: owns [ENTITIES]
- [Service 2]: owns [ENTITIES]
- [Service 3]: owns [ENTITIES]

Implement:
1. Gateway: Apollo Router or Apollo Server Gateway
2. Subgraph setup for each service
3. Entity definition: @key directive on shared types
4. Reference resolver: resolve entities from other subgraphs
5. Extend types across subgraphs
6. Federated subscriptions
7. Auth: propagate token from gateway to subgraphs
8. Performance: query planning and batching
9. Supergraph schema composition
10. Schema checks: validate before deploying

With Docker Compose for local development.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## GraphQL Schema Design Masterclass

**id:** `05-api-design/graphql-schema-design` · **Difficulty:** advanced · **Tags:** graphql, schema, api

**Placeholders:** [YOUR DOMAIN]

````text
Design a GraphQL schema for [YOUR DOMAIN].

Principles to apply:
1. Think in graphs, not endpoints
2. Nullable vs non-nullable fields — when to use each
3. Input types for mutations
4. Connection pattern for pagination (edges, nodes, pageInfo)
5. Interface and Union types for polymorphism
6. Enum types for fixed values
7. Custom scalars (Date, URL, JSON, Money)
8. Subscription types for real-time
9. Directives: @deprecated, @auth, @cacheControl
10. Schema stitching vs federation for distributed systems

Output: complete SDL schema + example queries for each type.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement GraphQL Subscriptions

**id:** `05-api-design/graphql-subscriptions` · **Difficulty:** advanced · **Tags:** graphql, subscriptions, websockets, real-time

**Placeholders:** [DESCRIBE]

````text
Implement GraphQL subscriptions for real-time features.

Real-time features needed: [DESCRIBE]

Using: Apollo Server + graphql-ws

1. Subscription schema definition
2. PubSub setup (in-memory for single server, Redis for multiple)
3. Resolver: publish events + subscribe to topics
4. Authentication: verify JWT on WebSocket connection
5. Authorization: filter subscription events per user
6. Connection lifecycle: onConnect, onSubscribe, onDisconnect
7. Error handling: close connection on auth failure
8. Reconnection: client auto-reconnects with same subscription
9. Scaling: Redis PubSub adapter for horizontal scaling
10. Testing: subscription tests with graphql-ws client

Client implementation: React hook with Apollo Client.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Choose Between gRPC, REST, and GraphQL

**id:** `05-api-design/grpc-vs-rest` · **Difficulty:** advanced · **Tags:** grpc, rest, graphql, architecture

**Placeholders:** [DESCRIBE YOUR SYSTEM: services, clients, requirements]

````text
Help me choose the right API style for my use case: [DESCRIBE YOUR SYSTEM: services, clients, requirements].

Provide a rigorous comparison:

| Criteria | REST | GraphQL | gRPC |
|---|---|---|---|
| Performance | | | |
| Type safety | | | |
| Browser support | | | |
| Tooling | | | |
| Learning curve | | | |
| Caching | | | |
| Schema evolution | | | |

For MY use case specifically:
- Recommendation with justification
- Where each would fail
- Hybrid approach (if applicable)
- Implementation starter for the recommended option
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build a Hypermedia (HATEOAS) API

**id:** `05-api-design/hypermedia-api` · **Difficulty:** advanced · **Tags:** hateoas, rest, hypermedia, api

**Placeholders:** [LIST YOUR MAIN RESOURCES]

````text
Implement HATEOAS for my REST API to make it truly discoverable.

Resources: [LIST YOUR MAIN RESOURCES]

Implement:
1. `_links` in every response (self, related resources, actions)
2. Link relations using IANA-registered names (collection, item, edit, etc.)
3. `_actions` for available operations on this resource based on current state
4. Embedded resources (avoid extra round trips)
5. API root: GET / returns all available resources
6. HAL (Hypertext Application Language) format
7. Link templates (RFC 6570) for parameterized links
8. Siren or JSON:API as alternatives — compare

Example: Order resource with links to: payment, shipment, cancel (only if cancellable), invoice.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design Idempotent API Operations

**id:** `05-api-design/idempotency-design` · **Difficulty:** advanced · **Tags:** idempotency, api, reliability, payments

**Placeholders:** [LIST YOUR OPERATIONS]

````text
Design idempotent API operations for my payment-critical system.

Critical operations: [LIST YOUR OPERATIONS]

Implement:
1. `Idempotency-Key` header specification (UUID format, required for mutations)
2. Key storage: Redis with TTL (24h) + database for permanent record
3. Response caching: first successful response cached and returned on retry
4. In-flight protection: Redis lock during processing
5. Key fingerprinting: cache key = idempotency-key + request body hash
6. What to do if same key but different body (reject with 422)
7. Conditional requests: ETag + If-Match for read-modify-write
8. Testing: how to simulate retry scenarios
9. Client retry logic: when to retry and when not to
10. Documentation: how to communicate this to API consumers
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Write a Complete OpenAPI 3.1 Spec

**id:** `05-api-design/openapi-spec` · **Difficulty:** intermediate · **Tags:** openapi, swagger, api, documentation

**Placeholders:** [DESCRIBE YOUR API: purpose, main resources, auth method]

````text
Write a complete OpenAPI 3.1 specification for my API:

[DESCRIBE YOUR API: purpose, main resources, auth method]

Include:
1. `info` block with description and contact
2. `servers` for development and production
3. `securitySchemes` for your auth method
4. All `paths` with every operation
5. Request bodies with inline examples
6. Response schemas for 200, 400, 401, 403, 404, 422, 500
7. Reusable `components/schemas` (avoid repetition)
8. Reusable `components/responses` for common errors
9. Reusable `components/parameters`
10. Webhook definitions (if applicable)

Output: valid YAML, importable into Postman or Swagger UI.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Critique and Improve an Existing REST API

**id:** `05-api-design/rest-api-design-critique` · **Difficulty:** intermediate · **Tags:** rest, api, critique, refactoring

**Placeholders:** [PASTE YOUR API ROUTES AND SCHEMAS]

````text
Review and critique this REST API design:

[PASTE YOUR API ROUTES AND SCHEMAS]

Analyze:
1. URL design issues (verbs in URLs, inconsistent naming)
2. HTTP method misuse (GET with side effects, POST for everything)
3. Status code problems (200 for errors, 500 for everything)
4. Response shape inconsistencies
5. Missing pagination, filtering, sorting
6. Auth vulnerabilities
7. Missing error details
8. Performance issues (no caching headers, N+1 in related data)
9. Breaking change risks in current design
10. Security gaps

For each issue: severity (critical/major/minor), explanation, and the fix.
Output: improved API spec.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## REST API Design from Scratch

**id:** `05-api-design/rest-design-principles` · **Difficulty:** beginner · **Tags:** rest, api-design, best-practices

**Placeholders:** [YOUR DOMAIN]

````text
Design a REST API for [YOUR DOMAIN] from scratch applying every best practice:
1. Resource naming (nouns, plural, nested where appropriate)
2. HTTP methods (GET safe+idempotent, POST create, PUT replace, PATCH partial, DELETE)
3. Status codes (cheat sheet for every case)
4. Request/response shapes
5. Error format (RFC 7807 Problem Details)
6. Pagination, filtering, sorting query params
7. Versioning strategy
8. Authentication (Bearer JWT)
9. Rate limiting headers
10. HATEOAS links

Output: complete OpenAPI 3.1 YAML + sample cURL commands for every endpoint.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design a Streaming API

**id:** `05-api-design/streaming-api` · **Difficulty:** advanced · **Tags:** streaming, api, sse, ndjson

````text
Design a streaming API for: [USE CASE — AI responses / data export / live events].

Options to evaluate:
1. **Server-Sent Events**: unidirectional, browser-native, auto-reconnect
2. **WebSocket**: bidirectional, lower overhead
3. **gRPC streaming**: binary, typed, low latency
4. **NDJSON over HTTP**: newline-delimited JSON, simple
5. **HTTP chunked transfer**: progressive loading

For MY use case, implement:
- Server implementation
- Client (browser + Node.js) SDK
- Backpressure handling
- Error recovery
- Authentication
- Progress reporting
- Cancellation

With concrete code examples for each layer.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Secure Webhook Endpoints

**id:** `05-api-design/webhook-security` · **Difficulty:** intermediate · **Tags:** webhooks, security, api, hmac

**Placeholders:** [LIST: Stripe, GitHub, Twilio, etc.]

````text
Secure my webhook-receiving endpoints against abuse and spoofing.

Webhooks I receive from: [LIST: Stripe, GitHub, Twilio, etc.]

For each webhook provider:
1. Signature verification (HMAC-SHA256, provider-specific header)
2. Timestamp validation (reject webhooks > 5 minutes old)
3. Raw body parsing (not parsed JSON — signature is over raw bytes)
4. Idempotency: deduplicate events using event ID
5. Async processing: immediately return 200, process in queue
6. Retry handling: idempotent handlers for safe retries
7. Error handling: return 4xx only if payload is invalid (causes retries)
8. Monitoring: alert on missing expected webhooks
9. Testing: replay webhooks from provider dashboard
10. Webhook signing secret rotation procedure
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design a Webhook Delivery System

**id:** `05-api-design/webhook-system` · **Difficulty:** advanced · **Tags:** webhooks, api, events, reliability

**Placeholders:** [LIST YOUR EVENTS]

````text
Design and implement a production webhook system.

My service sends events when: [LIST YOUR EVENTS]

Consumers register endpoints to receive these events.

Implement:
1. Webhook registration API (URL, events to subscribe, secret)
2. Signature generation: HMAC-SHA256 of payload + timestamp
3. Delivery: HTTP POST to consumer endpoint
4. Retry: exponential backoff (1s, 5s, 30s, 5min, 30min, 2h, 12h, 24h)
5. Dead letter: mark webhook as failed after all retries
6. Delivery log: per-webhook history (status, response, attempts)
7. Dashboard: consumer can view delivery log, replay events
8. Verification guide: how consumers should verify signatures
9. Event catalog: document every event type with example payload
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design [SPEC_FORMAT] for [DOMAIN]

**id:** `05-api-design/design-spec-format-for-domain` · **Difficulty:** beginner/intermediate · **Tags:** graphql, rest, spec, grpc, api-design, openapi

**Variant group** (3 generated prompts collapsed). Pick one value per placeholder:
- `[SPEC_FORMAT]`: OpenAPI 3.1 | gRPC protobuf schemas
- `[DOMAIN]`: a medical appointment scheduler | a subscription billing workflow | an IoT telemetry stream

````text
Write the comprehensive design for [SPEC_FORMAT] mapping [DOMAIN]. Make sure to define request/response shapes, headers, and status codes.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** design-grpc-protobuf-schemas-for-a-medical-appointment-scheduler, design-openapi-31-for-a-subscription-billing-workflow, design-openapi-31-for-an-iot-telemetry-stream


## Implement [POLICY] policies for [DOMAIN] API

**id:** `05-api-design/implement-policy-policies-for-domain-api` · **Difficulty:** beginner/intermediate/advanced · **Tags:** graphql, rest, server-sent, spec, api-design, webhook, openapi

**Variant group** (4 generated prompts collapsed). Pick one value per placeholder:
- `[DOMAIN]`: a localized product search Engine | a logistics package tracker | a medical appointment scheduler
- `[POLICY]`: rate limiting policies | semantic API versioning

````text
Design the schema and specification to handle [POLICY] for [DOMAIN]. Provide concrete code examples and failure cases.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** implement-rate-limiting-policies-policies-for-a-logistics-package-tracker-api, implement-rate-limiting-policies-policies-for-a-medical-appointment-scheduler-api, implement-semantic-api-versioning-policies-for-a-localized-product-search-engine-api, implement-semantic-api-versioning-policies-for-a-medical-appointment-scheduler-api

