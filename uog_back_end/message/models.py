from django.db import models
from user.models import user_information

# Create your models here.


class message(models.Model):
    user_id = models.ForeignKey(
    user_information, on_delete=models.CASCADE)
    from_number = models.CharField(max_length=50)
    to_number = models.CharField(max_length=50)
    message_text = models.TextField()
    time = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    message_seen = models.CharField(max_length=50)
    expert_in=models.CharField(max_length=50)
    roll=models.CharField(max_length=50)
    