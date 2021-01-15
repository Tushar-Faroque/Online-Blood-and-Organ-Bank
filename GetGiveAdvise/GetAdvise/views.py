from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from . models import ConsultWithDoctor
# Create your views here.

"""
    This method will load the consult_doctor page
	:param name: request - used to generate responses(Http) depending on the request that it receives.
	:param type: HttpResponse
	:return: returns the consult_doctor page
	
"""

#used Class based view 
def patient(request):
    return render(request, 'consult_doctor.html')
    
