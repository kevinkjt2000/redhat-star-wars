.PHONY: test
test:
	poetry run pytest -vvv --exitfirst tests/

.PHONY: bootstrap
bootstrap:
	poetry install
