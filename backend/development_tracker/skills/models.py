from django.db import models

# from users.models import CustomUser


class Skill(models.Model):
    name = models.CharField(max_length=100)
    editable = models.BooleanField(default=False)


# class UserSkill(models.Model):
#     skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
#     rate = models.IntegerField()
#     notes = models.CharField(max_length=100)
#     editable = models.BooleanField(default=True)
