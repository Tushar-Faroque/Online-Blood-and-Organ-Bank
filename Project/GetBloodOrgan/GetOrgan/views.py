from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from .forms import CustomerDetailsForm

# Create your views here.


def organ(request):
    return render(request, 'GetOrgan/get_organ.html')


def submission(request):
        
    form = CustomerDetailsForm()

    if request.method == 'POST':
        form = CustomerDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment')

    context = {'form': form}
    return render(request, 'GetOrgan/submit.html', context)

