# Generated by Django 5.0.1 on 2024-02-08 09:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveapp', '0008_alter_teacher_t_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaverequest',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='leaveapp.student'),
        ),
    ]
