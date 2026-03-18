# Makefile
#
# Operation interface for {{cookiecutter.project_name}}.
# Usage: make <command>
#
# Convention: targets with ## appear in `make help`.
# Targets without ## are internal (not shown).


# .PHONY tells make that these targets are not files.
# Without this, if a file named "test" existed, make would not execute the target
.PHONY: help dev down down-clean status health clean

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

down: ## Stops all services (data is preserved)
	docker compose down

down-clean: ## Stops all services and removes volumes (total reset)
	docker compose down -v
	@echo "  All volumes removed (MLflow, models)"

# Operations
status: ## Check status of services
	docker compose ps

health: ## Checks if API is healthy
	@curl -s http://localhost:{{cookiecutter.api_port}}/health \
		| python -m json.tool

# Clean
clean: ## Removes python cache files and temp files
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	rm -rf .pytest_cache .coverage coverage.xml .ruff_cache
	@echo "  Limpieza completada"
