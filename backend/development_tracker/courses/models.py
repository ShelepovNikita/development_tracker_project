from django.db import models
from skills.models import Skill

# from users.models import CustomUser


class Course(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    skills = models.ManyToManyField(
        Skill,
        through="CourseDefaultSkill",
        through_fields=("course", "skill"),
    )
    # user = models.ManyToManyField(
    #     User,
    #     through="CourseUser",
    #     through_fields=("course", "user"),
    # )


class CourseDefaultSkill(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)


# class CourseUser(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
