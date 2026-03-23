# Makefile
#
# Operation interface for {{cookiecutter.project_name}}.
# Usage: make <command>
#
# Convention: targets with ## appear in `make help`.
# Targets without ## are internal (not shown).


# .PHONY tells make that these targets are not files.
# Without this, if a file named "test" existed, make would not execute the target
.PHONY: help dev prod down down-clean test lint lint-fix status health clean

# ── Help ──────────────────────────────────────────────────────────────────────
# This target is the first in the file → it runs with `make` without arguments.
# The grep/awk trick automatically extracts the ## comments as help.
help: ## Shows available commands
	@echo ""
	@echo "  {{cookiecutter.project_name}}"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo ""

# ── Environments ───────────────────────────────────────────────────────────────
dev: ## Starts the development stack with hot-reload
	docker compose up --build

prod: ## Starts the full production stack in background
	docker compose -f docker-compose.prod.yml up -d
	@echo ""
	@echo "  Production stack started:"
	@echo "  API        → http://localhost:{{cookiecutter.api_port}}/docs"
	@echo "  MLflow     → http://localhost:{{cookiecutter.mlflow_port}}"
	@echo ""

down: ## Stops all services (data is preserved)
	docker compose -f docker-compose.prod.yml down

down-clean: ## Stops all services and removes volumes (total reset)
	docker compose -f docker-compose.prod.yml down -v
	@echo "  All volumes removed (MLflow, models)"

# Code quality
test: ## Unit testing
	pytest tests/ -v --cov=src --cov-report=term-missing

lint: ## 
	ruff check src/ api/ tests/

lint-fix: ##
	ruff check --fix src/ api/ tests/

# Operations
status: ## Check status of services
	docker compose -f docker-compose.prod.yml ps

health: ## Checks if API is healthy
	@curl -s http://localhost:{{cookiecutter.api_port}}/health \
		| python -m json.tool

# Clean
clean: ## Removes python cache files and temp files
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	rm -rf .pytest_cache .coverage coverage.xml .ruff_cache
	@echo " Cleaned "
