from django.db import models

# Create your models here.

#class GetORGAN(models.Model):
    
	#name = models.CharField(max_length=200, null=True)
	#phone = models.CharField(max_length=200, null=True)
	#email = models.CharField(max_length=200, null=True)
	#date_created = models.DateTimeField(auto_now_add=True, null=True)
	#bloodtype = models.CharField(max_length= 10 ,  null=True)
    #organname = models.CharField(max_length =200)
    #contact  = models.CharField(max_length =200,  null=True)
	#address = models.CharField(max_length=200, null=True)


	#def __str__(self):
		
	#	return self.name

   
# Create your models here.
# Create your models here.
class GetORGAN(models.Model):
    """
    This class contains the essential fields and behaviors of the data you’re storing. 
    Each model maps to a single database table.
    This class is used to create a database table containg those attributes.
    """
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=1200, null=True)
    phone = models.CharField(max_length=200, null=True)
    bloodtype = models.CharField(max_length=200, null=True)
    organname = models.CharField(max_length=1200, null=True)
    contact = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    



    