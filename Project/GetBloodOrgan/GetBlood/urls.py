
from django.urls import path

urlpatterns = [
    path('blood/', views.blood),
    path('submission/', views.submission) 
    #path('submit', views.submission, name= 'submit')
   
]