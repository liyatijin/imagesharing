# Generated by Django 4.0.3 on 2022-03-12 12:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images', '0009_image_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='description',
        ),
        migrations.AlterField(
            model_name='image',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
