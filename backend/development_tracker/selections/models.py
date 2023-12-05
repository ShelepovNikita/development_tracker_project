from django.db import models
from skills.models import Skill


class Selection(models.Model):
    name = models.CharField(max_length=100)
    skills = models.ManyToManyField(
        Skill,
        through="SelectionSkill",
        through_fields=("selection", "skill"),
    )


class SelectionSkill(models.Model):
    selection = models.ForeignKey(Selection, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
