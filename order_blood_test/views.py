from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .models import BloodTest

def orderBloodTest(request):
    return render(request, 'blood_test/order_blood_test.html')
