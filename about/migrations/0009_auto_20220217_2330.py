# Generated by Django 3.0.8 on 2022-02-17 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_social_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]