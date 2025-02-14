# Generated by Django 5.0 on 2024-10-17 02:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_alter_student_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_profile',
            name='profile_picture',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='student_profile'),
            preserve_default=False,
        ),
    ]
