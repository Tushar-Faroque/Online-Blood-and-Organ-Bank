from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from .forms import DonatorsDetailsForm

# Create your views here.


def blood(request):
    return render(request, 'DonateBlood/donate_blood.html')


def for_submission(request):
        
    form = DonatorsDetailsForm()

    if request.method == 'POST':
        form = DonatorsDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment')

    context = {'form': form}
    return render(request, 'DonateOrgan/submit1.html', context)