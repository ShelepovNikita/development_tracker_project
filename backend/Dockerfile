FROM python:3.10.12

# Переходим в образе в директорию /development_tracker_app:
# Если директории с указанным именем нет, она будет создана. 
WORKDIR /development_tracker_app

# Дальнейшие инструкции будут выполняться в директории /development_tracker_app
# Скопировать с локального компьютера файл зависимостей
# в текущую директорию (текущая директория — это /development_tracker_app).
COPY requirements.txt .

# Выполнить в текущей директории команду терминала
# для установки зависимостей.
RUN pip install -r requirements.txt --no-cache-dir

# Скопировать всё необходимое содержимое 
# той директории локального компьютера, где сохранён Dockerfile,
# в текущую рабочую директорию образа — /development_tracker_app.
COPY development_tracker/ .

# Копирование entrypoint.sh в контейнер
COPY entrypoint.sh /

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
# При старте контейнера запустить сервер разработки.
#CMD ["python", "manage.py", "runserver", "0:8000"]