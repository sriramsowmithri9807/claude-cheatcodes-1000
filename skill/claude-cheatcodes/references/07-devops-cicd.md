# 07-devops-cicd

CI/CD pipelines, Docker, Kubernetes, Terraform/CDK, GitHub Actions/GitLab CI/Jenkins, deployments.

41 prompts. Search `## ` headings or ids; see index.md for the one-line list.

## Write Ansible Playbooks for Server Config

**id:** `07-devops-cicd/ansible-playbook` · **Difficulty:** advanced · **Tags:** ansible, configuration-management, devops, linux

**Placeholders:** [DESCRIBE: Ubuntu 22.04, what services run on them]

````text
Write Ansible playbooks to configure and manage my servers.

Servers: [DESCRIBE: Ubuntu 22.04, what services run on them]

Playbooks to write:
1. **base.yml**: system updates, timezone, NTP, swap, kernel params
2. **security.yml**: UFW firewall, fail2ban, SSH hardening (no root, no password auth)
3. **docker.yml**: install Docker + Docker Compose, manage with systemd
4. **nginx.yml**: install, configure, SSL with Certbot, test config
5. **app.yml**: deploy application, environment config, systemd service
6. **monitoring.yml**: install node exporter, configure log shipping
7. **backup.yml**: configure database backup cron job

Inventory: staging and production groups
Vault: encrypt sensitive values
Idempotent: safe to run multiple times
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Deploy with AWS ECS and Fargate

**id:** `07-devops-cicd/aws-ecs-deployment` · **Difficulty:** advanced · **Tags:** aws, ecs, fargate, containers

**Placeholders:** [DESCRIBE YOUR CONTAINERIZED APP]

````text
Set up complete deployment to AWS ECS Fargate.

App: [DESCRIBE YOUR CONTAINERIZED APP]

Infrastructure (using Terraform):
1. VPC with public/private subnets (2 AZs)
2. Application Load Balancer in public subnets
3. ECS Cluster
4. ECS Task Definition: container spec, CPU/memory, env vars from Secrets Manager
5. ECS Service: desired count, deployment config (rolling update)
6. Auto Scaling: scale on CPU > 70%
7. Security Groups: ALB → ECS only, ECS → RDS only
8. IAM Role for task: least privilege
9. CloudWatch logs
10. ECR repository for Docker images

CI/CD:
- GitHub Actions: build → push to ECR → update ECS service
- Blue/green deployment using CodeDeploy
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Deploy AWS Lambda Functions

**id:** `07-devops-cicd/aws-lambda-deploy` · **Difficulty:** intermediate · **Tags:** aws, lambda, serverless, devops

**Placeholders:** [DESCRIBE YOUR FUNCTIONS AND THEIR TRIGGERS]

````text
Deploy and manage AWS Lambda functions for my serverless backend.

Functions: [DESCRIBE YOUR FUNCTIONS AND THEIR TRIGGERS]

Using: AWS CDK (TypeScript) for infrastructure

1. **Lambda function code**: handler structure, cold start optimization
2. **CDK stack**: define Lambda, IAM role, triggers
3. **Triggers**:
   - API Gateway HTTP API
   - SQS queue trigger
   - EventBridge schedule
   - S3 object created
4. **Layers**: shared dependencies without bundling per function
5. **Environment variables + SSM Parameter Store**
6. **VPC config**: if function needs to access RDS
7. **Provisioned concurrency**: eliminate cold starts for latency-sensitive
8. **X-Ray tracing**: distributed tracing
9. **CloudWatch alarms**: error rate, duration, throttles
10. **CI/CD**: GitHub Actions → CDK deploy
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement Blue-Green Deployment

**id:** `07-devops-cicd/blue-green-deployment` · **Difficulty:** advanced · **Tags:** blue-green, deployment, zero-downtime, devops

**Placeholders:** [DESCRIBE YOUR DEPLOYMENT INFRASTRUCTURE]

````text
Implement blue-green deployment for zero-downtime releases.

Current setup: [DESCRIBE YOUR DEPLOYMENT INFRASTRUCTURE]

Blue-green strategy:
1. Blue: current production version (100% traffic)
2. Green: new version (deployed but no traffic)
3. Smoke test green environment
4. Switch traffic: blue → green (instant or gradual)
5. Keep blue running for 30 minutes (rollback window)
6. Tear down blue

Implementation options:
- **AWS ECS**: blue/green with CodeDeploy
- **Kubernetes**: two Deployments, update Service selector
- **Nginx**: upstream groups, reload config without downtime
- **Feature flags**: code-level blue/green

For MY stack: complete implementation with rollback procedure.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design Infrastructure Caching

**id:** `07-devops-cicd/caching-infrastructure` · **Difficulty:** advanced · **Tags:** caching, cdn, cloudfront, redis

**Placeholders:** [DESCRIBE]

````text
Design a multi-layer caching infrastructure for my application.

App: [DESCRIBE]

Layer 1 — CDN (Cloudflare or CloudFront):
1. Cache static assets (JS, CSS, images) at edge
2. Cache API responses at edge for public content
3. Cache-Control headers for each asset type
4. Cache invalidation on deploy

Layer 2 — Nginx caching:
5. `proxy_cache` for upstream responses
6. Cache by URL, vary by auth header

Layer 3 — Application cache (Redis):
7. Cache expensive DB queries
8. Cache external API responses
9. Rate limiting counters

Layer 4 — Database cache:
10. PostgreSQL shared_buffers (25% RAM)
11. Materialized views for expensive reports

Draw the request flow showing which layer serves each request type.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## CI/CD Best Practices for Production

**id:** `07-devops-cicd/cicd-best-practices` · **Difficulty:** intermediate · **Tags:** ci-cd, devops, best-practices, pipelines

**Placeholders:** [DESCRIBE YOUR CURRENT CI/CD SITUATION]

````text
Implement CI/CD best practices for my team's deployment pipeline.

Current setup: [DESCRIBE YOUR CURRENT CI/CD SITUATION]

Best practices to implement:
1. **Fail fast**: run fastest checks first (lint before tests)
2. **Parallelism**: run independent jobs in parallel
3. **Caching**: dependency cache, Docker layer cache
4. **Artifact storage**: pass build artifacts between jobs
5. **Environment parity**: staging = production config
6. **Rollback**: one-click rollback to previous version
7. **Feature flags**: deploy code without enabling feature
8. **Canary deployment**: route 1% traffic to new version first
9. **Smoke tests**: post-deploy verification
10. **Secrets rotation**: no long-lived secrets
11. **Dependency updates**: Dependabot or Renovate bot
12. **DORA metrics**: track deployment frequency, lead time, MTTR, change failure rate
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Secure Your CI/CD Pipeline

**id:** `07-devops-cicd/cicd-security` · **Difficulty:** advanced · **Tags:** security, ci-cd, supply-chain, devops

````text
Harden my CI/CD pipeline against supply chain attacks.

Current pipeline: GitHub Actions

Threats:
1. Compromised dependencies (supply chain attack)
2. Stolen secrets from CI logs
3. Untrusted code in pull requests
4. Malicious GitHub Actions

Hardening:
1. **Pin action versions**: use SHA hash, not tags
2. **Minimal permissions**: `permissions: read-all` by default, grant write only where needed
3. **OIDC for cloud auth**: no long-lived AWS/GCP credentials
4. **Secret masking**: secrets never in logs
5. **Dependency lock files**: commit package-lock.json, poetry.lock
6. **Verify downloads**: checksum verification for any downloaded tools
7. **Code signing**: sign your container images (cosign)
8. **SBOM generation**: Software Bill of Materials on every build
9. **OpenSSF Scorecard**: measure and improve supply chain security
10. **Third-party action audit**: review all actions in use
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Deploy with Cloudflare Workers

**id:** `07-devops-cicd/cloudflare-workers` · **Difficulty:** intermediate · **Tags:** cloudflare, workers, edge, deployment

````text
Deploy my application to Cloudflare Workers (edge computing).

App type: [API / static site / SSR / proxy]

Implement:
1. **Worker script** in TypeScript using Hono framework
2. **KV storage**: for caching, session state, feature flags
3. **D1 database**: SQLite at the edge for small datasets
4. **R2 storage**: S3-compatible object storage
5. **Durable Objects**: stateful edge (real-time collaboration, rate limiting)
6. **Queue**: Cloudflare Queues for background processing
7. **Cron triggers**: scheduled jobs
8. **Wrangler config**: `wrangler.toml` with environments
9. **CI/CD**: GitHub Actions → `wrangler deploy`
10. **Custom domain**: bind to your domain with Cloudflare DNS
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Set Up a Container Registry

**id:** `07-devops-cicd/container-registry` · **Difficulty:** intermediate · **Tags:** docker, registry, ghcr, ecr

````text
Set up a container registry and image management workflow.

Registry options:
- **GitHub Container Registry (GHCR)**: free for public, free private with GitHub Team
- **AWS ECR**: pay-per-storage, no egress if in same region as ECS
- **Docker Hub**: easy, limited free tier
- **Artifact Registry (GCP)**: if using GCP

For MY choice:
1. Registry setup and authentication
2. Push workflow from GitHub Actions
3. Image tagging strategy: `latest`, git SHA, semantic version
4. Multi-architecture builds (linux/amd64 + linux/arm64)
5. Image scanning for vulnerabilities (before pushing)
6. Retention policy: keep last 10 images, delete older
7. Pull secrets in Kubernetes
8. Rate limiting considerations
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement Cloud Cost Allocation Tags

**id:** `07-devops-cicd/cost-allocation` · **Difficulty:** intermediate · **Tags:** cost, aws, finops, tagging

**Placeholders:** [TEAMS, PROJECTS, COST CENTERS]

````text
Implement comprehensive cost allocation tagging for AWS resources.

Business context: [TEAMS, PROJECTS, COST CENTERS]

Tagging strategy:
1. **Mandatory tags**: Environment, Team, Project, CostCenter, Owner
2. **AWS Organizations**: tag policies to enforce mandatory tags
3. **Resource-specific tags**: Service, Version, Tier
4. **Propagation**: EC2 → EBS, ECS → tasks, RDS → snapshots
5. **Cost Explorer**: filter and group by tags
6. **Budgets**: per-team budget with alerts at 80%, 100%, 120%
7. **Anomaly detection**: alert on unexpected cost spikes
8. **Showback reports**: monthly cost per team email
9. **Untagged resource hunting**: find and tag orphaned resources
10. **Terraform tagging**: `default_tags` in provider config

Output: tagging policy document + Terraform provider config.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Database DevOps: Migrations in CI/CD

**id:** `07-devops-cicd/database-devops` · **Difficulty:** advanced · **Tags:** database, migrations, ci-cd, devops

````text
Integrate database migrations safely into CI/CD pipeline.

Stack: PostgreSQL + Flyway (or Liquibase)
CI: GitHub Actions

1. **Migration file standards**: naming, rollback scripts, idempotency
2. **CI**: validate migration syntax on every PR
3. **Staging deploy**: run migrations before app deploy
4. **Production**: run migrations before rolling app deploy
5. **Zero-downtime patterns**:
   - New column: add nullable first, backfill, add NOT NULL constraint later
   - Drop column: two-phase (stop reading → deploy → drop)
   - Rename: expand-contract pattern
6. **Rollback**: automated rollback if migration fails
7. **Drift detection**: alert if prod schema differs from expected
8. **Data migrations**: separate from schema migrations (async job)
9. **Migration testing**: test against prod data copy weekly
10. **Permissions**: migration runner has limited privileges
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Production Deployment Checklist

**id:** `07-devops-cicd/deployment-checklist` · **Difficulty:** intermediate · **Tags:** deployment, checklist, devops, production

**Placeholders:** [DESCRIBE YOUR STACK AND INFRASTRUCTURE]

````text
Create a comprehensive production deployment checklist.

My app: [DESCRIBE YOUR STACK AND INFRASTRUCTURE]

**Pre-deployment**:
□ All tests passing (unit, integration, E2E)
□ Security scan passed (Snyk / npm audit)
□ Performance regression test passed
□ Database migrations tested on staging with production data copy
□ Feature flags set correctly for rollout plan
□ Rollback plan documented and tested
□ On-call engineer aware and available
□ Stakeholders notified (if user-visible change)

**During deployment**:
□ Deploy to staging first
□ Smoke test staging
□ Monitor error rates during rollout
□ Deploy to production (blue/green or rolling)
□ Watch dashboards for 15 minutes

**Post-deployment**:
□ Smoke test production
□ Alert the team
□ Update changelog
□ Close the deployment issue/PR
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build an Internal Developer Platform

**id:** `07-devops-cicd/devops-platform` · **Difficulty:** advanced · **Tags:** idp, platform, devops, developer-experience

**Placeholders:** [DESCRIBE: long deploy times, environment parity, etc.]

````text
Design an Internal Developer Platform (IDP) for my engineering team.

Team size: [N engineers]
Current pain points: [DESCRIBE: long deploy times, environment parity, etc.]

Platform components:
1. **Self-service infrastructure**: create environments with one command
2. **Backstage**: service catalog, documentation, runbooks
3. **Golden paths**: opinionated templates for new services
4. **Secrets management**: self-service secret storage
5. **Observability portal**: logs, metrics, traces in one place
6. **Deployment portal**: see deploy status, trigger deploys, roll back
7. **Cost portal**: per-team cloud spend visibility
8. **Runbook automation**: common operations as self-service buttons
9. **DORA metrics dashboard**: track engineering effectiveness
10. **On-call scheduler**: PagerDuty integration, fair rotation

Start small: what to build in week 1 vs month 6.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Design a Disaster Recovery Plan

**id:** `07-devops-cicd/disaster-recovery` · **Difficulty:** advanced · **Tags:** disaster-recovery, rto, rpo, architecture

**Placeholders:** [DESCRIBE]

````text
Design a disaster recovery plan for my application.

Application: [DESCRIBE]
RTO (Recovery Time Objective): [e.g., < 4 hours]
RPO (Recovery Point Objective): [e.g., < 1 hour]

Failure scenarios to plan for:
1. Database failure → automated failover to replica
2. Single AZ outage → multi-AZ deployment
3. Entire region outage → multi-region failover
4. Application bug in production → rollback procedure
5. Data corruption → point-in-time restore
6. DDoS attack → rate limiting + CDN + WAF
7. Third-party API failure → circuit breaker + fallback
8. Developer error → change management, peer review gates

For each:
- Prevention measures
- Detection (how to know it happened)
- Response playbook (step by step)
- Recovery time estimate
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Create Docker Compose for Development

**id:** `07-devops-cicd/docker-compose` · **Difficulty:** intermediate · **Tags:** docker, docker-compose, local-dev, containers

**Placeholders:** [OTHER SERVICES: Elasticsearch, MinIO, Mailhog, etc.]

````text
Create a complete Docker Compose setup for local development of my app.

Services:
- App: [Node.js / Python / Go]
- Database: PostgreSQL 16
- Cache: Redis 7
- [OTHER SERVICES: Elasticsearch, MinIO, Mailhog, etc.]

`docker-compose.yml`:
1. Each service with health checks
2. Volume mounts for hot reload (don't copy code into container)
3. Named volumes for persistent data (DB data survives container restart)
4. Environment variables from `.env` file
5. Networking (internal DNS between services)
6. `depends_on` with health check conditions
7. Resource limits (prevent one service from hogging all RAM)

Also:
- `docker-compose.override.yml` for dev-specific overrides
- `docker-compose.prod.yml` for production-like settings
- Makefile with: `make up`, `make down`, `make logs`, `make shell`
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Harden Docker Containers for Production

**id:** `07-devops-cicd/docker-security` · **Difficulty:** advanced · **Tags:** docker, security, containers, devops

**Placeholders:** [PASTE OR DESCRIBE]

````text
Harden my Docker containers for production security.

Current Dockerfile: [PASTE OR DESCRIBE]

Security improvements:
1. **Non-root user**: run process as non-root inside container
2. **Read-only filesystem**: `--read-only`, writable mounts only where needed
3. **Minimal base image**: distroless or alpine (reduce attack surface)
4. **Multi-stage build**: no build tools in final image
5. **No secrets in image**: use runtime env vars or secrets manager
6. **Pinned versions**: specific tags, not `latest`
7. **Layer ordering**: cache dependencies layer separately from code
8. **Image scanning**: Trivy or Snyk in CI pipeline
9. **COPY vs ADD**: use COPY, never ADD
10. **HEALTHCHECK**: define health check in Dockerfile
11. **Capabilities**: drop all, add back only what's needed
12. `.dockerignore`: exclude .git, .env, node_modules
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Deploy to Fly.io

**id:** `07-devops-cicd/fly-io-deployment` · **Difficulty:** beginner · **Tags:** fly-io, deployment, containers, devops

**Placeholders:** [DESCRIBE: what it is, what port it listens on, any databases/redis needed]

````text
Deploy my application to Fly.io.

App: [DESCRIBE: what it is, what port it listens on, any databases/redis needed]

1. **fly.toml**: complete config file
   - app name, region selection
   - HTTP service with internal port
   - health check configuration
   - environment variables
   - volume mounts for persistent data
2. **Dockerfile**: optimized for Fly.io
3. **PostgreSQL**: provision Fly Postgres cluster
4. **Redis**: Upstash Redis integration
5. **Secrets**: `fly secrets set KEY=VALUE`
6. **Scaling**: `fly scale count 2` for zero-downtime deploys
7. **GitHub Actions**: auto-deploy on push to main
8. **Custom domain**: add and configure SSL
9. **Monitoring**: Fly metrics integration
10. **Connecting locally**: fly proxy for local DB access
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Write a Complete GitHub Actions CI/CD Pipeline

**id:** `07-devops-cicd/github-actions` · **Difficulty:** intermediate · **Tags:** github-actions, ci-cd, devops, automation

````text
Write a complete GitHub Actions CI/CD pipeline for my [Node.js / Python / Go] project.

Workflows to create:

**CI workflow** (on every PR):
1. Checkout code
2. Setup Node/Python/Go with version caching
3. Install dependencies (with cache)
4. Lint (ESLint, Ruff, golint)
5. Type check (TypeScript tsc, mypy)
6. Unit tests (with coverage report)
7. Integration tests (spin up Docker services)
8. Build (verify it compiles)
9. Security scan (CodeQL or Snyk)
10. Post results as PR comment

**CD workflow** (on merge to main):
11. Build Docker image
12. Push to registry (GHCR)
13. Deploy to staging (Fly.io / Railway / AWS ECS)
14. Run smoke tests
15. Deploy to production (manual approval gate)

Output: complete YAML workflow files.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement GitOps with ArgoCD

**id:** `07-devops-cicd/gitops-workflow` · **Difficulty:** advanced · **Tags:** gitops, argocd, kubernetes, devops

````text
Implement GitOps workflow using ArgoCD for Kubernetes deployments.

Setup:
- Kubernetes cluster (EKS / GKE / self-hosted)
- Multiple environments: dev, staging, production

Implement:
1. **ArgoCD installation** in the cluster
2. **App of Apps pattern**: manage multiple apps from one ArgoCD app
3. **Repository structure**:
   ```
   gitops-repo/
     apps/          # ArgoCD Application definitions
     environments/
       dev/         # Kustomize overlays for dev
       staging/
       production/
     base/          # Base Kubernetes manifests
   ```
4. **Sync policies**: auto-sync dev, manual approval for production
5. **Health checks**: define custom health assessment
6. **Notifications**: Slack on sync/failure
7. **RBAC**: developer can view, SRE can sync, admin can delete
8. **Secret management**: Sealed Secrets or External Secrets Operator
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Create a Helm Chart for Kubernetes

**id:** `07-devops-cicd/helm-chart` · **Difficulty:** advanced · **Tags:** helm, kubernetes, charts, devops

**Placeholders:** [DESCRIBE YOUR APPLICATION]

````text
Create a Helm chart for deploying my application to Kubernetes.

App: [DESCRIBE YOUR APPLICATION]

Chart structure:
```
mychart/
  Chart.yaml
  values.yaml
  templates/
    deployment.yaml
    service.yaml
    ingress.yaml
    configmap.yaml
    secret.yaml
    hpa.yaml
    pdb.yaml
    _helpers.tpl
```

Values to parameterize:
- Image repo and tag
- Replica count
- Resource limits
- Ingress host and TLS
- Environment variables
- Secrets (from external secrets operator)
- Enable/disable optional components

Include: `Chart.yaml`, complete `values.yaml` with comments, and all templates.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Optimize Cloud Infrastructure Costs

**id:** `07-devops-cicd/infrastructure-cost` · **Difficulty:** advanced · **Tags:** cost-optimization, aws, cloud, finops

**Placeholders:** [DESCRIBE YOUR CURRENT CLOUD SPEND AND RESOURCES]

````text
Optimize my cloud infrastructure costs.

Current spend: [DESCRIBE YOUR CURRENT CLOUD SPEND AND RESOURCES]

Optimization strategies:
1. **Right-sizing**: identify over-provisioned instances (CloudWatch metrics)
2. **Reserved instances / savings plans**: 30-70% discount for committed usage
3. **Spot instances**: 70-90% discount for non-critical workloads
4. **Auto-scaling**: don't run at peak capacity 24/7
5. **S3 lifecycle policies**: move old data to Glacier
6. **NAT Gateway**: expensive, minimize traffic through it
7. **Data transfer**: avoid cross-region and cross-AZ transfers
8. **RDS**: stop non-production databases on nights/weekends
9. **Unused resources**: find and delete orphaned volumes, old snapshots
10. **CloudWatch metrics**: which metrics you're paying for vs actually using

Target: 30% cost reduction. Show the calculation.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Test Infrastructure as Code

**id:** `07-devops-cicd/infrastructure-testing` · **Difficulty:** advanced · **Tags:** terraform, testing, inspec, devops

**Placeholders:** [DESCRIBE YOUR TERRAFORM RESOURCES]

````text
Write tests for my Terraform infrastructure code.

Infrastructure: [DESCRIBE YOUR TERRAFORM RESOURCES]

Testing layers:
1. **Static analysis**: `terraform validate` + `tflint` + `checkov` (security)
2. **Unit tests**: `Terratest` — deploy to real AWS sandbox, verify resources
3. **Policy tests**: OPA (Open Policy Agent) policies for compliance
4. **Drift detection**: `terraform plan` output — alert if diff exists in prod
5. **Integration**: real infrastructure test with smoke tests
6. **Destruction test**: verify `terraform destroy` cleans up cleanly

CI pipeline:
7. On PR: static analysis + security scan
8. On merge to main: deploy to staging + integration tests
9. On tag: deploy to production with manual approval

Output: Terratest Go test file + GitHub Actions workflow.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Set Up Kubernetes Autoscaling

**id:** `07-devops-cicd/kubernetes-autoscaling` · **Difficulty:** advanced · **Tags:** kubernetes, autoscaling, hpa, keda

````text
Set up comprehensive autoscaling for my Kubernetes deployment.

App: [DESCRIBE YOUR WORKLOAD PATTERN — steady, bursty, schedule-based]

1. **Horizontal Pod Autoscaler (HPA)**:
   - Scale on CPU utilization > 70%
   - Scale on custom metrics (queue depth, requests per pod)
   - Min replicas, max replicas
   - Scale-down delay (prevent flapping)
2. **Vertical Pod Autoscaler (VPA)**:
   - Automatically right-size CPU/memory requests
   - Off mode for recommendations only
3. **KEDA** (event-driven autoscaling):
   - Scale to zero when no traffic
   - Scale on SQS queue depth
   - Scale on Kafka consumer lag
4. **Cluster Autoscaler**:
   - Add/remove nodes based on pod demand
   - Node group configuration
5. **Spot instances**: use spot for bursty workloads

Output: YAML manifests for all autoscalers.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Deploy to Kubernetes

**id:** `07-devops-cicd/kubernetes-deployment` · **Difficulty:** advanced · **Tags:** kubernetes, k8s, deployment, helm

**Placeholders:** [DESCRIBE YOUR APP: what containers, what dependencies]

````text
Write Kubernetes manifests to deploy my application.

App: [DESCRIBE YOUR APP: what containers, what dependencies]

Manifests to create:
1. **Namespace**: isolate resources
2. **Deployment**: replicas, container spec, resource requests/limits, liveness/readiness probes
3. **Service**: ClusterIP for internal, LoadBalancer or NodePort for external
4. **Ingress**: route traffic with Nginx ingress controller
5. **ConfigMap**: non-sensitive config
6. **Secret**: sensitive values (base64 encoded, or External Secrets Operator)
7. **HorizontalPodAutoscaler**: scale on CPU or custom metrics
8. **PodDisruptionBudget**: ensure at least N pods always available
9. **ServiceAccount**: least-privilege RBAC
10. **NetworkPolicy**: restrict pod-to-pod traffic

Also: `kubectl apply` order and health check commands.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Configure Load Balancing

**id:** `07-devops-cicd/load-balancing` · **Difficulty:** advanced · **Tags:** load-balancing, nginx, haproxy, architecture

````text
Set up load balancing for my application.

Architecture: [N app servers, what protocol, session requirements]

Options to evaluate:

**Nginx upstream**:
- round_robin (default)
- least_conn
- ip_hash (sticky sessions)
- weight distribution

**HAProxy** (more features):
- ACL-based routing
- Health checks (active and passive)
- SSL termination
- Connection rate limiting
- Stats page

**AWS ALB**:
- Target groups + rules
- Path-based routing
- Weighted routing (canary)
- Sticky sessions

For MY setup: which to use and why.
Output: complete config + health check setup.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Set Up Centralized Log Aggregation

**id:** `07-devops-cicd/log-aggregation` · **Difficulty:** advanced · **Tags:** logging, elk, grafana-loki, devops

**Placeholders:** [LIST SERVICES]

````text
Set up centralized log aggregation for my distributed application.

Logs to aggregate from: [LIST SERVICES]

Option A — ELK Stack (self-hosted):
1. Elasticsearch: store and index logs
2. Logstash: parse and transform
3. Kibana: visualize and search
4. Filebeat / Fluentd: ship logs from each service
5. Index lifecycle policy: hot → warm → cold → delete

Option B — Grafana Loki (cheaper):
6. Loki: log aggregation without full-text indexing
7. Promtail: log shipper
8. Grafana: query with LogQL
9. Cost: 10x cheaper than ELK for most use cases

For both:
- Structured JSON logging from applications
- Log retention and archiving policy
- Alerting on error patterns
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Configure Log Retention and Compliance

**id:** `07-devops-cicd/log-retention` · **Difficulty:** intermediate · **Tags:** logging, compliance, retention, gdpr

````text
Configure log retention and management for compliance.

Compliance: [GDPR / HIPAA / SOC2 / none — just best practices]

Log types and retention:
1. Application logs: 90 days hot, 1 year cold storage
2. Access logs: 1 year (security audit trail)
3. Error logs: 1 year with alerting
4. Security events: 2 years
5. Business events: indefinite (anonymized after 1 year)

Implement:
6. Structured logging (JSON, no PII in log messages)
7. Log levels: control verbosity per environment
8. Automatic PII detection and redaction
9. Centralized storage: S3 with lifecycle to Glacier
10. Access controls: who can query logs (SOC2 requirement)
11. Audit log: log who accessed the logs
12. GDPR: ability to delete a user's logs on request
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Set Up Production Monitoring Stack

**id:** `07-devops-cicd/monitoring-setup` · **Difficulty:** advanced · **Tags:** monitoring, prometheus, grafana, alerting

````text
Set up a complete production monitoring stack.

Stack: Prometheus + Grafana + Alertmanager

Using Docker Compose:
1. **Prometheus**: scrape config for your services + node exporter
2. **Grafana**: pre-configured datasource, provisioned dashboards
3. **Alertmanager**: route alerts to Slack/PagerDuty
4. **Node Exporter**: host-level metrics (CPU, memory, disk, network)
5. **cAdvisor**: Docker container metrics
6. **Blackbox Exporter**: HTTP endpoint monitoring (uptime)
7. **Application metrics**: your app exposes /metrics (Prometheus format)

Dashboards to create:
- System health (CPU, memory, disk)
- Application (request rate, error rate, latency)
- Business metrics (signups, revenue, active users)

Alerts: list the 10 most important alerts with thresholds.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Deploy a Multi-Region Architecture

**id:** `07-devops-cicd/multi-region` · **Difficulty:** advanced · **Tags:** multi-region, aws, global, architecture

````text
Design and deploy a multi-region architecture for global availability.

Current: Single region [us-east-1]
Goal: Add [eu-west-1] for European users with < 50ms latency from Europe

Design:
1. **DNS routing**: Route 53 latency-based routing (user → nearest region)
2. **Primary region**: active, handles all writes
3. **Secondary region**: read replica + static content
4. **Database**: PostgreSQL streaming replication to secondary
5. **Read routing**: read from local replica, write to primary
6. **CDN**: CloudFront (global edge already)
7. **Session state**: Redis with cross-region sync (ElastiCache Global Datastore)
8. **Failover**: if primary fails, promote secondary to primary
9. **Data residency**: European user data stays in EU (GDPR)
10. **Cost**: estimate the additional monthly cost
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Write Production Nginx Configuration

**id:** `07-devops-cicd/nginx-config` · **Difficulty:** intermediate · **Tags:** nginx, web-server, reverse-proxy, ssl

**Placeholders:** [LIST YOUR DOMAINS]

````text
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
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Load Test Infrastructure

**id:** `07-devops-cicd/nginx-load-test` · **Difficulty:** intermediate · **Tags:** load-testing, k6, infrastructure, performance

**Placeholders:** [DESCRIBE: Nginx + App + DB], [TARGET]

````text
Load test my infrastructure to find the breaking point.

Infrastructure: [DESCRIBE: Nginx + App + DB]

Using: k6

Test scenarios:
1. **Smoke test**: 1 VU, 1 minute — verify test script works
2. **Load test**: ramp to [TARGET] RPS over 5 min, sustain 10 min
3. **Stress test**: keep increasing until failure — find capacity
4. **Spike test**: instant jump to 10x normal
5. **Soak test**: moderate load for 1-2 hours (memory leaks)

Metrics to collect:
- HTTP request rate, error rate, response times (p50/p95/p99)
- Server CPU, memory, network
- Database connections, query latency
- Redis hit rate

Results analysis: where did it break? What's the fix?
Output: complete k6 script for realistic user scenarios.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build Full Observability Stack

**id:** `07-devops-cicd/observability-stack` · **Difficulty:** advanced · **Tags:** observability, otel, metrics, tracing

````text
Build a complete observability stack (metrics + traces + logs).

Using: OpenTelemetry + Grafana Stack (LGTM: Loki, Grafana, Tempo, Mimir)

1. **OpenTelemetry SDK** setup in your services (Node.js + Python)
2. **Auto-instrumentation**: HTTP, DB, Redis, message queues
3. **Manual spans** for business operations
4. **Metrics**: counters, histograms, gauges exported to Prometheus
5. **Traces**: OTLP export to Tempo
6. **Logs**: structured JSON → Promtail → Loki
7. **Correlation**: link log lines to traces (trace_id in logs)
8. **Dashboards**: pre-built Grafana dashboards from grafana.com
9. **SLOs**: define and track Service Level Objectives
10. **Alerting**: Grafana unified alerting

Docker Compose for local + Helm charts for production.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Deploy to Railway

**id:** `07-devops-cicd/railway-deployment` · **Difficulty:** beginner · **Tags:** railway, deployment, devops, beginner

**Placeholders:** [DESCRIBE: frontend, backend, database]

````text
Deploy my full-stack app to Railway.

App: [DESCRIBE: frontend, backend, database]

Step-by-step:
1. `railway init` and `railway link` for existing project
2. **Environment variables**: set via dashboard or CLI
3. **PostgreSQL plugin**: provision and link to your app (DATABASE_URL auto-set)
4. **Redis plugin**: add for caching/queues
5. **Build command**: override if not auto-detected
6. **Start command**: override if needed
7. **Health checks**: configure for zero-downtime deploys
8. **Custom domain**: CNAME setup
9. **GitHub integration**: auto-deploy on push
10. **Deploy environments**: production + staging environments
11. **Monorepo**: deploy specific service from monorepo
12. **Viewing logs**: `railway logs`
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Manage Secrets in Production

**id:** `07-devops-cicd/secret-management` · **Difficulty:** advanced · **Tags:** secrets, security, vault, aws-secrets-manager

**Placeholders:** [LIST TYPES: DB passwords, API keys, JWT secrets, etc.]

````text
Set up secure secrets management for my production environment.

Secrets to manage: [LIST TYPES: DB passwords, API keys, JWT secrets, etc.]

Options:
**AWS Secrets Manager**:
1. Store secrets with automatic rotation
2. IAM policy: EC2/ECS can read specific secrets
3. SDK integration (Node.js, Python)
4. Rotation lambda for database passwords

**HashiCorp Vault**:
5. Dynamic secrets: Vault generates short-lived DB credentials
6. App role authentication
7. Kubernetes integration (vault-agent-injector)

**GitHub Actions**:
8. Environment secrets for CI/CD
9. OIDC federation: GitHub → AWS without long-lived keys

Never again:
- Hardcode secrets in code
- Store secrets in environment files committed to git
- Share secrets via Slack/email
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Monitor Serverless Functions

**id:** `07-devops-cicd/serverless-monitoring` · **Difficulty:** intermediate · **Tags:** serverless, monitoring, lambda, devops

**Placeholders:** [LIST YOUR FUNCTIONS AND THEIR IMPORTANCE]

````text
Set up monitoring for my serverless (Lambda/Vercel) functions.

Functions: [LIST YOUR FUNCTIONS AND THEIR IMPORTANCE]

Key metrics:
1. **Invocation count**: requests per minute per function
2. **Error rate**: 4xx, 5xx, unhandled exceptions
3. **Duration**: p50, p95, p99 cold starts vs warm starts
4. **Throttling**: when functions are throttled (capacity issue)
5. **Concurrent executions**: approaching account limit?
6. **Memory utilization**: right-size memory allocation

Alerting:
7. Error rate > 1%: Slack alert
8. Cold start > 2s: investigate provisioned concurrency
9. Duration > 25s (approaching 30s timeout): alert + optimize
10. Throttle rate > 0: alert + request limit increase

Dashboard: Lambda Insights or Lumigo or custom CloudWatch.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Automate SSL Certificate Management

**id:** `07-devops-cicd/ssl-certificate-management` · **Difficulty:** intermediate · **Tags:** ssl, automation, certbot, devops

**Placeholders:** [DESCRIBE: how many domains, how managed — Nginx, AWS, Cloudflare]

````text
Automate SSL certificate management at scale.

Infrastructure: [DESCRIBE: how many domains, how managed — Nginx, AWS, Cloudflare]

**Let's Encrypt automation**:
1. Certbot with `--webroot` or `--dns-cloudflare` challenge
2. Auto-renewal cron: `0 12 * * * /usr/bin/certbot renew --quiet`
3. Nginx reload hook after renewal
4. Wildcard certificates: `*.example.com` with DNS challenge

**AWS Certificate Manager**:
5. Auto-renewing certificates for ALB/CloudFront
6. DNS validation (add CNAME record)
7. Terraform: `aws_acm_certificate` + validation record

**Monitoring**:
8. Certificate expiry monitoring (alert at 30 days)
9. Certificate transparency log monitoring
10. Automated alerting: page on-call if renewal fails

Never have a certificate expire in production again.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Set Up SSL/TLS Correctly

**id:** `07-devops-cicd/ssl-tls-setup` · **Difficulty:** intermediate · **Tags:** ssl, tls, https, certbot

````text
Set up SSL/TLS correctly for my web application.

Setup: Nginx + Let's Encrypt (Certbot)

1. **Certbot installation and certificate issuance** (webroot or DNS challenge)
2. **Auto-renewal**: cron job + Nginx reload hook
3. **TLS configuration**:
   - Minimum TLS 1.2 (drop TLS 1.0/1.1)
   - Strong cipher suites (ECDHE + AES-GCM)
   - Perfect Forward Secrecy
   - Diffie-Hellman params (4096-bit)
4. **HSTS**: Strict-Transport-Security header with preload
5. **OCSP stapling**: reduce latency on handshake
6. **HTTP/2**: enable for performance
7. **Testing**: SSL Labs A+ rating target
8. **Wildcard certificate**: if needed for subdomains
9. **Certificate monitoring**: alert 30 days before expiry
10. **CAA DNS record**: restrict certificate issuance to Let's Encrypt
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Infrastructure as Code with Terraform

**id:** `07-devops-cicd/terraform-aws` · **Difficulty:** advanced · **Tags:** terraform, aws, iac, devops

**Placeholders:** [LIST YOUR RESOURCES: VPC, EC2, RDS, S3, CloudFront, ALB, etc.]

````text
Write Terraform code for my AWS infrastructure.

Infrastructure to provision:
- [LIST YOUR RESOURCES: VPC, EC2, RDS, S3, CloudFront, ALB, etc.]

Best practices to follow:
1. **State management**: S3 backend + DynamoDB lock table
2. **Modules**: one module per logical group (networking, database, app)
3. **Variables**: with type, description, validation
4. **Locals**: computed values
5. **Outputs**: export values to other modules
6. **Data sources**: reference existing AWS resources
7. **Workspaces** or **separate state**: staging vs production
8. **Secrets**: never hardcode — use AWS Secrets Manager
9. **Tagging**: consistent tags on all resources
10. **Destroy protection**: `prevent_destroy = true` on critical resources

Output: complete, working Terraform code with modules.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Set Up a VPN for Database Access

**id:** `07-devops-cicd/vpn-setup` · **Difficulty:** intermediate · **Tags:** vpn, security, wireguard, devops

````text
Set up secure VPN access to my production databases.

Using: WireGuard (modern, fast, simple)

1. **WireGuard server setup** on a bastion EC2/VPS:
   - Installation (Ubuntu)
   - Generate server keys
   - Interface config (`/etc/wireguard/wg0.conf`)
   - Enable IP forwarding
   - iptables rules for routing
2. **Client config**: generate config for each developer
3. **Peer management**: add/remove peers without restart
4. **Routing**: route only production subnets through VPN (split tunneling)
5. **DNS**: resolve internal hostnames through VPN
6. **Automation**: script to generate new peer configs
7. **Security**: key rotation procedure
8. **Alternative**: AWS Client VPN (managed, per-hour cost)

Connect to: PostgreSQL (port 5432) and Redis (port 6379) without exposing to internet.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build a [TOOL] pipeline for deploying to [DEPLOY_TARGET]

**id:** `07-devops-cicd/build-a-tool-pipeline-for-deploying-to-deploy-target` · **Difficulty:** beginner/intermediate/advanced · **Tags:** gitlab, devops, cicd, cloud, docker, jenkins, kubernetes, terraform

**Variant group** (5 generated prompts collapsed). Pick one value per placeholder:
- `[TOOL]`: GitLab CI | Jenkins | Kubernetes | Terraform
- `[DEPLOY_TARGET]`: a Google Cloud Run instance | a Vercel serverless environment | a horizontal pod autoscaler in Kubernetes | an AWS ECS cluster
- `[PIPELINE_FEATURE]`: blue-green deployments setups | secret injection configurations

````text
Create a [TOOL] pipeline file that deploys code to [DEPLOY_TARGET]. Include [PIPELINE_FEATURE] and environment variable overrides.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** build-a-gitlab-ci-pipeline-for-deploying-to-an-aws-ecs-cluster, build-a-jenkins-pipeline-for-deploying-to-a-google-cloud-run-instance, build-a-kubernetes-pipeline-for-deploying-to-a-google-cloud-run-instance, build-a-kubernetes-pipeline-for-deploying-to-a-horizontal-pod-autoscaler-in-kubernetes, build-a-terraform-pipeline-for-deploying-to-a-vercel-serverless-environment


## Write a [TOOL] config for [DEPLOY_TARGET] with [PIPELINE_FEATURE]

**id:** `07-devops-cicd/write-a-tool-config-for-deploy-target-with-pipeline-feature` · **Difficulty:** beginner/intermediate/advanced · **Tags:** aws, devops, cicd, cloud, docker, github, gitlab

**Variant group** (6 generated prompts collapsed). Pick one value per placeholder:
- `[TOOL]`: AWS CDK | Docker | GitHub Actions | GitLab CI
- `[DEPLOY_TARGET]`: a Google Cloud Run instance | a Vercel serverless environment | a horizontal pod autoscaler in Kubernetes | an AWS ECS cluster
- `[PIPELINE_FEATURE]`: automated testing stages | blue-green deployments setups | secret injection configurations

````text
Configure [TOOL] for [DEPLOY_TARGET] incorporating [PIPELINE_FEATURE]. Ensure security practices and low build execution times.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** write-a-aws-cdk-config-for-an-aws-ecs-cluster-with-automated-testing-stages, write-a-docker-config-for-a-vercel-serverless-environment-with-automated-testing-stages, write-a-docker-config-for-an-aws-ecs-cluster-with-secret-injection-configurations, write-a-github-actions-config-for-a-vercel-serverless-environment-with-automated-testing-stages, write-a-gitlab-ci-config-for-a-google-cloud-run-instance-with-blue-green-deployments-setups, write-a-gitlab-ci-config-for-a-horizontal-pod-autoscaler-in-kubernetes-with-automated-testing-stages

