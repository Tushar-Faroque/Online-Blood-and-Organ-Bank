from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from .forms import SignUpForm

def home(request):
    return render(request, 'online_payment/index.html')

def login(request):
    return render(request, 'online_payment/login.html')

def register(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'online_payment/registration.html', context)

def payment(request):
    return render(request, 'online_payment/payment.html')

def thanks_reg(request):
    return render(request, 'online_payment/thanks_reg.html')
