from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

from courses.models import Course
from skills.models import Skill


class CustomUser(AbstractUser):
    courses = models.ManyToManyField(
        Course,
    )
    user_skills = models.ManyToManyField(
        Skill, through="UserSkill", through_fields=("user", "skill")
    )


class UserSkill(models.Model):
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
            MinValueValidator(limit_value=1, message='Минимальное значение - 1'),
            MaxValueValidator(limit_value=5, message='Максимальное значение - 5')
        ]
    )
    notes = models.CharField(max_length=100)
    editable = models.BooleanField(default=True)
