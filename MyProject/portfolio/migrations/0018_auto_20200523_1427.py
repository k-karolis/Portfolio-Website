# Generated by Django 3.0.6 on 2020-05-23 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0017_auto_20200521_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_image',
            field=models.ImageField(default='notfound.jpg', upload_to='portfolio_logo'),
        ),
    ]
