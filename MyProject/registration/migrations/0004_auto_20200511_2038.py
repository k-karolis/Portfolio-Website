# Generated by Django 3.0.6 on 2020-05-11 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20200505_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='portfolio_site',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='profile_pic',
        ),
    ]
