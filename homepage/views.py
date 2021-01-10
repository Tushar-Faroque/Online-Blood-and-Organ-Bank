from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from .forms import SignUpForm


def home(request):
    """
    docstring
    """
    return render(request, 'homepage/index.html')

def login_page(request):
    """
    docstring
    """
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'username or password is incorrect')
                return render(request, 'homepage/login.html')

        return render(request, 'homepage/login.html')

def logout_page(request):
    """
    docstring
    """
    logout(request)
    return redirect('login')

def register(request):
    """
    docstring
    """
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = SignUpForm()

        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Welcome ' + user + ', you can login now')
                return redirect('login')

        context = {'form': form}
        return render(request, 'homepage/registration.html', context)

@login_required(login_url='login')
def thanks_registration(request):
    """
    docstring
    """
    return render(request, 'homepage/thanks_reg.html')
