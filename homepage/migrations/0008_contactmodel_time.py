# Generated by Django 3.0.5 on 2020-05-09 10:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_auto_20200509_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmodel',
            name='time',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Time'),
        ),
    ]
