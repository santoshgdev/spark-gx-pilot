lint:
	uv run pre-commit run --all-files

docker:
	docker build -t spark-gx-pilot .
