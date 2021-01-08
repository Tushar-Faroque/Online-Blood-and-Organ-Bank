from django.urls import path
from . import views

urlpatterns = [
    path('blood_test', views.orderBloodTest),

]
