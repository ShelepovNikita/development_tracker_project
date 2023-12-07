import base64
from django.core.files.base import ContentFile

from rest_framework import serializers

from courses.models import Course
from skills.models import Skill
from users.models import UserSkill
from selections.models import Selection


class Base64ImageField(serializers.ImageField):
    """
    Преобразует base64-кодированное изображение в объект ContentFile.
    Args:
        data (str): base64-кодированное изображение в формате "data:image/формат;base64,данные".
    Returns:
        ContentFile: Объект ContentFile, представляющий декодированное изображение.
    """

    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith("data:image"):
            format, imgstr = data.split(";base64,")
            ext = format.split("/")[-1]

            data = ContentFile(base64.b64decode(imgstr), name="temp." + ext)

        return super().to_internal_value(data)


class CourseSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = Course
        fields = ("name", "image", "url")


class SkillSerializer(serializers.ModelSerializer):
    editable = serializers.HiddenField(default=False)

    class Meta:
        model = Skill
        fields = ("name", "editable")


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
