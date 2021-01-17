from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CurrencyConfig(AppConfig):
    name = 'django_telegram_currency'
    verbose_name = _('Currencies')
