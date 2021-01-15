from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from . models import Doctor
# Create your views here.


#used Class based view 
def doctoradvise(request):
    return render(request, 'doctor_advise.html')