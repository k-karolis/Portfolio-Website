# Generated by Django 3.0.6 on 2020-05-31 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0021_project_project_github'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_summary',
            field=models.TextField(),
        ),
    ]