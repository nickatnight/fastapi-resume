ruff:
	@echo "running ruff...."
	uv run ruff check .

black:
	@echo "running black...."
	uv run black .

isort:
	@echo "running isort...."
	uv run isort .

mypy:
	@echo "running mypy...."
	uv run mypy .

lint-all: black isort ruff mypy

test:
	@echo "running tests...."
	uv run pytest --cov-report=html --cov=fastapi_resume/ tests/ -vv

sphinx:
	@echo "building docs...."
	uv run sphinx-build -b html docs/source docs/build
