---
title: "Implement Security Logging and Monitoring"
category: security
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [security, logging, monitoring, siem]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Implement security logging and monitoring for my application.

**What to log** (security events):
1. Authentication: login success/fail, logout, token refresh
2. Authorization: access denied events
3. Account changes: password change, email change, role change
4. Sensitive data access: who accessed what and when
5. Admin actions: all admin panel operations
6. Rate limit exceeded: potential brute force
7. Input validation failures: potential injection attempts
8. System events: service starts/stops, config changes

**Log format**:
9. Structured JSON: timestamp, user_id, ip, action, resource, result, session_id
10. NEVER log: passwords, tokens, card numbers, PII (or mask them)

**Monitoring and alerting**:
11. Alert: > 10 failed logins from same IP in 5 min
12. Alert: admin action outside business hours
13. Alert: bulk data export
14. SIEM: ship to Splunk / ELK / Datadog

Output: security event logger + alert rules.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
