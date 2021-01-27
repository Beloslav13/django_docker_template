from django.db import models
from django.utils.translation import ugettext as _


class BaseCurrency(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False, verbose_name=_('Currency'))
    value = models.FloatField(verbose_name=_('Course'), blank=False, null=False)
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name=_('Updated at'))

    def __str__(self):
        return _(f'Currency {self.name}, value: {str(self.value)}')

    class Meta:
        verbose_name = _('Currency')
        verbose_name_plural = _('Currencies')

    def get_currency(self):
        raise NotImplementedError()

    def set_cache_currency(self):
        pass


class CurrencyUSD(BaseCurrency):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'USD'

    class Meta:
        verbose_name = _('Currency USD')
        verbose_name_plural = _('Currencies USD')

    def get_currency(self):
        return self.value
