.PHONY: run
run:
	poetry install
	poetry run python task_one.py

.PHONY: test
test:
	poetry run pytest -vvv --exitfirst tests/

.PHONY: bootstrap
bootstrap:
	@echo > .env
	@echo MYSQL_ROOT_PASSWORD=$(shell poetry run python -c 'import secrets; print(secrets.token_urlsafe(18))') >> .env
	poetry install
	docker-compose up -d --remove-orphans --force-recreate
