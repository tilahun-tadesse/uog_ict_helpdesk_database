from django.db import models

# Create your models here.


class on_work_expert(models.Model):
    expert_id = models.CharField(max_length=50)
    campus = models.CharField(max_length=50)
    expert_in = models.CharField(max_length=50)
    work_area = models.CharField(max_length=50)
    today_on_work=models.CharField(max_length=40)
    on_work = models.CharField(max_length=50)
    number_work_on_today = models.CharField(max_length=50, null=True)
