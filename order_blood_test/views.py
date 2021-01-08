from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .models import SignUpForm

# def orderBloodTest(request):
#     return render(request, 'blood_test/order_blood_test.html')


def orderBloodTest(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = form.save()
            user.refresh_from_db()
            user.profile.display_name = form.cleaned_data.get('display_name')
            user.save()
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=user.username, password=raw_password)
    else:
        form = SignUpForm()

    return render(request, 'blood_test/order_blood_test.html', context={'form': form})