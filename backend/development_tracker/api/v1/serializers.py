import base64
from django.core.files.base import ContentFile
from django.conf import settings
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
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]

            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

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
    skill = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserSkill
        fields = ("skill", "rate", "notes", "editable")
        read_only_fields = ("skill", "rate", "notes")

    def validate(self, data):
        # Получаем имя навыка и пользователя из контекста запроса
        skill_name = self.context['request'].data.get('name')
        user = self.context['request'].user

        # Проверяем, существует ли уже UserSkill для данного пользователя и навыка
        if UserSkill.objects.filter(skill__name__iexact=skill_name.title(), user=user).exists():
            raise serializers.ValidationError("Такой навык уже существует для данного пользователя.")

        return data


class PatchUserSkillSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField(source="skill")

    class Meta:
        model = UserSkill
        fields = ("name", "rate", "notes", "editable")
        read_only_fields = ("editable", "name")


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
    image = Base64ImageField()
    # да простит меня Гвидо ван Россум за переменную imageHover
    imageHover = Base64ImageField()

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
