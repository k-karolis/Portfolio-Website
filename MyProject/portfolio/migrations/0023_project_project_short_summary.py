# Generated by Django 3.0.6 on 2020-05-31 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0022_auto_20200531_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_short_summary',
            field=models.CharField(default='Short summary', max_length=100),
        ),
    ]
