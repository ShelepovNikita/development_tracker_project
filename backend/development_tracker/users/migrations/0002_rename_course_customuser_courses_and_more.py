# Generated by Django 4.2.7 on 2023-12-05 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='course',
            new_name='courses',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='user_skill',
            new_name='user_skills',
        ),
    ]