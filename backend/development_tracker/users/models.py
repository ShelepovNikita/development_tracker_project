from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

from courses.models import Course
from skills.models import Skill


class CustomUser(AbstractUser):
    """Кастомная модель пользователя для связи с курсами и скиллами."""

    courses = models.ManyToManyField(
        Course,
    )
    user_skills = models.ManyToManyField(
        Skill, through="UserSkill", through_fields=("user", "skill")
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class UserSkill(models.Model):
    """Модель для связи пользователя и скилла.
    Предполагается что после первого входа пользователь уже имеет скиллы
    так как уже прошел хотя бы один курс Яндекс Практикума."""

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name="user_skills",
        unique=True,
    )
    rate = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(
                limit_value=1, message="Минимальное значение - 1"
            ),
            MaxValueValidator(
                limit_value=5, message="Максимальное значение - 5"
            ),
        ],
    )
    notes = models.CharField(max_length=100)
    editable = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Скиллы пользователя"
        verbose_name_plural = "Скиллы пользователя"
