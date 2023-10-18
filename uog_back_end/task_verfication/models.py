from django.db import models
from customer.models import customer_information
from customer_ask_help.models import customer_ask_help
# Create your models here.


class task_verfication(models.Model):
    customer_id = models.ForeignKey(customer_information, on_delete=models.CASCADE)
    expert_id = models.CharField(max_length=60)
    task_id = models.ForeignKey(customer_ask_help, on_delete=models.CASCADE)
    user_verfication_number = models.CharField(max_length=50, null=True)
    user_verify = models.CharField(max_length=50, null=True)
    expert_verify = models.CharField(max_length=50, null=True)
