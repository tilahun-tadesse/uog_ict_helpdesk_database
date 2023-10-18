from django.db import models

# Create your models here.


class customer_information(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=40,)
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    phonenumber = models.CharField(max_length=40)
    image = models.ImageField(
        upload_to='customer/image/', default='image/customer.png', blank=True, null=True)
    def __str__(self):
        return self.customer_id
    
