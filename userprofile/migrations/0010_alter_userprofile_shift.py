# Generated by Django 3.2.4 on 2021-06-20 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shift', '0001_initial'),
        ('userprofile', '0009_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='shift',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='shift.shift'),
        ),
    ]
