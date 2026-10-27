# 14-security

OWASP hardening, auth security, XSS/CSRF/SQLi defenses, secrets, encryption, audits, threat models.

28 prompts. Search `## ` headings or ids; see index.md for the one-line list.

## Implement API Key Management

**id:** `14-security/api-key-management` · **Difficulty:** intermediate · **Tags:** api-keys, security, authentication, backend

**Placeholders:** [DESCRIBE], [DEVELOPERS / INTERNAL SERVICES]

````text
Implement a secure API key management system.

My API: [DESCRIBE]
Key consumers: [DEVELOPERS / INTERNAL SERVICES]

1. **Key generation**: cryptographically random, 32 bytes, base64-encoded
2. **Key format**: prefix for identification (e.g., `sk_live_` or `key_`)
3. **Storage**: store HASH of key (not plaintext), using SHA-256
4. **First display**: show key only once after creation, then never again
5. **Key scopes**: read-only, write, admin — principle of least privilege
6. **Expiration**: optional expiry date
7. **Rate limiting**: per-key rate limits
8. **Usage tracking**: log every request with key ID (not full key)
9. **Key rotation**: create new → test → revoke old
10. **Revocation**: instant revocation, check blocklist in auth middleware
11. **Multi-key**: users can have multiple keys (dev vs production)
12. **Dashboard**: users view/manage/revoke their own keys

Output: complete implementation with all endpoints.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Secure REST APIs

**id:** `14-security/api-security` · **Difficulty:** advanced · **Tags:** api, security, auth, rest

**Placeholders:** [DESCRIBE]

````text
Implement comprehensive security for my REST API.

API: [DESCRIBE]

**Authentication**:
1. JWT with RS256 (not HS256)
2. Short expiry access tokens (15 min)
3. Secure refresh token rotation

**Authorization**:
4. Check on every endpoint (not just middleware)
5. Resource ownership check (IDOR prevention)
6. Role validation for admin operations

**Input validation**:
7. Validate all inputs with Zod
8. Sanitize strings (trim, max length)
9. Validate file uploads (type, size, magic bytes)

**Output security**:
10. Never expose internal IDs if sequential (use UUID)
11. Filter response fields (don't return password hash)
12. Rate limiting per endpoint

**Infrastructure**:
13. HTTPS only (HSTS header)
14. Security headers (Helmet.js)
15. Request logging for audit
16. Secrets in environment variables

Output: security middleware stack for Express.js.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Secure Container Deployments

**id:** `14-security/container-security` · **Difficulty:** advanced · **Tags:** docker, security, containers, kubernetes

````text
Secure my container deployment.

**Docker security**:
1. Non-root user in container
2. Read-only filesystem: `--read-only`
3. No privileged mode: never `--privileged`
4. Dropped capabilities: `--cap-drop ALL --cap-add NET_BIND_SERVICE`
5. Resource limits: `--memory 512m --cpus 0.5`
6. No host network: use Docker networks
7. Secrets: Docker secrets, not ENV vars in Dockerfile

**Image security**:
8. Minimal base image: distroless or alpine
9. Multi-stage build: no build tools in final image
10. Image scanning: Trivy in CI (fail on CRITICAL)
11. Signed images: cosign for supply chain security

**Kubernetes security**:
12. PodSecurityContext: `runAsNonRoot: true`
13. SecurityContext: `readOnlyRootFilesystem: true`
14. NetworkPolicy: default deny, explicit allow
15. RBAC: least-privilege ServiceAccount per pod
16. Secrets: External Secrets Operator (don't store in etcd)

Output: secure Dockerfile + Kubernetes security config.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Configure CORS Correctly

**id:** `14-security/cors-configuration` · **Difficulty:** intermediate · **Tags:** cors, security, web, api

````text
Configure CORS (Cross-Origin Resource Sharing) correctly for my API.

My origins:
- Production frontend: https://myapp.com
- Staging: https://staging.myapp.com
- Development: http://localhost:3000

Node.js/Express setup:
1. Allow specific origins (NOT `*` for authenticated endpoints)
2. Allow specific methods: GET, POST, PUT, PATCH, DELETE
3. Allow specific headers: Content-Type, Authorization
4. `credentials: true` for cookies (requires specific origin, not *)
5. Preflight caching: `maxAge: 86400` (24h cache for OPTIONS requests)
6. Error response for rejected origins

Config:
7. Different origins per environment (env variable)
8. Dynamic origin validation (regex for subdomains)

Common mistakes:
9. Using `*` with `credentials: true` (doesn't work, AND is insecure)
10. Forgetting preflight: OPTIONS requests must also pass CORS

Output: complete CORS configuration for Express + Nginx.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement CSRF Protection

**id:** `14-security/csrf-protection` · **Difficulty:** intermediate · **Tags:** csrf, security, web, tokens

**Placeholders:** [DESCRIBE YOUR AUTHENTICATION METHOD]

````text
Implement CSRF (Cross-Site Request Forgery) protection.

App: [DESCRIBE YOUR AUTHENTICATION METHOD]

1. **What is CSRF**: malicious site makes authenticated requests on behalf of user
2. **When you're vulnerable**: session cookies, no Origin/Referer check
3. **SameSite cookies**: `SameSite=Lax` or `Strict` — primary defense
4. **CSRF token**: synchronizer token pattern
   - Generate per-session random token
   - Include in every form as hidden field
   - Validate on backend
5. **Double submit cookie**: stateless CSRF prevention
6. **Origin/Referer check**: server validates request origin
7. **Custom header**: `X-Requested-With` for AJAX requests
8. **Framework built-in**: Express CSRF middleware, Django CSRF, Rails authenticity token
9. **SPA/JWT**: cookie-less → no CSRF risk
10. **Testing**: use Burp Suite to verify protection

Implement CSRF protection for my specific setup.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Audit and Secure Dependencies

**id:** `14-security/dependency-security` · **Difficulty:** intermediate · **Tags:** dependencies, security, supply-chain, npm

````text
Audit and secure my application's dependencies.

Package manager: [npm / yarn / pnpm / pip / go mod]

Vulnerability scanning:
1. `npm audit` — find known vulnerabilities
2. Snyk: `snyk test` — more comprehensive scan
3. GitHub Dependabot: automated PRs for security updates
4. OWASP Dependency-Check: for Java/Python

Fix strategy:
5. Critical: update immediately
6. High: update within 1 week
7. Medium: update within 1 month
8. Low: add to tech debt backlog

Prevention:
9. `npm audit` in CI — fail build on high+ severity
10. Renovate bot: auto-update minor/patch versions
11. Lock files: commit `package-lock.json`
12. Pin exact versions for security-critical packages

Supply chain:
13. Only use packages with active maintainers
14. Verify package signatures (npm provenance)
15. Prefer `--ignore-scripts` for untrusted packages

Output: audit results + remediation plan.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement Data Encryption

**id:** `14-security/encryption-implementation` · **Difficulty:** advanced · **Tags:** encryption, security, crypto, data-protection

**Placeholders:** [LIST: PII, health data, financial, etc.]

````text
Implement encryption for sensitive data in my application.

Sensitive data to encrypt: [LIST: PII, health data, financial, etc.]

**Encryption at rest**:
1. **Disk-level**: cloud provider disk encryption (baseline, not sufficient alone)
2. **Column-level**: encrypt specific sensitive DB columns
   - AES-256-GCM (authenticated encryption)
   - Node.js: `crypto.createCipheriv`
3. **Key management**: AWS KMS or HashiCorp Vault (NEVER store key with data)
4. **Key rotation**: rotate without re-encrypting everything (envelope encryption)

**Encryption in transit**:
5. TLS 1.3 for all external communication
6. TLS for internal service communication (mTLS)
7. Certificate pinning in mobile apps

**Specific implementations**:
8. Password hashing: bcrypt (cost=12) or argon2id
9. Tokenization: replace PAN/SSN with non-sensitive token
10. Searchable encryption: how to search encrypted fields

Output: encryption implementation for my specific data.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Secure File Uploads

**id:** `14-security/file-upload-security` · **Difficulty:** advanced · **Tags:** file-upload, security, validation, malware

**Placeholders:** [DESCRIBE]

````text
Implement secure file upload handling.

File types accepted: [DESCRIBE]

**Client-side validation** (UX only, not security):
1. MIME type from file input (`accept` attribute)
2. File size check before upload
3. Preview for images

**Server-side validation** (actual security):
4. **MIME type**: read magic bytes (not extension or Content-Type header)
   - `file-type` npm package for detection
5. **Extension allow-list**: only allow specific extensions
6. **File size limit**: enforce in server/nginx
7. **Virus scanning**: ClamAV or Cloudmersive API
8. **Image reprocessing**: re-save images through Sharp to strip metadata and exploits
9. **Rename**: generate UUID filename, don't use user's filename
10. **Isolate**: serve uploads from separate domain (prevent XSS)
11. **No execution**: uploads directory outside webroot, no execute permissions
12. **Malicious SVG**: SVG can contain JavaScript — treat as code
13. **ZIP bombs**: limit extracted size
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement GDPR Compliance

**id:** `14-security/gdpr-implementation` · **Difficulty:** advanced · **Tags:** gdpr, privacy, compliance, data

**Placeholders:** [DESCRIBE], [LIST PERSONAL DATA TYPES]

````text
Implement GDPR compliance for my application.

App: [DESCRIBE]
Data processed: [LIST PERSONAL DATA TYPES]

**User rights implementation**:
1. **Right to access**: endpoint to export all user data as JSON/CSV
2. **Right to erasure**: delete account → delete all PII (or anonymize)
3. **Right to portability**: machine-readable format
4. **Right to rectification**: update any personal data
5. **Right to object**: opt out of marketing, profiling

**Consent**:
6. Cookie consent banner (necessary vs analytics vs marketing)
7. Granular consent per purpose
8. Store consent with timestamp and version
9. Easy withdrawal of consent

**Data protection**:
10. Data minimization: collect only what you need
11. Retention policy: auto-delete after X months
12. Third-party processor agreements (DPA)
13. Breach notification: 72-hour window to DPA
14. DPO: designate if required

Output: GDPR compliance checklist + implementation code for user rights.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Configure HTTPS and TLS Perfectly

**id:** `14-security/https-tls` · **Difficulty:** intermediate · **Tags:** https, tls, ssl, security

````text
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
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement Comprehensive Input Validation

**id:** `14-security/input-validation` · **Difficulty:** intermediate · **Tags:** validation, security, sanitization, web

**Placeholders:** [LIST YOUR API INPUTS]

````text
Implement comprehensive input validation for my application.

Inputs to validate: [LIST YOUR API INPUTS]

**Principles**:
1. **Allow-list**: define what IS allowed, reject everything else
2. **Server-side**: always validate on server (client validation is UX, not security)
3. **Sanitization**: sanitize for output context (HTML, SQL, shell)
4. **Length limits**: set max length for all string inputs

**Implement validation for**:
5. Email: format + MX record check
6. URLs: protocol allow-list (http/https only)
7. File uploads: MIME type (magic bytes), size, name
8. Numbers: range, type
9. Dates: valid date, reasonable range
10. Enums: only allow defined values
11. HTML content: sanitize with DOMPurify
12. JSON: schema validation before processing

Using: Zod for TypeScript, Pydantic for Python.
Output: validation schema for each of my inputs.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement Secure JWT Authentication

**id:** `14-security/jwt-security` · **Difficulty:** advanced · **Tags:** jwt, auth, security, tokens

````text
Implement JWT authentication with all security best practices.

1. **Algorithm**: use RS256 (asymmetric), NOT HS256 for distributed systems
   - Private key: sign on auth server
   - Public key: verify on resource servers
2. **Payload**: minimal claims (sub, iat, exp, jti)
   - Never put sensitive data in JWT payload (it's base64-decodable)
3. **Expiry**: access token 15 minutes, refresh token 7 days
4. **JTI**: JWT ID for replay prevention
5. **Refresh token rotation**: new refresh token on each use
6. **Token revocation**: Redis blocklist for logged-out tokens
7. **Storage**: httpOnly secure cookie (not localStorage)
8. **CSRF protection**: if using cookies
9. **Algorithm confusion attack**: explicitly verify algorithm
10. **Key rotation**: rotate signing keys without downtime

Node.js implementation with `jose` or `jsonwebtoken` library.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement OAuth 2.0 Securely

**id:** `14-security/oauth-security` · **Difficulty:** advanced · **Tags:** oauth, oidc, security, auth

````text
Implement OAuth 2.0 security best practices.

OAuth flow: Authorization Code + PKCE (for web/mobile apps)

**Authorization Code + PKCE**:
1. Generate `code_verifier`: 32 random bytes, base64url encoded
2. `code_challenge`: SHA-256 hash of code_verifier, base64url
3. Include in authorization request
4. Server verifies challenge on token exchange

**State parameter**:
5. Generate random state, store in session
6. Verify state matches on callback (prevent CSRF)

**Token handling**:
7. Access tokens: short-lived (15 min)
8. Refresh tokens: rotate on each use
9. Store in httpOnly cookies or secure storage
10. Never in localStorage

**Authorization server choices**:
11. Auth0 / Clerk / AWS Cognito (managed)
12. Keycloak (self-hosted)

**Threats to protect against**:
13. Authorization code interception (solved by PKCE)
14. Token leakage in URL (use POST for token endpoint)
15. Open redirect (validate redirect_uri strictly)
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Fix OWASP Top 10 Vulnerabilities

**id:** `14-security/owasp-top-10` · **Difficulty:** advanced · **Tags:** owasp, security, vulnerabilities, web

**Placeholders:** [DESCRIBE YOUR STACK AND WHAT IT DOES]

````text
Audit and fix OWASP Top 10 vulnerabilities in my application.

App: [DESCRIBE YOUR STACK AND WHAT IT DOES]

For each vulnerability: explain, find in my code, and fix:

1. **A01 Broken Access Control**: check every endpoint for authorization
2. **A02 Cryptographic Failures**: find plaintext storage of secrets
3. **A03 Injection**: SQL, command, LDAP injection points
4. **A04 Insecure Design**: missing rate limiting, missing business logic guards
5. **A05 Security Misconfiguration**: debug mode, default creds, exposed admin
6. **A06 Vulnerable Components**: npm audit, outdated dependencies
7. **A07 Auth Failures**: brute force, weak session management
8. **A08 Integrity Failures**: unsigned updates, deserialization
9. **A09 Logging Failures**: not logging security events
10. **A10 SSRF**: user-controlled URLs in server-side requests

For each: code example of the vulnerability + the fix + test to verify.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement Password Security Best Practices

**id:** `14-security/password-security` · **Difficulty:** intermediate · **Tags:** passwords, security, hashing, auth

````text
Implement password security best practices.

**Hashing** (NOT encryption):
1. **Algorithm**: Argon2id (preferred) or bcrypt (cost=12+)
2. **Salt**: automatic per-password (done by argon2/bcrypt library)
3. **Node.js**: `argon2` npm package
4. Never: MD5, SHA1, SHA256 for passwords (too fast)

**Password policy**:
5. Minimum 8 characters (12+ encouraged)
6. Check against HaveIBeenPwned breached password list
7. Allow spaces and all special characters
8. Don't force regular rotation (causes weaker passwords)
9. Strength meter feedback (zxcvbn library)

**Password reset**:
10. Random token, not predictable
11. Short expiry: 15 minutes
12. Single-use: invalidate after use
13. Email to registered address only
14. Rate limit: 3 reset requests per hour

**Account protection**:
15. Failed attempt lockout (with alert to user)
16. Password change → invalidate all other sessions

Output: complete password management implementation.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Perform Penetration Testing

**id:** `14-security/penetration-testing` · **Difficulty:** advanced · **Tags:** pen-testing, security, owasp-zap, burp-suite

**Placeholders:** [DESCRIBE YOUR APP], [WHAT IS IN/OUT OF SCOPE]

````text
Perform penetration testing on my web application.

App: [DESCRIBE YOUR APP]
Scope: [WHAT IS IN/OUT OF SCOPE]

**OWASP ZAP** (open source):
1. Spider: discover all URLs
2. Active scan: automated vulnerability detection
3. Manual testing: using ZAP as proxy
4. Authentication: configure to test authenticated areas
5. Report: generate HTML report

**Manual testing checklist**:
6. Authentication bypass: try accessing protected pages without login
7. IDOR: change user IDs in requests
8. Parameter tampering: modify prices, quantities, roles
9. File inclusion: path traversal in file parameters
10. XXE: XML input with entity injection
11. CORS: check what origins are allowed
12. Cookie security: httpOnly, Secure, SameSite flags

**Remediation**:
13. Prioritize by CVSS severity score
14. Fix → retest → close finding
15. Report: executive summary + technical findings

Output: pen test checklist for my specific app.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement Security Rate Limiting

**id:** `14-security/rate-limiting-security` · **Difficulty:** advanced · **Tags:** rate-limiting, security, brute-force, ddos

````text
Implement rate limiting to prevent brute force and DDoS attacks.

Endpoints to protect:
- Login: strict (5 attempts per 15 minutes per IP)
- Registration: moderate (10 per hour per IP)
- Password reset: strict (3 per hour per email)
- API: per-key limits
- Static: generous (1000/min per IP)

Implement:
1. Express rate limiting middleware (express-rate-limit)
2. Redis backend for distributed limiting
3. Sliding window algorithm
4. IP-based limiting (with proxy header handling)
5. User-based limiting (authenticated endpoints)
6. Account lockout after N failed logins
7. Exponential backoff message (don't reveal exact limit)
8. Bypass for monitoring/health checks
9. DDoS mitigation at CDN level (Cloudflare)
10. 429 response with Retry-After header

Output: complete middleware implementation.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Prevent Secrets in Source Code

**id:** `14-security/secrets-scanning` · **Difficulty:** intermediate · **Tags:** secrets, security, git, scanning

````text
Prevent and detect secrets committed to source code.

**Prevention** (pre-commit):
1. `git-secrets`: detect AWS keys, passwords before commit
2. `detect-secrets`: Yelp's pre-commit hook
3. `trufflehog`: scan git history for secrets
4. Pre-commit hook: `.husky/pre-commit` → run detection

**Detection in existing repo**:
5. `gitleaks`: scan entire git history
6. `trufflehog git`: entropy-based secret detection
7. GitHub Advanced Security: automatic secret scanning

**Remediation when secrets are found**:
8. Rotate the secret IMMEDIATELY (before fixing code)
9. Remove from git history: `git filter-repo --invert-paths --path secrets.txt`
10. Force push (coordinate with team)
11. Add `.gitignore` entry
12. Use environment variables instead

**Process**:
- `.env.example` with placeholder values (never real values)
- All secrets via environment variables
- Secrets manager for production

Output: pre-commit hook setup + scan report.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Conduct a Security Audit

**id:** `14-security/security-audit` · **Difficulty:** advanced · **Tags:** security-audit, review, checklist, security

**Placeholders:** [DESCRIBE], [WHAT'S INCLUDED]

````text
Conduct a comprehensive security audit of my application.

App: [DESCRIBE]
Audit scope: [WHAT'S INCLUDED]

**Audit checklist**:

Authentication:
□ Password hashing (bcrypt/argon2, not MD5/SHA1)
□ Brute force protection
□ MFA availability
□ Session fixation protection
□ Secure password reset

Authorization:
□ Every endpoint checks authentication
□ Every operation checks ownership (IDOR)
□ Admin functions separately protected

Data:
□ Sensitive data encrypted at rest
□ PII minimization
□ Secure deletion

Infrastructure:
□ Secrets not in code
□ HTTPS everywhere
□ Security headers set
□ Dependencies up to date

Code:
□ Input validation
□ Output encoding
□ No eval(), no innerHTML with user data

Output: findings report with severity ratings + remediation plan.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement HTTP Security Headers

**id:** `14-security/security-headers` · **Difficulty:** beginner · **Tags:** security, headers, http, web

````text
Implement all necessary HTTP security headers.

Server: [Nginx / Express / Next.js / Cloudflare]

Required headers:
1. **Content-Security-Policy**: strict policy preventing XSS
   - `default-src 'self'; script-src 'self'; ...`
   - Start with Report-Only mode, then enforce
2. **Strict-Transport-Security**: `max-age=31536000; includeSubDomains; preload`
3. **X-Content-Type-Options**: `nosniff`
4. **X-Frame-Options**: `DENY` (use CSP frame-ancestors instead for flexibility)
5. **Referrer-Policy**: `strict-origin-when-cross-origin`
6. **Permissions-Policy**: disable unused APIs: camera, microphone, geolocation
7. **Cross-Origin-Opener-Policy**: `same-origin`
8. **Cross-Origin-Resource-Policy**: `same-origin`

Remove:
9. `X-Powered-By` header (reveals stack)
10. `Server` header (reveals server software)

Test: securityheaders.com (target: A+).
Output: Nginx config / Express Helmet.js config / Next.js headers config.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement Security Logging and Monitoring

**id:** `14-security/security-logging` · **Difficulty:** advanced · **Tags:** security, logging, monitoring, siem

````text
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
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement Secure Session Management

**id:** `14-security/session-management` · **Difficulty:** advanced · **Tags:** sessions, security, auth, web

**Placeholders:** [DESCRIBE YOUR AUTH APPROACH]

````text
Implement secure session management.

App: [DESCRIBE YOUR AUTH APPROACH]

1. **Session ID generation**: `crypto.randomBytes(32)` — cryptographically random
2. **Storage**: server-side (Redis) — not stateful client-side (JWT for stateless)
3. **Cookie flags**: `httpOnly; Secure; SameSite=Lax; Path=/`
4. **Session expiry**: idle timeout (30 min) + absolute timeout (8 hours)
5. **Session fixation**: regenerate session ID on login
6. **Concurrent sessions**: detect and limit (optional)
7. **Session revocation**: ability to invalidate specific sessions
8. **Log all sessions**: device, IP, created time — show to user
9. **Logout**: invalidate server-side immediately
10. **"Remember me"**: separate long-lived token, not just longer session

Node.js with Express + `express-session` + Redis store:
11. Configuration code
12. Middleware setup
13. Login/logout handlers
14. Admin: view and terminate user sessions
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Prevent SQL Injection

**id:** `14-security/sql-injection` · **Difficulty:** intermediate · **Tags:** sql-injection, security, postgresql, parameterized

**Placeholders:** [LANGUAGE], [PASTE YOUR DATABASE QUERY CODE]

````text
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
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement Two-Factor Authentication

**id:** `14-security/two-factor-auth` · **Difficulty:** advanced · **Tags:** 2fa, totp, auth, security

**Placeholders:** [DESCRIBE YOUR AUTH SYSTEM]

````text
Implement two-factor authentication (2FA) for my application.

App: [DESCRIBE YOUR AUTH SYSTEM]

**TOTP (Time-based One-Time Password)**:
1. Generate secret: `speakeasy.generateSecret()`
2. QR code: encode otpauth URI as QR code (qrcode library)
3. Show to user for Google Authenticator / Authy
4. Verify code: `speakeasy.totp.verify()` with 1-window tolerance
5. Backup codes: generate 10 single-use codes on setup
6. Store: secret encrypted in database

**2FA enrollment flow**:
7. User enables 2FA in settings
8. Show QR code + manual entry code
9. Verify user scanned correctly (enter code to confirm)
10. Show backup codes once (require user to save them)

**2FA login flow**:
11. After password → if 2FA enabled → prompt for TOTP
12. "Remember this device" option (30 day cookie)
13. Rate limit TOTP attempts (3 per minute)
14. Backup code flow when TOTP not available

Output: complete 2FA implementation.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Prevent Cross-Site Scripting (XSS)

**id:** `14-security/xss-prevention` · **Difficulty:** intermediate · **Tags:** xss, security, web, input-validation

**Placeholders:** [PASTE YOUR FRONTEND/BACKEND CODE]

````text
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
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement Zero Trust Security

**id:** `14-security/zero-trust` · **Difficulty:** advanced · **Tags:** zero-trust, security, architecture, network

**Placeholders:** [DESCRIBE YOUR INFRASTRUCTURE]

````text
Implement Zero Trust security architecture for my system.

Current setup: [DESCRIBE YOUR INFRASTRUCTURE]

**Zero Trust principles**:
1. **Never trust, always verify**: every request authenticated and authorized
2. **Least privilege**: minimal permissions for every identity
3. **Assume breach**: design for breach containment

**Implementation**:
4. **Identity**: strong MFA for all users and services
5. **Device trust**: verify device health before access
6. **Micro-segmentation**: network isolation, no implicit east-west trust
7. **Service mesh**: mTLS between all services (Istio)
8. **API gateway**: every API call authenticated
9. **Just-in-time access**: temporary elevated permissions
10. **Continuous verification**: re-auth on sensitive operations

**Monitoring**:
11. All access logged
12. Behavioral analytics: anomaly detection
13. Automated response: block suspicious activity

For my infrastructure: specific implementation plan.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement [DEFENSE] in [APP_STACK]

**id:** `14-security/implement-defense-in-app-stack` · **Difficulty:** beginner/intermediate/advanced · **Tags:** hardened, encryption, hardening, security, owasp, secured, sql, xss

**Variant group** (10 generated prompts collapsed). Pick one value per placeholder:
- `[DEFENSE]`: SQL injection mitigations | XSS sanitization layers | hardened CORS configurations | secured file uploads checks
- `[APP_STACK]`: a FastAPI application | a Python Django server | a Ruby on Rails application | a Spring Boot endpoint | an Express.js backend

````text
Hardened [APP_STACK] by implementing [DEFENSE]. Write the code setup, middleware configurations, and verification commands.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** implement-hardened-cors-configurations-in-a-fastapi-application, implement-hardened-cors-configurations-in-a-python-django-server, implement-hardened-cors-configurations-in-a-ruby-on-rails-application, implement-hardened-cors-configurations-in-a-spring-boot-endpoint, implement-secured-file-uploads-checks-in-a-fastapi-application, implement-secured-file-uploads-checks-in-a-spring-boot-endpoint, implement-sql-injection-mitigations-in-a-spring-boot-endpoint, implement-xss-sanitization-layers-in-a-ruby-on-rails-application, implement-xss-sanitization-layers-in-a-spring-boot-endpoint, implement-xss-sanitization-layers-in-an-expressjs-backend


## Write secure code guidelines for [APP_STACK] to prevent [DEFENSE]

**id:** `14-security/write-secure-code-guidelines-for-app-stack-to-prevent-defense` · **Difficulty:** beginner/intermediate/advanced · **Tags:** encryption, hardening, security, csrf, owasp, automated, xss, hardened, secured, sql

**Variant group** (14 generated prompts collapsed). Pick one value per placeholder:
- `[DEFENSE]`: CSRF token tracking | SQL injection mitigations | XSS sanitization layers | automated dependency vulnerability scans | hardened CORS configurations | secured file uploads checks
- `[APP_STACK]`: a FastAPI application | a Python Django server | a Ruby on Rails application | a Spring Boot endpoint | an Express.js backend
- `[CONTROL]`: Argon2id password hashing | HTML inputs sanitizers | database encryption rules | rate limiting middleware blocks

````text
Analyze potential vulnerabilities in [APP_STACK] and write security controls using [CONTROL] to block [DEFENSE] attempts.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** write-secure-code-guidelines-for-a-fastapi-application-to-prevent-csrf-token-tracking, write-secure-code-guidelines-for-a-python-django-server-to-prevent-automated-dependency-vulnerability-scans, write-secure-code-guidelines-for-a-python-django-server-to-prevent-csrf-token-tracking, write-secure-code-guidelines-for-a-python-django-server-to-prevent-xss-sanitization-layers, write-secure-code-guidelines-for-a-ruby-on-rails-application-to-prevent-hardened-cors-configurations, write-secure-code-guidelines-for-a-ruby-on-rails-application-to-prevent-xss-sanitization-layers, write-secure-code-guidelines-for-a-spring-boot-endpoint-to-prevent-automated-dependency-vulnerability-scans, write-secure-code-guidelines-for-a-spring-boot-endpoint-to-prevent-hardened-cors-configurations, write-secure-code-guidelines-for-a-spring-boot-endpoint-to-prevent-secured-file-uploads-checks, write-secure-code-guidelines-for-an-expressjs-backend-to-prevent-automated-dependency-vulnerability-scans, write-secure-code-guidelines-for-an-expressjs-backend-to-prevent-hardened-cors-configurations, write-secure-code-guidelines-for-an-expressjs-backend-to-prevent-secured-file-uploads-checks, write-secure-code-guidelines-for-an-expressjs-backend-to-prevent-sql-injection-mitigations, write-secure-code-guidelines-for-an-expressjs-backend-to-prevent-xss-sanitization-layers

