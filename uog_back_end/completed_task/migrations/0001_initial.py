# Generated by Django 4.2.3 on 2023-07-29 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='completed_task',
            fields=[
                ('customer_id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('expert_id', models.CharField(max_length=40)),
                ('task_id', models.CharField(max_length=40)),
                ('date', models.CharField(max_length=40)),
                ('completed', models.CharField(max_length=40)),
            ],
        ),
    ]
