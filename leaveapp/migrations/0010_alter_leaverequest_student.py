# Generated by Django 5.0.1 on 2024-02-08 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveapp', '0009_alter_leaverequest_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaverequest',
            name='student',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
