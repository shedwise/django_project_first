# Generated by Django 5.0 on 2024-11-17 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0007_alter_student_options_student_date_join_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
