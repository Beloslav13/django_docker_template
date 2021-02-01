import time

from django.core.management.base import BaseCommand, CommandError

from django_telegram_currency.models.currency import Currency


class Command(BaseCommand):

    def handle(self, *args, **options):
        currencies = Currency.objects.all()
        for currency in currencies:
            data = currency.parse_currency()
            time.sleep(3)
            currency.value = float(data['value'])
            currency.save()
