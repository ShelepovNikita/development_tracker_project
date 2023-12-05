from django.core.validators import MinLengthValidator
from django.db import models
from users.models import User


class DefaultSkill(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название навыка')

    class Meta:
        verbose_name = 'Навык по умолчанию'
        verbose_name_plural = 'Навыки по умолчанию'


class EditableSkill(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Название навыка',
        validators=[MinLengthValidator(2)]
    )
    rate = models.IntegerField(verbose_name='Оценка')
    notes = models.CharField(max_length=100, verbose_name='Заметки')

    class Meta:
        verbose_name = 'Редактируемый навык'
        verbose_name_plural = 'Редактируемые навыки'
