import logging

from celery import shared_task
from django.core.cache import cache

from django_telegram_currency.models.currency import Currency

logger = logging.getLogger('logfile')


@shared_task
def set_cache_currency(cache_key, cache_duration):
    res = {
        'success': 0,
        'cache_key': [],
        'error': 0
    }
    try:
        currency_value = Currency.parse_currency()
        cache.set(cache_key, currency_value, cache_duration)
    except Exception as exc:
        res['error'] += 1
        logger.error(f'Error in set cache task: {exc}')
    else:
        res['success'] += 1
        res['cache_key'].append(cache_key)
        logger.info(f'Success in set cache {cache_key}')

    return res

