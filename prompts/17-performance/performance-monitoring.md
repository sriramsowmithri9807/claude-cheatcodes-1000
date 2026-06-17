---
title: "Monitor Performance in Production"
category: performance
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [performance, monitoring, rum, web-vitals]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
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
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
