# from django.contrib.auth import get_user_model
from django.db import models


# User = get_user_model()

from django.contrib.auth.models import AbstractUser

# from django.db import models
from courses.models import Course

from skills.models import Skill


class CustomUser(AbstractUser):
    courses = models.ManyToManyField(
        Course,
        # through="UserCourse",
        # through_fields=("user", "Course"),
    )
    user_skills = models.ManyToManyField(
        Skill, through="UserSkill", through_fields=("user", "skill")
    )


#     def __str__(self):
#         return self.username


class UserSkill(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    rate = models.IntegerField()
    notes = models.CharField(max_length=100)
    editable = models.BooleanField(default=True)
