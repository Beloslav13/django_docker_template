import os

from django.conf import settings

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_telegram_currency.settings')

app = Celery('django_telegram_currency')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.update(
    CELERY_DEFAULT_QUEUE=settings.CELERY_DEFAULT_QUEUE,
    CELERY_TIMEZONE='Europe/Moscow',
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_RESULT_SERIALIZER='json',
    CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'


)


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
