.PHONY: run_frontend run_backend migrations migrate

install: install_python install_js
install_js:
	yarn install
install_python:
	pipenv sync

run_frontend:
	yarn dev

run_backend:
	pipenv run python manage.py runserver

migrations:
	pipenv run python manage.py makemigrations

migrate:
	pipenv run python manage.py migrate