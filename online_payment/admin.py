from django.contrib import admin
from django.contrib.auth.models import User

from .models import BloodTest

# Register your models here.
admin.site.register(BloodTest)
