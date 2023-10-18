from django.db import models
# Create your models here.


class customer_ask_help(models.Model):
    task_id=models.AutoField(primary_key=True)
    expert_id = models.CharField(max_length=60)
    customer_id = models.CharField(max_length=70)
    problem_catagory = models.CharField(max_length=50)
    problem_description=models.CharField(max_length=60)
    device_name = models.CharField(max_length=50)
    problem_priority = models.CharField(max_length=50)
    campus = models.CharField(max_length=50)
    building = models.CharField(max_length=50)
    room = models.CharField(max_length=40)
    data= models.CharField(max_length=40)
    def __int__(self):
        return self.task_id