from django.urls import path
from . import views

urlpatterns = [
    path('organ/', views.organ),
    #path('for_submission/', views.for_submission) 
    path('submit1', views.submission, name= 'submit1')
    
]