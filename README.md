# development_tracker_project
Hackathon+ development tracker from Yandex

## Docker develop mode
Клонировать репозиторий и перейти в него в командной строке:

    html git clone git@github.com:ShelepovNikita/development_tracker_project.git
    cd development_tracker_project

Перейти в папку backend:

    cd backend

Создать образ бэкэнда:

    sudo docker build -t development_tracker_backend .

Запустить контейнер из образа:

    sudo docker run --name development_tracker_backend_container --rm -p 8000:8000 development_tracker_backend

Доступ к документации по адресу

    http://localhost:8000/swagger/
