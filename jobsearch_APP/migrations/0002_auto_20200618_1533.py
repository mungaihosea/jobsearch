# Generated by Django 3.0.7 on 2020-06-18 15:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobsearch_APP', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WorkExperience',
            new_name='Experience',
        ),
    ]
