from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from .forms import BloodTestForm


@login_required(login_url='login')
def orderBloodTest(request):
    """
    This method will create a blood test order request and after successfull order,
    it will redirect to the payment page.
    This method will only load this page if the user is logged in.

	:param name: request - used to generate responses(Http) depending on the request that it receives.
	:param type: HttpResponse
	:return: returns payment page if the order is successful else, returns the order_blood_test page
	"""
    form = BloodTestForm()

    if request.method == 'POST':
        form = BloodTestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment')

    context = {'form': form}
    return render(request, 'order_blood_test/order_blood_test.html', context)

