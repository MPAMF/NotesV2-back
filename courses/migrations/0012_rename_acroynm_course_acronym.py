# Generated by Django 3.2.7 on 2021-10-20 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_course_acroynm'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='acroynm',
            new_name='acronym',
        ),
    ]