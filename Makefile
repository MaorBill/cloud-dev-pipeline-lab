.PHONY: check lint typecheck test

check: lint typecheck test

lint:
	python -m ruff check .

typecheck:
	python -m mypy src

test:
	python -m pytest
