# Generated by Django 3.0.8 on 2022-01-30 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_social'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='social',
            name='image',
        ),
    ]
