# Generated by Django 4.2.7 on 2023-12-08 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('imageHover', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SelectionSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='selections.selection')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selection_skills', to='skills.skill')),
            ],
        ),
        migrations.AddField(
            model_name='selection',
            name='skills',
            field=models.ManyToManyField(through='selections.SelectionSkill', to='skills.skill'),
        ),
    ]
