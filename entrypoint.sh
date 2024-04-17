#!/bin/bash

# Executa as migrações do Django
python manage.py migrate

# Inicia o servidor Django
python manage.py runserver 0.0.0.0:8000

exec "$@"