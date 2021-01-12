from django.db import models


# Create your models here.
class BloodTest(models.Model):
	"""
    This class is extended from the Model class, thus it has all the functionality
    of the model class.

    This class used to create objects for database entry
    """
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date = models.CharField(max_length=200, null=True)
	time = models.CharField(max_length=200, null=True)
	address = models.CharField(max_length=200, null=True)
	nid = models.CharField(max_length=200, null=True)

	def __str__(self):
		"""
		
		"""
		return self.name