from django.db import models

# Create your models here.
# Create your models here.
class  ConsultWithDoctor(models.Model):
	"""
    This class contains the essential fields and behaviors of the data you’re storing. 
	Each model maps to a single database table.
    This class is used to create a database table containg those attributes.
    """
	pname = models.CharField(max_length=200, null=True)
	pemail = models.CharField(max_length=200, null=True)
	pid = models.CharField(max_length=200, null=True)
	bloodgroup = models.CharField(max_length=1200, null=True)
	

	def __str__(self):
		"""
		This method will show the list as username in the django database Users table.
		:param name: self - used to access the attributes and methods of the class in python.
		:param type: reference
		:return: str
		"""
		return self.pname