# Generated by Django 4.2.7 on 2023-12-05 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='skill',
            new_name='skills',
        ),
    ]