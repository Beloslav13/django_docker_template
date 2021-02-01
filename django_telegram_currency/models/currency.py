import time

import requests

import xml.dom.minidom

from django.db import models
from django.core.cache import cache
from django.utils.translation import ugettext as _


class Currency(models.Model):
    CURRENCY_CACHE_KEY = 'currency_value'
    CURRENCY_CACHE_DURATION = 1000

    CURRENCY_UNDEFINED = 0
    CURRENCY_USD = 10
    CURRENCY_EUR = 20

    CURRENCY_CHOICE = {
        CURRENCY_UNDEFINED: _('Undefined'),
        CURRENCY_USD: _('USD'),
        CURRENCY_EUR: _('EUR')
    }

    name = models.PositiveSmallIntegerField(choices=[(k, v) for k, v in CURRENCY_CHOICE.items()],
                                            verbose_name=_('Currency'), default=CURRENCY_UNDEFINED)
    value = models.FloatField(verbose_name=_('Course'), blank=False, null=False)
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name=_('Updated at'))

    def __str__(self):
        return _(f'Currency {self.name}, value: {str(self.value)}')

    class Meta:
        verbose_name = _('Currency')
        verbose_name_plural = _('Currencies')

    @staticmethod
    def parse_currency():
        base_url = 'https://www.cbr-xml-daily.ru/daily_utf8.xml'
        try:
            resp = requests.get(base_url)
        except Exception as exc:
            print(f'Error: {exc}')
        else:
            dom = xml.dom.minidom.parseString(resp.text)
            dom.normalize()

            data = {}
            for currency in dom.getElementsByTagName('Valute'):
                name = currency.getElementsByTagName('CharCode')[0].childNodes[0].nodeValue
                if name == 'USD':
                    value = currency.getElementsByTagName('Value')[0].childNodes[0].nodeValue
                    value = value.replace(',', '.')
                    data.update({
                        "name": name,
                        "value": float(value)
                    })
            return data

    def start_task_set_cache_currency(self):
        from django_telegram_currency.tasks import set_cache_currency
        set_cache_currency.apply_async(
            kwargs={
                'cache_key': self.CURRENCY_CACHE_KEY,
                'cache_duration': self.CURRENCY_CACHE_DURATION
            }
        )

    def get_currency(self):
        currency_data = cache.get(self.CURRENCY_CACHE_KEY, None)
        if currency_data is None:
            self.start_task_set_cache_currency()
        else:
            time.sleep(5)
            try_currency_data = cache.get(self.CURRENCY_CACHE_KEY, None)
            return try_currency_data if try_currency_data is not None else ""

    def update_currency_value(self):
        """Тестовое обновление валюты"""
        currencies = Currency.objects.all()
        currency_data = cache.get(self.CURRENCY_CACHE_KEY, None)
        if currency_data is None:
            self.get_currency()
            time.sleep(10)
        currency_data = cache.get(self.CURRENCY_CACHE_KEY, None)
        for currency in currencies:
            setattr(currency, 'value', currency_data['value'])
            currency.save()
