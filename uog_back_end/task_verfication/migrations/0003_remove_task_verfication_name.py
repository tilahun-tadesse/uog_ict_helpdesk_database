# Generated by Django 4.2.3 on 2023-07-30 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_verfication', '0002_task_verfication_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task_verfication',
            name='name',
        ),
    ]