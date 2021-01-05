from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('login', views.login),
    path('register', views.register),
    path('payment', views.payment),
    
]
