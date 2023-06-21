# Generated by Django 4.1.7 on 2023-06-21 18:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='competitors',
            field=models.ManyToManyField(related_name='competitors', to=settings.AUTH_USER_MODEL),
        ),
    ]
