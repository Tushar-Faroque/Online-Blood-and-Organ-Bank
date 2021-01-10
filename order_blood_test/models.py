from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
	bkash = models.CharField(max_length=200, null=True)
	trxid = models.CharField(max_length=200, null=True)

	def __str__(self):
		"""
		
		"""
		return self.name