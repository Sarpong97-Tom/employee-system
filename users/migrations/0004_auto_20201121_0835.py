# Generated by Django 3.1.2 on 2020-11-21 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_delete_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_designer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_developer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_photographer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_planner',
        ),
    ]
