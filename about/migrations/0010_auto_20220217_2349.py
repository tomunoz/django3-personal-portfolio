# Generated by Django 3.0.8 on 2022-02-17 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0009_auto_20220217_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]
