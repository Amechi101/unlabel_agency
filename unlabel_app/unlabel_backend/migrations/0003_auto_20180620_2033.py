# Generated by Django 2.0.1 on 2018-06-20 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unlabel_backend', '0002_auto_20180620_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, verbose_name='Slug'),
        ),
    ]