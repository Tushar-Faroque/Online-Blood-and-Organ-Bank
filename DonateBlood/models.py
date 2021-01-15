from django.db import models

# Create your models here.
class DonateBLOOD(models.Model):
    """
    This class contains the essential fields and behaviors of the data you’re storing. 
	Each model maps to a single database table.
    This class is used to create a database table containg those attributes.
    """
    first_name = models.CharField(max_length=200, null=True)
    email_address = models.CharField(max_length=200, null=True)
    address_house = models.CharField(max_length=1200, null=True)
    phone_number = models.CharField(max_length=200, null=True)
    bloodgroup = models.CharField(max_length=200, null=True)
  
	
    def __str__(self):
	     return self.first_name