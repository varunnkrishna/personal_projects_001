# Generated by Django 3.0.5 on 2020-05-10 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_auto_20200509_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactmodel',
            name='time',
        ),
    ]