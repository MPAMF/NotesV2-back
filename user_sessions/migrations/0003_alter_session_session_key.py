# Generated by Django 3.2.7 on 2021-09-14 08:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('user_sessions', '0002_auto_20210914_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='session_key',
            field=models.TextField(default='5vbm7QkX', editable=False, max_length=8),
        ),
    ]
