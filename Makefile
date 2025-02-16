.PHONY: up
up:
	docker compose up -d

.PHONY: down
down:
	docker compose down --rmi all --volumes --remove-orphans

.PHONY: restart
restart:
	docker compose restart

.PHONY: test
test:
	docker compose run --entrypoint "poetry run pytest" app
