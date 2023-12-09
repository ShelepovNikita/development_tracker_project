from django.db import models


class Skill(models.Model):
    """Модель для информации о скиллах."""

    name = models.CharField(max_length=100)
    editable = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Скиллы"
        verbose_name_plural = "Скиллы"
