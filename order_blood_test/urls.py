from django.urls import path
from . import views

urlpatterns = [
    path('blood_test', views.orderBloodTest, name='blood_test'),
    path('confirmation', views.confirmation, name='confirmation'),

]
