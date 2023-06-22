# Generated by Django 4.1.7 on 2023-06-22 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='awards',
            field=models.ManyToManyField(null=True, to='base.award'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='comments',
            field=models.ManyToManyField(null=True, to='base.comment'),
        ),
    ]
