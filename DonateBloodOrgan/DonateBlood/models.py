from django.db import models

# Create your models here.
class DonateBLOOD(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    email_address = models.CharField(max_length=200, null=True)
    address_house = models.CharField(max_length=1200, null=True)
    phone_number = models.CharField(max_length=200, null=True)
    bloodgroup = models.CharField(max_length=200, null=True)
  
	
    def __str__(self):
	     return self.first_name