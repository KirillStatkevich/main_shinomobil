from django.db import models
from django.core.validators import RegexValidator
from . import logic
# Create your models here.

class online_zapis (models.Model):
    name = models.CharField('Как к Вам обращаться?', default='', max_length=50)
    place = models.CharField('Куда нам приехать?', default="", max_length=100)
    date = models.DateField('Дата', choices=logic.datechoce(), default='', max_length=10)
    phone_number = models.CharField('Контактный телефон:', default='', max_length=20, validators=[
        RegexValidator(
            r'^\+375\d{9}$', message='Номер телефона должен быть введен в формате: +375XXXXXXXXX')])
    time = models.CharField('Время', max_length=5, choices=logic.time_choice())
    main_text = models.TextField('Комментарий', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Онлайн запись'
        verbose_name_plural = 'Онлайн записи'
