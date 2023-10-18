from django.db import models
from expert.models import expert_information
# Create your models here.


class work_area(models.Model):
    # expertid = models.ForeignKey(expert_information, on_delete=models.CASCADE)
    expertid = models.CharField(max_length=40)
    work_areas = models.CharField(max_length=40)
    expert_in = models.CharField(max_length=50)
    campus = models.CharField(max_length=40)
