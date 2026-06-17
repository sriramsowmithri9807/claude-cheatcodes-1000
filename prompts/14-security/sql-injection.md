---
title: "Prevent SQL Injection"
category: security
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [sql-injection, security, postgresql, parameterized]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Audit and prevent SQL injection in my application.

Database layer code:
```[LANGUAGE]
[PASTE YOUR DATABASE QUERY CODE]
```

1. **Find all vulnerable queries**: string concatenation in SQL
2. **Parameterized queries**: the correct fix
3. **ORM safety**: how Prisma/Drizzle protect you (and where they don't)
4. **Stored procedures**: are they safe?
5. **Dynamic table/column names**: special cases where params don't work
6. **Blind SQL injection**: time-based, boolean-based
7. **Error messages**: never show DB errors to users
8. **Least privilege**: DB user has only SELECT/INSERT/UPDATE (not DROP)
9. **Testing**: sqlmap for automated injection testing
10. **WAF**: last line of defense

Fix all vulnerabilities in my code with parameterized equivalents.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
