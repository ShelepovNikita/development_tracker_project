from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from courses.models import Course
# from skills.models import EditableSkill


# class CustomUser(AbstractUser):
#     course = models.ManyToManyField(
#         Course,
#         through="UserCourse",
#         through_fields=("user", "Course"),
#     )


#     def __str__(self):
#         return self.username


# class UserCourse(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
