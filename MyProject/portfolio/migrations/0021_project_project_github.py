# Generated by Django 3.0.6 on 2020-05-30 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0020_auto_20200525_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_github',
            field=models.CharField(default='No link', max_length=255),
        ),
    ]
