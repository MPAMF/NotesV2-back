# Generated by Django 3.2.7 on 2021-10-14 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20211014_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examdate',
            name='tp_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='date_tp_groups', to='courses.tpgroup'),
        ),
    ]
