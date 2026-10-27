# 09-debugging-code-review

Debugging bugs, memory leaks, races, deadlocks, slow queries; structured code reviews and refactors.

33 prompts. Search `## ` headings or ids; see index.md for the one-line list.

## Debug API Contract Mismatches

**id:** `09-debugging-code-review/api-contract` · **Difficulty:** intermediate · **Tags:** api, contract, debugging, types

**Placeholders:** [PASTE ACTUAL API RESPONSE], [PASTE YOUR TYPESCRIPT INTERFACE OR EXPECTED SHAPE]

````text
Debug the mismatch between my API response and my frontend/client expectations.

API response (actual):
```json
[PASTE ACTUAL API RESPONSE]
```

Expected by client:
```typescript
[PASTE YOUR TYPESCRIPT INTERFACE OR EXPECTED SHAPE]
```

1. List every mismatch (field name, type, nesting, missing field, extra field)
2. Which side is wrong — API or client?
3. Fix both sides to match
4. Add Zod validation to catch this at runtime
5. Add TypeScript types that match the actual API
6. How to prevent this drift: OpenAPI spec + codegen
7. Write a test that would have caught this mismatch
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Debug API Integration Issues

**id:** `09-debugging-code-review/api-debugging` · **Difficulty:** beginner · **Tags:** api, debugging, http, integration

**Placeholders:** [API NAME / URL], [DESCRIBE], [PASTE ERROR OR WRONG RESPONSE]

````text
Debug my API integration issue.

I'm calling: [API NAME / URL]
Request I'm sending: [PASTE curl command or request code]
Expected response: [DESCRIBE]
Actual response: [PASTE ERROR OR WRONG RESPONSE]

1. Analyze the request — is it correctly formed?
2. Check auth headers — are they present and correct format?
3. Check request body — content-type, encoding, required fields
4. Check status code — what does this code specifically mean for this API?
5. Parse the error message — what is it actually saying?
6. Check rate limits — am I being throttled?
7. Fix the request
8. How to test it: corrected curl command

Also: how to debug this type of API issue independently in the future.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Debug Async/Await Problems

**id:** `09-debugging-code-review/async-bugs` · **Difficulty:** intermediate · **Tags:** async, debugging, promises, node-js

**Placeholders:** [DESCRIBE: unhandled rejections, race conditions, sequential when should be parallel, deadlock], [PASTE YOUR ASYNC CODE]

````text
Debug these async/await problems in my code:

```javascript
[PASTE YOUR ASYNC CODE]
```

Errors/symptoms: [DESCRIBE: unhandled rejections, race conditions, sequential when should be parallel, deadlock]

Check for:
1. Missing `await` — sync when should be async
2. `await` in loops — sequential when could be `Promise.all()`
3. Unhandled promise rejections
4. Race conditions — two async ops modifying same state
5. Error swallowing — catch block does nothing
6. Promise constructor antipattern
7. async function returning a value that isn't awaited by caller
8. Finally block issues

Fix all issues and explain each one.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Reduce Code Complexity

**id:** `09-debugging-code-review/code-complexity` · **Difficulty:** intermediate · **Tags:** complexity, refactoring, clean-code, cognitive

**Placeholders:** [LANGUAGE], [N], [PASTE CODE]

````text
Reduce the complexity of this code:

```[LANGUAGE]
[PASTE CODE]
```

Metrics (if available): Cyclomatic complexity: [N], Lines per function: [N]

Techniques to apply:
1. **Extract Method**: break long functions into smaller ones
2. **Replace Conditionals**: strategy pattern, polymorphism, lookup tables
3. **Early returns**: reduce nesting with guard clauses
4. **Replace loop with pipeline**: map/filter/reduce
5. **Introduce Parameter Object**: group related params
6. **Remove dead code**: unreachable branches
7. **Simplify boolean**: `return condition` not `if (x) return true else return false`
8. **Extract constants**: replace magic numbers with named constants

Target: cyclomatic complexity < 10, functions < 20 lines.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Perform a Thorough Code Review

**id:** `09-debugging-code-review/code-review` · **Difficulty:** intermediate · **Tags:** code-review, quality, feedback

**Placeholders:** [LANGUAGE], [PASTE YOUR CODE]

````text
You are a senior engineer with 15 years experience. Perform a thorough code review on this code:

```[LANGUAGE]
[PASTE YOUR CODE]
```

Review for:
1. **Bugs**: logic errors, edge cases not handled, potential exceptions
2. **Security**: injection, auth, data exposure, input validation
3. **Performance**: N+1 queries, unnecessary loops, memory leaks
4. **Readability**: naming, comments, cognitive complexity
5. **Design**: SOLID principles, separation of concerns
6. **Testability**: is this code easy to unit test?
7. **Error handling**: missing try/catch, unhandled promise rejections
8. **TypeScript**: type safety, any usage, type assertions

Format: severity (critical/major/minor) + line reference + explanation + fix
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Identify and Fix Code Smells

**id:** `09-debugging-code-review/code-smell` · **Difficulty:** intermediate · **Tags:** code-smells, refactoring, clean-code, quality

**Placeholders:** [LANGUAGE], [PASTE CODE]

````text
Identify and fix code smells in this codebase:

```[LANGUAGE]
[PASTE CODE]
```

Scan for all 22 classic code smells:
1. Long Method
2. Large Class
3. Primitive Obsession
4. Long Parameter List
5. Divergent Change
6. Shotgun Surgery
7. Feature Envy
8. Data Clumps
9. Switch Statements
10. Parallel Inheritance Hierarchies
11. Lazy Class
12. Speculative Generality
13. Temporary Field
14. Message Chains
15. Middle Man
16. Inappropriate Intimacy
17. Alternative Classes with Different Interfaces
18. Incomplete Library Class
19. Data Class
20. Refused Bequest
21. Comments (that explain bad code instead of fixing it)
22. Duplicate Code

For each found: location + explanation + refactoring.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Debug Concurrency Issues

**id:** `09-debugging-code-review/concurrency-debug` · **Difficulty:** advanced · **Tags:** concurrency, async, race-conditions, debugging

**Placeholders:** [DESCRIBE: data inconsistency, duplicate processing, lost updates], [PASTE CODE], [SINGLE SERVER / MULTIPLE SERVERS / SERVERLESS]

````text
Debug concurrency issues in my application.

Code: [PASTE CODE]
Issue: [DESCRIBE: data inconsistency, duplicate processing, lost updates]
Environment: [SINGLE SERVER / MULTIPLE SERVERS / SERVERLESS]

1. **Identify shared state**: what data can be modified concurrently?
2. **Is this a real race or just looks like one?**
3. **Database-level fix**: `SELECT FOR UPDATE`, transactions, advisory locks
4. **Application-level fix**: distributed lock (Redis SETNX), queue, debounce
5. **Idempotency**: make the operation safe to run multiple times
6. **Optimistic locking**: version column + retry on conflict
7. **Testing**: how to write a test that reliably triggers the race
8. **Monitoring**: track and alert on conflict rate in production

Fix for my specific concurrency issue.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Debug Cross-Browser Compatibility Issues

**id:** `09-debugging-code-review/cross-browser` · **Difficulty:** intermediate · **Tags:** browser, compatibility, css, javascript

**Placeholders:** [DESCRIBE: looks broken in Safari / IE / Firefox / Mobile Chrome], [PASTE CODE]

````text
Debug cross-browser compatibility issues with my code.

Issue: [DESCRIBE: looks broken in Safari / IE / Firefox / Mobile Chrome]
Code causing the issue:
```css/html/js
[PASTE CODE]
```

1. Identify the browser-specific API or CSS property causing the issue
2. Check caniuse.com compatibility for the feature
3. Provide a cross-browser fix:
   - CSS: fallback values, -webkit- prefixes, feature queries (@supports)
   - JS: polyfills, alternative APIs
4. Test in: Chrome, Firefox, Safari, Edge, iOS Safari, Android Chrome
5. Postcss/Autoprefixer: automate prefix addition
6. Browserslist config: define browser targets for build tools
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Debug CSS Layout Problems

**id:** `09-debugging-code-review/css-layout-debug` · **Difficulty:** beginner · **Tags:** css, layout, debugging, flexbox

**Placeholders:** [DESCRIBE: element is overlapping, not centering, not full-width, disappearing, wrong on mobile], [DESCRIBE], [PASTE CSS], [PASTE HTML]

````text
Debug my CSS layout problem.

Problem: [DESCRIBE: element is overlapping, not centering, not full-width, disappearing, wrong on mobile]
HTML:
```html
[PASTE HTML]
```
CSS:
```css
[PASTE CSS]
```
Browser/device where it breaks: [DESCRIBE]

1. Inspect in DevTools: check computed styles, box model, margins
2. Identify the specific property causing the issue
3. Common causes check:
   - Collapsing margins
   - Float clearing
   - Position context (relative parent for absolute child)
   - Flexbox vs Grid confusion
   - z-index without position
   - Missing `box-sizing: border-box`
   - Viewport units on mobile (100vh issue)
4. Fix with minimum CSS change
5. Make it responsive if not already
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Debug Database Query Issues

**id:** `09-debugging-code-review/database-query-debug` · **Difficulty:** intermediate · **Tags:** database, sql, orm, debugging

**Placeholders:** [DESCRIBE: wrong results / slow / error / no results], [PASTE QUERY], [PASTE RELEVANT SCHEMA]

````text
Debug database query issues in my application.

ORM/Query builder: [Prisma / Drizzle / TypeORM / raw SQL]
Schema: [PASTE RELEVANT SCHEMA]
Query code: [PASTE QUERY]
Problem: [DESCRIBE: wrong results / slow / error / no results]

1. Log the generated SQL: `DEBUG=prisma:query` or `.explain()`
2. Run the SQL directly in psql/pgAdmin — same result?
3. Check WHERE conditions — are they correct?
4. Check JOINs — LEFT JOIN vs INNER JOIN matters
5. Check NULL handling — `= NULL` doesn't work, use `IS NULL`
6. Check case sensitivity — text comparison is case-sensitive
7. Check timezone — TIMESTAMPTZ vs TIMESTAMP
8. Add EXPLAIN ANALYZE if it's slow
9. Fix the query
10. Write a test that confirms correct results
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Debug Any Error Message

**id:** `09-debugging-code-review/debug-this-error` · **Difficulty:** beginner · **Tags:** debugging, errors, troubleshooting

**Placeholders:** [DESCRIBE], [PASTE THE RELEVANT CODE]

````text
You are an expert debugger. I'm getting this error:

```
[PASTE ERROR MESSAGE + STACK TRACE]
```

Context:
- Language/framework: [e.g., Node.js 20, Express 4]
- What I was doing when it happened: [DESCRIBE]
- Relevant code: [PASTE THE RELEVANT CODE]

Please:
1. Explain exactly what this error means in plain English
2. Identify the root cause (not just the symptom)
3. Show me the fix with before/after code
4. Explain why the fix works
5. Tell me how to prevent this class of error in the future
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Systematic Debugging Checklist

**id:** `09-debugging-code-review/debugging-checklist` · **Difficulty:** beginner · **Tags:** debugging, process, methodology, troubleshooting

**Placeholders:** [ALWAYS / INTERMITTENTLY / RARELY], [ANY DEPLOYMENTS OR CODE CHANGES], [DESCRIBE THE BUG], [WHAT IS HAPPENING], [WHAT SHOULD HAPPEN]

````text
Walk me through systematic debugging for this problem:

Problem: [DESCRIBE THE BUG]
Expected behavior: [WHAT SHOULD HAPPEN]
Actual behavior: [WHAT IS HAPPENING]
Frequency: [ALWAYS / INTERMITTENTLY / RARELY]
Recent changes: [ANY DEPLOYMENTS OR CODE CHANGES]

Systematic debugging process:
1. **Reproduce**: confirm I can reproduce it consistently
2. **Isolate**: narrow down where the bug occurs (binary search the code)
3. **Understand**: trace the execution path, check assumptions
4. **Hypothesis**: form a specific hypothesis about the cause
5. **Test hypothesis**: make one change at a time
6. **Fix**: implement the fix
7. **Verify**: confirm the fix works and didn't break anything else
8. **Post-mortem**: why did this happen? How to prevent it?

Apply this process to my specific bug.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Debug Dependency Conflicts

**id:** `09-debugging-code-review/dependency-issues` · **Difficulty:** beginner · **Tags:** dependencies, npm, debugging, node-js

**Placeholders:** [OS], [PASTE RELEVANT SECTION], [VERSION]

````text
Debug my dependency conflicts.

Error: [PASTE npm install / yarn / pnpm error]
package.json: [PASTE RELEVANT SECTION]
Node version: [VERSION]
OS: [OS]

1. Explain what the conflict is (peer dependency, incompatible version, etc.)
2. Check `npm ls [package-name]` — which versions are installed?
3. Check if there's a version that satisfies all peer deps
4. Override strategy: use `resolutions` (yarn) or `overrides` (npm v8+)
5. Check if the package has a version that drops the conflicting dep
6. Alternative: is there a replacement package without the conflict?

Output: exact commands to resolve the conflict + updated package.json.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Debug Development Environment Setup

**id:** `09-debugging-code-review/environment-setup` · **Difficulty:** beginner · **Tags:** environment, setup, debugging, devops

**Placeholders:** [DESCRIBE WHAT'S NOT WORKING], [LIST WHAT YOU'VE ATTEMPTED], [PASTE ALL ERROR OUTPUT]

````text
Help me debug my development environment setup issue.

OS: [Mac / Windows / Linux]
Language/Runtime: [Node.js / Python / Go / etc.]
Tool/Framework: [e.g., Next.js, Docker, PostgreSQL]

Issue: [DESCRIBE WHAT'S NOT WORKING]

Error messages:
```
[PASTE ALL ERROR OUTPUT]
```

What I've already tried:
- [LIST WHAT YOU'VE ATTEMPTED]

Please:
1. Diagnose the root cause
2. Step-by-step fix
3. Verification: how to confirm it's fixed
4. Prevent this from happening again (document the correct setup steps)
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement Comprehensive Error Handling

**id:** `09-debugging-code-review/error-boundaries` · **Difficulty:** intermediate · **Tags:** error-handling, debugging, resilience, node-js

**Placeholders:** [DESCRIBE: unhandled errors, unclear error messages, missing logging], [PASTE RELEVANT CODE]

````text
Implement comprehensive error handling for my application.

Current code: [PASTE RELEVANT CODE]
Current problem: [DESCRIBE: unhandled errors, unclear error messages, missing logging]

1. **Error classification**: operational vs programmer errors
2. **Error types**: create domain-specific error classes
3. **Async error handling**: catch all promise rejections
4. **Middleware**: centralized Express error handler
5. **Logging**: structured error logging with context
6. **User messages**: never show stack traces to users
7. **Recovery**: graceful degradation for non-fatal errors
8. **Alerting**: page on-call for critical errors
9. **Error tracking**: Sentry or equivalent integration
10. **Testing**: test that errors are caught and handled correctly

Transform my code with all these patterns applied.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Debug Feature Flag Problems

**id:** `09-debugging-code-review/feature-flag-debug` · **Difficulty:** beginner · **Tags:** feature-flags, debugging, configuration

**Placeholders:** [DESCRIBE HOW FLAGS ARE STORED AND CHECKED], [DESCRIBE: flag not applying, wrong users seeing feature, flag causing errors], [PASTE RELEVANT CODE]

````text
Debug issues with my feature flag implementation.

Feature flag system: [DESCRIBE HOW FLAGS ARE STORED AND CHECKED]
Problem: [DESCRIBE: flag not applying, wrong users seeing feature, flag causing errors]
Code: [PASTE RELEVANT CODE]

1. Verify flag value: log the raw flag value before the check
2. Check the evaluation logic: is the condition correct?
3. Cache: is an old cached value being used?
4. User targeting: is the user ID/segment correctly identified?
5. Rollout percentage: is the hash function deterministic and correct?
6. Race condition: is the flag checked before it's loaded?
7. Default value: what happens if flag service is down?
8. Testing: how to test a feature behind a flag
9. Rollback: how to immediately disable the flag

Fix my specific feature flag issue.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Solve Git Problems

**id:** `09-debugging-code-review/git-problem` · **Difficulty:** beginner · **Tags:** git, debugging, version-control, recovery

**Placeholders:** [DESCRIBE YOUR GIT SITUATION AND WHAT WENT WRONG], [PASTE IF ANY], [PASTE: git log --oneline -10], [PASTE: git status]

````text
Help me solve this Git problem:

[DESCRIBE YOUR GIT SITUATION AND WHAT WENT WRONG]

My git log: [PASTE: git log --oneline -10]
Current status: [PASTE: git status]
Error message: [PASTE IF ANY]

Scenarios I need help with (check which apply):
□ Accidentally committed to wrong branch
□ Need to undo a commit (already pushed)
□ Merge conflict I can't resolve
□ Lost uncommitted work
□ Detached HEAD state
□ Rebased and things went wrong
□ Want to combine multiple commits
□ Need to cherry-pick a commit

Provide: step-by-step commands with explanation of what each one does. Warn me about any destructive operations.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Debug Infinite Loops and Hangs

**id:** `09-debugging-code-review/infinite-loop` · **Difficulty:** intermediate · **Tags:** debugging, loops, async, performance

**Placeholders:** [DESCRIBE: CPU spikes, process hangs, browser freezes, async never resolves], [PASTE CODE]

````text
Debug an infinite loop or hang in my code.

Code: [PASTE CODE]
Symptoms: [DESCRIBE: CPU spikes, process hangs, browser freezes, async never resolves]

1. **Identify the type**:
   - Infinite loop: condition never becomes false
   - Infinite recursion: base case missing or never reached
   - Async deadlock: waiting for something that never resolves
   - Event loop blockage: synchronous code blocking Node.js
2. **Find the loop**: which loop/recursion is infinite?
3. **Check the termination condition**: what should make it stop?
4. **Off-by-one**: is the counter changing correctly?
5. **Mutation**: is the loop modifying the array it's iterating?
6. **Async**: is there a circular dependency in async resolution?
7. **Fix and verify**: add a maximum iteration guard as safety net
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Analyze Logs to Find Root Cause

**id:** `09-debugging-code-review/log-analysis` · **Difficulty:** intermediate · **Tags:** logs, debugging, monitoring, analysis

**Placeholders:** [DESCRIBE WHAT USERS EXPERIENCED], [PASTE LOG OUTPUT], [TIMESTAMP]

````text
Analyze these logs to find the root cause of the issue.

Logs:
```
[PASTE LOG OUTPUT]
```

Symptoms reported: [DESCRIBE WHAT USERS EXPERIENCED]
Time of incident: [TIMESTAMP]

1. Identify the first error in the timeline
2. Trace the error propagation through the system
3. Find correlated events before the error (what triggered it?)
4. Identify the root cause vs symptoms
5. Check: is this a known pattern? (OOM, connection exhaustion, timeout cascade)
6. Estimate blast radius: how many users/requests affected?
7. Immediate fix recommendation
8. Long-term fix to prevent recurrence
9. Monitoring: what alert would have caught this earlier?

Formatted as a mini incident report.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Debug a Memory Leak

**id:** `09-debugging-code-review/memory-leak` · **Difficulty:** advanced · **Tags:** memory, debugging, node-js, performance

**Placeholders:** [DESCRIBE: heap growing over time, OOM crashes after N hours, memory never GC'd]

````text
Help me find and fix a memory leak in my Node.js application.

Symptoms: [DESCRIBE: heap growing over time, OOM crashes after N hours, memory never GC'd]
Code: [PASTE RELEVANT CODE — particularly long-lived objects, event listeners, caches]

1. **Common memory leak causes** in Node.js:
   - Event listeners not removed
   - Closures holding references
   - Global variables accumulating
   - Cache without eviction
   - Unresolved promises
   - Third-party library leaks
2. **Debugging tools**: heapdump, Chrome DevTools heap profiler, clinic.js
3. **Analysis**: compare heap snapshots — what's growing?
4. **Fix**: the specific fix for my code
5. **Prevention**: code patterns to avoid leaks

Provide heap snapshot analysis instructions + the fix.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Fix N+1 Query Problems

**id:** `09-debugging-code-review/n-plus-one` · **Difficulty:** intermediate · **Tags:** n-plus-one, sql, orm, performance

**Placeholders:** [DESCRIBE: slow API, thousands of queries in logs]

````text
Fix the N+1 query problem in my code.

Code: [PASTE CODE WITH N+1]
ORM: [Prisma / TypeORM / Sequelize / raw SQL]
Symptom: [DESCRIBE: slow API, thousands of queries in logs]

Detect N+1:
1. Log all SQL queries (enable ORM query logging)
2. Count queries — if N records → N+1 queries, that's N+1
3. Identify which relation causes the N+1

Fix:
4. Eager loading: `include` related models in one query
5. DataLoader pattern: batch multiple lookups into one query
6. JOIN query: write it as a single JOIN instead of multiple queries
7. Select only needed fields (avoid over-fetching)

Before and after: show query count reduction.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Find and Fix Performance Bottlenecks

**id:** `09-debugging-code-review/performance-bottleneck` · **Difficulty:** advanced · **Tags:** performance, profiling, optimization

**Placeholders:** [DESCRIBE: slow API, high CPU, memory growing, etc.], [PASTE CODE], [PASTE FLAME GRAPH / METRICS]

````text
Help me find and fix the performance bottleneck in this code.

Code: [PASTE CODE]
Performance symptoms: [DESCRIBE: slow API, high CPU, memory growing, etc.]
Profiling data (if available): [PASTE FLAME GRAPH / METRICS]

Analyze:
1. What is the most expensive operation?
2. What is the algorithmic complexity? Can it be improved?
3. Are there unnecessary computations in loops?
4. Are there memory allocations that could be avoided?
5. Is there blocking I/O that should be async?
6. Is there N+1 query pattern?
7. Can results be cached or memoized?

Output: fixed code with explanation of each optimization and expected improvement.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Profile and Optimize Application Performance

**id:** `09-debugging-code-review/performance-profiling` · **Difficulty:** advanced · **Tags:** profiling, performance, node-js, optimization

**Placeholders:** [DESCRIBE]

````text
Profile and optimize my application's performance.

Application: [DESCRIBE]
Performance goal: [e.g., reduce API response time from 2s to 200ms]

**Profiling in Node.js**:
1. `node --prof app.js` + `node --prof-process` → isolate output
2. Chrome DevTools CPU profiler via `--inspect`
3. `clinic.js`: `clinic doctor`, `clinic flame`, `clinic bubbleprof`
4. `autocannon`: HTTP load testing to identify bottlenecks under load

**Common optimizations I'll look for**:
5. Database queries (add indexes, reduce queries, add caching)
6. Synchronous code blocking the event loop
7. Expensive computation that can be cached or moved to worker thread
8. Unnecessary object creation in hot paths
9. Memory allocation patterns

After profiling MY code: specific fixes with before/after benchmarks.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Identify and Fix Race Conditions

**id:** `09-debugging-code-review/race-condition` · **Difficulty:** advanced · **Tags:** concurrency, race-conditions, async, debugging

**Placeholders:** [DESCRIBE: inconsistent state, different results on each run, intermittent failures], [LANGUAGE], [PASTE CODE]

````text
Identify and fix race conditions in this concurrent code:

```[LANGUAGE]
[PASTE CODE]
```

Symptoms: [DESCRIBE: inconsistent state, different results on each run, intermittent failures]

1. **Identify the shared state**: what data is accessed by concurrent operations?
2. **Identify the race window**: where can the interleaving cause issues?
3. **Reproduce**: minimal test case to trigger the race
4. **Fix options**:
   - Mutex/lock: serialize access
   - Atomic operations: use atomic compare-and-swap
   - Immutable data: avoid shared mutable state
   - Actor model: single writer
   - Database transactions: SERIALIZABLE isolation
5. **Verify**: test that proves the fix eliminates the race

For Node.js: remember — single-threaded, but async can still race.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Refactor Legacy Code

**id:** `09-debugging-code-review/refactor-legacy` · **Difficulty:** intermediate · **Tags:** refactoring, legacy, clean-code, modernization

**Placeholders:** [LANGUAGE], [PASTE LEGACY CODE]

````text
Refactor this legacy code to modern standards:

```[LANGUAGE]
[PASTE LEGACY CODE]
```

Refactoring goals:
1. **Readability**: meaningful names, small functions, clear intent
2. **Modern syntax**: arrow functions, destructuring, optional chaining, nullish coalescing
3. **Error handling**: proper try/catch, typed errors
4. **Type safety**: add TypeScript types if applicable
5. **DRY**: eliminate code duplication
6. **SOLID principles**: single responsibility, open/closed
7. **Remove dead code**: unused variables, unreachable branches
8. **Test coverage**: make it testable (dependency injection)

Show: diff-style before/after for each change, with explanation of why.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Debug and Write Regular Expressions

**id:** `09-debugging-code-review/regex-debug` · **Difficulty:** intermediate · **Tags:** regex, debugging, patterns, parsing

**Placeholders:** [COUNTER-EXAMPLE 1], [DESCRIBE OR GIVE EXAMPLES], [DESCRIBE], [EXAMPLE 1], [EXAMPLE 2], [YOUR REGEX]

````text
Help me write and debug a regular expression.

What I need to match: [DESCRIBE OR GIVE EXAMPLES]
Examples that should match:
- [EXAMPLE 1]
- [EXAMPLE 2]

Examples that should NOT match:
- [COUNTER-EXAMPLE 1]

My current regex (if any): [YOUR REGEX]
What's wrong with it: [DESCRIBE]

1. Write the correct regex
2. Explain each part of the regex
3. Test against all my examples
4. Handle edge cases I might have missed
5. Performance considerations for large inputs
6. Language-specific notes: [JavaScript / Python / Java]
7. Online regex tester link for further experimentation
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Identify Security Vulnerabilities in Code

**id:** `09-debugging-code-review/security-vulnerability` · **Difficulty:** advanced · **Tags:** security, vulnerabilities, owasp, audit

**Placeholders:** [LANGUAGE], [PASTE YOUR CODE]

````text
Audit this code for security vulnerabilities:

```[LANGUAGE]
[PASTE YOUR CODE]
```

Scan for:
1. **SQL injection**: string concatenation in queries
2. **XSS**: unescaped user input in HTML
3. **Path traversal**: user input in file paths
4. **Command injection**: user input in exec/shell
5. **Insecure deserialization**: parsing untrusted JSON/YAML/pickle
6. **Sensitive data exposure**: passwords/tokens in logs or responses
7. **Missing auth**: endpoints without authentication check
8. **IDOR**: accessing resources without ownership check
9. **SSRF**: fetching URLs from user input
10. **Prototype pollution**: merging untrusted objects

For each vulnerability: severity, proof of concept exploit, and the fix.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Debug SQL Query Problems

**id:** `09-debugging-code-review/sql-debug` · **Difficulty:** intermediate · **Tags:** sql, debugging, postgresql, performance

**Placeholders:** [DESCRIBE: wrong results, too slow, syntax error, N+1 detected], [PASTE RELEVANT TABLE DEFINITIONS], [PASTE YOUR SQL QUERY]

````text
Debug this SQL query:

```sql
[PASTE YOUR SQL QUERY]
```

Problem: [DESCRIBE: wrong results, too slow, syntax error, N+1 detected]
Database: [PostgreSQL / MySQL / SQLite]
Schema: [PASTE RELEVANT TABLE DEFINITIONS]

1. **Syntax check**: identify any syntax errors
2. **Logic check**: does the query do what was intended?
3. **Performance**: run EXPLAIN ANALYZE — what's slow?
4. **Index usage**: is an index being used? Should one be added?
5. **Correctness**: edge cases — NULLs, duplicates, wrong JOIN type
6. **Rewrite**: optimized version of the query
7. **Test cases**: sample data to verify the fix

Output: corrected, optimized query with explanation.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Debug Failing Tests

**id:** `09-debugging-code-review/test-debugging` · **Difficulty:** intermediate · **Tags:** testing, debugging, jest, vitest

**Placeholders:** [PASTE FAILING TEST OUTPUT], [PASTE FAILING TEST], [PASTE IMPLEMENTATION]

````text
Debug my failing tests.

Test output:
```
[PASTE FAILING TEST OUTPUT]
```

Test code:
```javascript
[PASTE FAILING TEST]
```

Implementation code:
```javascript
[PASTE IMPLEMENTATION]
```

1. Parse the test failure message — what exactly failed?
2. Is the test wrong or is the implementation wrong?
3. Check: mocking issues? Async test issues? Setup/teardown?
4. Fix whichever is incorrect
5. Identify any related tests that might also be broken
6. How to make these tests less brittle in the future?
7. Run: what command to run just this test for quick iteration?
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Fix TypeScript Type Errors

**id:** `09-debugging-code-review/type-errors` · **Difficulty:** intermediate · **Tags:** typescript, types, debugging, errors

**Placeholders:** [PASTE THE TSC ERROR OUTPUT], [PASTE YOUR CODE WITH TYPE ERRORS]

````text
Fix these TypeScript type errors:

```typescript
[PASTE YOUR CODE WITH TYPE ERRORS]
```

Errors:
```
[PASTE THE TSC ERROR OUTPUT]
```

For each error:
1. What the error means in plain English
2. Why TypeScript is complaining
3. The correct fix (not just `as any`)
4. If the fix reveals a logic bug, fix that too

Afterward:
- Are there any remaining `any` types I should address?
- Are there TypeScript strict mode settings I should enable?
- How to configure `tsconfig.json` for maximum type safety?
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Debug WebSocket Connection Issues

**id:** `09-debugging-code-review/websocket-debug` · **Difficulty:** intermediate · **Tags:** websockets, debugging, real-time, network

**Placeholders:** [DESCRIBE: can't connect, disconnects randomly, messages not received, duplicate messages]

````text
Debug WebSocket connection issues.

Setup: [Socket.io / native WebSocket / ws library]
Client: [Browser / React Native / Node.js]
Problem: [DESCRIBE: can't connect, disconnects randomly, messages not received, duplicate messages]

Debugging steps:
1. Open browser DevTools → Network tab → WS filter → inspect frames
2. Server logs: are connections being established?
3. CORS: for Socket.io, is the origin allowed?
4. Proxy: if behind nginx/load balancer, are Upgrade headers passed?
5. Reconnection: client should auto-reconnect — is it?
6. Event name mismatch: server emits 'foo', client listens to 'bar'
7. Room handling: is the user in the right room?
8. Authentication: is the handshake auth token valid?

Fix for my specific issue.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Conduct code review to fix [BUG_CLASS] in [COMPONENT]

**id:** `09-debugging-code-review/conduct-code-review-to-fix-bug-class-in-component` · **Difficulty:** beginner/intermediate/advanced · **Tags:** code-review, troubleshooting, debugging, java, node.js, python, slow

**Variant group** (11 generated prompts collapsed). Pick one value per placeholder:
- `[BUG_CLASS]`: Go data race conditions | Java multithreaded deadlocks | Node.js event loop blocks | Python pandas memory usage | Slow PostgreSQL join queries
- `[COMPONENT]`: a bulk data import CSV script | a continuous background task worker | a high-throughput server endpoint | an image resizing handler
- `[EVIDENCE]`: distributed tracing logs | error tracebacks | profiler metrics snapshots

````text
Review raw code for [COMPONENT] that causes [BUG_CLASS]. Explain the root cause and provide refactored, robust code using [EVIDENCE].
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** conduct-code-review-to-fix-go-data-race-conditions-in-a-bulk-data-import-csv-script, conduct-code-review-to-fix-go-data-race-conditions-in-a-continuous-background-task-worker, conduct-code-review-to-fix-go-data-race-conditions-in-a-high-throughput-server-endpoint, conduct-code-review-to-fix-go-data-race-conditions-in-an-image-resizing-handler, conduct-code-review-to-fix-java-multithreaded-deadlocks-in-a-high-throughput-server-endpoint, conduct-code-review-to-fix-java-multithreaded-deadlocks-in-an-image-resizing-handler, conduct-code-review-to-fix-nodejs-event-loop-blocks-in-an-image-resizing-handler, conduct-code-review-to-fix-python-pandas-memory-usage-in-a-bulk-data-import-csv-script, conduct-code-review-to-fix-python-pandas-memory-usage-in-a-high-throughput-server-endpoint, conduct-code-review-to-fix-slow-postgresql-join-queries-in-a-continuous-background-task-worker, conduct-code-review-to-fix-slow-postgresql-join-queries-in-an-image-resizing-handler


## Debug [BUG_CLASS] in [COMPONENT]

**id:** `09-debugging-code-review/debug-bug-class-in-component` · **Difficulty:** beginner/intermediate/advanced · **Tags:** code-review, troubleshooting, debugging, java, node.js, python, react, slow

**Variant group** (8 generated prompts collapsed). Pick one value per placeholder:
- `[BUG_CLASS]`: Go data race conditions | Java multithreaded deadlocks | Node.js event loop blocks | Python pandas memory usage | React memory leaks | Slow PostgreSQL join queries
- `[COMPONENT]`: a bulk data import CSV script | a continuous background task worker | a high-throughput server endpoint | a secure user checkout workflow

````text
Analyze and debug [BUG_CLASS] occurring in [COMPONENT]. Provide the diagnostics checklist, tools, sample buggy code, and the optimized fix.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** debug-go-data-race-conditions-in-a-bulk-data-import-csv-script, debug-go-data-race-conditions-in-a-continuous-background-task-worker, debug-go-data-race-conditions-in-a-high-throughput-server-endpoint, debug-java-multithreaded-deadlocks-in-a-secure-user-checkout-workflow, debug-nodejs-event-loop-blocks-in-a-bulk-data-import-csv-script, debug-python-pandas-memory-usage-in-a-bulk-data-import-csv-script, debug-react-memory-leaks-in-a-high-throughput-server-endpoint, debug-slow-postgresql-join-queries-in-a-bulk-data-import-csv-script

