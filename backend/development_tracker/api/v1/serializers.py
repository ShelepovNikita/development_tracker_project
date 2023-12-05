from rest_framework import serializers

from courses.models import Course
from skills.models import DefaultSkill, EditableSkill
from users.models import User

from core.constants import CHECK_LEN_SKILL_NAME


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("name", "image", "url",)


class DefaultSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultSkill
        fields = ("name",)


class EditableSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = EditableSkill
        fields = ("name",)

    def validate_name(self, value):
        """
        Проверяет длину значения поля 'name'.
        """
        if len(value) < 2:
            raise serializers.ValidationError(CHECK_LEN_SKILL_NAME)
        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "date_joined",
        )
