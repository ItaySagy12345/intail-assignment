# App
.PHONY: app
app:
	cd app && npm run dev

# Server
.PHONY: server
server:
	cd server/src && PYTHONPATH=$(PWD)/server uvicorn server:app --host 0.0.0.0 --port 8000 --reload

# Redis
redis:
	redis-server

redis-clear:
	redis-cli FLUSHALL

# Javascript npm management
init1:
	cd app && npm i

destroy1:
	cd app && rm -rf node_modules package-lock.json

# Python pip management
init2:
	cd server && python3 -m venv venv
	cd server && venv/bin/pip install --upgrade pip
	cd server && venv/bin/pip install -r requirements.txt

destroy2:
	cd server && rm -rf venv

# Alembic Migration Management
generate-migration:
	cd server && read -p "Enter migration description: " description && alembic -c ./alembic.ini revision --autogenerate -m "$$description"

upgrade-migration:
	cd server && alembic upgrade head

downgrade-migration:
	cd server && alembic downgrade -1

# Docker Compose
build:
	cd server && docker compose up --build

up:
	cd server && docker compose up

down:
	cd server && docker compose down
	cd server && docker container prune -f
	cd server && docker rmi server -f
	cd server && docker image prune -f
	cd server && docker volume prune -f
	cd server && docker network prune -f