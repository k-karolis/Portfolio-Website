# Generated by Django 3.0.6 on 2020-06-07 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0008_auto_20200529_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='experience_section',
            field=models.CharField(blank=True, choices=[(' ', ' '), ('WORK EXPERIENCE', 'WORK EXPERIENCE'), ('EDUCATION', 'EDUCATION'), ('SKILLS', 'SKILLS')], default='', max_length=50),
        ),
    ]
