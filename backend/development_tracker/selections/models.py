from django.db import models

from skills.models import Skill


class Selection(models.Model):
    """Модель для информации о подборках скиллов."""

    name = models.CharField(max_length=100)
    image = models.URLField()
    imageHover = models.URLField()
    description = models.TextField()
    skills = models.ManyToManyField(
        Skill,
        through="SelectionSkill",
        through_fields=("selection", "skill"),
    )


class SelectionSkill(models.Model):
    """Модель для информации о том,
    какие скиллы какмим подборкам принадлежат."""

    selection = models.ForeignKey(Selection, on_delete=models.CASCADE)
    skill = models.ForeignKey(
        Skill, related_name="selection_skills", on_delete=models.CASCADE
    )
