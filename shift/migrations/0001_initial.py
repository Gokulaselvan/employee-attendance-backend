# Generated by Django 3.2.4 on 2021-06-20 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift_name', models.CharField(max_length=50)),
                ('shift_timing_start', models.TimeField()),
                ('shift_timing_end', models.TimeField()),
            ],
        ),
    ]
