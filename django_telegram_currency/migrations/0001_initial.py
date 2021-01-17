# Generated by Django 3.1.5 on 2021-01-17 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Currency')),
                ('value', models.FloatField(verbose_name='Course')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'Currency',
                'verbose_name_plural': 'Currencies',
            },
        ),
    ]