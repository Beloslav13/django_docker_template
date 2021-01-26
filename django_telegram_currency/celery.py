import os

from django.conf import settings

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_telegram_currency.settings')

app = Celery('django_telegram_currency')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True, name='debug_task')
def debug_task(self):
    print(f'Request: {self.request!r}')
