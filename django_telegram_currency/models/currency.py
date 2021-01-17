from django.db import models
from django.utils.translation import ugettext_lazy as _


class Currency(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False, verbose_name=_('Currency'))
    value = models.FloatField(verbose_name=_('Course'), blank=False, null=False)
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name=_('Updated at'))

    def __str__(self):
        return f'Currency {self.name}, value: {self.value}'

    class Meta:
        verbose_name = _('Currency')
        verbose_name_plural = _('Currencies')
