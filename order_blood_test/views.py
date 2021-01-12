from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from .forms import BloodTestForm

@login_required(login_url='login')
def orderBloodTest(request):
    
    form = BloodTestForm()

    if request.method == 'POST':
        form = BloodTestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment')

    context = {'form': form}
    return render(request, 'order_blood_test/order_blood_test.html', context)


@login_required(login_url='login')
def confirmation(request):
    return render(request, 'order_blood_test/confirmation.html')
