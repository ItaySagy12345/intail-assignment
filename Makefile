# Python venv Management
init:
	python3 -m venv ../venv
	../venv/bin/pip install --upgrade pip
	../venv/bin/pip install -r requirements.txt

destroy:
	rm -rf ../venv

# Alembic Migration Management
generate-migration:
	@read -p "Enter migration description: " description && alembic -c ./alembic.ini revision --autogenerate -m "$$description"

upgrade-migration:
	alembic upgrade head

downgrade-migration:
	alembic downgrade -1

# Docker Compose
build:
	docker compose up --build

up:
	docker compose up

down:
	docker compose down
	docker rmi server
	docker image prune
	docker volume prune