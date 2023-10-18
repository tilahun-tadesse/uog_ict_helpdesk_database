from django.db import models

# Create your models here.


class user_information(models.Model):
    user_id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    phonenumber = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    user_name = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    roll= models.CharField(max_length=40)
    image = models.ImageField(
        upload_to='customer/image/', default='image/customer.png', blank=True, null=True)
    def __int__(self):
        return self.user_id
    
