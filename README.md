**Шаблон Django app обернутого в docker**


Структура джанго приложения, которая включает в себя БД postgresql, celery, redis.
Подключено дополнительно django_celery_results и django_celery_beat.

По умолчанию celery и celery_beaty запускаются отдельными контейнерами. Есть возможность запустить 
через supervisor вместе с gunicorn, но в данный момент падает celery_beat.
Поэтому оставил пока отдельными контейнерами. 
Папки **config**, **socket** для supervisor.
Все комментарии прописаны в docker-compose.yml и главном Dockerfile