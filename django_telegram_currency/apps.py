from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

import logging


class CurrencyConfig(AppConfig):
    name = 'django_telegram_currency'
    verbose_name = _('Currencies')


class CeleryBeatConfig(AppConfig):
    name = 'django_celery_beat'
    verbose_name = _('Django Celery')
    logger = logging.getLogger('django_celery_beat')


class CeleryResultsConfig(AppConfig):
    name = 'django_celery_results'
    verbose_name = _('Django Celery')
    logger = logging.getLogger('django_celery_results')
