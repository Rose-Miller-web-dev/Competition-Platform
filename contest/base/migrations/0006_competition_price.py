# Generated by Django 4.1.7 on 2023-06-21 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_competition_competitors'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
