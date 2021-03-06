# Generated by Django 3.0.7 on 2020-06-18 20:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobsearch_APP', '0003_auto_20200618_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='applicants',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_description',
            field=models.TextField(),
        ),
    ]
