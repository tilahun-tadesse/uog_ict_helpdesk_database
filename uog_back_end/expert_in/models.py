from django.db import models
from expert.models import expert_information


class expert_in(models.Model):
    # expert = models.ForeignKey(
    #     expert_information, on_delete=models.CASCADE)
    expert_id = models.CharField(max_length=40)
    expert_in = models.CharField(max_length=40)
