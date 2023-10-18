# Generated by Django 4.2.3 on 2023-07-29 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='on_work_expert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expert_id', models.CharField(max_length=50)),
                ('campus', models.CharField(max_length=50)),
                ('expert_in', models.CharField(max_length=50)),
                ('work_area', models.CharField(max_length=50)),
                ('today_on_work', models.CharField(max_length=40)),
                ('on_work', models.CharField(max_length=50)),
                ('number_work_on_today', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]