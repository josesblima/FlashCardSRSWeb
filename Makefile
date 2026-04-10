DB_CONTAINER=flashcards-test-db
DB_USER=user
DB_PASSWORD=password
DB_NAME=flashcards_test_db
DB_PORT=5432

test-db:
	docker run -d \
		--name $(DB_CONTAINER) \
		-e POSTGRES_USER=$(DB_USER) \
		-e POSTGRES_PASSWORD=$(DB_PASSWORD) \
		-e POSTGRES_DB=$(DB_NAME) \
		-p $(DB_PORT):5432 \
		postgres
	@echo "Waiting for database to be ready..."
	@sleep 2
	DATABASE_URL=postgresql://$(DB_USER):$(DB_PASSWORD)@localhost/$(DB_NAME) poetry run alembic upgrade head

test-db-stop:
	docker stop $(DB_CONTAINER)
	docker rm $(DB_CONTAINER)

psql:
	psql postgresql://user:password@localhost/flashcards_test_db

test:
	poetry run pytest

.PHONY: test-db-start test-db-stop test
