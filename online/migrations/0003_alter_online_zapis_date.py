# Generated by Django 4.2 on 2023-07-15 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0002_alter_online_zapis_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='online_zapis',
            name='date',
            field=models.DateField(choices=[('15-07-2023', '15-07-2023'), ('16-07-2023', '16-07-2023'), ('17-07-2023', '17-07-2023'), ('2023-07-18', '2023-07-18')], default='', max_length=10, verbose_name='Дата'),
        ),
    ]
