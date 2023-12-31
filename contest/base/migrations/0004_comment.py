# Generated by Django 4.1.7 on 2023-06-18 22:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0003_lecture_alter_competition_options_competition_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=1000)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.competition')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
