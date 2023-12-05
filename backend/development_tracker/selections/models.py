from django.db import models
from skills.models import DefaultSkill


class Selection(models.Model):
    name = models.CharField(max_length=100)
    skill = models.ManyToManyField(
        DefaultSkill,
        through="SelectionSkill",
        through_fields=("selection", "skill"),
    )


class SelectionSkill(models.Model):
    selection = models.ForeignKey(Selection, on_delete=models.CASCADE)
    skill = models.ForeignKey(DefaultSkill, on_delete=models.CASCADE)
