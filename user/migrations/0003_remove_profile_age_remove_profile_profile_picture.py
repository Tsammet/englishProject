# Generated by Django 5.1.4 on 2025-01-03 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_age_profile_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_picture',
        ),
    ]