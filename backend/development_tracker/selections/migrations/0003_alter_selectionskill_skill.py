# Generated by Django 4.2.7 on 2023-12-06 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0003_alter_skill_editable'),
        ('selections', '0002_rename_skill_selection_skills_selection_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selectionskill',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selection_skills', to='skills.skill'),
        ),
    ]
