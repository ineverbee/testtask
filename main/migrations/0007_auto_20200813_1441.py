# Generated by Django 3.1 on 2020-08-13 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200813_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagemodel',
            name='height',
        ),
        migrations.RemoveField(
            model_name='imagemodel',
            name='width',
        ),
    ]