# Generated by Django 4.0.3 on 2022-03-11 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_alter_image_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(default='', upload_to='media/file'),
        ),
    ]