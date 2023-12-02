from rest_framework import serializers

from courses.models import Course
from skills.models import DefaultSkill
from users.models import User


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("name", "image", "url")


class DefaultSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultSkill
        fields = ("name",)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "date_joined",
        ]
