#!/bin/bash

# Ожидание доступности базы данных перед выполнением миграций
python manage.py wait_for_db

# Выполнение миграций Django
python manage.py migrate

python manage.py runserver 0:8000