from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from .forms import DonatorsDetailsForm

# Create your views here.


def organ(request):
    return render(request, 'DonateOrgan/donate_organ.html')


def submission(request):
    """
    This method will submit the data from the user of organ,
    it will send an confirmation to the user like your request added successfully.
    This method will only load this page if the user is logged in.
	:param name: request - used to generate responses(Http) depending on the request that it receives.
	:param type: HttpResponse
	:return: returns payment page
	"""      
    form = DonatorsDetailsForm()

    if request.method == 'POST':
        form = DonatorsDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment')

    context = {'form': form}
    return render(request, 'DonateOrgan/submit1.html', context)