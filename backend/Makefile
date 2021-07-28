install:
	poetry install

run:
	poetry run python backend/manage.py runserver

gunicorn-run:
	source .venv/bin/activate ; \
	cd backend ; \
	gunicorn backend.wsgi

django-shell:
	cd backend ; \
	poetry run python manage.py shell

migrations:
	poetry run python backend/manage.py makemigrations

migrate:
	poetry run python backend/manage.py migrate

lint:
	poetry run flake8 backend

load-demo-data:
	poetry run python backend/manage.py loaddata backend/memo_api/fixtures/01_sections.yaml ; \
	poetry run python backend/manage.py loaddata backend/memo_api/fixtures/02_notes.yaml
