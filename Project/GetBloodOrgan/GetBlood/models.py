from django.db import models

# Create your models here.
class GetBLOOD(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=1200, null=True)
    phone = models.CharField(max_length=200, null=True)
    needblood = models.CharField(max_length=200, null=True)
    contact = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
	
    def __str__(self):
	     return self.name

