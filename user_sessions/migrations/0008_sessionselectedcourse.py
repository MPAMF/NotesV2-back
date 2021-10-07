# Generated by Django 3.2.7 on 2021-10-07 17:45

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_semester_activated'),
        ('user_sessions', '0007_session_tp_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionSelectedCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('activated', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='session_courses', to='courses.course')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selected_courses', to='user_sessions.session')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
