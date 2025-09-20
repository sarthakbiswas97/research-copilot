SHELL := /bin/zsh

.PHONY: up down logs rebuild fmt lint type precommit

up:
	docker compose -f infra/docker-compose.yml up -d --build

down:
	docker compose -f infra/docker-compose.yml down -v

logs:
	docker compose -f infra/docker-compose.yml logs -f

rebuild:
	docker compose -f infra/docker-compose.yml build --no-cache

fmt:
	uv run ruff format .
	uv run black .

lint:
	uv run ruff check .

type:
	uv run mypy .

precommit:
	uv run pre-commit run --all-files


# make up         # Start all services (Docker Compose)
# make down       # Stop and remove containers/volumes
# make logs       # Stream logs from Docker Compose
# make rebuild    # Rebuild containers without cache

# make fmt        # Format code (Ruff + Black)
# make lint       # Lint code with Ruff
# make type       # Type check with Mypy
# make precommit  # Run pre-commit hooks
