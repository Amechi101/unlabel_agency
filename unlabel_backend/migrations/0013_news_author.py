# Generated by Django 2.0.1 on 2018-06-23 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unlabel_backend', '0012_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
