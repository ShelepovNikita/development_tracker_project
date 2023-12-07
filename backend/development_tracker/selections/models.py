from django.core.validators import FileExtensionValidator
from django.db import models
from skills.models import Skill


class Selection(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(
        upload_to='collections/images/',
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'csv', 'svg', ])
        ],
        verbose_name='Изображение'
    )
    imageHover = models.FileField(
        upload_to='collections/imageshover/',
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'csv', 'svg', ])
        ],
        verbose_name='Ховер изображение'
    )
    description = models.CharField(max_length=255)
    skills = models.ManyToManyField(
        Skill,
        through="SelectionSkill",
        through_fields=("selection", "skill"),
    )


class SelectionSkill(models.Model):
    selection = models.ForeignKey(Selection, on_delete=models.CASCADE)
    skill = models.ForeignKey(
        Skill, related_name="selection_skills", on_delete=models.CASCADE
    )
