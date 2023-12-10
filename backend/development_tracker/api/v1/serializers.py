from rest_framework import serializers

from courses.models import Course
from skills.models import Skill
from users.models import UserSkill
from selections.models import Selection


class CourseSerializer(serializers.ModelSerializer):
    """Сериализация полей модели Курсов."""

    class Meta:
        model = Course
        fields = ("name", "image", "url")


class SkillSerializer(serializers.ModelSerializer):
    """Сериализация полей модели Скиллов."""

    editable = serializers.HiddenField(default=False)

    class Meta:
        model = Skill
        fields = ("id", "name", "editable")
        read_only_fields = ("id",)


class UserSkillSerializer(serializers.ModelSerializer):
    """Сериализация полей модели пользовательских скиллов
    для добавления скилла."""

    name = serializers.StringRelatedField(read_only=True, source="skill")

    class Meta:
        model = UserSkill
        fields = ("id", "name", "rate", "notes", "editable")
        read_only_fields = ("id", "name", "rate", "notes")

    def validate(self, data):
        # Получаем имя навыка и пользователя из контекста запроса
        skill_name = self.context["request"].data.get("name")
        user = self.context["request"].user

        # Проверяем, существует ли уже UserSkill для
        # данного пользователя и навыка
        if UserSkill.objects.filter(
            skill__name__iexact=skill_name.title(), user=user
        ).exists():
            raise serializers.ValidationError(
                "Такой навык уже существует для данного пользователя."
            )

        return data


class PatchUserSkillSerializer(serializers.ModelSerializer):
    """Сериализация полей модели пользовательских скиллов
    для обновления."""

    name = serializers.StringRelatedField(source="skill")

    class Meta:
        model = UserSkill
        fields = ("id", "name", "rate", "notes", "editable")
        read_only_fields = ("id", "editable")


class UserDataSkillSerializer(serializers.ModelSerializer):
    """Сериализация полей модели пользовательских скиллов
    для получения информции о пользователе."""

    name = serializers.StringRelatedField(source="skill")

    class Meta:
        model = UserSkill
        fields = (
            "id",
            "skill",
            "name",
            "rate",
            "notes",
            "editable",
        )
        read_only_fields = ("editable",)


class SkillSelectionSerializer(serializers.ModelSerializer):
    """Для сериализации скиллов по запросу о подборках."""

    class Meta:
        model = Skill
        fields = ("name",)


class SelectionSerializer(serializers.ModelSerializer):
    """Сериализация полей модели подборок
    для получения информции о них."""

    count = serializers.IntegerField(source="skills.count")
    skills = SkillSelectionSerializer(many=True, read_only=True)
    # да простит меня Гвидо ван Россум за переменную imageHover

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
