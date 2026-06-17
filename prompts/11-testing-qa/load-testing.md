---
title: "Write Load Tests"
category: testing-qa
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [load-testing, k6, performance, qa]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
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
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
