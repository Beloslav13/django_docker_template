from django.contrib import admin

from django_telegram_currency.models.currency import Currency


class CurrencyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Currency, CurrencyAdmin)
