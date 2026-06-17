---
title: "Create a Project Makefile"
category: devex-tooling
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [makefile, automation, developer-experience, scripts]
difficulty: beginner
author: community
tested: true
---

## 🎯 Prompt

```
Create a project Makefile with useful developer commands.

Project: [DESCRIBE YOUR STACK]

Makefile targets to create:

```makefile
.PHONY: help up down logs shell db test lint build deploy

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk '...'

up:  ## Start all services
	docker compose up -d

down:  ## Stop all services  
	docker compose down

logs:  ## Tail logs
	docker compose logs -f

shell:  ## Open shell in app container
	docker compose exec app sh

db:  ## Open database CLI
	docker compose exec db psql -U postgres

test:  ## Run tests
	npm test

lint:  ## Run linters
	npm run lint

build:  ## Build for production
	npm run build

migrate:  ## Run database migrations
	npm run migrate

deploy:  ## Deploy to production
	./scripts/deploy.sh
```

For my specific project: all relevant targets.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
