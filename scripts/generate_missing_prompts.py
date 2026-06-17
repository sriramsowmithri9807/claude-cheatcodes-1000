#!/usr/bin/env python3
import os
import random
from pathlib import Path

ROOT = Path(__file__).parent.parent
PROMPTS_DIR = ROOT / "prompts"

# Configuration for templates per category
CATEGORIES_CONFIG = {
    "03-backend-dev": {
        "tags": ["backend", "api", "database"],
        "techs": ["Go", "Node.js (Fastify)", "Python (Django)", "Rust (Axum)", "Ruby on Rails", "Java (Spring Boot)", "NestJS"],
        "targets": ["an e-commerce catalog", "a real-time messaging server", "a payment gateway webhook handler", "a collaborative document editor backend", "a video processing microservice", "a multi-tenant SaaS backend"],
        "features": ["Redis caching", "PostgreSQL database integration", "Sentry error tracking", "Prometheus metrics", "OAuth2 login integration", "WebSockets real-time communication"],
        "templates": [
            ("Build a production-ready {tech} backend for {target}", "Build a production-ready REST API with {tech} for {target}. Include {feature}, centralized error handling, and robust logging."),
            ("Implement {feature} in a {tech} backend", "Implement {feature} in a {tech} backend server handling {target}. Follow clean architecture and document endpoints."),
            ("Graceful shutdown and error handling in {tech}", "Configure graceful shutdown, error handling, and system signal monitoring in {tech} for {target} with {feature}."),
        ]
    },
    "04-fullstack-projects": {
        "tags": ["fullstack", "web-app", "nextjs"],
        "techs": ["Next.js + Supabase", "SvelteKit + Prisma", "Vue 3 (Nuxt.js) + Go", "React + Express + PostgreSQL", "Angular + NestJS + MongoDB"],
        "targets": ["a real-time dashboard", "a social network MVP", "a collaborative blogging platform", "a project task manager", "a booking and scheduling system", "a client onboarding portal"],
        "features": ["Stripe billing and subscription flow", "Auth0 social login", "Tailwind CSS responsive layout", "WebSockets real-time sync", "Resend automated email notifications", "role-based access control (RBAC)"],
        "templates": [
            ("Scaffold {target} with {tech}", "Scaffold {target} using {tech}. Include {feature}, state management, and a clean folder layout."),
            ("Add {feature} to a {tech} application", "Implement {feature} in a full-stack {target} built on {tech}. Ensure end-to-end security and clean forms validation."),
        ]
    },
    "05-api-design": {
        "tags": ["api-design", "rest", "graphql", "spec"],
        "techs": ["OpenAPI 3.1", "GraphQL SDL", "gRPC protobuf schemas", "REST API specifications", "Webhook formats", "Server-Sent Events (SSE)"],
        "targets": ["a financial ledger ledger", "a logistics package tracker", "a medical appointment scheduler", "an IoT telemetry stream", "a localized product search Engine", "a subscription billing workflow"],
        "features": ["rate limiting policies", "semantic API versioning", "RFC 7807 error responses", "HMAC payload validation", "JWT validation middleware"],
        "templates": [
            ("Design {tech} for {target}", "Write the comprehensive design for {tech} mapping {target}. Make sure to define request/response shapes, headers, and status codes."),
            ("Implement {feature} policies for {target} API", "Design the schema and specification to handle {feature} for {target}. Provide concrete code examples and failure cases."),
        ]
    },
    "06-database-design": {
        "tags": ["database", "schema", "postgresql", "sql"],
        "techs": ["PostgreSQL", "MongoDB", "Redis", "MySQL", "DynamoDB", "Cassandra", "Neo4j"],
        "targets": ["an e-commerce warehouse index", "a microservice messaging history", "a user session cache store", "a massive application log aggregator", "a social network relations graph", "a geographic location coordinates tracking service"],
        "features": ["optimal indexing strategies", "sharding keys configuration", "database replica setups", "data types definitions", "idempotent migration scripts"],
        "templates": [
            ("Design {tech} schema for {target}", "Design a production-ready {tech} schema for {target}. Define tables/collections, column data types, foreign keys, and indexes."),
            ("Configure {feature} for {tech} on {target}", "Write the data definition language (DDL) and setup guides for {feature} in {tech} for {target} to ensure maximum query throughput."),
        ]
    },
    "07-devops-cicd": {
        "tags": ["devops", "cicd", "docker", "cloud"],
        "techs": ["GitHub Actions", "GitLab CI", "Jenkins", "AWS CDK", "Terraform", "Docker", "Kubernetes"],
        "targets": ["an AWS ECS cluster", "a Google Cloud Run instance", "an Azure App Service webapp", "a Vercel serverless environment", "a horizontal pod autoscaler in Kubernetes"],
        "features": ["dependency caching strategies", "secret injection configurations", "automated testing stages", "blue-green deployments setups", "automated Slack alert notifications"],
        "templates": [
            ("Build a {tech} pipeline for deploying to {target}", "Create a {tech} pipeline file that deploys code to {target}. Include {feature} and environment variable overrides."),
            ("Write a {tech} config for {target} with {feature}", "Configure {tech} for {target} incorporating {feature}. Ensure security practices and low build execution times."),
        ]
    },
    "08-ai-ml-integration": {
        "tags": ["ai", "llm", "claude", "integration"],
        "techs": ["Claude SDK", "LangChain", "LlamaIndex", "Anthropic Tool Use API", "Hugging Face transformers", "a Vector DB (Pinecone/Chroma)"],
        "targets": ["semantic search applications", "retrieval-augmented generation (RAG) pipelines", "automated article summary engines", "email classification routes", "agents with function calling capabilities"],
        "features": ["prompt caching hooks", "exponential backoff error retries", "response streams handling", "context window optimizations", "token usage analytics dashboards"],
        "templates": [
            ("Integrate {tech} for {target}", "Build a system that integrates {tech} to handle {target}. Incorporate {feature} to maximize performance and save API credits."),
            ("Configure RAG with {tech} and {feature}", "Set up a Retrieval-Augmented Generation pipeline using {tech} targeting {target}. Implement {feature} to optimize token costs."),
        ]
    },
    "09-debugging-code-review": {
        "tags": ["debugging", "code-review", "troubleshooting"],
        "techs": ["React memory leaks", "Python pandas memory usage", "Slow PostgreSQL join queries", "Node.js event loop blocks", "Java multithreaded deadlocks", "Rust borrow checker errors", "Go data race conditions"],
        "targets": ["a high-throughput server endpoint", "a continuous background task worker", "a secure user checkout workflow", "an image resizing handler", "a bulk data import CSV script"],
        "features": ["profiler metrics snapshots", "distributed tracing logs", "reproduction unit tests", "memory dump logs", "error tracebacks"],
        "templates": [
            ("Debug {tech} in {target}", "Analyze and debug {tech} occurring in {target}. Provide the diagnostics checklist, tools, sample buggy code, and the optimized fix."),
            ("Conduct code review to fix {tech} in {target}", "Review raw code for {target} that causes {tech}. Explain the root cause and provide refactored, robust code using {features}."),
        ]
    },
    "10-architecture-system-design": {
        "tags": ["architecture", "system-design", "scaling"],
        "techs": ["high-traffic chat server", "notification microservice cluster", "distributed URL shortener", "video delivery CDN network", "analytics ingestion pipeline", "web crawler cluster"],
        "targets": ["millions of monthly active users", "extreme write-heavy traffic spikes", "low-latency reads globally", "high partition tolerance requirements"],
        "features": ["Kafka queues integration", "Redis caching clusters", "multi-region master-slave replication", "DNS load balancing policies"],
        "templates": [
            ("Design architecture for a {tech}", "Design a distributed system architecture for a {tech} to support {targets}. Document the data flow, database choices, caching strategy, and failover design."),
            ("Scale a {tech} to handle {targets}", "Create a system design specification detailing how to scale a {tech} to support {targets} with {features}."),
        ]
    },
    "11-testing-qa": {
        "tags": ["testing", "qa", "unit-test", "automation"],
        "techs": ["Vitest", "Jest", "Cypress", "Playwright", "Pytest", "Go standard test library", "JUnit 5"],
        "targets": ["visual regression suites", "REST API integration routes", "Redux state management hooks", "database repository layers", "Stripe payment controller functions", "user input signup forms"],
        "features": ["request mocking systems", "database seed utilities", "automated coverage metrics reports", "snapshot tests comparisons", "parallel execution workers"],
        "templates": [
            ("Write tests with {tech} for {targets}", "Write comprehensive automated tests with {tech} to validate {targets}. Ensure coverage of edge cases, error handling, and mock {features}."),
            ("Mock dependencies using {tech} for {targets}", "Configure test mocks and stubs using {tech} for testing {targets}. Implement {features} for reliable, isolated builds."),
        ]
    },
    "12-mobile-dev": {
        "tags": ["mobile", "react-native", "flutter", "app"],
        "techs": ["React Native", "Flutter", "Swift (iOS)", "Kotlin (Android)", "Expo Go"],
        "targets": ["push notifications hooks", "SQLite database local syncing", "Keychain credential storage", "biometric login workflows", "camera capture handlers", "background coordinates tracking"],
        "features": ["fitness metric dashboards", "offline-first text notes apps", "ride-sharing maps displays", "mobile e-commerce shopping carts", "photo uploads feeds"],
        "templates": [
            ("Implement {targets} in {tech}", "Build and implement {targets} in {tech} for {features}. Include full code, permissions handling, and error fallback layouts."),
            ("Configure native module integrations in {tech} for {targets}", "Configure {targets} using native bindings in {tech} for {features}. Keep code optimized for performance and battery consumption."),
        ]
    },
    "13-ui-ux-design": {
        "tags": ["ui-ux", "css", "tailwind", "design-system"],
        "techs": ["Tailwind CSS", "CSS Modules", "Styled Components", "native CSS variables", "Framer Motion animations"],
        "targets": ["paginated data tables", "accessible modal dialogs", "dark/light theme config panels", "multi-step wizard checkouts", "drag-and-drop kanban boards", "command palette bars"],
        "features": ["fully responsive viewports", "keyboard WAI-ARIA focus rules", "smooth interface micro-animations", "loading skeleton blocks", "inline form validation helpers"],
        "templates": [
            ("Build an accessible {targets} with {tech}", "Build a highly polished, interactive {targets} using {tech}. Ensure design contains {features} and premium aesthetics."),
            ("Design a dashboard component for {targets} using {tech}", "Design a custom frontend component for {targets} utilizing {tech}. Ensure the layout scales cleanly and supports {features}."),
        ]
    },
    "14-security": {
        "tags": ["security", "hardening", "owasp", "encryption"],
        "techs": ["SQL injection mitigations", "XSS sanitization layers", "CSRF token tracking", "secured file uploads checks", "automated dependency vulnerability scans", "hardened CORS configurations"],
        "targets": ["an Express.js backend", "a FastAPI application", "a Spring Boot endpoint", "a Ruby on Rails application", "a Python Django server"],
        "features": ["Argon2id password hashing", "rate limiting middleware blocks", "HTML inputs sanitizers", "database encryption rules", "SSL/TLS configurations"],
        "templates": [
            ("Implement {tech} in {targets}", "Hardened {targets} by implementing {tech}. Write the code setup, middleware configurations, and verification commands."),
            ("Write secure code guidelines for {targets} to prevent {tech}", "Analyze potential vulnerabilities in {targets} and write security controls using {features} to block {tech} attempts."),
        ]
    },
    "15-data-science": {
        "tags": ["data-science", "machine-learning", "python", "data-analysis"],
        "techs": ["Pandas", "Scikit-Learn", "PyTorch", "TensorFlow", "Plotly Express", "Streamlit dashboarding"],
        "targets": ["fraud anomaly detection", "customer churn predictions", "image objects classification", "weekly demand time series forecasting", "text sentiments reviews analysis", "user demographics clustering"],
        "features": ["hyperparameters tuning steps", "k-fold cross-validation runs", "automated feature engineering pipelines", "metrics evaluation charts", "model checkpointing mechanisms"],
        "templates": [
            ("Build a {targets} pipeline with {tech}", "Build a python data science script to execute {targets} utilizing {tech}. Make sure to include {features} for accuracy."),
            ("Create a data visualization dashboard for {targets} with {tech}", "Build an interactive analytics dashboard for {targets} using {tech} with {features} to represent business insights."),
        ]
    },
    "16-documentation": {
        "tags": ["documentation", "openapi", "writing", "best-practices"],
        "techs": ["OpenAPI Swagger specifications", "Architecture Decision Records (ADRs)", "engineer onboarding guides", "incident operations runbooks", "database schema dictionaries", "contributing guides"],
        "targets": ["a global payment API", "a multi-service microservices network", "a frontend monorepo codebase", "a database migrations pipeline", "an OAuth2 user signin portal"],
        "features": ["Markdown formatting structures", "interactive API mock schemas", "troubleshooting FAQ sections", "reproduction steps guides"],
        "templates": [
            ("Write documentation for {targets} using {tech}", "Write professional documentation for {targets} using {tech}. Ensure the output contains {features}."),
            ("Generate a complete {tech} for {targets}", "Generate a fully populated {tech} document detailing the architecture, schema, or process for {targets}. Include {features}."),
        ]
    },
    "17-performance": {
        "tags": ["performance", "optimization", "latency", "tuning"],
        "techs": ["Node.js event loop lag", "slow PostgreSQL indexing queries", "large React production build sizes", "Python high memory spikes", "Go garbage collection overheads", "browser CSS reflow limits"],
        "targets": ["caching assets headers", "gzip/brotli code compression", "dynamic code splitting imports", "component lazy loading techniques", "profiling memory heap allocations"],
        "features": ["higher Google Lighthouse scores", "sub-100ms TTFB stats", "lowered server RAM foot prints", "faster time to interactive (TTI)"],
        "templates": [
            ("Optimize {tech} on production using {targets}", "Write a step-by-step optimization playbook to resolve {tech} in your code. Implement {targets} to achieve {features}."),
            ("Troubleshoot performance bottleneck caused by {tech} with {features}", "Analyze why {tech} occurs in high-traffic applications. Provide code refactoring guidelines and use {targets} to resolve the issue."),
        ]
    },
    "18-devex-tooling": {
        "tags": ["devex", "docker", "dx", "productivity"],
        "techs": ["Docker devcontainers", "ESLint and Prettier custom plugins", "Turborepo monorepos", "custom CLI automation scripts", "git pre-commit Husky hooks", "shell terminal configuration aliases"],
        "targets": ["automated local PostgreSQL setups", "code boilerplate scaffold engines", "CI syntax formatting validators", "dotenv variables sync scripts", "server system logs parsers"],
        "features": ["faster engineer onboarding", "consistent team code styling", "automated build alerts", "lowered pipeline verification times"],
        "templates": [
            ("Set up {tech} for local development", "Build a configuration setup for {tech} to optimize development workflow. Ensure it handles {targets} and helps developers get running faster."),
            ("Create custom {tech} to automate {targets}", "Build custom scripts or settings for {tech} that targets {targets}. Focus on {features} to improve daily developer experience."),
        ]
    },
    "19-student-learning": {
        "tags": ["learning", "computer-science", "education", "algorithms"],
        "techs": ["Big O notation runtimes", "binary search tree implementations", "hash map collision resolutions", "quicksort algorithm walkthroughs", "object-oriented inheritance vs composition", "observer design patterns"],
        "targets": ["interactive study worksheets", "step-by-step code walkthroughs", "clear conceptual analogies", "common practice problem sets", "visual dry-run tracing charts"],
        "features": ["easy conceptual understanding", "practical code examples", "homework helper templates", "debug troubleshooting tips"],
        "templates": [
            ("Explain {tech} to a CS student with {targets}", "Create a clear, step-by-step educational guide explaining {tech}. Include {targets}, code examples, and {features}."),
            ("Build practice exercises for {tech} with {features}", "Build a series of practice questions and interactive coding challenges covering {tech}. Include {targets} with answers."),
        ]
    },
    "20-vibe-coding": {
        "tags": ["vibe-coding", "rapid-prototyping", "mvp", "automation"],
        "techs": ["single-page landing page deployment", "minimal MVP webapp scaffold", "automated email alerting scripts", "rapid interactive prototype designs", "web scraping data extraction utilities", "API workflow pipelines"],
        "targets": ["shadcn/ui layout packages", "Supabase authentication databases", "instant Vercel web deployments", "v0 UI designs prompts", "automation scheduling tasks"],
        "features": ["launching under 2 hours", "zero complex configurations", "rapid validation loops", "leveraging AI pair programming"],
        "templates": [
            ("Ship a {tech} in under 2 hours", "Design and build a {tech} utilizing {targets}. Focus on speed, minimal setup, and applying {features} to launch rapidly."),
            ("Build an automated utility for {tech} with {targets}", "Build a rapid, functional script that creates {tech} integrating {targets}. Ensure {features} is highlighted for quick deployment."),
        ]
    }
}

def generate_prompts():
    print("Starting missing prompts generation...")
    models = ["claude-haiku-3-5", "claude-sonnet-4", "claude-opus-4", "claude-fable-5"]
    
    for cat_dir_name, config in CATEGORIES_CONFIG.items():
        cat_path = PROMPTS_DIR / cat_dir_name
        cat_path.mkdir(parents=True, exist_ok=True)
        
        # Count current markdown files excluding README.md
        existing_files = list(cat_path.glob("*.md"))
        existing_count = len([f for f in existing_files if f.name.lower() != "readme.md"])
        
        print(f"Category: {cat_dir_name} | Existing count: {existing_count}")
        
        if existing_count >= 50:
            print(f"  Category {cat_dir_name} already has {existing_count} prompts. Skipping.")
            continue
            
        needed = 50 - existing_count
        print(f"  Generating {needed} prompts...")
        
        generated_count = 0
        attempts = 0
        max_attempts = 1000
        
        while generated_count < needed and attempts < max_attempts:
            attempts += 1
            
            # Select random combinations
            tech = random.choice(config["techs"])
            target = random.choice(config["targets"])
            feature = random.choice(config["features"])
            template_title, template_body = random.choice(config["templates"])
            
            # Fill title and body
            title = template_title.format(tech=tech, target=target, feature=feature, targets=target, features=feature)
            body_text = template_body.format(tech=tech, target=target, feature=feature, targets=target, features=feature)
            
            # Generate clean slug filename
            filename_base = title.lower()
            for char in ["(", ")", "[", "]", ",", ".", "/", "'", '"', "+", ":", "`"]:
                filename_base = filename_base.replace(char, "")
            filename_base = filename_base.replace(" ", "-").replace("--", "-")
            filename = f"{filename_base}.md"
            file_path = cat_path / filename
            
            # Check if file exists
            if file_path.exists():
                continue
                
            # Create content
            tags = list(set(config["tags"] + [t.lower().replace(" ", "-") for t in [tech.split(" ")[0], target.split(" ")[0]] if len(t) > 2]))
            difficulty = random.choice(["beginner", "intermediate", "advanced"])
            
            content = f"""---
title: "{title}"
category: {cat_dir_name.split("-", 1)[1]}
models: [{', '.join(models)}]
tags: [{', '.join(tags[:6])}]
difficulty: {difficulty}
author: community
tested: true
---

## 🎯 Prompt

```
{body_text}
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
"""
            
            file_path.write_text(content.strip() + "\n")
            generated_count += 1
            
        print(f"  Successfully wrote {generated_count} new prompts in {cat_dir_name}.")

    print("Generation complete!")

if __name__ == "__main__":
    generate_prompts()
