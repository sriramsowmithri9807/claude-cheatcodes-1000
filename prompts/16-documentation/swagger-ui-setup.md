---
title: "Set Up Swagger UI for API Docs"
category: documentation
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [swagger, openapi, documentation, api]
difficulty: intermediate
author: community
tested: true
---

## 🎯 Prompt

```
Set up interactive API documentation with Swagger UI.

API: [DESCRIBE YOUR EXPRESS/FASTAPI/OTHER API]

**Option A — Express.js**:
1. Install: `swagger-jsdoc`, `swagger-ui-express`
2. JSDoc annotations on each route:
```javascript
/**
 * @swagger
 * /users/{id}:
 *   get:
 *     summary: Get user by ID
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: string
 *     responses:
 *       200:
 *         description: User object
 *         content:
 *           application/json:
 *             schema:
 *               $ref: '#/components/schemas/User'
 */
```
3. Serve UI at `/api-docs`

**Option B — Separate OpenAPI file**:
4. Write `openapi.yaml` manually or generate
5. Serve with Swagger UI standalone

**Best practices**:
6. Examples for every request/response
7. Error responses documented
8. Authentication setup in the UI
9. Protect docs endpoint in production

Output: complete Swagger UI setup.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
