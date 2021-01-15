from django.urls import path
from . import views

urlpatterns = [
    path('padvise/', views.patient , name = 'patient')
]