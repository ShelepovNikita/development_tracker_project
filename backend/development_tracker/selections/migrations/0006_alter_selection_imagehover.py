# Generated by Django 4.2.7 on 2023-12-07 20:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selections', '0005_alter_selection_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selection',
            name='imageHover',
            field=models.ImageField(default=None, upload_to='collections/imageshover/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'csv'])], verbose_name='Ховер изображение'),
        ),
    ]