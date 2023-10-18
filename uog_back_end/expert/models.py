from django.db import models

# Create your models here.


class expert_information(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=40)
    gender = models.CharField(max_length=40)
    birthdate = models.CharField(max_length=40)
    email = models.CharField(max_length=60)
    phonenumber = models.CharField(max_length=50)
    education = models.CharField(max_length=40)
    campus = models.CharField(max_length=40)
    building = models.CharField(max_length=40)
    room = models.CharField(max_length=40)
    expert_in = models.CharField(max_length=40)
    today_no_work=models.CharField(max_length=50)
    image = models.ImageField(
        upload_to='', default='/experts.png', blank=True, null=True)