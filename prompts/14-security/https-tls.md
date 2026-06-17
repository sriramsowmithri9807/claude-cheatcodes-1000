---
title: "Configure HTTPS and TLS Perfectly"
category: security
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [https, tls, ssl, security]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Configure HTTPS and TLS to achieve an A+ security rating.

Server: [Nginx / Apache / Caddy / Cloud load balancer]

1. **Minimum TLS version**: TLS 1.2 (disable 1.0, 1.1)
2. **Cipher suites**: prefer ECDHE for forward secrecy
   - TLS_AES_128_GCM_SHA256 (TLS 1.3)
   - ECDHE-RSA-AES128-GCM-SHA256 (TLS 1.2)
3. **ECDH curve**: use `X25519` and `P-256`
4. **DH parameters**: `ssl_dhparam /etc/nginx/dhparam.pem` (2048-bit min)
5. **HSTS**: max-age=63072000; includeSubDomains; preload
6. **OCSP stapling**: `ssl_stapling on` — reduce handshake latency
7. **Session tickets**: disable for perfect forward secrecy (`ssl_session_tickets off`)
8. **HTTP/2**: enable for performance
9. **Certificate**: Let's Encrypt (auto-renewing via Certbot)
10. **Certificate transparency**: monitor via CertSpotter

Test: `testssl.sh` or SSL Labs (target: A+).
Output: complete Nginx SSL config.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
