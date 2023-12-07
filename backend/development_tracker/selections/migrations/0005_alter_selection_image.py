# Generated by Django 4.2.7 on 2023-12-07 20:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selections', '0004_selection_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selection',
            name='image',
            field=models.ImageField(default=None, upload_to='collections/images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'csv'])], verbose_name='Изображение'),
        ),
    ]