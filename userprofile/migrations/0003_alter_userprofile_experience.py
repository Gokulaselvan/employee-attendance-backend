# Generated by Django 3.2.3 on 2021-06-13 11:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20210612_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='experience',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxLengthValidator(limit_value=2, message='Should not exceed two digits')]),
        ),
    ]