# Generated by Django 3.2.7 on 2021-09-27 07:21

from django.db import migrations, models
import django.db.models.deletion
import user_sessions.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_sessions', '0005_alter_session_session_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='session_key',
            field=models.TextField(default=user_sessions.models.generate_random_string, editable=False, max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='sessionnote',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='user_sessions.session'),
        ),
    ]
