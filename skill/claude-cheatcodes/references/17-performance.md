# 17-performance

Profiling and optimisation: web vitals, bundles, caching, DB queries, memory, Node/Go/Python runtime.

17 prompts. Search `## ` headings or ids; see index.md for the one-line list.

## Optimize API Performance

**id:** `17-performance/api-performance` · **Difficulty:** advanced · **Tags:** api, performance, caching, optimization

**Placeholders:** [DESCRIBE], [TARGET LATENCY]

````text
Optimize my API's performance.

API: [DESCRIBE]
Current latency: [p50, p95, p99]
Target: [TARGET LATENCY]

Profiling:
1. **Add timing headers**: X-Response-Time per request
2. **Distributed tracing**: OpenTelemetry to find bottlenecks
3. **Database monitoring**: pg_stat_statements for slow queries

Optimizations:
4. **N+1 queries**: DataLoader or eager loading
5. **Redis caching**: cache expensive DB queries (1s → 1ms)
6. **Database indexes**: for every WHERE and JOIN condition
7. **Streaming responses**: start sending before all data is ready
8. **Pagination**: limit result sets
9. **Field selection**: GraphQL or ?fields= parameter
10. **Compression**: gzip/brotli (80% size reduction for JSON)
11. **Connection pooling**: PgBouncer, Redis client pooling
12. **Async work**: move non-critical work to a queue

Infrastructure:
13. **CDN caching**: cache GET responses at edge
14. **Horizontal scaling**: more instances behind load balancer

Output: optimized code for my slowest endpoints.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Optimize JavaScript Bundle Size

**id:** `17-performance/bundle-optimization` · **Difficulty:** advanced · **Tags:** bundle, webpack, vite, performance

**Placeholders:** [DESCRIBE]

````text
Optimize my JavaScript bundle size.

Current bundle size: [DESCRIBE]
Build tool: [Webpack / Vite / Next.js]

Analysis:
1. **Bundle analyzer**: `webpack-bundle-analyzer` or `rollup-plugin-visualizer`
2. Identify: large libraries, duplicates, unused code

Optimizations:
3. **Code splitting**: dynamic `import()` for route-level splitting
4. **Tree shaking**: ensure proper ES modules (not CommonJS)
5. **Replace large libraries**:
   - moment.js → date-fns (tree-shakeable)
   - lodash → lodash-es or just use native JS
6. **Lazy load**: non-critical components with React.lazy()
7. **Image optimization**: WebP, AVIF, responsive srcset
8. **Font subsetting**: only include characters you use
9. **Third-party scripts**: load async, defer non-critical
10. **Source maps**: production source maps sent to Sentry, not end user

Target: < 100KB main bundle (gzipped), < 200KB per route chunk.
Output: specific changes for my bundle.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement Aggressive Caching for Performance

**id:** `17-performance/caching-performance` · **Difficulty:** advanced · **Tags:** caching, cdn, performance, http

**Placeholders:** [DESCRIBE YOUR ASSETS AND API RESPONSES]

````text
Implement aggressive caching to improve performance.

Assets to cache: [DESCRIBE YOUR ASSETS AND API RESPONSES]

HTTP caching strategy:
1. **Immutable assets** (hashed filenames): `Cache-Control: public, max-age=31536000, immutable`
2. **Static HTML**: `Cache-Control: no-cache` (revalidate always)
3. **API responses** (public): `Cache-Control: public, max-age=60, s-maxage=300`
4. **User-specific API**: `Cache-Control: private, max-age=30`
5. **ETags**: conditional GET (304 Not Modified)

Service Worker caching:
6. Cache-first for static assets
7. Network-first for API calls
8. Stale-while-revalidate for non-critical
9. Offline fallback page

CDN strategy:
10. Push static assets to CDN on deploy
11. CDN API cache with purge on data change
12. Edge functions for dynamic caching logic

Redis caching:
13. Cache expensive DB queries
14. Cache third-party API responses

Output: caching strategy implementation.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Set Up CDN for Maximum Performance

**id:** `17-performance/cdn-setup` · **Difficulty:** intermediate · **Tags:** cdn, cloudflare, performance, assets

**Placeholders:** [DESCRIBE]

````text
Set up and configure a CDN for maximum performance.

App: [DESCRIBE]
CDN options: Cloudflare (recommended) / CloudFront / Fastly

**Cloudflare setup**:
1. Add site to Cloudflare
2. Change DNS nameservers
3. Enable proxy (orange cloud) on A/CNAME records
4. SSL mode: Full (Strict) — encrypt everywhere
5. HTTPS upgrade: always redirect HTTP → HTTPS

**Performance rules**:
6. Cache static assets: CSS/JS/images (1 year)
7. Cache API responses: GET endpoints < 60s
8. Minify: HTML, CSS, JavaScript
9. Brotli compression: smaller than gzip
10. HTTP/2 + HTTP/3: enable both
11. Early hints: preconnect to origins

**Cache purging**:
12. Purge on deploy: `cloudflare.purgeCache()` in deploy script
13. Cache tags: purge specific content by tag

**Analytics**:
14. Real User Monitoring in Cloudflare dashboard
15. Cache hit rate target: > 80%

Output: Cloudflare configuration + deploy script.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Optimize Database Performance

**id:** `17-performance/database-performance` · **Difficulty:** advanced · **Tags:** database, postgresql, performance, indexes

**Placeholders:** [PASTE QUERIES OR DESCRIBE], [ROWS, RPS, LATENCY]

````text
Optimize database performance for my application.

Database: PostgreSQL
Slow queries: [PASTE QUERIES OR DESCRIBE]
Current scale: [ROWS, RPS, LATENCY]

Query optimization:
1. **EXPLAIN ANALYZE**: read and understand the plan
2. **Seq scan → Index scan**: add the right index
3. **Composite indexes**: order matters (equality first, range last)
4. **Partial indexes**: index WHERE condition reduces size
5. **Covering indexes**: INCLUDE columns to avoid heap access
6. **N+1**: eliminate with JOIN or DataLoader

Schema optimization:
7. **VACUUM ANALYZE**: update statistics for planner
8. **Table bloat**: find and fix bloated tables
9. **Index bloat**: rebuild bloated indexes (REINDEX CONCURRENTLY)
10. **Partitioning**: for very large tables

Configuration:
11. **shared_buffers**: 25% of RAM
12. **work_mem**: per-sort allocation
13. **Connection pooling**: PgBouncer

Monitoring:
14. pg_stat_statements: find slowest queries
15. pg_activity: see what's running now

Output: optimized queries + index strategy.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Frontend Performance Checklist

**id:** `17-performance/frontend-performance-checklist` · **Difficulty:** intermediate · **Tags:** performance, frontend, checklist, web

**Placeholders:** [DESCRIBE YOUR APP]

````text
Apply the complete frontend performance checklist to my web app.

App URL or description: [DESCRIBE YOUR APP]

**Loading performance**:
□ LCP < 2.5 seconds
□ TTFB < 200ms (server response)
□ FCP < 1.8 seconds (first content visible)
□ Total blocking time < 200ms
□ JavaScript bundle < 100KB gzipped (main)
□ CSS < 30KB gzipped
□ No render-blocking scripts in <head>
□ Images in WebP/AVIF format
□ Images have width + height attributes
□ LCP image preloaded
□ Fonts use `font-display: swap`
□ Fonts subsetted to characters used
□ Third-party scripts loaded async/defer
□ HTTP/2 enabled
□ Gzip/Brotli compression enabled
□ CDN for static assets

**Runtime performance**:
□ No layout thrashing (batch reads before writes)
□ List virtualization for 100+ item lists
□ `will-change` only for actual animations
□ CSS animations use transform/opacity only
□ Event listeners removed when not needed

For each failing item: how to fix it.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Optimize Images for Web

**id:** `17-performance/image-optimization` · **Difficulty:** intermediate · **Tags:** images, webp, performance, cdn

**Placeholders:** [DESCRIBE: image formats, sizes, how they're served]

````text
Optimize all images in my web application.

Current state: [DESCRIBE: image formats, sizes, how they're served]

1. **Format selection**:
   - Photos: WebP (30-35% smaller than JPEG) or AVIF (50% smaller)
   - Graphics: SVG (infinitely scalable) or WebP-lossless
   - Animations: WebP animation or AVIF animation (not GIF)
2. **Responsive images**: `srcset` + `sizes` for different viewports
3. **Lazy loading**: `loading='lazy'` for below-fold images
4. **Dimensions**: always specify width + height to prevent CLS
5. **Priority loading**: `fetchpriority='high'` for LCP image
6. **Compression**: 85% quality for WebP (imperceptible quality loss)
7. **CDN delivery**: Cloudflare Images, Cloudinary, or imgproxy
8. **Preload**: `<link rel='preload'>` for critical above-fold images
9. **Sprite sheets**: for many small icons
10. **Blur-up placeholder**: low-res placeholder → full image

Next.js: use `<Image>` component (handles all of the above automatically).
Output: specific optimizations for my images.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement High-Performance Infinite Scroll

**id:** `17-performance/infinite-scroll` · **Difficulty:** intermediate · **Tags:** infinite-scroll, performance, react, virtual

**Placeholders:** [DESCRIBE: posts, products, messages, etc.], [MAX ITEMS]

````text
Implement high-performance infinite scroll.

Data: [DESCRIBE: posts, products, messages, etc.]
Expected list size: [MAX ITEMS]

**Naive infinite scroll problems**:
- DOM grows unboundedly (thousands of nodes → slow render)
- Memory leak from non-virtualized list

**Solution: Virtual list**:
1. Only render visible items (+ a small buffer)
2. Use TanStack Virtual (React) or react-window

Implementation:
3. **TanStack Query infinite query**: `useInfiniteQuery`
4. **Intersection Observer**: detect when user reaches bottom
5. **TanStack Virtual**: virtualize the list items
6. **Loading states**: spinner at bottom, skeleton items
7. **Error recovery**: retry button on load failure
8. **Scroll restoration**: preserve scroll position on back-navigate
9. **Performance**: `memo` on list items, stable key
10. **Accessibility**: announce new items to screen reader

Output: complete infinite scroll component.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Optimize Memory Usage

**id:** `17-performance/memory-optimization` · **Difficulty:** advanced · **Tags:** memory, performance, node-js, optimization

**Placeholders:** [DESCRIBE], [MEMORY GROWTH, OOM CRASHES, HIGH RSS]

````text
Optimize memory usage in my application.

App: [DESCRIBE]
Symptoms: [MEMORY GROWTH, OOM CRASHES, HIGH RSS]

**Profiling Node.js**:
1. `process.memoryUsage()`: baseline RSS, heapUsed, external
2. `--inspect` + Chrome DevTools: heap snapshot comparison
3. `clinic.js bubble`: visualize memory over time
4. `heapdump`: capture heap snapshot

**Common memory leaks to fix**:
5. **Event listeners**: always call `removeEventListener`
6. **Closures**: check what's captured in long-lived closures
7. **Global variables**: accidentally accumulated in modules
8. **Cache without eviction**: LRU cache with max size
9. **Unresolved promises**: pending promises hold references
10. **Circular references**: prevent GC (in older V8)
11. **Timer references**: always call `clearInterval`

**Optimization techniques**:
12. Stream large files (don't buffer all in memory)
13. Worker threads: isolate memory-intensive work
14. Process limits: `--max-old-space-size=512`

Output: memory leak fixes for my specific case.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Monitor Performance in Production

**id:** `17-performance/performance-monitoring` · **Difficulty:** advanced · **Tags:** performance, monitoring, rum, web-vitals

````text
Monitor application performance in production.

**Real User Monitoring (RUM)**:
1. Web Vitals reporting: send LCP, FID, CLS to your analytics
   ```javascript
   import { onLCP, onFID, onCLS } from 'web-vitals';
   onLCP(metric => sendToAnalytics(metric));
   ```
2. Segment by: browser, device type, country, page
3. P75 threshold: Googlescores at 75th percentile
4. Tools: Vercel Analytics, Datadog RUM, New Relic, Cloudflare Analytics

**Synthetic monitoring**:
5. Lighthouse CI: run Lighthouse on every deploy
6. WebPageTest: deep analysis from multiple locations
7. Pingdom: uptime + performance from multiple regions

**Backend monitoring**:
8. Response time percentiles per endpoint
9. Error rate per endpoint
10. Database query duration distribution
11. Cache hit rate

**Alerting**:
12. LCP degrades > 500ms from baseline
13. p95 API latency > 500ms
14. Error rate > 1%

Output: monitoring setup + alerting config.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Optimize React Application Performance

**id:** `17-performance/react-performance` · **Difficulty:** advanced · **Tags:** react, performance, memoization, rendering

**Placeholders:** [DESCRIBE: slow renders, janky animations, high memory usage], [DESCRIBE]

````text
Optimize my React application's rendering performance.

App: [DESCRIBE]
Symptoms: [DESCRIBE: slow renders, janky animations, high memory usage]

**Profiling**:
1. React DevTools Profiler: find expensive renders
2. Chrome Performance tab: find long tasks
3. Why-did-you-render: log unnecessary re-renders

**Memoization**:
4. `React.memo()`: prevent re-render if props unchanged
5. `useMemo()`: expensive computations
6. `useCallback()`: stable function references
7. When NOT to memoize: premature optimization

**State management**:
8. Colocate state: don't lift state higher than needed
9. Split contexts: separate frequently-changing state
10. Zustand selectors: re-render only on relevant state change

**Lists**:
11. Virtual lists: TanStack Virtual for large lists
12. Stable keys: avoid index-as-key when order changes

**Data fetching**:
13. TanStack Query: background refresh, no loading flash
14. Suspense: progressive loading

Output: specific optimizations for my app with measurements.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Optimize Node.js Server Performance

**id:** `17-performance/server-performance` · **Difficulty:** advanced · **Tags:** node-js, performance, express, server

**Placeholders:** [DESCRIBE], [RPS, LATENCY]

````text
Optimize my Node.js server performance.

Server: Express.js / Fastify
Current performance: [DESCRIBE]
Target: [RPS, LATENCY]

**Event loop optimization**:
1. Avoid blocking: no sync filesystem, crypto, or parsing in request handlers
2. `setImmediate` vs `process.nextTick` — know the difference
3. Worker threads for CPU-intensive work
4. Async I/O: always use async versions of fs, crypto

**Fastify over Express** (2-5x faster):
5. JSON serialization with schemas (avoids JSON.stringify overhead)
6. Hooks: lifecycle hooks instead of middleware chain

**Clustering**:
7. `node:cluster` or PM2: use all CPU cores
8. N workers = N CPU cores

**HTTP optimizations**:
9. Keep-alive connections
10. Response compression: `compression` middleware
11. HTTP/2 push for critical assets

**Profiling tools**:
12. `clinic.js flame`: find CPU bottlenecks
13. `autocannon`: HTTP benchmark
14. `0x`: flame graph from Node.js

Output: performance optimizations for my server.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Write High-Performance SQL Queries

**id:** `17-performance/sql-query-performance` · **Difficulty:** advanced · **Tags:** sql, performance, postgresql, optimization

**Placeholders:** [PASTE SLOW QUERIES], [PASTE YOUR TABLES]

````text
Write high-performance SQL queries for my use case.

Schema: [PASTE YOUR TABLES]
Queries to optimize: [PASTE SLOW QUERIES]

Query writing principles:
1. **SELECT specific columns**: avoid SELECT *
2. **Filter early**: WHERE before GROUP BY
3. **EXISTS vs IN**: EXISTS is often faster for subqueries
4. **Avoid functions on indexed columns**: `WHERE LOWER(email) =` prevents index use
5. **Batch inserts**: INSERT with multiple value rows
6. **RETURNING**: get inserted row without second query
7. **CTEs**: improve readability (materialized in PostgreSQL 12+)
8. **Window functions**: avoid self-joins for running totals
9. **LATERAL joins**: for per-row subqueries
10. **DISTINCT vs GROUP BY**: GROUP BY often more optimizable
11. **LIMIT early**: push limit into subqueries
12. **Index-only scans**: covering index eliminates table access

For my specific queries:
- EXPLAIN ANALYZE interpretation
- Rewritten optimized version
- Index to create

Output: optimized queries + index strategy.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Optimize Web Application Performance

**id:** `17-performance/web-performance` · **Difficulty:** advanced · **Tags:** web-performance, lighthouse, optimization, frontend

**Placeholders:** [DESCRIBE YOUR APP AND CURRENT SCORES]

````text
Optimize my web application's performance to achieve Core Web Vitals targets.

App: [DESCRIBE YOUR APP AND CURRENT SCORES]
Targets: LCP < 2.5s, FID < 100ms, CLS < 0.1, INP < 200ms

**LCP optimization** (Largest Contentful Paint):
1. Preload LCP image: `<link rel='preload' as='image'>`
2. Server-push or preconnect to image server
3. Optimize image: WebP, correct size, lazy load below-fold
4. Eliminate render-blocking resources
5. Server response time < 200ms (TTFB)

**INP optimization** (Interaction to Next Paint):
6. Move heavy work off main thread (Web Workers)
7. Break up long tasks (> 50ms) with `setTimeout(fn, 0)`
8. Use `startTransition` for non-urgent state updates (React)

**CLS optimization** (Cumulative Layout Shift):
9. Always define width/height on images and videos
10. Font loading: `font-display: swap` or subset fonts
11. Reserve space for ads and embeds

Output: Lighthouse audit + specific fixes.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Use Web Workers for Performance

**id:** `17-performance/web-workers` · **Difficulty:** advanced · **Tags:** web-workers, performance, javascript, concurrency

**Placeholders:** [DESCRIBE: data processing, parsing, encryption, image manipulation]

````text
Use Web Workers to move heavy computation off the main thread.

Heavy operations: [DESCRIBE: data processing, parsing, encryption, image manipulation]

1. **When to use Web Workers**:
   - JS > 50ms → user feels janky
   - Data processing, parsing large JSON
   - Image/video processing
   - Crypto operations
   - Compression/decompression

2. **Basic Worker setup**:
   ```javascript
   const worker = new Worker(new URL('./worker.ts', import.meta.url));
   worker.postMessage({ data });
   worker.onmessage = (e) => setResult(e.data);
   ```

3. **Comlink**: simplify worker communication
   - Call worker functions like async functions

4. **Transferable objects**: zero-copy for ArrayBuffers

5. **Worker thread pool**: reuse workers (don't create/destroy)

6. **React integration**: `useWorker` hook

7. **Vite/webpack**: import worker with `?worker` suffix

8. **Testing**: jsdom doesn't support workers → mock in tests

Output: Web Worker implementation for my heavy operation.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Optimize [BOTTLENECK] on production using [TECHNIQUE]

**id:** `17-performance/optimize-bottleneck-on-production-using-technique` · **Difficulty:** beginner/intermediate/advanced · **Tags:** tuning, browser, latency, performance, component, optimization, profiling, caching, dynamic, gzip/brotli, large, node.js, python, slow

**Variant group** (21 generated prompts collapsed). Pick one value per placeholder:
- `[BOTTLENECK]`: Go garbage collection overheads | Node.js event loop lag | Python high memory spikes | browser CSS reflow limits | large React production build sizes | slow PostgreSQL indexing queries
- `[TECHNIQUE]`: caching assets headers | component lazy loading techniques | dynamic code splitting imports | gzip/brotli code compression | profiling memory heap allocations
- `[GOAL]`: faster time to interactive (TTI) | higher Google Lighthouse scores | lowered server RAM foot prints | sub-100ms TTFB stats

````text
Write a step-by-step optimization playbook to resolve [BOTTLENECK] in your code. Implement [TECHNIQUE] to achieve [GOAL].
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** optimize-browser-css-reflow-limits-on-production, optimize-browser-css-reflow-limits-on-production-using-component-lazy-loading-techniques, optimize-browser-css-reflow-limits-on-production-using-profiling-memory-heap-allocations, optimize-go-garbage-collection-overheads-on-production, optimize-go-garbage-collection-overheads-on-production-using-component-lazy-loading-techniques, optimize-go-garbage-collection-overheads-on-production-using-dynamic-code-splitting-imports, optimize-go-garbage-collection-overheads-on-production-using-gzipbrotli-code-compression, optimize-large-react-production-build-sizes-on-production, optimize-large-react-production-build-sizes-on-production-using-caching-assets-headers, optimize-large-react-production-build-sizes-on-production-using-profiling-memory-heap-allocations, optimize-nodejs-event-loop-lag-on-production, optimize-nodejs-event-loop-lag-on-production-using-caching-assets-headers, optimize-nodejs-event-loop-lag-on-production-using-dynamic-code-splitting-imports, optimize-nodejs-event-loop-lag-on-production-using-profiling-memory-heap-allocations, optimize-python-high-memory-spikes-on-production, optimize-python-high-memory-spikes-on-production-using-component-lazy-loading-techniques, optimize-python-high-memory-spikes-on-production-using-gzipbrotli-code-compression, optimize-slow-postgresql-indexing-queries-on-production, optimize-slow-postgresql-indexing-queries-on-production-using-caching-assets-headers, optimize-slow-postgresql-indexing-queries-on-production-using-gzipbrotli-code-compression, optimize-slow-postgresql-indexing-queries-on-production-using-profiling-memory-heap-allocations


## Troubleshoot performance bottleneck caused by [BOTTLENECK] with [GOAL]

**id:** `17-performance/troubleshoot-performance-bottleneck-caused-by-bottleneck-with-goal` · **Difficulty:** beginner/intermediate/advanced · **Tags:** tuning, browser, latency, performance, component, optimization, caching, large, gzip/brotli, node.js, dynamic, python, slow, profiling

**Variant group** (14 generated prompts collapsed). Pick one value per placeholder:
- `[BOTTLENECK]`: Go garbage collection overheads | Node.js event loop lag | Python high memory spikes | browser CSS reflow limits | large React production build sizes | slow PostgreSQL indexing queries
- `[TECHNIQUE]`: caching assets headers | component lazy loading techniques | dynamic code splitting imports | gzip/brotli code compression | profiling memory heap allocations

````text
Analyze why [BOTTLENECK] occurs in high-traffic applications. Provide code refactoring guidelines and use [TECHNIQUE] to resolve the issue.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** troubleshoot-performance-bottleneck-caused-by-browser-css-reflow-limits, troubleshoot-performance-bottleneck-caused-by-browser-css-reflow-limits-with-higher-google-lighthouse-scores, troubleshoot-performance-bottleneck-caused-by-go-garbage-collection-overheads, troubleshoot-performance-bottleneck-caused-by-go-garbage-collection-overheads-with-sub-100ms-ttfb-stats, troubleshoot-performance-bottleneck-caused-by-large-react-production-build-sizes, troubleshoot-performance-bottleneck-caused-by-large-react-production-build-sizes-with-sub-100ms-ttfb-stats, troubleshoot-performance-bottleneck-caused-by-nodejs-event-loop-lag, troubleshoot-performance-bottleneck-caused-by-nodejs-event-loop-lag-with-faster-time-to-interactive-tti, troubleshoot-performance-bottleneck-caused-by-nodejs-event-loop-lag-with-sub-100ms-ttfb-stats, troubleshoot-performance-bottleneck-caused-by-python-high-memory-spikes, troubleshoot-performance-bottleneck-caused-by-python-high-memory-spikes-with-faster-time-to-interactive-tti, troubleshoot-performance-bottleneck-caused-by-slow-postgresql-indexing-queries, troubleshoot-performance-bottleneck-caused-by-slow-postgresql-indexing-queries-with-faster-time-to-interactive-tti, troubleshoot-performance-bottleneck-caused-by-slow-postgresql-indexing-queries-with-higher-google-lighthouse-scores

