# Generated by Django 3.0.6 on 2020-05-14 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_auto_20200514_2212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_joined',
        ),
    ]
