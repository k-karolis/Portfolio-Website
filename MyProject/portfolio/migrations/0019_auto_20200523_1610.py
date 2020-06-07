# Generated by Django 3.0.6 on 2020-05-23 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_auto_20200523_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_summary',
            field=models.CharField(default='No summary', max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_author',
            field=models.CharField(default='No author', max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_title',
            field=models.CharField(max_length=50),
        ),
    ]
