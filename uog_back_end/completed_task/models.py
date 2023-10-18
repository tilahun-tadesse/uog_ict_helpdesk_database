from django.db import models

# Create your models here.


class completed_task(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=40)
    expert_id = models.CharField(max_length=40)
    task_id = models.CharField(max_length=40)
    date = models.CharField(max_length=40)
    completed=models.CharField(max_length=40)
    