# Generated by Django 4.0.3 on 2022-03-20 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0014_image_description_image_time_image_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]