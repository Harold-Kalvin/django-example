PROJECT_NAME := $(notdir $(shell pwd))
CONTAINER_NAME := $(PROJECT_NAME)-web-1

all: down build up

build:
	docker compose build

up:
	docker compose up

down:
	docker compose down

stop:
	docker compose stop

restart:
	docker compose restart

sh:
	docker exec -it $(CONTAINER_NAME) sh

migrations:
	docker exec $(CONTAINER_NAME) sh -c "python manage.py makemigrations --name $(name) $(app)"

migrate:
	docker exec $(CONTAINER_NAME) sh -c "python manage.py migrate"

fmt:
	uv run ruff check --select I --fix .
	uv run ruff format

lint:
	uv run ruff check

type-check:
	uv run mypy .

checks: fmt lint type-check

fmt-templates:
	uv run djlint . --reformat

lint-templates:
	uv run djlint . --lint

checks-templates: fmt-templates lint-templates

requirements:
	uv export --no-group dev --no-hashes --format requirements-txt > requirements.txt
