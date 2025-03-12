install:
	uv sync

build:
	uv build

package-install:
	uv tool install --force --python='3.13' dist/*.whl

lint:
	uv run ruff check --fix gendiff

gen-diff:
	uv run gendiff --help
