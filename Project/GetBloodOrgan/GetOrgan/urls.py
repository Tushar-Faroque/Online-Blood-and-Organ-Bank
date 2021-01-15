from django.urls import path
from . import views

urlpatterns = [
    path('organ/', views.organ),
   # path('submission/', views.submission) 
    path('submit', views.submission, name= 'submit')
   
]

