# Generated by Django 2.0.1 on 2018-06-23 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unlabel_backend', '0013_news_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True, verbose_name='Slug'),
        ),
    ]