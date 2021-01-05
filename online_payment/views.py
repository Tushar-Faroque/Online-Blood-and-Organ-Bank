from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'online_payment/index.html')

def login(request):
    return render(request, 'online_payment/login.html')

def register(request):
    return render(request, 'online_payment/registration.html')

def payment(request):
    return render(request, 'online_payment/payment.html')
