# Generated by Django 3.1 on 2020-08-19 15:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20200819_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2020, 8, 19, 15, 21, 44, 644352)),
        ),
        migrations.AlterField(
            model_name='user',
            name='real_name',
            field=models.CharField(max_length=3),
        ),
    ]