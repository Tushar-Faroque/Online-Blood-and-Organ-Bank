from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from . models import Doctor
# Create your views here.


"""
    This method will load the doctor_advise page
	:param name: request - used to generate responses(Http) depending on the request that it receives.
	:param type: HttpResponse
	:return: returns the doctor_advise page
	
"""
#used Class based view 
def doctoradvise(request):
    return render(request, 'doctor_advise.html')