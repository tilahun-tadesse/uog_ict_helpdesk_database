from django.db import models

# Create your models here.

class manager_information(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=40)
    gender = models.CharField(max_length=40)
    email = models.CharField(max_length=60)
    phonenumber = models.CharField(max_length=40)
    education = models.CharField(max_length=40)
    image = models.ImageField(
        upload_to='', default='/experts.png', blank=True, null=True)
    