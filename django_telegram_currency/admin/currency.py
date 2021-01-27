from django.contrib import admin

from django_telegram_currency.models.currency import CurrencyUSD


class CurrencyUSDAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value', 'updated_at')
    list_display_links = ('id', 'name', 'value', 'updated_at')


admin.site.register(CurrencyUSD, CurrencyUSDAdmin)
