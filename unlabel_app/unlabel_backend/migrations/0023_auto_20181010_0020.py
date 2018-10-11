# Generated by Django 2.1 on 2018-10-10 00:20

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('unlabel_backend', '0022_auto_20181003_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='client_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Client Name'),
        ),
        migrations.AlterField(
            model_name='project',
            name='services',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('CONT', 'Content'), ('DESI', 'Design'), ('INFL', 'Influence'), ('TECH', 'Technology')], max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(help_text='for internal reference only', max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Client',
        ),
    ]