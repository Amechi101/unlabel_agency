# Generated by Django 2.0.1 on 2018-06-20 20:16

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('client_name', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(max_length=1000, null=True)),
                ('services', multiselectfield.db.fields.MultiSelectField(choices=[('CONSULT', 'Consulation'), ('CONTENT', 'Content Creation'), ('DESIGN', 'Design'), ('INFLUENCE', 'Influence'), ('SALES', 'Sales'), ('STARTEGY', 'Strategy'), ('TECH', 'Technology')], max_length=100)),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'verbose_name_plural': 'Projects',
                'verbose_name': 'Project',
            },
        ),
    ]
