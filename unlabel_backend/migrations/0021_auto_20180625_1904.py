# Generated by Django 2.0.1 on 2018-06-25 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unlabel_backend', '0020_auto_20180625_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capability',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
