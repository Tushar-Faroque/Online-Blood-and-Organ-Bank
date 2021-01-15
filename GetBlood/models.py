from django.db import models

"""
This class contains the essential fields and behaviors of the data you’re storing. 
Each model maps to a single database table.
This class is used to create a database table containing those attributes.
"""

class GetBLOOD(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=1200, null=True)
    phone = models.CharField(max_length=200, null=True)
    needblood = models.CharField(max_length=200, null=True)
  