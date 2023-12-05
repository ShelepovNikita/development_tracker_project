from django.db import models
from skills.models import DefaultSkill
from users.models import User


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название курса')
    image = models.CharField(max_length=255, verbose_name='Изображение')
    url = models.CharField(max_length=255, verbose_name='URL')
    skill = models.ManyToManyField(
        DefaultSkill,
        through="CourseDefaultSkill",
        through_fields=("course", "skill"),
        verbose_name='Навыки'
    )
    user = models.ManyToManyField(
        User,
        through="CourseUser",
        through_fields=("course", "user"),
        verbose_name='Пользователи'
    )

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


class CourseDefaultSkill(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='Курс'
    )
    skill = models.ForeignKey(
        DefaultSkill,
        on_delete=models.CASCADE,
        verbose_name='Навык'
    )

    class Meta:
        verbose_name = 'Связь курса и навыка'
        verbose_name_plural = 'Связи курсов и навыков'


class CourseUser(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='Курс'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )

    class Meta:
        verbose_name = 'Связь курса и пользователя'
        verbose_name_plural = 'Связи курсов и пользователей'
