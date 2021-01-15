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
    """
    This method will create submission form request and after successfully adding user's info to form,
    it will redirect to the payment page.
    This method will only load this page if the user is logged in.
	:param name: request - used to generate responses(Http) depending on the request that it receives.
	:param type: HttpResponse
	:return: returns payment page if the order is successful else, returns the submit page
	""" 
        
    form = CustomerDetailsForm()

    if request.method == 'POST':
        form = CustomerDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment')

    context = {'form': form}
    return render(request, 'GetOrgan/submit.html', context)

