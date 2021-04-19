.DEFAULT_GOAL := serve
.PHONY: serve detached build stop test


serve:
ifdef input
	poetry run python fakeit/main.py $(input)
else
	poetry run python fakeit/main.py example.json
endif

detached:
	docker-compose up -d

build:
	docker-compose up -d --build

stop:
	docker-compose down

test:
	poetry run pytest -v tests
