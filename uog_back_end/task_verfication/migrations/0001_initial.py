# Generated by Django 4.2.3 on 2023-07-30 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer_ask_help', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='task_verfication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expert_id', models.CharField(max_length=50)),
                ('user_verfication_number', models.CharField(max_length=50, null=True)),
                ('user_verify', models.CharField(max_length=50, null=True)),
                ('expert_verify', models.CharField(max_length=50, null=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer_information')),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_ask_help.customer_ask_help')),
            ],
        ),
    ]
