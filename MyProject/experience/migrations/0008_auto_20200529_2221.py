# Generated by Django 3.0.6 on 2020-05-29 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0007_remove_experience_experience_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='experience_section',
            field=models.CharField(blank=True, choices=[(' ', ' '), ('WORK EXPERIENCE', 'WORK EXPERIENCE'), ('EDUCATION', 'EDUCATION'), ('SKILLS', 'SKILLS')], default=' ', max_length=50),
        ),
    ]