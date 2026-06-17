---
title: "Write Production Nginx Configuration"
category: devops-cicd
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [nginx, web-server, reverse-proxy, ssl]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Write a production-ready Nginx configuration for my app.

Setup:
- Nginx as reverse proxy in front of [Node.js / Python / other] app
- SSL/TLS with Let's Encrypt
- Multiple domains: [LIST YOUR DOMAINS]

Configuration:
1. HTTPS redirect (HTTP → HTTPS)
2. TLS 1.2 / 1.3 only, strong cipher suites
3. HSTS header with preload
4. Security headers (see OWASP recommendations)
5. Gzip compression for text assets
6. Proxy to upstream with timeouts
7. WebSocket support (Upgrade/Connection headers)
8. Rate limiting: limit_req_zone
9. Static file serving with long cache headers
10. Health check endpoint passthrough
11. Access log format (structured for log analysis)
12. Worker processes = auto, worker_connections = 1024
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
