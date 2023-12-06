from django.db import models
from skills.models import Skill


class Selection(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    imageHover = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    skills = models.ManyToManyField(
        Skill,
        through="SelectionSkill",
        through_fields=("selection", "skill"),
    )


class SelectionSkill(models.Model):
    selection = models.ForeignKey(Selection, on_delete=models.CASCADE)
    skill = models.ForeignKey(
        Skill, related_name="selection_skills", on_delete=models.CASCADE
    )
