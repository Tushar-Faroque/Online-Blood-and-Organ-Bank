from django.urls import path
from . import views

urlpatterns = [
    path('dadvise/', views.doctoradvise , name = 'doctoradvise')
]