# Generated by Django 3.2.7 on 2021-09-14 07:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('user_sessions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessionnote',
            name='activated',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='session_key',
            field=models.TextField(default='49FHgunC', editable=False, max_length=8),
        ),
    ]
