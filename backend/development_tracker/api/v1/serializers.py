import base64
from django.core.files.base import ContentFile

from rest_framework import serializers

from courses.models import Course
from skills.models import Skill
from users.models import UserSkill
from selections.models import Selection


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("name", "image", "url")


class SkillSerializer(serializers.ModelSerializer):
    editable = serializers.HiddenField(default=False)

    class Meta:
        model = Skill
        fields = ("id", "name", "editable")
        read_only_fields = ("id",)


class UserSkillSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField(read_only=True, source="skill")

    class Meta:
        model = UserSkill
        fields = ("id", "name", "rate", "notes", "editable")
        read_only_fields = ("id", "name", "rate", "notes")


class PatchUserSkillSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField(source="skill")

    class Meta:
        model = UserSkill
        fields = ("id", "name", "rate", "notes", "editable")
        read_only_fields = ("id", "editable")


class UserDataSkillSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField(source="skill")

    class Meta:
        model = UserSkill
        fields = ("id", "name", "rate", "notes", "editable")
        read_only_fields = ("editable",)


class SkillSelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ("name",)


class SelectionSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(source="skills.count")
    skills = SkillSelectionSerializer(many=True, read_only=True)

    class Meta:
        model = Selection
        fields = (
            "id",
            "name",
            "count",
            "image",
            "imageHover",
            "description",
            "skills",
        )
