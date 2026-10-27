# 11-testing-qa

Unit/integration/E2E tests, mocking, Jest/Vitest/Playwright/Cypress/Pytest, coverage, test strategy.

30 prompts. Search `## ` headings or ids; see index.md for the one-line list.

## Test Accessibility (a11y)

**id:** `11-testing-qa/accessibility-testing` · **Difficulty:** intermediate · **Tags:** accessibility, a11y, testing, wcag

**Placeholders:** [DESCRIBE]

````text
Test and fix accessibility in my web application.

App: [DESCRIBE]
Compliance target: WCAG 2.1 AA

Automated testing:
1. **axe-core**: integrate with React Testing Library
2. **Lighthouse**: accessibility audit in CI
3. **Playwright**: axe-playwright for E2E a11y tests

Manual testing:
4. **Keyboard navigation**: tab through entire app, no mouse
5. **Screen reader**: VoiceOver (Mac) + NVDA (Windows)
6. **High contrast mode**: Windows high contrast
7. **Zoom to 400%**: no content lost
8. **Color contrast**: check all text/background pairs

Common issues to check:
9. Missing alt text on images
10. No focus indicator
11. Missing form labels
12. Poor color contrast
13. Non-descriptive link text
14. Dynamic content not announced

Output: axe integration + list of found issues + fixes.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Write API Contract Tests

**id:** `11-testing-qa/api-contract-tests` · **Difficulty:** advanced · **Tags:** contract-testing, pact, api, testing

**Placeholders:** [YOUR API / MICROSERVICE], [YOUR FRONTEND / SERVICE]

````text
Write consumer-driven contract tests using Pact.

Consumer: [YOUR FRONTEND / SERVICE]
Provider: [YOUR API / MICROSERVICE]

Consumer side:
1. Define interactions: request + expected response shape
2. Pact test: real HTTP calls against Pact mock server
3. Pact file generated: the contract
4. Publish contract to Pact Broker

Provider side:
5. Pull contracts from Pact Broker
6. Run provider verification against real provider
7. Provider test: does the provider fulfill the contract?
8. Publish verification results

**Can I deploy check**:
9. Before deploying consumer: can it talk to this provider version?
10. Before deploying provider: does it satisfy all consumer contracts?

CI integration: GitHub Actions workflow for both sides.
Output: consumer test + provider test + GitHub Actions config.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## API Testing Patterns

**id:** `11-testing-qa/api-testing-patterns` · **Difficulty:** intermediate · **Tags:** api, testing, rest, patterns

**Placeholders:** [DESCRIBE]

````text
Implement comprehensive API testing patterns for my REST API.

API: [DESCRIBE]
Testing tool: Vitest + Supertest OR Postman Collections

Test patterns:
1. **Happy path**: successful requests with valid data
2. **Validation errors**: test every required field and format
3. **Auth tests**:
   - No token → 401
   - Expired token → 401
   - Wrong role → 403
   - Correct auth → 200
4. **Not found**: request non-existent resources → 404
5. **Conflict**: create duplicate → 409
6. **Rate limit**: exceed limit → 429
7. **Pagination**: first page, last page, out-of-bounds page
8. **Sorting**: ascending and descending
9. **Filtering**: test all filter combinations
10. **Large payloads**: test max request body size

Organize tests by: resource → operation → scenario.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Set Up Cucumber for BDD Testing

**id:** `11-testing-qa/bdd-cucumber` · **Difficulty:** intermediate · **Tags:** cucumber, bdd, gherkin, testing

**Placeholders:** [DESCRIBE IN BUSINESS TERMS], [YOUR FEATURE IN GHERKIN]

````text
Set up Cucumber.js for BDD testing in my Node.js project.

Features to test: [DESCRIBE IN BUSINESS TERMS]

1. **Installation**: `@cucumber/cucumber`, `@playwright/test` or Supertest
2. **Feature files**: write in Gherkin syntax
3. **Step definitions**: implement each Given/When/Then step
4. **World**: shared context between steps
5. **Hooks**: Before/After for setup and teardown
6. **Tags**: @slow, @smoke, @regression — run subsets
7. **Parameterized scenarios**: Scenario Outline with Examples table
8. **Background**: common steps for all scenarios in a feature
9. **Reports**: cucumber-html-reporter for stakeholders
10. **Page objects**: for UI scenarios

Feature to implement end-to-end:
```gherkin
[YOUR FEATURE IN GHERKIN]
```

Output: feature file + step definitions + cucumber config.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Write BDD-Style Tests

**id:** `11-testing-qa/bdd-testing` · **Difficulty:** intermediate · **Tags:** bdd, cucumber, gherkin, testing

**Placeholders:** [ACTION], [ADDITIONAL ASSERTION], [BUSINESS VALUE], [DESCRIBE FEATURES IN BUSINESS TERMS], [EXPECTED OUTCOME], [FEATURE NAME], [GOAL], [INITIAL STATE], [SCENARIO NAME], [USER TYPE]

````text
Write Behavior-Driven Development (BDD) tests for my features.

Features to test: [DESCRIBE FEATURES IN BUSINESS TERMS]
Framework: Cucumber.js (or Vitest with BDD syntax)

Gherkin feature files:
```gherkin
Feature: [FEATURE NAME]
  As a [USER TYPE]
  I want to [GOAL]
  So that [BUSINESS VALUE]

  Scenario: [SCENARIO NAME]
    Given [INITIAL STATE]
    When [ACTION]
    Then [EXPECTED OUTCOME]
    And [ADDITIONAL ASSERTION]
```

Step definitions:
- Given steps: set up state
- When steps: perform action
- Then steps: assert outcome

Best practices:
- Write scenarios with product owner, not after
- Scenarios describe behavior, not implementation
- Living documentation: scenarios are always up to date

Output: feature files + step definitions for my use cases.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Set Up Continuous Testing

**id:** `11-testing-qa/continuous-testing` · **Difficulty:** intermediate · **Tags:** ci-cd, testing, automation, pipeline

**Placeholders:** [DESCRIBE]

````text
Set up continuous testing integrated with my development workflow.

Stack: [DESCRIBE]
CI: GitHub Actions

Testing gates:
1. **Pre-commit hook** (local, < 30s):
   - Lint (ESLint)
   - Type check (TypeScript)
   - Unit tests for changed files only
2. **PR opened** (< 5 min):
   - Full unit test suite
   - Integration tests
   - Coverage check (fail if drops below threshold)
3. **Merge to main** (< 15 min):
   - Full test suite
   - E2E smoke tests
   - Performance regression test
4. **Nightly** (unlimited time):
   - Extended E2E suite
   - Load tests
   - Security scan
5. **Post-deploy**:
   - Smoke tests against production

Output: complete GitHub Actions workflows for each gate.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Write End-to-End Tests with Playwright

**id:** `11-testing-qa/e2e-testing` · **Difficulty:** intermediate · **Tags:** e2e, playwright, testing, automation

**Placeholders:** [DESCRIBE YOUR APP], [USER FLOW 1: e.g., Sign up → complete onboarding → first core action], [USER FLOW 2: e.g., Search → add to cart → checkout], [USER FLOW 3: e.g., Admin creates → user sees it]

````text
Write end-to-end tests for my web application using Playwright.

App: [DESCRIBE YOUR APP]
Key user flows to test:
1. [USER FLOW 1: e.g., Sign up → complete onboarding → first core action]
2. [USER FLOW 2: e.g., Search → add to cart → checkout]
3. [USER FLOW 3: e.g., Admin creates → user sees it]

Playwright best practices:
- Page Object Model: one class per page
- Stable locators: data-testid attributes
- Parallel test execution
- CI-ready: headless, record videos on failure
- No sleeps: use Playwright's auto-waiting
- Isolated tests: each test starts fresh
- API mocking for tests that don't need real data

Output: page objects + test specs + Playwright config.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Apply Fuzzing to Find Security Bugs

**id:** `11-testing-qa/fuzz-testing` · **Difficulty:** advanced · **Tags:** fuzzing, security, testing, bugs

**Placeholders:** [DESCRIBE YOUR PARSER / API / FUNCTION]

````text
Apply fuzzing to find security vulnerabilities and bugs in my code.

Code to fuzz: [DESCRIBE YOUR PARSER / API / FUNCTION]

Fuzzing types:
1. **Mutation fuzzing**: take valid input, randomly mutate
2. **Generation fuzzing**: generate inputs from grammar
3. **Coverage-guided fuzzing**: find inputs that cover new code paths

Tools:
4. **Node.js**: `@jazzer.js/core` (coverage-guided)
5. **Python**: `atheris` (coverage-guided fuzzer from Google)
6. **API fuzzing**: OWASP ZAP API scan
7. **Property-based**: fast-check with arbitrary generators

Targets to fuzz:
8. Parsers: JSON, XML, CSV, image formats
9. API inputs: all endpoint parameters
10. Cryptographic functions: key/message combinations

For my code: fuzz harness setup + initial seed corpus + how to interpret crashes.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Write Integration Tests

**id:** `11-testing-qa/integration-testing` · **Difficulty:** intermediate · **Tags:** testing, integration, supertest, database

**Placeholders:** [LIST YOUR ENDPOINTS]

````text
Write integration tests for my API.

API routes to test: [LIST YOUR ENDPOINTS]
Stack: Express.js + PostgreSQL + Redis

Setup:
1. Test database: isolated test DB, reset between test suites
2. Test server: start Express app with test config
3. Supertest: HTTP requests in tests
4. Mock external services: email, payment, third-party APIs

Test patterns:
5. **Auth flows**: register → login → access protected route
6. **CRUD flows**: create → read → update → delete
7. **Error flows**: invalid input, unauthorized, not found
8. **Business rules**: ensure business rules are enforced
9. **Pagination**: test page boundaries
10. **Concurrent requests**: test race condition protection

Database strategy: transactions that rollback after each test (or Docker Postgres per test run).
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Write Load Tests

**id:** `11-testing-qa/load-testing` · **Difficulty:** intermediate · **Tags:** load-testing, k6, performance, qa

**Placeholders:** [DESCRIBE]

````text
Write load tests for my application.

Application: [DESCRIBE]
Target: [X requests/second with p99 < Yms]

Using: k6

```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '2m', target: 100 },   // ramp up
    { duration: '10m', target: 100 },  // stay at 100 VUs
    { duration: '2m', target: 0 },    // ramp down
  ],
  thresholds: {
    http_req_duration: ['p(99)<500'],
    http_req_failed: ['rate<0.01'],
  },
};
```

1. Realistic user scenarios (not just one endpoint)
2. Auth: login first, use token for subsequent requests
3. Think time: `sleep(1)` between requests
4. Data variation: different users, different data
5. Checks: verify response correctness under load
6. Custom metrics: track specific business events
7. HTML report output
8. Grafana integration: real-time metrics during test

Output: complete k6 test script for my application.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Master Mocking Strategies

**id:** `11-testing-qa/mock-strategies` · **Difficulty:** intermediate · **Tags:** mocking, testing, jest, msw

**Placeholders:** [PASTE CODE WITH EXTERNAL DEPENDENCIES]

````text
Master mocking strategies for comprehensive testing.

Code to test: [PASTE CODE WITH EXTERNAL DEPENDENCIES]

Mocking approaches:
1. **Manual mocks**: custom mock implementations
2. **Jest spies**: `jest.spyOn(obj, 'method')`
3. **Module mocks**: `jest.mock('./module')`
4. **Mock Service Worker (MSW)**: intercept HTTP at network level
5. **Test doubles taxonomy**: stub, spy, mock, fake, dummy — when to use each

What to mock:
6. **Always mock**: external APIs, email, payment, time
7. **Usually mock**: database (use test DB instead)
8. **Never mock**: the code under test itself

Bad mocking patterns:
9. Over-mocking: testing implementation not behavior
10. Brittle mocks: break when implementation changes

For my code: complete mocking setup for each dependency.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Apply Mutation Testing

**id:** `11-testing-qa/mutation-testing` · **Difficulty:** advanced · **Tags:** mutation-testing, stryker, quality, testing

**Placeholders:** [PASTE OR DESCRIBE YOUR CODE AND TESTS]

````text
Apply mutation testing to measure real test quality.

Code to mutate: [PASTE OR DESCRIBE YOUR CODE AND TESTS]
Framework: Stryker (JavaScript/TypeScript)

What mutation testing does:
- Automatically introduces bugs (mutations) into your code
- Runs tests against each mutation
- If tests PASS with a bug → tests are not catching this case
- Mutation score = killed mutations / total mutations

Setting up Stryker:
1. Install: `npm install --save-dev @stryker-mutator/core`
2. Configure: stryker.config.json
3. Run: `npx stryker run`
4. Interpret: HTML report showing survived mutations

For each survived mutation:
5. What bug wasn't caught?
6. Write a test that kills it
7. Target: > 80% mutation score

Output: Stryker config + analysis of gaps + new tests to kill survivors.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Write Performance Tests

**id:** `11-testing-qa/performance-testing` · **Difficulty:** advanced · **Tags:** performance, load-testing, k6, artillery

**Placeholders:** [DESCRIBE], [N], [X]

````text
Write performance tests for my application.

Application: [DESCRIBE]
Performance goals:
- Throughput: [X] requests/second
- Latency: p95 < [X]ms
- Error rate: < [X]%

Using: k6

1. **Baseline test**: single user, measure baseline latency
2. **Load test**: ramp to target load, hold, ramp down
3. **Stress test**: exceed target load, find breaking point
4. **Spike test**: sudden load spike (traffic burst)
5. **Soak test**: sustained load for [N] hours (find memory leaks)

For each test:
- k6 script with realistic user scenarios (not just one endpoint)
- Assertions: fail if performance goals not met
- Metrics to capture
- Analysis: how to read the results

Integrate into CI: run nightly, alert on regression.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Apply Property-Based Testing

**id:** `11-testing-qa/property-based-testing` · **Difficulty:** advanced · **Tags:** property-based, fast-check, testing, generative

**Placeholders:** [PASTE YOUR FUNCTIONS]

````text
Apply property-based testing to find edge cases I'd never think of.

Code to test: [PASTE YOUR FUNCTIONS]
Framework: fast-check (JavaScript)

Property-based testing:
- Instead of `expect(add(1, 2)).toBe(3)`, you define PROPERTIES
- Properties: things that should ALWAYS be true
- fast-check generates hundreds of random inputs
- Shrinks failing input to the simplest case

Examples of properties:
- `sort(arr)` should always return same length as `arr`
- `add(a, b) === add(b, a)` (commutativity)
- `parse(serialize(data))` equals `data` (roundtrip)
- `encode` then `decode` returns original string

For my code:
1. Identify properties that should always hold
2. Write fast-check tests for each property
3. Run and interpret failures
4. Add any found edge cases to unit tests as regression tests
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Set Up Regression Testing

**id:** `11-testing-qa/regression-testing` · **Difficulty:** intermediate · **Tags:** regression, testing, automation, ci-cd

**Placeholders:** [DESCRIBE NOTABLE BUGS THAT OCCURRED], [DESCRIBE]

````text
Set up a regression testing process to prevent old bugs from returning.

Application: [DESCRIBE]
Past bugs: [DESCRIBE NOTABLE BUGS THAT OCCURRED]

1. **Bug-driven tests**: for every bug fixed, write a test that proves it's fixed
2. **Regression test suite**: dedicated suite of known-to-have-broken scenarios
3. **Run on every PR**: catch regressions before they merge
4. **Snapshot tests**: UI components don't visually regress
5. **API contract tests**: API responses don't regress
6. **Performance benchmarks**: latency doesn't regress (k6 + assertions)
7. **Database queries**: query counts don't regress (N+1 guard)
8. **Dependency updates**: test before merging Dependabot PRs

For my past bugs, write specific regression tests that would have caught them.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Perform Security Testing

**id:** `11-testing-qa/security-testing` · **Difficulty:** advanced · **Tags:** security, testing, owasp, penetration

**Placeholders:** [DESCRIBE YOUR APP]

````text
Perform security testing on my application.

App: [DESCRIBE YOUR APP]
Auth type: [JWT / session / OAuth]

Security tests to run:

**Authentication**:
1. Brute force: rate limiting works?
2. JWT manipulation: tampered token rejected?
3. Session fixation: session ID changes on login?

**Authorization (IDOR)**:
4. Access other user's resources by changing ID in URL
5. Horizontal privilege escalation
6. Vertical privilege escalation (regular → admin)

**Injection**:
7. SQL injection: special chars in all inputs
8. XSS: script tags in all text inputs
9. Command injection: shell metacharacters

**Logic**:
10. Price manipulation: modify amount in request
11. Race conditions: parallel requests

Tool: OWASP ZAP or manual testing with Burp Suite.
Output: test scripts + found vulnerabilities + fixes.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Use Snapshot Testing Effectively

**id:** `11-testing-qa/snapshot-testing` · **Difficulty:** intermediate · **Tags:** snapshot, testing, react, visual

**Placeholders:** [LIST]

````text
Use snapshot testing effectively in my React project.

Components to test: [LIST]

**When snapshots are useful**:
1. Large output that's hard to assert manually
2. JSON/XML output from transformations
3. Initial component render

**When snapshots are harmful**:
4. Snapshots that change constantly (flaky, meaningless)
5. Snapshots of third-party component internals
6. Using snapshots instead of meaningful assertions

**Best practices**:
7. Commit snapshots to git
8. Review snapshot diffs in PRs
9. Small snapshots (one component at a time)
10. Inline snapshots for small values: `toMatchInlineSnapshot`
11. Component-level not full-page

**Visual regression testing** (better alternative for UI):
12. Chromatic + Storybook: compare screenshots across commits
13. Playwright screenshot comparison

For my components: which to snapshot vs which to test with specific assertions.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Apply Test-Driven Development

**id:** `11-testing-qa/tdd-workflow` · **Difficulty:** intermediate · **Tags:** tdd, red-green-refactor, testing, methodology

**Placeholders:** [DESCRIBE THE FEATURE TO IMPLEMENT]

````text
Apply TDD to implement this feature:

[DESCRIBE THE FEATURE TO IMPLEMENT]

TDD workflow (Red → Green → Refactor):

**Red phase** — write failing tests first:
1. Write a test for the simplest case that doesn't work yet
2. Run it, confirm it fails for the right reason
3. Write tests for all known cases (don't implement yet)

**Green phase** — minimum code to pass:
4. Write the minimum code to make the first test pass
5. Don't optimize, just make it work
6. Repeat for each test

**Refactor phase** — improve while tests stay green:
7. Improve naming, structure, eliminate duplication
8. Tests must remain passing

Output: complete test file + implementation file, built test by test.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design Test Automation Strategy

**id:** `11-testing-qa/test-automation-strategy` · **Difficulty:** advanced · **Tags:** testing, strategy, automation, qa

**Placeholders:** [DAILY / MULTIPLE TIMES PER DAY], [DESCRIBE]

````text
Design a comprehensive test automation strategy for my project.

Project: [DESCRIBE]
Team: [N developers, Y QA engineers]
Deployment frequency: [DAILY / MULTIPLE TIMES PER DAY]

Test pyramid:
```
           E2E (10%)
         Integration (20%)
       Unit Tests (70%)
```

For each layer:
1. What to test at this layer
2. Tools and frameworks
3. Who writes these tests (dev or QA)
4. When they run (pre-commit, pre-merge, post-deploy)
5. Target coverage and speed

Test pipeline:
6. Pre-commit: lint + fast unit tests (< 30s)
7. PR: unit + integration tests + linting
8. Merge to main: full suite including E2E
9. Nightly: performance, security, extended E2E
10. Monitoring: alert on flaky tests

Output: testing strategy document + recommended tools.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Achieve High Test Coverage

**id:** `11-testing-qa/test-coverage` · **Difficulty:** intermediate · **Tags:** coverage, testing, quality, metrics

**Placeholders:** [PASTE COVERAGE REPORT OR DESCRIBE]

````text
Help me achieve and maintain high test coverage for my codebase.

Current coverage: [CURRENT %]
Target: [TARGET %]
Uncovered code: [PASTE COVERAGE REPORT OR DESCRIBE]

1. **Identify gaps**: which files/functions have low coverage?
2. **Prioritize**: cover critical paths first (auth, payments, data mutations)
3. **Write tests for each gap**: generate tests for uncovered code
4. **Branch coverage**: test all if/else branches
5. **Edge case coverage**: empty arrays, null values, error paths
6. **Integration coverage**: tests that cover multiple units together
7. **Coverage thresholds**: fail CI if coverage drops below threshold
8. **Coverage reports**: HTML report + PR comment showing change
9. **Mutation testing**: does changing code make tests fail? (Stryker)
10. **What to not test**: 3rd party code, generated code, trivial getters

Output: specific tests for my coverage gaps.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Manage Test Data Effectively

**id:** `11-testing-qa/test-data-management` · **Difficulty:** intermediate · **Tags:** test-data, testing, factories, seeding

**Placeholders:** [DATABASE], [NODE.JS / PYTHON]

````text
Set up effective test data management.

Stack: [NODE.JS / PYTHON] + [DATABASE]

1. **Factory pattern**: create test objects with sensible defaults
2. **Override specific fields**: `createUser({ email: 'custom@test.com' })
3. **Traits**: `createUser('admin')`, `createUser('verified')`
4. **Sequence numbers**: unique IDs, emails, usernames
5. **Relationships**: `createPost({ author: createUser() })`

Database strategy:
6. **Test database**: separate DB for tests
7. **Transactions**: wrap each test in a transaction, rollback
8. **Reset between tests**: DELETE all rows (faster than recreate)
9. **Seed**: minimal seed data that all tests can rely on

Test fixtures:
10. JSON files for complex nested structures
11. Shared fixtures for common scenarios
12. Parameterized tests with multiple data sets

Implement using: fishery (TypeScript) or factory_boy (Python).
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Master Test Doubles

**id:** `11-testing-qa/test-doubles` · **Difficulty:** intermediate · **Tags:** mocking, stubs, fakes, testing

**Placeholders:** [PASTE CODE WITH DEPENDENCIES]

````text
Master test doubles (the proper terminology for mocks).

Code under test: [PASTE CODE WITH DEPENDENCIES]

Test double types:
1. **Dummy**: object passed but never used (fill required params)
2. **Stub**: returns canned answer, no behavior verification
3. **Spy**: records calls, can assert on them later
4. **Mock**: pre-programmed with expectations, verifies behavior
5. **Fake**: working implementation, but simplified (in-memory DB)

When to use each:
6. Dummy: when a dep is required but irrelevant to the test
7. Stub: when you need controlled return values
8. Spy: when you want to verify a function was called
9. Mock: when behavior (call count, args) matters
10. Fake: when real implementation is too slow for tests (DB)

Implement each type for my specific dependencies.
Mistakes to avoid: over-mocking, testing the mock instead of the code.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build Test Infrastructure

**id:** `11-testing-qa/test-infrastructure` · **Difficulty:** advanced · **Tags:** testing, infrastructure, docker, ci-cd

````text
Build robust test infrastructure for my application.

Requirements:
- Tests should be reproducible anywhere
- Fast: parallel execution
- Isolated: tests don't interfere
- Real: use real services where possible, not mocks

Infrastructure:
1. **Docker Compose for tests**: PostgreSQL + Redis + app in containers
2. **Database per test run**: each CI job gets fresh database
3. **Testcontainers**: spin up DB in Docker from test code
4. **Test environment management**: create/destroy on demand
5. **Parallelism**: split tests across multiple CI workers
6. **Caching**: cache Docker images, dependencies
7. **GitHub Actions matrix**: run against multiple versions
8. **Artifact storage**: test results, coverage reports, screenshots
9. **Flaky test retry**: retry up to 3 times before failing CI
10. **Test result reporting**: PR comment with pass/fail + coverage

Output: complete infrastructure setup.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Track and Improve Test Quality Metrics

**id:** `11-testing-qa/test-metrics` · **Difficulty:** intermediate · **Tags:** metrics, testing, quality, ci-cd

````text
Track and improve test quality metrics for my project.

Metrics to track:
1. **Coverage**: line, branch, function coverage trends
2. **Test duration**: total suite time, slowest tests
3. **Flakiness rate**: % of tests that fail intermittently
4. **Test failure rate**: % of CI runs that fail due to tests
5. **Defect escape rate**: bugs found in production vs in tests
6. **MTTR**: how long to fix a broken test suite

Implement:
7. Coverage report → PR comment (threshold check)
8. Slow test detection: flag tests > 1 second
9. Flaky test detection: track tests that pass/fail on retry
10. Test report: HTML report in CI artifacts

Dashboard:
- Grafana: coverage over time, flakiness trend
- GitHub Actions: test result annotations

Output: GitHub Actions workflow for all metrics.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Organize a Large Test Suite

**id:** `11-testing-qa/test-organization` · **Difficulty:** intermediate · **Tags:** testing, organization, structure, maintenance

**Placeholders:** [DESCRIBE: N test files, what's messy, what's slow]

````text
Organize my growing test suite for maintainability.

Current state: [DESCRIBE: N test files, what's messy, what's slow]

Organization principles:
1. **Mirror source structure**: test file next to source file
2. **Group by feature**: tests for the same feature together
3. **Setup/teardown**: `beforeAll`, `afterAll`, `beforeEach` correctly
4. **Shared utilities**: test helpers in a shared folder
5. **Test categories**: unit | integration | e2e — run separately

Speed optimization:
6. **Parallel execution**: run test files in parallel (Vitest default)
7. **Selective running**: `--testPathPattern` for fast iteration
8. **Skip slow tests in watch mode**
9. **Mocking**: mock all I/O in unit tests (keep them fast)
10. **Order**: fast tests first (fail fast in CI)

CI strategy: unit tests always, integration on push, e2e nightly.
Output: recommended folder structure + vitest.config.ts.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Develop a Testing Philosophy

**id:** `11-testing-qa/testing-philosophy` · **Difficulty:** intermediate · **Tags:** testing, philosophy, strategy, best-practices

**Placeholders:** [DESCRIBE TEAM SIZE AND EXPERIENCE LEVEL], [DESCRIBE: no tests / some tests / comprehensive tests but slow]

````text
Help me develop a testing philosophy and practical guidelines for my team.

Team: [DESCRIBE TEAM SIZE AND EXPERIENCE LEVEL]
Current state: [DESCRIBE: no tests / some tests / comprehensive tests but slow]

Philosophy principles:
1. **Tests are documentation**: tests show what the code should do
2. **Test behavior, not implementation**: don't test internal private methods
3. **Fast feedback**: unit tests in < 30s, full suite in < 10min
4. **Trust**: if you don't trust a test, fix or delete it
5. **TDD where appropriate**: TDD for complex logic, not boilerplate

Practical rules:
6. Bug → test → fix (always write regression test)
7. New feature → test coverage > 80%
8. Refactoring → tests protect you
9. Code review: check test quality not just code quality
10. Flaky tests → fix immediately, they erode trust

Output: a one-page Testing Guidelines document for my team.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Write Comprehensive Unit Tests

**id:** `11-testing-qa/unit-testing` · **Difficulty:** intermediate · **Tags:** testing, unit-tests, jest, vitest

**Placeholders:** [LANGUAGE], [PASTE YOUR CODE]

````text
Write comprehensive unit tests for this code:

```[LANGUAGE]
[PASTE YOUR CODE]
```

Requirements:
1. **Test every function** — not just the happy path
2. **Edge cases**: empty input, null, undefined, zero, negative numbers, max values
3. **Error cases**: test that errors are thrown correctly
4. **Boundaries**: values at the edge of acceptable ranges
5. **Integration points**: mock external dependencies (DB, API, time)
6. **Arrange-Act-Assert**: clean test structure
7. **Descriptive names**: `it('should return empty array when no users exist')`
8. **No test duplication**: parameterized tests where appropriate
9. **Coverage**: target 100% for this module
10. **Fast**: all tests run in < 100ms (mock I/O)

Framework: Vitest (Jest compatible).
Output: complete test file with all tests passing.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Set Up Visual Regression Testing

**id:** `11-testing-qa/visual-regression-testing` · **Difficulty:** intermediate · **Tags:** visual-regression, storybook, chromatic, testing

**Placeholders:** [DESCRIBE]

````text
Set up visual regression testing to catch UI changes.

App: [DESCRIBE]
Option A — Chromatic (Storybook hosted):
1. Connect Storybook to Chromatic
2. GitHub Action: run Chromatic on every PR
3. Review visual diffs in Chromatic UI
4. Approve or reject changes
5. Baseline updates on approval

Option B — Playwright screenshot comparison:
6. Navigate to each page
7. Take screenshot
8. Compare to stored baseline (pixel diff)
9. Fail on diff > threshold
10. Update baselines manually

For Chromatic:
- Install and configure
- Per-story vs per-component tests
- Flaky story handling (animations)
- Interaction tests with Storybook

For Playwright:
- Screenshot strategy (full page vs viewport)
- Mask dynamic content (dates, user names)
- Cross-browser visual testing

Output: complete setup for your chosen option.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Mock dependencies using [TEST_FRAMEWORK] for [TEST_TARGET]

**id:** `11-testing-qa/mock-dependencies-using-test-framework-for-test-target` · **Difficulty:** beginner/intermediate/advanced · **Tags:** cypress, automation, testing, database, unit-test, qa, rest, stripe, redux, jest, junit, playwright, pytest, user, vitest

**Variant group** (11 generated prompts collapsed). Pick one value per placeholder:
- `[TEST_FRAMEWORK]`: Cypress | Go standard test library | JUnit 5 | Jest | Playwright | Pytest | Vitest
- `[TEST_TARGET]`: REST API integration routes | Redux state management hooks | Stripe payment controller functions | database repository layers | user input signup forms
- `[TEST_FEATURE]`: automated coverage metrics reports | database seed utilities | parallel execution workers | request mocking systems | snapshot tests comparisons

````text
Configure test mocks and stubs using [TEST_FRAMEWORK] for testing [TEST_TARGET]. Implement [TEST_FEATURE] for reliable, isolated builds.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** mock-dependencies-using-cypress-for-database-repository-layers, mock-dependencies-using-go-standard-test-library-for-rest-api-integration-routes, mock-dependencies-using-go-standard-test-library-for-stripe-payment-controller-functions, mock-dependencies-using-jest-for-redux-state-management-hooks, mock-dependencies-using-junit-5-for-database-repository-layers, mock-dependencies-using-junit-5-for-rest-api-integration-routes, mock-dependencies-using-playwright-for-rest-api-integration-routes, mock-dependencies-using-pytest-for-stripe-payment-controller-functions, mock-dependencies-using-pytest-for-user-input-signup-forms, mock-dependencies-using-vitest-for-database-repository-layers, mock-dependencies-using-vitest-for-redux-state-management-hooks


## Write tests with [TEST_FRAMEWORK] for [TEST_TARGET]

**id:** `11-testing-qa/write-tests-with-test-framework-for-test-target` · **Difficulty:** beginner/intermediate/advanced · **Tags:** stripe, cypress, automation, testing, unit-test, qa, redux, rest, user, jest, junit, visual, playwright, pytest, vitest

**Variant group** (11 generated prompts collapsed). Pick one value per placeholder:
- `[TEST_FRAMEWORK]`: Cypress | Go standard test library | JUnit 5 | Jest | Playwright | Pytest | Vitest
- `[TEST_TARGET]`: REST API integration routes | Redux state management hooks | Stripe payment controller functions | user input signup forms | visual regression suites
- `[TEST_FEATURE]`: automated coverage metrics reports | database seed utilities | parallel execution workers | request mocking systems | snapshot tests comparisons

````text
Write comprehensive automated tests with [TEST_FRAMEWORK] to validate [TEST_TARGET]. Ensure coverage of edge cases, error handling, and mock [TEST_FEATURE].
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** write-tests-with-cypress-for-stripe-payment-controller-functions, write-tests-with-go-standard-test-library-for-redux-state-management-hooks, write-tests-with-go-standard-test-library-for-rest-api-integration-routes, write-tests-with-go-standard-test-library-for-user-input-signup-forms, write-tests-with-jest-for-rest-api-integration-routes, write-tests-with-junit-5-for-rest-api-integration-routes, write-tests-with-junit-5-for-visual-regression-suites, write-tests-with-playwright-for-visual-regression-suites, write-tests-with-pytest-for-user-input-signup-forms, write-tests-with-vitest-for-redux-state-management-hooks, write-tests-with-vitest-for-user-input-signup-forms

