---
title: "Prevent Cross-Site Scripting (XSS)"
category: security
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [xss, security, web, input-validation]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Prevent XSS vulnerabilities in my web application.

Code with potential XSS:
```javascript
[PASTE YOUR FRONTEND/BACKEND CODE]
```

1. **Reflected XSS**: input → page without sanitization
2. **Stored XSS**: malicious content saved and displayed later
3. **DOM-based XSS**: client-side DOM manipulation with user input
4. **Fixes**:
   - React: JSX escapes by default (dangerouslySetInnerHTML is the danger)
   - HTML: use textContent not innerHTML
   - Backend: escape output with DOMPurify or equivalent
5. **Content Security Policy**: strict CSP to block inline scripts
6. **Input validation**: allow-list approach
7. **HTTPOnly cookies**: protect session cookies
8. **Trusted Types API**: browser-level XSS prevention

For my code: identify all XSS vectors and fix each one.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
