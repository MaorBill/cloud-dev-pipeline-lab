.PHONY: check lint typecheck test

check: lint typecheck test

lint:
	python3 -m ruff check .

typecheck:
	python3 -m mypy src

test:
	python3 -m pytest
