# Generated by Django 3.0.6 on 2020-05-14 21:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20200514_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 14, 21, 14, 50, 827975, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 14, 21, 14, 50, 827975, tzinfo=utc)),
        ),
    ]
