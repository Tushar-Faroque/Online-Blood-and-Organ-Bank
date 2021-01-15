
from django.urls import path
from . import views

urlpatterns = [
    path('blood/', views.blood),
    #path('for_submission/', views.for_submission) 
    path('submit1', views.for_submission, name= 'submit1')
    
]