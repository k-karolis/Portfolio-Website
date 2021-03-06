# Generated by Django 3.0.6 on 2020-05-21 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0016_auto_20200521_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_image',
            field=models.ImageField(default='No Image selected', upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_published',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date_published'),
        ),
    ]
