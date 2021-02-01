import requests

import xml.dom.minidom

from django.db import models
from django.utils.translation import ugettext as _


class Currency(models.Model):

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

    def parse_currency(self):
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
                        "value": value
                    })
            return data

    def get_currency(self):
        raise NotImplementedError()

    def set_cache_currency(self):
        pass
