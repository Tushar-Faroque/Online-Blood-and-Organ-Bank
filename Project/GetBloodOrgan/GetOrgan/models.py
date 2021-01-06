from django.db import models

# Create your models here.

class COM(models.Model):

    username = models.CharField(max_length=10)
    bloodtype = models.CharField(max_length= 3)
    date = models.IntegerField(max_length=10)
    organlist = models.CharField(max_length =10)

    def __str__(self):
        return self.username