# Generated by Django 5.1.1 on 2024-11-08 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_student_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cohortgroup',
            name='students',
            field=models.ManyToManyField(related_name='cohort_groups', to='hello.student'),
        ),
    ]
