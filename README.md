# Проект Трекер развития
## Описание проекта

Платформа "Трекер развития" позволяет пользователю (студенту или выпускнику Яндекс Практикума) отслеживать свой личный прогресс и изучении навыков, а так же получать рекомендации на основе них. При первом подключении пользователь либо уже имеет набор навыков, в случае если это выпускник, либо имеет возможность добавлять навыки самостоятельно.


## Технологии использованные в проекте:
* Python 3.10
* Django 4.2.7
* DRF 3.14.0
* Docker
* БД PostgreSQL
* REST API

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

    git clone git@github.com:ShelepovNikita/development_tracker_project.git
    cd development_tracker_project


Cоздать в папке infra .env файл с переменными окружения.
Используемые переменные окружения (с примерами):

    DB_HOST=DB_HOST
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=DB_NAME
    POSTGRES_USER=POSTGRES_USER
    POSTGRES_USER=POSTGRES_USER
    POSTGRES_PASSWORD=POSTGRES_PASSWORD
    DB_PORT=DB_PORT

Запустить проект с помощью Docker:

    docker compose up

Документация проекта доступна по адресам:

    http://127.0.0.1:8000/redoc/
    http://127.0.0.1:8000/swagger/


## Как импортировать данные из csv-файлов в базу данных

С помощью management-команд. Для того, чтобы загрузить все данные, из корневой директории проекта выполните команду:

    docker exec -it development_tracker_backend python manage.py import_csv

Чтобы загрузить данные из определённого файла для конкретной модели, выполните команду:

    docker exec -it development_tracker_backend python manage.py import_csv --path <путь к csv-файлу> --model_name <имя модели> --app_name <название приложения>

Данные из файлов необходимо загружать в следующем порядке:

* courses.csv
* skills.csv
* selections.csv
* course_skill.csv
* selection_skill.csv

## Авторизация:

Авторизация по токену. Необходимо создать пользователя через админ панель и сделать ему токен. Все запросы передавать вместе с токеном в headers (authorization: "Token ...")
Авторизация не входила в MVP, предполагается интеграция с сервисами Яндекса.

## Примеры запросов к API:

Получение списка всех скиллов (GET):

    http://localhost:8000/api/v1/skills/

Добавление навыка пользователю (POST):

    http://localhost:8000/api/v1/skills/

Получение списка скиллов пользователя(GET):

    http://localhost:8000/api/v1/userData/

Получение списка рекомендаций курсов на основе скиллов пользователя(GET):

    http://localhost:8000/api/v1/recommended-courses-tracker/

Получение списка рекомендаций курсов на основе открытого скилла (режим редактирования)(GET):

    http://localhost:8000/api/v1/recommended-courses-skill/int:pk/


**Проект написан в рамках Хакатон+, разработка MVP сервиса Трекер Развития.**


## Над проектом работали

[ShelepovNikita](https://github.com/ShelepovNikita) - Шелепов Никита

[terrazavr](https://github.com/Lexxar91) - Муратов Дмитрий
