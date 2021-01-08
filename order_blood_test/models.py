from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


# Create your models here.
class SignUpForm(UserCreationForm):
    display_name = forms.CharField(max_length=32, help_text='Your display name')

    class Meta:
        model = User
        fields = ('username', 'display_name', 'password1', 'password2', )
