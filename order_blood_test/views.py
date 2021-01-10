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
    template = render_to_string('order_blood_test/email_template.html', {'name': request.user.first_name})

    email_message = EmailMessage(
        'Blood Test Order',
        template,
        settings.EMAIL_HOST_USER,
        [request.user.email],
    )

    email_message.fail_silently=False
    # email_message.send()

    form = BloodTestForm()

    if request.method == 'POST':
        form = BloodTestForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, 'A confirmation mail has been sent to your email ' + email)
            email_message.send()

    context = {'form': form}
    return render(request, 'order_blood_test/order_blood_test.html', context)


@login_required(login_url='login')
def confirmation(request):
    return render(request, 'order_blood_test/confirmation.html')
