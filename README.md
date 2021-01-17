**Сборка проекта локально:**

- склонировать репозиторий
- зайти в каталог django_telegram_currency
- в корне проекта создать файл .env и прописать туда переменные
  - **DOCKER_PROJ_PATH**: пусть где лежит проект
  - **POSTGRES_USER POSTGRES_DB POSTGRES_PASSWORD POSTGRES_HOST POSTGRES_PORT PGDATA PROJ_SECRET_KEY**
    

- сделать билд проекта `(docker-compose build)`
- запустить (если у вас Linux)
    - `docker exec -it --user $(id -u):$(id -g) django_telegram_currency_app_1 bash`
    - остальные OC `docker exec -it django_telegram_currency_app_1 bash`
- если база данных была новая то создать и применить миграции
- `python manage.py makemigrations python manage.py migrate`
- если база данных есть `python manage.py migrate`
- запустить сервер `python manage.py runserver 0.0.0.0:8000`