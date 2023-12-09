from django.db import models

from skills.models import Skill


class Course(models.Model):
    """Модель для информации о курсах платформы Яндекс Практикум."""

    name = models.CharField(max_length=100)
    image = models.URLField()
    url = models.URLField()
    skills = models.ManyToManyField(
        Skill,
        through="CourseDefaultSkill",
        through_fields=("course", "skill"),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курсы Яндекс Практикум"
        verbose_name_plural = "Курсы Яндекс Практикума"


class CourseDefaultSkill(models.Model):
    """Модель для информации о том, какие скиллы какмим курсам принадлежат."""

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return self.skill

    class Meta:
        verbose_name = "Скиллы курса"
        verbose_name_plural = "Скиллы курса"
