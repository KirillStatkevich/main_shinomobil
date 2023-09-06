# Generated by Django 4.2 on 2023-07-15 15:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0004_alter_online_zapis_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='online_zapis',
            name='date',
            field=models.DateField(choices=[(datetime.date(2023, 7, 15), '2023-07-15'), (datetime.date(2023, 7, 16), '2023-07-16'), (datetime.date(2023, 7, 17), '2023-07-17'), ('2023-07-18', '2023-07-18')], default='', max_length=10, verbose_name='Дата'),
        ),
    ]