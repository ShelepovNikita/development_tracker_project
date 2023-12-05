from django.db import models
from users.models import User


class DefaultSkill(models.Model):
    name = models.CharField(max_length=100)
    editable = models.BooleanField(default=False)


class EditableSkill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rate = models.IntegerField()
    notes = models.CharField(max_length=100)
    editable = models.BooleanField(default=True)
