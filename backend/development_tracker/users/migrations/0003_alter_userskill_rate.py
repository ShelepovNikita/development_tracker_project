# Generated by Django 4.2.7 on 2023-12-06 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_course_customuser_courses_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userskill',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]
