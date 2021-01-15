from django.db import models

# Create your models here.
class DonateBLOOD(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=1200, null=True)
    phone = models.CharField(max_length=200, null=True)
    bloodgroup = models.CharField(max_length=200, null=True)
  
	
    def __str__(self):
	     return self.name