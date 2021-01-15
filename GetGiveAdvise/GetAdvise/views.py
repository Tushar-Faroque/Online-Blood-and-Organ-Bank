from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from . models import ConsultWithDoctor
# Create your views here.



#used Class based view 
def patient(request):
    return render(request, 'consult_doctor.html')
    
