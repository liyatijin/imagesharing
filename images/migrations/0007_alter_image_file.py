# Generated by Django 4.0.3 on 2022-03-12 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0006_alter_image_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.FileField(default=None, upload_to='media/file'),
        ),
    ]